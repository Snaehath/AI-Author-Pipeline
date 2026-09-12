"""
Text and Manuscript Sanitizer Module.

Filters out Project Gutenberg legal headers, illustration markers, play script stage cues,
and unwanted character leaks from generated prose outputs.
"""

import re


def sanitize_generated_prose(text: str) -> str:
    """Cleans raw AI generated text to ensure professional manuscript standards.

    Args:
        text: Raw generated prose text.

    Returns:
        Cleaned, professional narrative text.
    """
    if not text:
        return ""

    cleaned = text

    # 1. Remove prompt leakage, ChatML tags, and tool call tags
    cleaned = re.sub(r"(?i)<tool_call>.*?</tool_call>", "", cleaned)
    cleaned = re.sub(r"(?i)<tool_call>", "", cleaned)
    cleaned = re.sub(r"(?i)<\|im_start\|>.*?\n", "", cleaned)
    cleaned = re.sub(r"(?i)<\|im_end\|>", "", cleaned)
    cleaned = re.sub(r"(?i)Write a character introduction.*?\n", "", cleaned)
    cleaned = re.sub(r"(?i)THE PROCEEDINGS AGAINST THE ROYAL CHARTER.*?\n", "", cleaned)

    # 1B. Remove historical pre-training memory leaks, footnotes, and hyphenated adjective chains
    cleaned = re.sub(r"\[Footnote:[^\]]*\]", "", cleaned)
    cleaned = re.sub(r"(?i)court-martial proceedings.*?\n", "", cleaned)
    cleaned = re.sub(r"(?i)Earl Spencer.*?\n", "", cleaned)
    cleaned = re.sub(r"(?i)H\.M\.S\..*?\n", "", cleaned)
    cleaned = re.sub(r"(?i)letter dated.*?\n", "", cleaned)
    cleaned = re.sub(r"\b\w+-\w+-\w+-\w+-\w+[\w-]*\b", "", cleaned)  # Strips 5+ hyphenated adjective chains

    # 2. Remove Gutenberg header/footer disclaimers
    cleaned = re.sub(r"(?i)The Project Gutenberg eBook of.*?\n", "", cleaned)
    cleaned = re.sub(r"(?i)Project Gutenberg.*?\n", "", cleaned)
    cleaned = re.sub(r"(?i)\*\*\* START OF THE PROJECT GUTENBERG EBOOK.*?\*\*\*", "", cleaned)
    cleaned = re.sub(r"(?i)\*\*\* END OF THE PROJECT GUTENBERG EBOOK.*?\*\*\*", "", cleaned)

    # 3. Remove illustration and picture tags
    cleaned = re.sub(r"\[Picture:[^\]]*\]", "", cleaned)
    cleaned = re.sub(r"\[Illustration[^\]]*\]", "", cleaned)
    cleaned = re.sub(r"\[Music:[^\]]*\]", "", cleaned)
    cleaned = re.sub(r"\[_?Click_?\]", "", cleaned)
    cleaned = re.sub(r"\[Act [^\]]*\]", "", cleaned)
    cleaned = re.sub(r"\[Scene:[^\]]*\]", "", cleaned)

    # 4. Clean play script stage direction cues like CHAPTER II. inside text
    cleaned = re.sub(r"CHAPTER\s+[I|V|X|L|C|D|M]+\.\s*", "", cleaned)
    cleaned = re.sub(r"THE GREAT COMEDY OF ERRORS AND MYSTERIES\s*", "", cleaned)

    # 5. Split long run-on sentences (>20 words) at conjunctions (and, but, so, while) to enforce 10-12 word cadence
    lines = cleaned.splitlines()
    sanitized_lines = []
    for line in lines:
        if line.startswith('"') or line.startswith('#') or not line.strip():
            sanitized_lines.append(line)
            continue
        # Process narrative paragraphs to enforce crisp 10-12 word sentence cadence
        sents = re.split(r'(?<=[.!?])\s+', line)
        crisp_sents = []
        for s in sents:
            words = s.split()
            if len(words) > 20:
                # Split at mid-conjunctions like ', and ' or ', but ' or ', while '
                split_s = re.sub(r'(,\s+and\s+)', '. ', s, count=1)
                split_s = re.sub(r'(,\s+but\s+)', '. ', split_s, count=1)
                split_s = re.sub(r'(,\_while\s+)', '. ', split_s, count=1)
                crisp_sents.append(split_s)
            else:
                crisp_sents.append(s)
        sanitized_lines.append(" ".join(crisp_sents))
    cleaned = "\n".join(sanitized_lines)

    # 4. Replace abstract role tokens with target character names
    token_replacements = {
        "[COMPANION]": "Barnaby",
        "[COMPANION_A]": "Barnaby",
        "[COMPANION_B]": "Reggie",
        "[PROTAGONIST]": "Lord Reginald",
        "[FRIEND]": "Professor Thorne",
        "[ANTAGONIST]": "Inspector Higgins",
        "[AUNT_FIGURE]": "Lady Beatrice",
        "[DOG_COMPANION]": "Barnaby",
        "[UNCLE_FIGURE]": "Uncle Peters",
        "[DETECTIVE]": "Inspector Higgins",
    }
    for token, real_name in token_replacements.items():
        cleaned = cleaned.replace(token, real_name)

    # 5. Replace copyrighted character name leaks if present
    name_replacements = {
        "Father Brown": "Lord Reginald",
        "Flambeau": "Barnaby",
        "Jeeves": "Barnaby",
        "Bertie": "Reggie",
        "Lady Malvern": "Lady Beatrice",
        "Dr. Voules": "Professor Thorne",
        "Stella Maris": "Lady Beatrice",
    }
    for old_name, new_name in name_replacements.items():
        cleaned = re.sub(rf"\b{re.escape(old_name)}\b", new_name, cleaned)

    # 5. Clean extra blank lines and line whitespace
    lines = [line.strip() for line in cleaned.splitlines()]
    non_empty = []
    prev_blank = False

    for line in lines:
        if line:
            non_empty.append(line)
            prev_blank = False
        elif not prev_blank:
            non_empty.append("")
            prev_blank = True

    return "\n".join(non_empty).strip()
