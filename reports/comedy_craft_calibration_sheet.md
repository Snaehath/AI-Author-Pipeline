# Comedy Craft Annotation Calibration Sheet

> **Audit Instructions**: Review each AI annotation against the unabridged source passage.
> Check whether the primary mechanism, structural beats (setup/escalation/reversal/payoff),
> and tone match your literary judgment. Record your human ground truth in the blanks provided.

---

## Example 01 — `the_man_upstairs_ch14_01053`

**Source**: *The Man Upstairs* (Chapter 14)  
**Characters Identified**: Legrand  
**Dialogue Ratio**: `0.32` | **Surface Slang Isolated**: None  

### Passage
```text
"I am sure you must see the antennae. I made them as distinct as they are in the original insect, and I presume that is sufficient," But where are the antennae you spoke of?" "The antennae!" said Legrand, who seemed to be getting unaccountably warm upon the subject; "Well, well," I said, "perhaps you have - still I don't see them;" and I handed him the paper without additional remark, not wishing to ruffle his temper; but I was much surprised at the turn affairs had taken; his ill humor puzzled me - and, as for the drawing of the beetle, there were positively NO antennae visible, and the whole DID bear a very close resemblance to the ordinary cuts of a death's head.
```

### AI Extraction
- **Primary Mechanism**: `MISUNDERSTANDING` (Detector Confidence: `0.20`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: "I am sure you must see the antennae.
- **Escalation**: I made them as distinct as they are in the original insect, and I presume that is sufficient," But where are the antennae you spoke of?" "The antennae!" said Legrand, who seemed to be getting unaccountably warm upon the subject; "Well, well," I said, "perhaps you have - still I don't see them;" and I handed him the paper without additional remark, not wishing to ruffle his temper; but I was much surprised at the turn affairs had taken; his ill humor puzzled me - and, as for the drawing of the beetle, there were positively NO antennae visible, and the whole DID bear a very close resemblance to the ordinary cuts of a death's head.
- **Reversal**: Expectation upended.
- **Payoff**: I made them as distinct as they are in the original insect, and I presume that is sufficient," But where are the antennae you spoke of?" "The antennae!" said Legrand, who seemed to be getting unaccountably warm upon the subject; "Well, well," I said, "perhaps you have - still I don't see them;" and I handed him the paper without additional remark, not wishing to ruffle his temper; but I was much surprised at the turn affairs had taken; his ill humor puzzled me - and, as for the drawing of the beetle, there were positively NO antennae visible, and the whole DID bear a very close resemblance to the ordinary cuts of a death's head.

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 02 — `right_ho_ch15_06961`

**Source**: *Right Ho* (Chapter 15)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.69` | **Surface Slang Isolated**: None  

### Passage
```text
"As you know, you will have my money when I am gone; but until now I have never been able to see my way to giving you an allowance. I have now decided to do so - on one condition. I have written to a firm of lawyers in New York, giving them instructions to pay you quite a substantial sum each month. My one condition is that you live in New York and enjoy yourself as I have always wished to do. I want you to be my representative, to spend this money for me as I should do myself. I want you to plunge into the gay, prismatic life of New York. I want you to be the life and soul of brilliant supper parties," " Above all, I want you - indeed, I insist on this - to write me letters at least once a week giving me a full description of all you are doing and all that is going on in the city, so that I may enjoy at second-hand what my wretched health prevents my enjoying for myself.
```

### AI Extraction
- **Primary Mechanism**: `MISUNDERSTANDING` (Detector Confidence: `0.12`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: '"As you know, you will have my money when I am gone; but until now I have never ...'
- **Escalation**: Complication rises around misunderstanding: 'I have now decided to do so - on one condition....'
- **Reversal**: Expectation or status is inverted: 'My one condition is that you live in New York and enjoy yourself as I have alway...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'I want you to be the life and soul of brilliant supper parties," " Above all, I ...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 03 — `my_man_jeeves_ch9_10492`

**Source**: *My Man Jeeves* (Chapter 9)  
**Characters Identified**: Professor Some  
**Dialogue Ratio**: `0.62` | **Surface Slang Isolated**: None  

### Passage
```text
"And the week we went one of the turns was Professor Some One's Terpsichorean Cats. I recollect them distinctly. Now, are we narrowing it down, or aren't we? Reggie, I'm going round to the Coliseum this minute, and I'm going to dig the date of those Terpsichorean Cats out of them, if I have to use a crowbar," " So that got him within six days; for the management treated us like brothers; brought out the archives, and ran agile fingers over the pages till they treed the cats in the middle of May.
```

### AI Extraction
- **Primary Mechanism**: `MISUNDERSTANDING` (Detector Confidence: `0.12`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Professor Some establish scene context: '"And the week we went one of the turns was Professor Some One's Terpsichorean Ca...'
- **Escalation**: Complication rises around misunderstanding: 'I recollect them distinctly....'
- **Reversal**: Expectation or status is inverted: 'Now, are we narrowing it down, or aren't we?...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'Reggie, I'm going round to the Coliseum this minute, and I'm going to dig the da...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 04 — `jill_the_reckless_chNone_01895`

**Source**: *Jill The Reckless* (Chapter None)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.37` | **Surface Slang Isolated**: None  

### Passage
```text
The man had his mouth open and his hand raised to give an order which would certainly have sent Anne de Caylus from the world, when I cried passionately--it was my last chance, and I never wished to live more strongly than at that moment--I cried passionately, "Andrea Pallavicini, if such be your name, look at that!  Look at that!"  I repeated, shaking my open hand with the ring on it before his face, "and then hinder me if you dare! To-morrow if you have quarterings enough, I will see to your quarrel!  Now send me on my way, or your fate be on your own head!  Disobey--ay, do but hesitate--and I will call on these very men of yours to cut you down!"  It was a bold throw, for I staked all on a talisman of which I did not know the value!  To me it was the turn of a die, for I had had no leisure to look at the ring, and knew no more than a babe whose it was
```

### AI Extraction
- **Primary Mechanism**: `MISUNDERSTANDING` (Detector Confidence: `0.12`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: 'The man had his mouth open and his hand raised to give an order which would cert...'
- **Escalation**: Complication rises around misunderstanding: 'Look at that!"  I repeated, shaking my open hand with the ring on it before his ...'
- **Reversal**: Expectation or status is inverted: 'Now send me on my way, or your fate be on your own head!...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'To me it was the turn of a die, for I had had no leisure to look at the ring, an...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 05 — `a_damsel_in_distress_ch11_06131`

**Source**: *A Damsel In Distress* (Chapter 11)  
**Characters Identified**: Lord Wisbeach, Mr Pett, Mrs Crocker, Mrs Pett, Pett, Wisbeach  
**Dialogue Ratio**: `0.51` | **Surface Slang Isolated**: None  

### Passage
```text
Partridgite, was to be the result of a continuation of
experiments which his father had been working upon at the time of
his death. That Dwight Partridge had been trying experiments in
the direction of a new and powerful explosive during the last
year of his life was common knowledge in those circles which are
interested in such things. Foreign governments were understood to
have made tentative overtures to him. But a sudden illness,
ending fatally, had finished the budding career of Partridgite
abruptly, and the world had thought no more of it until an
interview in the _Sunday Chronicle_, that store-house of
information about interesting people, announced that Willie was
carrying on his father's experiments at the point where he had
left off. Since then there had been vague rumours of possible
sensational developments, which Willie had neither denied nor
confirmed. He preserved the mysterious silence which went so well
with his appearance. Having turned slowly so that his eyes rested on Lord Wisbeach's
ingenuous countenance, Willie paused, and his face assumed the
expression of his photograph in the _Chronicle_. "Ah, Wisbeach!" he said. Lord Wisbeach did not appear to resent the patronage of his
manner. He plunged cheerily into talk. He had a pleasant, simple
way of comporting himself which made people like him. "I was just telling Mrs. Pett," he said, "that I shouldn't be
surprised if you were to get an offer for your stuff from our
fellows at home before long. I saw a lot of our War Office men
when I was in England, don't you know. Several of them mentioned
the stuff." Willie resented Partridgite as being referred to as "the stuff,"
but he made allowance. All Englishmen talked that way, he
supposed. "Indeed?" he said. "Of course," said Mrs. Pett, "Willie is a patriot and would have
to give our own authorities the first chance." "Rather!" "But you know what officials are all over the world. They are so
sceptical and they move so slowly." "I know. Our men at home are just the same as a rule. I've got a
pal who invented something-or-other, I forget what, but it was a
most decent little contrivance and very useful and all that; and
he simply can't get them to say Yes or No about it. But, all the
same, I wonder you didn't have some of them trying to put out
feelers to you when you were in London." "Oh, we were only in London a few hours. By the way, Lord
Wisbeach, my sister--"--Mrs. Pett paused; she disliked to have to
mention her sister or to refer to this subject at all, but
curiosity impelled her--"my sister said that you are a great
friend of her step-son, James Crocker. I didn't know that you
knew him." Lord Wisbeach seemed to hesitate for a moment. "He's not coming over, is he? Pity! It would have done him a
world of good. Yes, Jimmy Crocker and I have always been great
pals. He's a bit of a nut, of course, . . . I beg your pardon!
. . . I mean . . ." He broke off confusedly, and turned to Willie
again to cover himself. "How are you getting on with the jolly
old stuff?" he asked. If Willie had objected to Partridgite being called "the stuff,"
he was still less in favour of its being termed "the jolly old
stuff." He replied coldly. "I have ceased to get along with the jolly old stuff." "Struck a snag?" enquired Lord Wisbeach sympathetically. "On the contrary, my experiments have been entirely successful. I
have enough Partridgite in my laboratory to blow New York to
bits!" "Willie!" exclaimed Mrs. Pett. "Why didn't you tell me before?
You know I am so interested." "I only completed my work last night." He moved off with an important nod. He was tired of Lord
Wisbeach's society. There was something about the young man which
he did not like. He went to find more congenial company in a
group by the window. Lord Wisbeach turned to his hostess. The vacuous expression had
dropped from his face like a mask. A pair of keen and intelligent
eyes met Mrs. Pett's. "Mrs. Pett, may I speak to you seriously?" Mrs. Pett's surprise at the alteration in the man prevented her
from replying. Much as she liked Lord Wisbeach, she had never
given him credit for brains, and it was a man with brains and
keen ones who was looking at her now. She nodded. "If your nephew has really succeeded in his experiments, you
should be awfully careful. That stuff ought not to lie about in
his laboratory, though no doubt he has hidden it as carefully as
possible. It ought to be in a safe somewhere. In that safe in
your library. News of this kind moves like lightning. At this
very moment, there may be people watching for a chance of getting
at the stuff." Every nerve in Mrs. Pett's body, every cell of a brain which had
for years been absorbing and giving out sensational fiction,
quivered irrepressibly at these words, spoken in a low, tense
voice which gave them additional emphasis. Never had she
misjudged a man as she had misjudged Lord Wisbeach. "Spies?" she quavered. "They wouldn't call themselves that," said Lord Wisbeach. "Secret
Service agents. Every country has its men whose only duty it is
to handle this sort of work." "They would try to steal Willie's--?" Mrs. Pett's voice failed. "They would not look on it as stealing. Their motives would be
patriotic. I tell you, Mrs. Pett, I have heard stories from
friends of mine in the English Secret Service which would amaze
you. Perfectly straight men in private life, but absolutely
unscrupulous when at work. They stick at nothing--nothing. If I
were you, I should suspect every one, especially every stranger."
He smiled engagingly. "You are thinking that that is odd advice
from one who is practically a stranger like myself. Never mind.
Suspect me, too, if you like. Be on the safe side." "I would not dream of doing such a thing, Lord Wisbeach," said
Mrs. Pett horrified. "I trust you implicitly. Even supposing such
a thing were possible, would you have warned me like this, if you
had been--?" "That's true," said Lord Wisbeach. "I never thought of that.
Well, let me say, suspect everybody but me." He stopped abruptly.
"Mrs. Pett," he whispered, "don't look round for a moment.
Wait." The words were almost inaudible. "Who is that man behind
you? He has been listening to us. Turn slowly." With elaborate carelessness, Mrs. Pett turned her head. At first
she thought her companion must have alluded to one of a small
group of young men who, very improperly in such surroundings,
were discussing with raised voices the prospects of the clubs
competing for the National League Baseball Pennant. Then,
extending the sweep of her gaze, she saw that she had been
mistaken. Midway between her and this group stood a single
figure, the figure of a stout man in a swallow-tail suit, who
bore before him a tray with cups on it. As she turned, this man
caught her eye, gave a guilty start, and hurried across the room. "You saw?" said Lord Wisbeach. "He was listening. Who is that
man? Your butler apparently. What do you know of him?" "He is my new butler. His name is Skinner." "Ah, your _new_ butler? He hasn't been with you long, then?" "He only arrived from England three days ago." "From England? How did he get in here? I mean, on whose
recommendation?" "Mr. Pett offered him the place when we met him at my sister's in
London. We went over there to see my sister, Eugenia--Mrs.
Crocker. This man was the butler who admitted us. He asked Mr.
Pett something about baseball, and Mr. Pett was so pleased that
he offered him a place here if he wanted to come over. The man
did not give any definite answer then, but apparently he sailed
on the next boat, and came to the house a few days after we had
returned." Lord Wisbeach laughed softly. "Very smart. Of course they had him planted there for the
purpose." "What ought I to do?" asked Mrs. Pett agitatedly. "Do nothing. There is nothing that you can do, for the present,
except keep your eyes open. Watch this man Skinner. See if he has
any accomplices. It is hardly likely that he is working alone.
Suspect everybody. Believe me . . ." At this moment, apparently from some upper region, there burst
forth an uproar so sudden and overwhelming that it might well
have been taken for a premature testing of a large sample of
```

### AI Extraction
- **Primary Mechanism**: `MISUNDERSTANDING` (Detector Confidence: `0.86`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.90`
- **Tone**: `LIGHT_SATIRICAL`
- **Setup**: Characters Lord Wisbeach, Mr Pett establish scene context: 'Partridgite, was to be the result of a continuation of
experiments which his fat...'
- **Escalation**: Complication rises around misunderstanding: '....'
- **Reversal**: Expectation or status is inverted: 'News of this kind moves like lightning....'
- **Payoff**: Comedic resolution or deadpan beat lands: '." At this moment, apparently from some upper region, there burst
forth an uproa...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 06 — `right_ho_ch1_08652`

**Source**: *Right Ho* (Chapter 1)  
**Characters Identified**: Lady Write, Mr Corcoran, Sir Quite  
**Dialogue Ratio**: `0.57` | **Surface Slang Isolated**: None  

### Passage
```text
"It is the way these New York apartments are constructed, sir. Quite unlike our London houses. The partitions between the rooms are of the flimsiest nature. With no wish to overhear, I have sometimes heard Mr. Corcoran expressing himself with a generous strength on the subject I have mentioned," " "How on earth did you know that he was fond of birds?" "Oh! Well?" "Why should not the young lady write a small volume, to be entitled - let us say - _The Children's Book of American Birds_, and dedicate it to Mr.
```

### AI Extraction
- **Primary Mechanism**: `STATUS_REVERSAL` (Detector Confidence: `0.57`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DRY_WIT`
- **Setup**: Characters Lady Write, Mr Corcoran establish scene context: '"It is the way these New York apartments are constructed, sir....'
- **Escalation**: Complication rises around status_reversal: 'Quite unlike our London houses....'
- **Reversal**: Expectation or status is inverted: 'With no wish to overhear, I have sometimes heard Mr....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'Well?" "Why should not the young lady write a small volume, to be entitled - let...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 07 — `my_man_jeeves_ch1_05572`

**Source**: *My Man Jeeves* (Chapter 1)  
**Characters Identified**: Lady Write, Mr Corcoran, Sir Quite  
**Dialogue Ratio**: `0.57` | **Surface Slang Isolated**: None  

### Passage
```text
"It is the way these New York apartments are constructed, sir. Quite unlike our London houses. The partitions between the rooms are of the flimsiest nature. With no wish to overhear, I have sometimes heard Mr. Corcoran expressing himself with a generous strength on the subject I have mentioned," " "How on earth did you know that he was fond of birds?" "Oh! Well?" "Why should not the young lady write a small volume, to be entitled - let us say - _The Children's Book of American Birds_, and dedicate it to Mr.
```

### AI Extraction
- **Primary Mechanism**: `STATUS_REVERSAL` (Detector Confidence: `0.57`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DRY_WIT`
- **Setup**: Characters Lady Write, Mr Corcoran establish scene context: '"It is the way these New York apartments are constructed, sir....'
- **Escalation**: Complication rises around status_reversal: 'Quite unlike our London houses....'
- **Reversal**: Expectation or status is inverted: 'With no wish to overhear, I have sometimes heard Mr....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'Well?" "Why should not the young lady write a small volume, to be entitled - let...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 08 — `the_man_upstairs_ch16_05512`

**Source**: *The Man Upstairs* (Chapter 16)  
**Characters Identified**: Legrand  
**Dialogue Ratio**: `0.43` | **Surface Slang Isolated**: None  

### Passage
```text
"you infernal black villain! - speak, I tell you! - answer me this instant, without prevarication! - which - which is your left eye?," "You scoundrel!" said Legrand, hissing out the syllables from between his clenched teeth - "Oh, my golly, Massa Will! aint dis here my lef eye for sartain?" roared the terrified Jupiter, placing his hand upon his RIGHT organ of vision, and holding it there with a desperate pertinacity, as if in immediate, dread of his master's attempt at a gouge.
```

### AI Extraction
- **Primary Mechanism**: `STATUS_REVERSAL` (Detector Confidence: `0.44`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DRY_WIT`
- **Setup**: Characters Legrand establish scene context: '"you infernal black villain!...'
- **Escalation**: Complication rises around status_reversal: '- speak, I tell you!...'
- **Reversal**: Expectation or status is inverted: '- answer me this instant, without prevarication!...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'aint dis here my lef eye for sartain?" roared the terrified Jupiter, placing his...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 09 — `the_inimitable_jeeves_ch44_05272`

**Source**: *The Inimitable Jeeves* (Chapter 44)  
**Characters Identified**: Append, April, Aug, Chron, Cleop, Const, Cornhill, Dec, Dorothy, Dr Temple, Eliz, Feb, For, Hist, Holborn, Introd, Islington, Jan, June, Lady Abbess, Lady Jane, Lady Marie, London, Lord Bacon, Lord Lieutenant, Lord Lisle, Lord Maior, Lord Mayor, Lord Mayre, Lord Protector, Lord Scales, Mar, March, May, Mr Froude, Nos, Nov, Oct, Oxford, Pref, Preface, Sept, Shambles, Sir Arthur, Sir Christopher, Sir Edmund, Sir Edward, Sir Francis, Sir Henry, Sir John, Sir Ralph, Sir Richard, Sir Rowland, Sir Thomas, Sir William, Sunday, Vitell, William, Yorks  
**Dialogue Ratio**: `0.49` | **Surface Slang Isolated**: right ho  

### Passage
```text
Book I, fo. 103b. In 1417 the mayor and aldermen ordained that the
      rector of St. Peter's for the time being should in future take
      precedence of the rectors of all other city churches, on the ground
      that Saint Peter's was the first church founded in the city of
      London, having been built in 199 by King Lucius, and for 400 years
      or more held the metropolitan chair.--Letter Book I, fo. 203.
      (Memorials, pp. 651-653.) _Cf._ Journal 1, fo. 21b. M397 Further proceedings against Oldcastle and the Lollards, 1413. 750 "Eminentissima turris Ecclesię Anglicanę et pugil invictus Dominus
      Thomas de Arundelia."--Hist. Angl. ii, 300. M398 Meeting of Lollards in St. Giles' Fields, 12 Jan., 1414. 751 A certain William Fyssher, a _parchemyner_ or parchment-maker of
      London, was afterwards (1416) convicted of assisting in Oldcastle's
      escape, and was executed at Tyburn.--Letter Book I, fo. 181b.
      (Memorials, p. 641.) 752 Walsingham, ii, 292-299; Fasc. Zizan. (Rolls Series No. 5), 433-449;
      Chron. of London (ed. by Sir H. Nicolas), p. 97. 753 Letter Book I, fos. 286-290. M399 The last Statute against the Lollards, 1414. 754 2 Hen. V. Stat. i, c. 7. 755 It was not, however, the last occasion upon which parliamentary
      action was attempted. In 1422, and again in 1425, the Lollards were
      formidable in London, and parliament on both occasions ordered that
      those who were in prison should be delivered at once to the
      Ordinary, in accordance with the provisions of this Statute.--Stubbs,
      Const. Hist., iii, 81, 363. M400 The king's offer of pardon refused by Oldcastle, 1415. 756 Letter Book I, fo. 147. 757 Walsingham, ii, 306, 307. M401 Trial and execution of Cleydon, a Lollard, 1415. 758 Hist. Angl., ii, 307. 759 Letter Book I, fol. 154. 760 See letter from the mayor to the king, giving an account of
      Cleydon's trial, 22nd August, 1415.--Letter Book I, fo. 155.
      (Memorials, p. 617). Foxe, "Acts and Monuments," iii, 531-534. M402 Oldcastle taken and executed, 1417. 761 Walsingham, ii, 327, 328. 762 Engl. Chron. (Camd. Soc., No. 64), p. 46; Chron. of London
      (Nicolas), p. 106. 763 Stubbs, Const. Hist., iii., 363, 364. M403 Preparations for the invasion of France, 1414-1415.
 M404 A question of precedence in the city. 764 Letter Book I, fo. 150. This "very antient memorandum" of the Lord
      Mayor's precedence in the City was submitted to Charles II in 1670,
      when that monarch insisted upon Sir Richard Ford, the Lord Mayor of
      the day, giving "the hand and the place" to the Prince of Orange
      (afterwards William III of England), on the occasion of the prince
      being entertained by the City.--Repertory, 76, fos. 28b, 29. 765 Letter Book I, fo. 158b. (Memorials, p. 613). 766 -_Id._, fo. 157. M405 The king takes leave of the citizens on Blackheath, June, 1415. 767 Gregory's Chron. (Camd. Soc, N.S., No. 17), pp. 108-109. Gregory was
      an alderman of the City, and an eye-witness of much that he relates. 768 Letter dated 2nd August--the day on which Sir Thomas Grey, one of the
      chief conspiritors was executed.--Letter Book I, fo. 180. M406 The capture of Harfleur, 18 Sept., 1415. 769 Letter Book I, fo. 143. (Memorials, p. 619). M407 Volunteers for service in France required, Oct., 1415.
 M408 Citizens invited to reside in Harfleur. 770 Letter Book I, fo. 177. M409 Joy in the city at the news of the battle of Agincourt, Oct., 1415.
 M410 The citizens welcome the king on his return from France. 771 Letter Book I, fo. 159. (Memorials, pp. 620, 622). 772 "Quali gaudio, quali tripudio, quali denique triumpho, sit acceptus
      a Londoniensibus, dicere prętermitto. Quia revera curiositas
      apparatumn, nimietas expensarum, varietates spectaculorum, tractatus
      exigerent merito speciales."--Walsingham, ii, 314. 773 Chron. of London (Nicolas), p. 103. M411 Preparations for another expedition, 1416-1417. 774 Letter Book I, fo. 178b. Other proclamations on the same subject are
      recorded in the same place, most of which will be found in
      "Memorials" (pp. 627-629). 775 Letter Book I, fo. 190b. 776 -_Id._, fos. 188, 188b. M412 City loans, 1417. 777 Letter Book I, fo. 191b. 778 Letter Book I, fo. 218b. In May, 1419, the sword was surrendered,
      and the security changed to one on wool, woolfells, &c.--_Id._, fo.
      227b. M413 Letter from the king to the City announcing his success, 9 Aug.,
      1417.
 M414 Another letter informing them of the capture of Caen, 5 Sept. 779 Letter Book I, fo. 229. (Memorials, p. 654.) 780 Journal 1, fo. 30b. 781 Letter Book I, fo. 200b. (Memorials, p. 657.) 782 Letter, dated Caen, 11 September.--Letter Book I, fo. 200b. M415 Proclamation by the Duke of Bedford, 18 Oct.
 M416 Supplies granted by parliament, Dec, 1417. 783 Writ, dated 18th Oct.--Letter Book I, fo. 203. 784 Stubbs, Const. Hist., iii, 89. 785 Letter Book I, fo. 222. M417 Henry's conquest of Normandy, 1417-1419. 786 Letter Book I, fos. 211b, 212b, 217. Proclamations made by the civic
      authorities at this time were subscribed "Carpenter"--the name of the
      Common Clerk or Town Clerk of the City. The custom of the Town Clerk
      of London for the time being, signing official documents of this
      kind with his surname alone, continues at the present day. 787 Letter Book I, fo. 215b. 788 Letter Book I, fo. 216. (Memorials, p. 664). 789 Letter Book I, fo. 216. On the 15th September the question of
      payment to the brewers, wine drawers and turners of the cups was
      considered.--Journal I, fo. 48. (Memorials, pp. 665, 666). 790 Gregory's Chron. (Camd. Soc, N.S., No. 17), 1222. 791 Letter Book I, fos. 236, 236b. M418 The king's letter to the City, 17 Aug., 1419. 792 Letter Book I, fo. 237. (Memorials, p. 674). M419 The treaty of Troyes, 20 May. 1420. 793 -_Id._, fo. 241b. 794 Letter Book I, fo. 252. 795 Walsingham, ii, 335. M420 The king's letter to the City, 12 July, 1420.
 M421 The mayor's reply, 2 Aug. 796 Letter Book I, fo. 263. M422 The queen's coronation. 797 Letter Book I, fo. 259.  According to Walsingham (ii, 336), the
      ceremony took place on the _first_ Sunday in Lent. 798 Walsingham, ii, 336, 337. M423 Henry's last expedition, and death, Aug., 1422. 799 Parliament voted a fifteenth and a tenth to assist the king in his
      necessities; John Gedney, alderman, John Perneys, John Bacon,
      grocer, and John Patesley, goldsmith, being appointed commissioners
      to levy the same within the City.--Letter Book I, fo. 277b. 800 Letter Book K, fo. 1b. M424 Rivalry between Bedford and Gloucester, 1422. 801 Letter Book I, fo. 282b. 802 Letter Book I, fo. 282b; Letter Book K, fo. 12. 803 Letter Book K, fo. 2. 804 Stubbs, Const. Hist., iii, 97. M425 An expedition to start for France, 1 March, 1423. 805 Letter Book K, fos. 10, 10b. M426 Sir John Mortimer. 806 -_Id._, fo. 15b. M427 The debts of Henry IV. 807 Letter Book K, fos. 10-18. M428 Gloucester and Beaufort, 1425-1428. 808 Chron. London (Nicolas), p. 114; Gregory's Chron. (Camd. Soc., N.S.,
      No. 17), p. 159; Engl. Chron. (Camd. Soc., No. 64), pp. 53, 54. 809 See two letters from the mayor.--Letter Book K, fos. 18b, 21. 810 Gregory's Chron., p. 160. M429 End of the quarrel between Gloucester and Beaufort. 811 -_Id._, p. 162. M430 Gloucester loses the favour of the citizens. 812 Journal 2, fos. 22b, 64b (new pagination). 813 Letter Book K, fo. 50b. M431 The siege of Orleans, 1428-1429. 814 Gregory's Chron., p. 161. 815 Letter Book K, fo. 55b. M432 Famine in London, 1429. 816 Letter Book K, fos. 62, 63b; Gregory's Chron., p. 164. M433 Beaufort joins Bedford in France. 817 Letter Book K, fo. 66b; Gregory's Chron., p. 164. M434 Allowances made to those representing the City in parliament, 1429. 818 Letter Book K, fo. 68b. In 1443 the Common Council agreed to allow
      the City members their reasonable expenses out of the chamber
      (Journal 5, fo. 129b), but when parliament met at Coventry in 1459,
      the City members were allowed 40_s._ a day, besides any
      disbursements they might make in the City's honour (Journal 6, fo.
      166b), and the same allowance was made in 1464, when parliament sat
      at York (Journal 7, fos. 52, 54). M435 The coronation of Henry VI, 6 Nov., 1429. 819 -_Id._, fo. 69b. 820 Gregory's Chron., pp. 164-168. 821 City Records, Liber Dunthorn, fo. 61b; Letter Book K, fo. 70. 822 Cal. of Wills, Court of Husting, London, ii, 509. M436 Sets out for France, April, 1430.
 M437 And is crowned in Paris, Dec., 1431. 823 Letter Book K, fo. 84. 824 A long account of his entry into the French capital, and of the
      pageantry in honour of the occasion, is set out in full in the
      City's Records.--Letter Book K, fos. 101b-103. M438 The citizens welcome him on his return, 1432.
 M439 The mayor and aldermen present him with a gift of £1,000. 825 A full descriptive account of Henry's reception on his return from
      France is set out in the City Records (Letter Book K, fos.
      103b-104b). It purports to be an account sent by John Carpenter, the
      Town Clerk, to a friend, and has been printed at the end of the
      _Liber Albus_ (Rolls Series); _Cf._ Gregory's Chron., pp. 173-175. M440 Gloucester's attacks on Beaufort and Bedford, 1432-1433. 826 He informed the City of his intention by letter, dated from Ghent
      the 13th April.--Letter Book K, fo. 105. 827 Stubbs, Const. Hist., iii, 114-117. M441 Financial reform, 1433. 828 Letter Book K, fo. 137b. 829 Letter Book K, fo. 138. M442 The death of Bedford, 14 Sept., 1435. 830 Gregory's Chron., p. 177. M443 Calais appeals to London for assistance, 27 June, 1436. 831 Letter Book K, fo. 148. 832 "And that same yere (1437), the Mayre of London sende, by the good
      a-vyse and consent of craftys, sent sowdyers to Calys, for hyt was
      sayde that the Duke of Burgone lay sege unto Calis."--Gregory's
      Chron. p. 178. 833 Letter Book K, fos. 160-162. 834 Gregory's Chron. p. 179. M444 A tax imposed on aliens, 1439. 835 Letter Book K. fo. 183b. The tax was found to be so successful that
      it was subsequently renewed. In 1453 it was renewed for the king's
      life.--_Id._, fo. 280b. M445 The penance of Eleanor Cobham, Gloucester's wife, 1441. 836 Journal 3, fo. 103b. 837 Chron. of London (Nicolas), p. 129. M446 The king's charter to the City, 26 Oct., 1444. 838 The validity as well as the effect of this charter (which is
      preserved in the Town Clerk's office) has been made the subject of
      much controversy, some contending that it is in effect a grant of
      the soil of the river from Staines to Yantlet, that being the extent
      of the City's liberties on the Thames, whilst others restrict the
      grant to the City's territorial limits, _i.e._, from Temple Bar to
      the Tower. 839 Letter Book K, fo. 220b. M447 Henry's marriage with Margaret of Anjou, 22 April, 1445. 840 Chron. of London (Nicholas), p. 134. M448 Jack Cade's rebellion, 1450. 841 See "Historical Memoranda," by Stow, printed in "Three Fifteenth
      Cent. Chron." (Camd. Soc., N.S., No. 28), pp. 94-99. 842 "And the Meire of London with the comynes of the city came to the
      kynge besekynge him that he wolde tarye in the cite, and they wolde
      lyve and dye with him, and pay for his costes of householde an halff
      yere; but he wold nott, but toke his journey to
      Kyllyngworthe."--"Three Fifteenth Cent. Chronicles" (Camd. Soc.), p.
      67. M449 The city prepares to defend itself. 843 Journal 5, fo. 36b. 844 Journal 5, fo. 39. 845 He had been admitted alderman of Lime Street ward in 1448, at the
      king's special request, and had only recently been
      discharged.--Journal 4, fo. 213b; Journal 5, fo. 38b. In 1461 he left
      England, but was captured at sea by the French and put to ransom for
      4,000 marks.--Fabyan, p. 638. 846 Holinshed, iii, 224. 847 Gregory's Chron., p. 192. 848 Journal 5, fo. 40b. M450 Mock trials held by the rebels at the Guildhall.
 M451 Cade apprehended. 849 Alexander Iden, who appears to have pursued Cade beyond the limits
      of his own jurisdiction, as Sheriff of Kent, into the neighbouring
      county of Sussex, where the rebel was apprehended in a garden at
      Heathfield.--"Three Fifteenth Cent. Chron.," preface, p. vii. M452 The question of the succession to the throne.
 M453 Rivalry between the Dukes of York and Somerset, 1450. 850 The exclusion of the Duke and other nobles from the king's council
      had been made an express ground of complaint by the Kentish
      insurgents. 851 Chron., p. 196. M454 Civil war averted. 852 "And so thei brought (the duke) ungirt thurgh London bitwene ij
      bisshoppes ridyng unto his place; and after that made hym swere at
      Paulis after theire entent, and put him frome his good peticions
      which were for the comoen wele of the realme."--Chron. of London
      (Nicolas), p. 138. M455 The king's illness, 1453. 853 Journal 5, fos. 131, 132b, 133b. M456 The City again called upon to assist in the defence of Calais,
      1453-1454. 854 Journal 5, fos. 134b, 135b, 136. 855 -_Id._, fo. 148. 856 -_Id._, fo. 152. 857 -_Id._, fo. 152b. 858 -_Id._, fos. 183, 184. 859 Journal 5, fo. 206. 860 Report of City Chamberlain to the Court of Common Council.--Journal
      5, fos. 227-228b. M457 The Duke of York and his supporters take up their quarters in the
      city, 1454. 861 News-letter of John Stodeley, 19 Jan., 1454; Paston Letters
      (Gairdner), i, 265, 266. 862 Journal 5, fos 143, 145b, 152, 152b-160b. M458 The Duke of York nominated protector, 1454. 863 Journal 5, fo. 150. 864 -_Id._, fos. 162, 162b. 865 -_Id._, fo. 164b. M459 The first battle of St. Albans, 22 May, 1455.
 M460 A rising against the Lombards in the city, May, 1456. 866 Booking to Paston, 15 May; Paston Letters (Gairdner), i, 387; _Cf._
      Chron. of London (Nicolas), p. 139; Gregory's Chron., p. 199. 867 William Cantelowe, alderman of Cripplegate and Billingsgate wards,
      from the latter of which he was discharged in October, 1461, on the
      score of old age and infirmity (Journal 6, fo. 81b). He appears in
      his time to have had financial dealings with the crown, on one
      occasion conveying money over sea for bringing Queen Margaret to
      England, and on another supplying gunpowder to the castle of
      Cherbourg, when it was in the hands of the English. He is thought by
      some to be identical with the William Cantelowe who afterwards (in
      1464) captured Henry VI in a wood in the North of England.--"Three
      Fifteenth Cent. Chron." (Camd. Soc, N.S., No. 28), Preface, p. viii. 868 Short English Chron. (Camd. Soc., N.S., No. 28), p. 70. M461 Letter from the king for safe-guarding the city, 3 Sept., 1456. 869 Letter Book K, fo. 287. M462 The citizens offer to man and victual ships to punish France, 1457. 870 -_Id._, fo. 288b. M463 A general reconciliation at St. Paul's, 25 March, 1458. 871 Cotton MS., Vitell. A, xvi, fo. 114. 872 Engl. Chron., 1377-1461 (Camd. Soc., No. 64), p. 77. 873 Fabyan, Chron. (ed. 1811), p. 633; _Cf._ Chron. of London (Nicolas),
      p. 139. M464 Warwick implicated in a riot, Nov., 1458.
 M465 Seeks refuge in the city.
 M466 Leaves for Calais. 874 Journal 6, fos. 138, 138b, 139. 875 Engl. Chron., 1377-1461 (Camd. Soc., No. 64), p. 78; _Cf._ Fabyan,
      p. 633; Holinshed, iii, 249. M467 Riot between citizens and Templars, April, 1459. 876 Short Engl. Chron. (Camd. Soc., N.S., No. 28), p. 71; Chron. of
      London (Nicolas), p. 140. M468 The battle of Blore Heath, 23 Sept., 1459.
 M469 Parliament at Coventry, 20 Nov., 1459. 877 Journal 6, fo. 166. 878 -_Id._, fo. 145. M470 The king loses favour. 879 -_Id._, fo. 163. 880 English Chron., 1377-1461 (Camd. Soc., No. 64), p. 179. M471 Unconstitutional conduct of the king in issuing commissions to raise
      an army, Jan., 1460.
 M472 A deputation from the City waits upon the king at Northampton.
 M473 The City's liberties not to be prejudiced. 881 Journal 6, fo. 224b. 882 William Paston, writing to his brother John, under date 28th
      January, 1460, remarks, "Item, the kyng cometh to London ward, and,
      as it is seyd, rereth the pepyll as he come; but it is certayn ther
      be comyssyons made in to dyvers schyres that every man be redy in
      his best aray to com when the kyng send for hem."--Paston Letters
      (Gairdner), i, 506. 883 Paston Letters (Gairdner), Introd., p. cxl. 884 The king's letter, dated 2 Feb., was read before the Common Council
      on the 5 Feb.--Letter Book K, fo. 313b; Journal 6, fo. 196b. M474 Military precautions taken by the City, Feb., 1460. 885 Journal 6, fo. 197b. 886 -_Id._, fo. 203b. 887 -_Id._, fo. 158. M475 Landing of the confederate earls.
 M476 The Common Council determine to oppose their entrance to the city,
      27 June, 1460. 888 Journal 6, fo. 237. 889 It had been destroyed by fire during the Kentish outbreak.--Gregory's
      Chron., p. 193. 890 Journal 6, fo. 237b. M477 Meeting of Common Council on Sunday, 29 June. 891 Journal 6, fo. 238. 892 -_Id._, fo. 238b. M478 The Yorkist earls admitted into the city, 2 July, 1460. 893 Journal 6, fos. 239, 239b; Eng. Chron., 1377-1461 (Camd. Soc. No.
      64), p. 94. M479 The Tower holds out. 894 Journal 6, fo. 252b. 895 Eo quod nullus alius modus videtur esse tutus pro civitate.--_Id._,
      fo. 251. 896 Journal 6, fo. 251b. M480 The Tower surrendered, 19 July.
 M481 Murder of Lord Scales. 897 -_Id._, fo. 250b. 898 Eng. Chron. (Camd. Soc., No. 64), p. 98. The Thames boatmen and
      sailors were almost as powerful and troublesome a body of men as the
      London apprentices. The Common Council had recently (11th July)
      endeavoured to subdue their turbulent spirit by the distribution
      among them of a large sum of money (£100).--Journal 6, fo. 254. M482 Battle of Northampton, 10 July, 1460. 899 On the 4th July the Common Council voted the earls the sum of £1,000
      by way of loan.--Journal 6, fo. 253. 900 Journal 6, fo. 256. By some inadvertence two copies of the agreement
      were sealed, one of which was returned to the mayor to be cancelled. M483 Measures for restoring confidence in the city. 901 Journal 6, fo. 257. M484 Parliament of 7 Oct., 1460.
 M485 The Duke of York's claim to the throne allowed.
 M486 The Livery Companies declare their allegiance to the king. 902 Gregory's Chron., p. 208; Engl. Chron., pp, 99-100; Short Engl.
      Chron., p. 75. 903 The interview with the wardens of the companies took place at a
      Common Council held on the 13th December, 1460.--Journal 6, fo. 282b. M487 The battle of Wakefield, 29 Dec., 1460.
 M488 The second battle of St. Albans, 17 Feb., 1461. 904 Journal 6, fo. 13. 905 The governing body in the city was still Lancastrian at heart. On
      the 13th Feb. the Common Council had voted Henry, at that time in
      the hands of Warwick, a loan of 1,000 marks, and a further sum of
      500 marks (making in all £1,000) for the purpose of _garnysshyng_
      and safeguarding the city. On the 24th a certain number of aldermen
      and commoners were deputed to answer for the safe custody of the
      Tower, and on the following day (25 Feb.) the mayor forbade, by
      public proclamation, any insult being offered to Sir Edmund Hampden
      and others, who had been despatched by the king and queen to London
      for the purpose of ascertaining "the true and faithful disposition"
      of the city.--Journal 6, fos. 35, 35b, 40. M489 The Earls of March and Warwick admitted into the city, Feb., 1461. 906 Gregory's Chron., p. 215. M490 Edward's claim to the crown recognised, 1 March, 1461. 907 Stubbs, Const. Hist., iii, 189. 908 Journal 6, fo. 37b. M491 The accession of King Edward IV, March, 1461. 909 Letter Book L, fo. 4; Lib. Dunthorn, fo. 62; Journal 7, fo. 98. 910 Short English Chron. (Camd. Soc., N.S., No. 28), p. 80. 911 Journal 7, fos. 97b, 98. M492 Edward's first charter to the city, 26 Aug., 1461. 912 Charter, dat. Winchecombe, 26 Aug., 1461. Preserved at the Guildhall
      (Box No. 28). M493 Second charter of Edward IV, 25 March, 1462. 913 Inspeximus charter, dated Westminster, 25 March, 1462.  Preserved at
      the Guildhall (Box No. 13). M494 City Loans, 1462. 914 Journal 7, fo. 8. 915 -_Id._, fo. 15. 916 See Inspeximus charter 15 Charles II. M495 The king's reception in the city on his return from the North, Feb.,
      1463. 917 Journal 7, fo. 21b. M496 Estrangement of Warwick, 1464-1468.
 M497 Alliance between England and Burgundy, 1468. 918 Journal 7, fo. 175. M498 Renewal of the civil war, 1469. 919 Ancestor of Lord Bacon and others of the nobility.--See Orridge
      "Citizens and their Rulers," p. 222. 920 Fabyan, p. 656. He was deprived of his aldermanry (Broad Street
      Ward) by the king's orders.--Journal 7, fo. 128. 921 Journal 7, fos. 196, 198, 199. 922 Journal 7, fos. 215b, 222b. 923 -_Id._, fos. 229b, 230b. M499 Flight of Edward and restoration of Henry VI, Oct., 1470. 924 -_Id._, fo. 222b. 925 A record of what took place in the city between the 1st and 6th
      October is set out in Journal 7, fo. 223b. 926 -_Id._, fo. 225. 927 He had, after Warwick's flight to France in March of this year, put
      to death and impaled twenty of the earl's followers.--Warkworth's
      Chron. (Camd. Soc., No. 10), p. 9. 928 Journal 7, fo. 225. M500 Sir Thomas Cooke or Coke, late alderman. 929 Fabyan Chron., p. 660. M501 Edward recovers the throne, April, 1471. 930 Warkworth's Chron. (Camd. Soc., No. 10), p. 15.--According to the
      chronicler, the _Commons_ of the city were still loyal to Henry,
      whom Archbishop Nevill had carried through the streets, weak and
      sickly as he was, in the hope of exciting the sympathy of the
      burgesses. Had the archbishop been a true man, "as the Commons of
      London were," Edward would not have gained an entry into the city
      until after the victory of Barnet-field. M502 The Kentish rising under "bastard" Fauconberg, May, 1471.
 M503 Attack made on the City. 931 Journal 5, fos. 152, 175. 932 The "bastard's" letter and the reply of the mayor and aldermen are
      set out in Journal 8, fos. 4b-6b, and Letter Book L, fo. 78. 933 Holinshed, iii, 323; Fabyan, p. 662.--According to Warkworth (p. 19),
      the _Commons_ would willingly have admitted the rebels had the
      latter not attempted to fire Aldgate and London Bridge. 934 Paston Letters, iii, 17. M504 Edward's return to London, and death of Henry VI, May, 1471. 935 The 21st May is the day usually given as that on which Edward
      returned. The City's Journal, however, gives the day as the Eve of
      the Ascension, that festival falling on May the 23rd.--Journal 8, fo.
      7. 936 Warkworth's Chron., p. 21. 937 Namely, Richard Lee, Matthew Philip, Ralph Verney, John Young,
      William Tailour, [COMPANION_B] Irlond, William Hampton, Bartholomew James,
      Thomas Stalbrok, and William Stokker.--Journal 8, fo. 7. 938 Journal 7, fo. 246. M505 Birth of Edward V. 939 -_Id._, 8, fo. 98. M506 The invasion of France, 1475. 940 -_Id._, fo. 101. 941 Journal 8, fo. 110b. M507 Edward and the citizens. 942 Preserved at the Guildhall (Box No. 28). 943 Journal 8, fo. 244. 944 Fabyan, p. 667. M508 A famine threatened, 1482. 945 Proclamation, dated 21 Nov., 22 Edw. IV.--Letter Book L, fo. 281b;
      Journal 9, fo. 2. M509 Edward's last parliament, 1483. 946 Journal 9, fo. 12. 947 -_Id._, fo. 14. 948 -_Id._, fo. 14b. M510 Preparations for the coronation of Edward V. 949 -_Id._, fos. 18, 18b. 950 Journal 9, fo. 21b. 951 The oath taken by Gloucester to King Edward V, as well as the oath
      which he was willing to take to the queen, if she consented to quit
      Westminster, were read before the Common Council on the 23rd
      March.--Journal 9, fo. 23b. M511 Shaw's sermon at Paul's Cross, Sunday, 22 June, 1483.
 M512 The Duke of Buckingham at the Guildhall, 24 June, 1483. 952 Wife of Matthew Shore, a respectable goldsmith of Lombard Street:-- "In Lombard-street, I once did dwelle,
        As London yet can witness welle;
        Where many gallants did beholde
        My beautye in a shop of golde." (_Percy Reliques_). She had recently been made to do penance by Gloucester in a white
      sheet for practising witchcraft upon him; but her unhappy position,
      as well as her well-known charity in better days, gained for her
      much sympathy and respect. 953 The duke's speech, interesting as it is, as showing the importance
      attached to gaining the favour of the City, cannot be regarded as
      historical.--Stubbs, Const. Hist., iii, 224 note. M513 The deposition of Edward V, 26 June, 1483.
 M514 The coronation of Richard III, 6 July, 1433. 954 Journal 9, fo. 27. 955 Journal 9, fo. 33b. The names of the citizens selected for that
      honour are recorded.--_Id._, fo. 21b. The names also of those who
      attended coronations in the same capacity down to the time of [COMPANION_B]
      IV are, with one exception (the coronation of Charles I), entered in
      the City's archives.--(See Report on Coronations, presented to Co.
      Co., 18 Aug., 1831. _Printed_.) 956 -_Id._, fo. 43. 957 -_Id._, fo. 114b. M515 Rebellion of the Duke of Buckingham, 1483.
 M516 His execution, 2 Nov.
 M517 The king's reception in the city, Nov., 1483.
 M518 Bold speech of the Londoners. 958 Journal 9, fo. 39. 959 Green, Hist. of the English People, ii, 63. M519 Richard's Parliament, Jan., 1484. 960 Stat. 1 Richard III, c. 9. 961 -_Id._, c. 2. M520 Expected invasion of Henry of Richmond, 1484. 962 Journal 9, fo. 43b. 963 Journal 9, fo. 56. 964 Cotton MS. Vitellius A, xvi, fo. 140. M521 Richard defeated and slain at Bosworth, 22 Aug., 1485. 965 Journal 9, fos. 78b, 81. Richard issued a proclamation against Henry
      "Tydder" on the 23 June, calling upon his subjects to defend
      themselves against his proposed attack.--Paston Letters (Gairdner),
      iii, 316-320. 966 Journal 9, fos. 81b-83b. M522 Henry VII escorted to the city. 967 Journal 9, fos. 84, 85b, 86b; _Cf._ "Materials illustrative of the
      reign of Henry VII" (Rolls Series, No. 60), i, 4-6. 968 Holinshed, iii, 479. M523 The sweating sickness, Sept.-Oct., 1485. 969 Hecker's "Epidemics of the Middle Ages," p. 168. 970 Journal 9, fo. 87b. 971 The day for election of mayor varied; at one time it was the Feast
      of the Translation of S. Edward (13 Oct.), at another the Feast of
      SS. Simon and Jude (28 Oct.). 972 Journal 9, fo. 88. 973 -_Id._, fo. 78b. 974 -_Id._, fo. 89b. M524 A City loan of £2,000. 975 Holinshed, iii, 482, 483; Cotton MS. Vitellius A, xvi, fo. 141b.
      According to Fabyan (p. 683), the Mercers, Grocers and Drapers
      subscribed nearly one half of the loan. M525 Henry's marriage with Elizabeth of York, Jan., 1486. 976 Pol. Verg., 717; "Materials illustrative of the reign of Henry VII"
      (Rolls Series, No. 60), i, 3. 977 Gairdner's "Henry the Seventh" (Twelve English Statesmen Series), p.
      47. No record of this appears in the City's archives. M526 The insurrection of Lambert Simnel, 1487.
 M527 City gifts to the king, June and July, 1487. 978 Journal 9, fos. 150b, 151. 979 -_Id._, fo. 151. M528 The king escorted to London, Oct., 1487.
 M529 The City's gift to the queen at her coronation, 25 Nov., 1487. 980 He arrived on the 3rd Nov.--Gairdner, p. 57. 981 Journal 9, fos. 157b, 158. 982 -_Id._, fo. 161. M530 Henry VII and Brittany, 1488-1492. 983 Journal 9, fo. 223b; Cotton MS. Vitellius A, xvi, fo. 142b; Fabyan,
      p. 683; Holinshed, iii, 492. M531 Parliamentary supplies and City loans. 984 Henry's second parliament was summoned to meet the 9th Nov., 1487.
      The names of the City's representatives have not come down to us,
      but we know that William White, an alderman, was elected one or the
      members in the place of Thomas Fitz-William, who was chosen member
      for Lincolnshire, and we have the names of six men chosen to
      superintend the City's affairs in this parliament (_ad prosequendum
      in parliamento pro negociis civitatis_), viz:--William Capell,
      alderman, Thomas Bullesdon, Nicholas Alwyn, Simon Harrys, William
      Brogreve, and Thomas Grafton.--Journal 9, fo. 224. 985 Holinshed, iii, 492. 986 Journal 9, fo. 273b. 987 Fabyan, p. 684. M532 Perkin Warbeck conspiracy, 1496-1497.
 M533 The city put into a state of defence. 988 Journal 10, fos. 80b, 83; Repertory 1, fos. 10b, 13. The
      "Repertories"--containing minutes of the proceedings of the Court of
      Aldermen, distinct from those of the Common Council--commence in
      1495. 989 Repertory 1, fo. 19b. 990 Two years later, when the post was held by Arnold Babyngton,
      complaint being made of the noisome smell arising from the burning
      of bones, horns, shavings of leather, &c., in preparing food for the
      City's hounds, near Moorgate, the Common Hunt was allowed a sum of
      26_s._ 8_d._ in addition to his customary fees for the purpose of
      supplying wood for the purpose.--Repertory 1, fo. 70. The office was
      maintained as late as the year 1807, when it was abolished by order
      of the Common Council.--Journal 84, fo. 135b. 991 Repertory 1, fo. 20b. 992 -_Id._, fos. 20, 20b. M534 The rebels defeated at Blackheath, 22 June, 1497.
 M535 Perkin Warbeck in Cornwall.
 M536 Surrenders to the king's forces and is brought prisoner to London,
      Oct., 1498.
 M537 Is executed at Tyburn, 1499. 993 Journal 10, fo. 104b. 994 -_Id._, fo. 105. 995 -_Id._, fo. 108. 996 Fabyan, p. 687. M538 Visit of Henry VIII as a boy to the city, 30 Oct., 1498. 997 Cotton MS. Vitellius A, xvi, fo. 176. M539 His speech. 998 Repertory 1, fo. 41b. M540 Negotiations for a marriage between Prince Arthur and Catherine of
      Aragon.
 M541 Preparations for reception of the princess, Nov., 1499. 999 Repertory 1, fo. 62. 1000 Journal 10, fo. 187b. M542 Death of an infant prince, June, 1500. 1001 Journal 10, fo. 190b. 1002 -_Id._, fo. 191. M543 The marriage of Prince Arthur with Catherine of Aragon, 14 Nov.,
      1501. 1003 This is the date given by Gairdner (p. 198).  According to Fabyan
      (p. 687) she arrived on the 4th Oct. 1004 Journal 10, fos. 238, 238b. M544 More rejoicings in the city, March, 1503 1005 Repertory 1, fos. 122b-126. The account will be found in Archęol.,
      vol. xxxii, p. 126. 1006 Repertory 1, fos. 130, 130b. M545 Charter of Henry VII to the Tailors of London, 6 June 1503. 1007 By Stat. 19 Henry VII, c. 7, annulling Stat. 15 Henry VI, c. 6. 1008 Repertory 2, fo. 146. M546 Henry's charter to the City, 23 July, 1505. 1009 Charter dated 23 July, 1505, preserved at the Guildhall (Box No.
      15). 1010 Repertory 1, fo. 175. M547 Henry's high-handed policy towards the City, 1506-1509. 1011 Strype, Stow's "Survey" (1720), bk. ii, p. 193. 1012 Repertory 2, fos. 12, 14; Grey Friars Chron. (Camd. Soc., No. 53),
      p. 29. 1013 The sum mentioned by Holinshed (iii. 539), is £1,400; _Cf._ Fabyan,
      p. 689. 1014 Baker, in his Chronicle (ed. 1674), p. 248, puts Capel's fine at
      £1,400; _Cf._ Fabyan, p. 689; Holinshed, iii, 530; Journal 11, fo.
      94. 1015 Fabyan, p. 690. M548 Marriage of the Princess Mary, Dec., 1508. 1016 Letter Book M, fo. 138; Journal 11, fo. 28. 1017 Journal 11, fos. 37-39. 1018 Gairdner's "Henry the Seventh," p. 206. M549 Henry's taste for the fine arts.
 M550 The King's Chapel and Chantry at Westminster. 1019 Journal 10, fos. 318, 318b; Repertory 2, fos. 10b-11b. A list of
      "such places as have charged themself and promysed to kepe the
      yerely obit" of Henry VII, as well as a copy of indentures made for
      the assurance of the same obit, with schedule of sums paid to
      various religious houses for the observance of the same, are entered
      in the City's Records.--Repertory 1. fo. 167b; Letter Book P, fo.
      186b. M551 The king's death, 22 April, 1509. 1020 The generally accepted day of his death, although the City's
      Archives in one place record it as having taken place on the
      21st.--Journal 2, fo. 67b; _Cf._ Fabyan, 690. 1021 Holinshed, iii, 541. 1022 Journal 11, fos. 67b-69. 1023 "Aldermen barons and presenting barons astate whiche hath been
      Maires." 1024 Journal 2, fo. 69. 1025 Repertory 11, fo. 68b. M552 Proceeding against Empson and Dudley and their agents. 1026 Letters Patent, dated 9 June, 1509, preserved at the Guildhall (Box
      No. 29). 1027 Letter Book M, fo. 159; Journal 11, fo. 74b. 1028 Repertory 2, fo. 68. M553 City gift on occasion of the king's coronation, 24 June, 1509. 1029 Journal 11, fos. 80, 81b, 82; Letter Book M, fo. 160. 1030 Journal 11, fo. 80. 1031 Holinshed, iii, 547. M554 The war with France, 1512-1513. 1032 According to Holinshed (iii, 567), Parliament opened on the 25th
      Jan., 1512. The Parliamentary Returns give the date as the 4th Feb.
      with "no returns found." The names of the City's members, however,
      are recorded in the City's Archives. They were Alderman Sir William
      Capell, who had suffered so much at the close of the last reign,
      Richard Broke, the City's new Recorder, William Cawle or Calley,
      draper, and John Kyme, mercer, commoners.--Journal 11, fo. 147b;
      Repertory 2, fo. 125b. 1033 The Act for levying the necessary subsidy ordained that every alien
      made a denizen should be rated like a native, but that aliens who
      had not become denizens should be assessed at double the amount at
      which natives were assessed.--See "Historical Introd. to Cal. of
      Denizations and Naturalizations of Aliens in England, 1509-1603."
      (Huguenot Soc.), viii, 7. 1034 Journal 11, fo. 1. 1035 -_Id._, fo. 1b. 1036 Journal 11, fo. 171; Repertory 2, fos. 150b, 172. 1037 Repertory 2, fos. 151b-152. 1038 Journal 11, fo. 2. 1039 Repertory 2, fo. 153. M555 The Battle of Spurs, 16 Aug., 1513.
 M556 Peace with France, 1514.
 M557 The New Learning.
 M558 Thomas More. 1040 Letter Book M., fo. 257; Repertory 3, fo. 221. In July, 1517, the
      Fellowship of Saddlers of London consented, on the recommendation of
      Archbishop Warham, to refer a matter of dispute between it and the
      parishioners of St. Vedast to the Recorder and Thomas More,
      gentleman, for settlement (Repertory 3, fo. 149); and in Aug., 1521,
      "Thomas More, late of London, gentleman," was bound over, in the sum
      of £20, to appear before the mayor for the time being, to answer
      such charges as might be made against him.--Journal 12, fo. 123. 1041 Roper's Life of Sir Thomas More, pp. 3, 5, 6. M559 Dean Colet. 1042 Journal 8, fo. 144; Journal 9, fos. 13, 142b. M560 Education in the city. 1043 William Lichfield, rector of All Hallows the Great, Gilbert
      Worthington, rector of St. Andrew's, Holborn, John Cote, rector of
      St. Peter's, Cornhill, and John Nigel or Neel, master of the
      hospital of St. Thomas de Acon and parson of St. Mary
      Colechurch.--Rot. Parl. v, 137. M561 The City of London School. 1044 Stow's Survey (Thoms's ed., 1876), p. 42. 1045 Chamber Accounts (Town Clerk's office), i, fos. 202b, 203. M562 St. Paul's School. 1046 Repertory 2, fos. 121b, 123. 1047 -_Id._, fo. 126b; Journal 11, fo. 147b. 1048 Journal 11, fo. 163; Repertory 2, fos. 133b, 142. 1049 Letter of Erasmus to Justus Jonas quoted in Lupton's Life of Colet,
      pp. 166, 167. 1050 Survey (Thoms's ed., 1876), p. 28. M563 Provincial grammar schools founded by citizens of London. 1051 "The number of grammar schools, in various parts of the country,
      which owe their foundation and endowment to the piety and liberality
      of citizens of London ... far exceeds what might be supposed,
      approaching as it does nearly to a hundred."--Preface to Brewer's
      Life of Carpenter, p. xi. M564 Birth of the Princess Mary, Feb., 1516. 1052 Repertory 3, fo. 46. M565 The city and Cardinal Wolsey, 1516. 1053 -_Id._, fos. 70b, 71. 1054 -_Id._, fos. 86, 86b, 88. 1055 Repertory 3, fos. 116, 116b. M566 Evil Mayday, 1517. 1056 Wares bought and sold between strangers--"foreign bought and
      sold"--were declared forfeited to the City by Letters Patent of Henry
      VII, 23 July. 1505, confirmed by Henry VIII, 12 July, 1523. 1057 In 1500, and again in 1516, orders were issued for all freemen to
      return with their families to the city on pain of losing their
      freedom.--Journal 10. fos. 181b, 259. 1058 Repertory 3, fos. 141b, 142. 1059 Holinshed, iii, 618. 1060 Or Munday; the name is said to appear in twenty-seven different
      forms. He was a goldsmith by trade, and was appointed (among others)
      by Cardinal Wolsey to report upon the assay of gold and silver
      coinage in 1526.--Journal 13, fo. 45b; Letter Book O, fo. 71b.  He
      served sheriff, 1514; and was mayor in 1522. 1061 In 1462 the Common Council ordered basket-makers, gold wire-drawers,
      and other foreigners plying a craft within the city, to reside at
      Blanchappleton--a manor in the vicinity of Mark Lane--and not
      elsewhere. 1062 Repertory 3, fo. 55b. 1063 For an account of the riot and subsequent proceedings, see
      Holinshed, iii, 621-623, and the Grey Friars Chron. (Camd. Soc., No.
      53). p. 30. M567 The City anxious to regain the king's lost favour. 1064 Repertory 3, fos. 143, 143b. M568 A deputation attends the king at Greenwich, 11 May, 1517.
 M569 Wolsey and other lords to be bought over with gifts.
 M570 The king's pardon obtained, 22 May. 1065 Holinshed, iii, 624. 1066 Repertory 3, fo. 144b. 1067 -_Id._, fo. 143b. 1068 Holinshed, 624. 1069 Repertory 3, fo. 145b. 1070 -_Id._, fo. 145. 1071 Repertory 3, fo. 165. 1072 -_Id._, fo. 166. 1073 "Thys yere was much a doo in the yelde-halle for the mayer for the
      comyns wold not have had Semer, for be cause of yell May-day."--Grey
      Friars Chron. (Camd. Soc., No. 53), p. 33. 1074 Repertory 11, fo. 351b. M571 The epidemic of 1518. 1075 Cal. Letters and Papers, For. and Dom. (Henry VIII), vol. ii, pt. i,
      Pref., p. ccxxi. 1076 -_Id._, vol. ii, pt. ii, p. 1276. 1077 Repertory 3, fos. 184b, 189b, 191, 192. 1078 Letter Book N, fo. 95b. 1079 Repertory 3, fos. 192, 194; Letter Book N, fos. 63b, 74. 1080 Repertory 3, fo. 197. M572 Marriage of the infant Princess Mary with the Dauphin, 5 Oct., 1518. 1081 Hall's Chron., pp. 593, 594. 1082 Holinshed, iii, 632. 1083 Cal. Letters and Papers, For. and Dom. (Henry VIII), vol. ii. pt. i,
      Pref., pp. clx, clxi. M573 Preparations for the reception of the legate in the city, July,
      1519. 1084 "An order devysed by the Mayer and hys brethrern the aldremen by the
      Kynges commandment for a Tryumphe to be done in the Citie of London
      at the Request of the Right honorable ambassadors of the Kynge of
      Romayns."--10 July, Journal 12, fo. 9. M574 The legate lands at Deal, 23 July, 1519.
 M575 A story told of his passage through the city. 1085 Hall, pp. 592, 593. M576 The contest for the empire, 1519. 1086 Holinshed, iii, 639. M577 The emperor's visit to the city, 1522. 1087 Journal 12, fos. 125, 172b, 173b; Letter Book N, fo. 194b. 1088 Knighted the next day at Greenwich.--Repertory 5, fo. 295. 1089 Repertory 5, fo. 294. 1090 -_Id._ 4, fo. 134b. 1091 -_Id._ 5, fo. 293. M578 Pestilence and famine, 1519-1522. 1092 Journal 12, fos. 75b-76; Letter Book N, fos. 142-143. 1093 Grey Friars Chron., p. 30; Repertory 4, fo. 71b. 1094 Repertory 4, fos. 1b, 12, 13. 1095 Journal 12, fo. 136. 1096 -_Id._, fo. 144. 1097 Journal 12, fos. 158, 161, 163b; Letter Book N, fos. 187b, 190b. 1098 Holinshed, iii, 675. M579 Execution of the Duke of Buckingham, 1521. 1099 Shakespere mentions the Duke's manor thus:-- "Not long before your highness sped to France,
        The duke being at the Rose, within the parish
        St. Laurence Poultney, did of me demand
        What was the speech among the Londoners
        Concerning the French journey." --Henry VIII, act 1, sc. 2. 1100 Cal. Letters and Papers, For. and Dom. (Henry VIII), vol. iii, pt.
      i, Pref., pp. cxxv, cxxvi, cxxxv, cxxxvi. 1101 On the 5th July steps were taken by the Court of Aldermen for
      putting a stop to the mutinous and seditious words that were current
      in the city "concerning the lamenting and sorrowing of the death of
      the duke"--men saying that he was guiltless--and special precautions
      were taken for the safe custody of weapons and harness for fear of
      an outbreak. The scribe evinced his loyalty by heading the page of
      the record with _Lex domini immaculata: Vivat Rex Currat
      L_.--Repertory 5, fo. 204. M580 City loan of £20,000 to assist the king against France, 1522. 1102 Repertory 5, fo. 288. 1103 Journal 12, fos. 187b, 188b, 195; Letter Book N, fos. 203b, 204,
      208. M581 The aldermen to be assessed with the commoners and not to be
      severed. 1104 Repertory 5, fo. 292. 1105 Journal 12, fo. 187b. 1106 Repertory 5, fos. 289, 290. 1107 -_Id._, fo. 291. 1108 Repertory 5, fos. 296b, 297. 1109 -_Id._, fo. 294. M582 A further loan of 4,000 marks.
 M583 Letter of thanks from Wolsey, 3 Sept., 1522. 1110 A portion remained unpaid on 16 August.--Journal 12, fo. 195. 1111 Letter dated 3 Sept.--Journal 12, fo. 196b. On 28 Sept. Wolsey asked
      for more time to repay the loan.--Repertory 5, fo. 326. 1112 Journal 12, fo. 200. M584 The City makes a stand against further loans. Nov., 1522.
 M585 Others follow its example. 1113 Journal 12, fo. 210. 1114 See Green's "Hist. of the English People," ii, 121. 122. M586 Appeal to parliament, April, 1523. 1115 Grey Friars Chron., p. 31. 1116 Repertory 4, fo. 144; _Cf._ Repertory 6, fo. 20b; Letter Book N, fo.
      222. 1117 Repertory 4, fo. 145b. 1118 Roper's "Life of More," pp. 17-20. M587 The City and Wolsey, 1523. 1119 Repertory 4, fos. 152, 168; _Cf._ Repertory 6, fo. 38. 1120 Repertory 4, fos. 144b, 145, 146, 150; _Cf._ Repertory 6, fos. 22b,
      29, 32b. M588 The king and queen of Denmark in the city. 1121 Grey Friars Chron. pp. 30, 31. 1122 Repertory 4, fos. 153b-154; _Cf._ Repertory 6, fo. 42. M589 England invaded by the Scots. 1523. 1123 Repertory 6, fo. 61b. 1124 Holinshed, iii, 692, 693. M590 Monoux refuses to accept the mayoralty a second time, Oct., 1523. 1125 Journal 12, fos. 249-250. 1126 Journal 12, fos. 287-288. M591 The king pledges himself to repay the City loan of £20,000. 1127 -_Id._, fo. 276. M592 Formation of a league against France. 1128 -_Id._, fo. 284. M593 Proclamation for the recovery of lost letters, 10 July, 1524.
 M594 The king of France made prisoner at Pavia, 24 Feb., 1525.
 M595 Rejoicing in the city. 1129 Letter Book N, fo. 280; Journal 12, fo. 329. 1130 Grey Friars Chron., p. 32. M596 The Amicable Loan, 1525. 1131 Hall's Chron., p. 695. 1132 Journal 12, fo. 331; Letter Book N. fo. 278. 1133 Journal 12, fo. 331b. 1134 Hall's Chron., p. 701. M597 A truce between England and France.
 M598 French ambassadors lodged in the city, 1527. 1135 The truce was to last from 14 August to 1 December.--Letter Book N,
      fos. 291, 293; Journal 12, fos. 300, 305. 1136 "Item in lyke wyse the Chamberleyn shall have allowance of and for
      suche gyftes and presentes as were geven presentyd on Sonday laste
      passyd at the Bysshoppes palace at Paules to the Ambassadours of
      Fraunce devysed and appoynted by my lorde Cardynalles Grace and most
      specyally at his contemplacioun geven for asmoch as lyke precedent
      in so ample maner hath not afore tyme be seen; the presents ensue
      etc."--Repertory 7, fo. 225. M599 Troubles over Wythypol's election as alderman, 1527-1528.
 M600 Wythypol again summoned to take office.
 M601 Committed to Newgate, 6 Feb., 1528.
 M602 Again summoned to take office, 22 May. 1137 He had been one of the commoners sent to confer with Wolsey touching
      the amicable loan (Journal 12, fo. 331b). He attended the coronation
      banquet of Anne Boleyn in 1533 (Repertory 9, fo. 2), and was M.P.
      for the city from 1529-1536 (Letter Book O, fo. 157). His daughter
      Elizabeth married Emanuel Lucar, also a merchant-tailor.--Repertory
      9, fos. 139. 140. 1138 Repertory 7, fos. 171b, 172, 174b, 179. 1139 Repertory 7, fos. 179b, 180. 1140 To the effect that he was not worth £1,000.--Journal 7, fo. 198. 1141 Repertory 7, fos. 238b, 240, 240b. 1142 -_Id._, fo. 243b. 1143 Repertory 7, fo. 206. The Common Council assessed the fine at
      £100.--Journal 13, fo. 61b; Letter Book O, fo. 80b. 1144 Repertory 7, fo. 264. M603 A great dearth in the city, 1529. 1145 Journal 13, fo. 184b. 1146 Letter Book O, fos. 88b, 89b. M604 The legatine court at the Blackfriars, 1529. 1147 Cal. Letters and Papers For. and Dom. (Henry VIII), vol. iv,
      Introd., p. cccclxv. M605 The lord mayor's banquet, 28 Oct., 1529. 1148 Letter Book O, fos. 174b-175; Journal 13, fo. 180b. M606 The fall of Wolsey, 1529-1530. 1149 Letter Book O, fo. 157. 1150 About the year 1522 Cromwell was living in the city, near Fenchurch,
      combining the business of a merchant with that of a money-lender. He
      sat in the parliament of 1523, and towards the close of that year
      served on a wardmote inquest for Bread Street Ward. In 1524 he
      entered Wolsey's service.--Cal. Letters and Papers For. and Dom.
      (Henry VIII.), vol. iii, pt. i, Introd., pp. cclvi, cclvii. 1151 Cal. Letters and Papers For. and Dom. (Henry VIII), vol. iv,
      Introd., pp. dliii-dlvi. M607 The House of Commons and the Clergy, 1529. 1152 Stat. 21, Henry VIII, caps. 5, 6 and 13. 1153 Proclamation, 12 Sept., 1530.--Letter Book O, fo. 199b. M608 Disputes touching tithes payable to city clergy, 1527-1534. 1154 Burnell, "London (City) Tithes Act, 1879," Introd., pp. 1, 2. 1155 Letter Book O, fos. 47, _seq._ 1156 A list of these, comprising seven churches, was submitted to the
      Court of Aldermen, 23 Feb., 1528.--Repertory 8, fo. 21. M609 The curates' book of articles. 1157 Letter Book O, fos. 140b, 141b. 1158 Repertory 8, fo. 27b. 1159 Letter Book O, fos. 145, 145b; Journal 13, fo. 125b. 1160 Letter book P, fos. 31, 34, 41b; Journal 13, fo. 417b. 1161 This order was confirmed by stat. 27, Henry VIII, cap. 21. Ten years
      later a decree was made pursuant to stat. 37, Henry VIII, cap. 12,
      regulating the whole subject of tithes, but owing to the decree not
      having been enrolled in accordance with the terms of the statute,
      much litigation has in recent times arisen.--Burnell, "London (City)
      Tithes Act, 1879," Introd., p. 3. M610 Elsing Spital and Holy Trinity Priory surrendered to the king,
      1530-1531. 1162 The well-known and somewhat romantic account of the origin of the
      priory and of its connection with the city cnihten-guild is given in
      Letter Book C, fos. 134b, _seq._; _Cf._ Liber Dunthorn, fo. 79. 1163 Grey Friars Chron. (Camd. Soc., No. 53), p. 35. Three years later
      (30 March, 1534) the Court of Aldermen resolved to wait upon the
      chancellor "to know his mind for the office concerning the lands"
      belonging to the late priory.--Repertory 9, fo. 53b. M611 The Great Beam reconveyed to the City after the lapse of ten years,
      1531. 1164 By letters patent dated 13 April, 1531 (preserved at the Guildhall,
      Box No. 16). 1165 Henry Lumnore, Lumnar or Lomner, a grocer by guild as well as
      calling (see Cal. Letters and Papers For. and Dom. (Henry VIII),
      vol. iii, pt. ii, p. 879), was associated with Sidney in holding the
      beam. The City offered to buy him out either by bestowing on him an
      annuity of £10 during the joint lives of himself and Sidney, or else
      by paying him a lump sum of £100.--Repertory 8, fo. 218b. 1166 Anne Boleyn. 1167 Repertory 8, fo. 131. 1168 -_Id._, fos. 142b. 202b. M612 Feeling in the city at Henry's marriage with Anne Boleyn, 1533. 1169 Chapuys to the emperor.--Cal. State Papers (Spanish), vol. iv., pt.
      ii, p. 646. M613 The queen's passage from the Tower to Westminster, 31 May, 1533. 1170 Repertory 9, fo. 1b. There is a fine drawing at Berlin by Holbein
      which is thought to be the original design for the triumphal arch
      erected by the merchants of the Steelyard on this occasion. M614 The City's gift of 1,000 marks. 1171 Journal 13, fo. 371b. According to Wriothesley (Camd. Soc., N.S.,
      No. 11, p. 19) the present to the queen was made to her in a purse
      of cloth of gold on the occasion of her passing through the city on
      the 31st May, the day before her coronation. 1172 Repertory 2, fo. 70b; Repertory 9, fo. 2. M615 The Act of Succession, 1534. 1173 Letter Book P, fos. 37-37b; Journal 13, fo. 408b. 1174 Letter to Lord Lisle.--Cal. Letters and Papers For. and Dom. (Henry
      VIII), vol. vii, p. 208. 1175 Repertory 9, fo. 57b. "Allso the same day [20 April] all the craftes
      in London were called to their halls, and there were sworne on a
      booke to be true to Queene Anne and to believe and take her for
      lawfull wife of the Kinge and rightfull Queene of Englande, and
      utterlie to thincke the Lady Marie, daughter to the Kinge by Queene
      Katherin, but as a bastarde, and thus to doe without any
      scrupulositie of conscience."--Wriothesley's Chron., i, 24. M616 Proceedings against those objecting to subscribe to the Act of
      Succession. 1176 Grey Friars Chron., p. 37. In November of the last year they had
      been made to do penance at Paul's Cross and afterwards at
      Canterbury. M617 The monks of the Charterhouse, 1534-1535. 1177 "Historia aliquot nostri sęculi martyrum," 1583.  Much of it is
      quoted by Father Gasquet in his work on "Henry VIII and the English
      Monasteries" (cap. vi), and also by Mr. Froude ("Hist. of England,"
      vol. ii, cap. ix). 1178 Cal. Letters and Papers For. and Dom. (Henry VIII), vol. vii, p.
      283. 1179 This convent--the most virtuous house of religion in England--was of
      the Order of St. Bridget, and received an annual visit from the
      mayor and aldermen of the City of London at what was known as "the
      pardon time of Sion," in the month of August. In return for the
      hospitality bestowed by the lady abbess on these occasions the Court
      of Aldermen occasionally made her presents of wine (Repertories 3,
      fo. 94b; 7, fo. 275). In 1517 the court instructed the chamberlain
      to avoid excess of diet on the customary visit. There was to be no
      breakfast on the barge and no swans at dinner (Repertory 3, fo.
      154b). In 1825 the Court of Common Council decreed (_inter alia_)
      that "as tonchyng the goyng of my lord mayre and my masters his
      brethern the aldermen [to] Syon, yt is sett at large and to be in
      case as it was before the Restreynt" (Journal 12, fo. 302). It was
      suppressed 25 Nov., 1539.--Wriothesley's Chron., i, 109. M618 The Act of Supremacy, 1534.
 M619 Execution of Houghton and others, 1535. 1180 The Act of Supremacy was passed in 1534, but the king's new title as
      Supreme Head of the Church was not incorporated in his style before
      the 15 Jan., 1535. 1181 Cal. Letters and Papers For. and Dom. (Henry VIII), vol. viii, p.
      321. 1182 -_Id._, p. 354. M620 Execution of Fisher and More, 1535. 1183 Repertory 9, fo. 145. M621 The Pilgrimage of Grace, 1536. 1184 -_Id._, fo. 199. 1185 He had been elected mayor for the second time in October last
      (1535), much against his own wish, at the king's express
      desire.--Journal 13, fo. 452b; Wriothesley, i, 31. He presented the
      City with a collar of SS. to be worn by the mayor for the time
      being.--Repertory 11, fo. 238. 1186 Repertory 9, fos. 199, 199b. 1187 Repertory 9, fo. 200. 1188 -_Id._, fo. 200b. 1189 Son of Thomas Warren, fuller; grandson of William Warren, of Fering,
      co. Sussex. He was knighted on the day that his election was
      confirmed by the king (Wriothesley. i, 59). His daughter Joan (by
      his second wife Joan, daughter of John Lake, of London) married Sir
      Henry Williams, _alias_ Cromwell (Repertory 14, fo. 180; Journal 17.
      fo. 137b), by whom she had issue Robert Cromwell, father of the
      Protector. Warren died 11 July, 1533, and his widow married Alderman
      Sir Thomas White.--See notes to Machyn's Diary, p. 330. 1190 Repertory 9, fo. 209b. M622 Henry's marriage with Jane Seymour, May, 1536. 1191 Henry attributed her miscarriage to licentiousness; others to her
      having received a shock at seeing her royal husband thrown from his
      horse whilst tilting at the ring.--Wriothesley, i, 33. 1192 Chapuys to [Granvelle] 25 Aug., 1536.--Cal. Letters and Papers For.
      and Dom. (Henry VIII), vol. xi., p. 145. M623 Convocation at St. Paul's, 9 June-20 July, 1536. 1193 Wriothesley, i, 52-53. M624 Preparation for the new queen's coronation.
 M625 She dies in childbed, 24 Oct., 1537. 1194 Letter Book P, fo. 103b. 1195 Wriothesley, i, 69. 1196 Letter Book P, fo. 135b; Wriothesley, i, 71, 72. M626 Anne of Cleves arrives at Dover, 27 Dec., 1539.
 M627 Her passage through the city, 4 Feb,. 1540. 1197 Repertory 10, fos. 152b, 153; Wriothesley, i, 109, 111. 1198 Repertory 10, fo. 161. The circumstance that Henry carried his new
      bride to Westminster by water instead of conducting her thither
      through the streets of the city has been considered a proof of his
      want of regard for her. M628 Cromwell's work of demolition in the city, 1537-1538. 1199 Holinshed, iii. 807. 1200 Letter Book P, fo. 113; Journal 14, fo. 30b. 1201 Stow's "Survey" (Thoms's ed., 1876), p. 68. 1202 The Mercers' Company applied for a grant of the chapel and other
      property of the hospital; and this was conceded by letters patent,
      21 April, 1542, upon payment of the sum of £969 17_s._ 6_d._,
      subject to a reserved rent of £7 8_s._ 10_d._, which was redeemed by
      the company in 1560.--Livery Comp. Com. (1880), Append. to Report,
      1884, vol. ii, p. 9. M629 The division of the spoil. 1203 On the re-establishment of the Dutch or Mother Strangers' Church, at
      Elizabeth's accession, it was declared by the Privy Council to be
      under the superintendence of the Bishop of London (Cal. State Papers
      Dom., Feb., 1560). Hence it was that Dr. Temple, Bishop of London,
      was memorialised in March, 1888, as superintendent of the French
      Church in London.--See "Eng. Hist. Review," April, 1891, pp. 388-389. 1204 Stow's "Survey" (Thoms's ed., 1876), p. 67. 1205 Nichols' "Progresses of Queen Eliz.," iii. 598. For particulars of
      Swinnerton see Clode's "Early Hist. of the Merchant Taylors'
      Company," i, 262, etc. M630 The mayor's effort to save the destruction of the steeple of the
      Austin Friars Church. 1206 Strype's Stow, bk. ii, pp. 114, 115. 1207 Remembrancia (Analytical Index), pp. 133, 134. M631 The priory of St. Helen without Bishopsgate. 1208 In 1439 Reginald Kentwode, Dean of St. Paul's, having in a recent
      visitation discovered "many defaults and excesses," drew up a
      schedule of injunctions for their better regulation.--Printed in
      London and Middlesex Archęol. Soc. Transactions, ii, 200-203. M632 Friendly relations between the Corporation and religious houses in
      the city. 1209 Journal 12, fo. 75. 1210 Repertory 2, fo. 185b. 1211 Repertory 5, fos. 15, 15b, 82b. 1212 Repertory 2, fo. 185; Grey Friars Chron., pp. 29, 31. M633 Royal injunction for keeping Parish Registers, 29 Sept., 1538. 1213 Sixteen other registers for city parishes commence in 1538, and four
      in 1539.--See Paper on St. James Garlickhithe, by W. D. Cooper,
      F.S.A. (London and Middlesex Arch. Soc. Trans., vol. iii, p. 392,
      note). M634 Great increase of London poor, consequent on the suppression of
      religious houses. 1214 Wriothesley's Chron. (Camd. Soc, N.S., No. 11), i, 77, 78. M635 Sir Richard Gresham's letter to the king for conveyance to the City
      of certain hospitals. 1215 Descended from a Norfolk family. Apprenticed to John Middleton,
      mercer, of London, and admitted to the freedom of the Mercers'
      Company in 1507. Alderman of Walbrook and Cheap Wards successively.
      Sheriff 1531-2. Married (1) Audrey, daughter of William Lynne, of
      Southwick, co. Northampton, (2) Isabella Taverson, _née_ Worpfall.
      Was the father of Sir Thomas Gresham, the founder of the Royal
      Exchange and of the college which bears his name.--_Ob._, 21 Feb.,
      1549. Buried in the church of St. Laurence Jewry. 1216 Cott. MS., Cleop. E., iv, fo. 222.--Printed in Burgon's "Life of
      Gresham," i, 26-29. M636 Two petitions from the City, Mar., 1539.
 M637 The City offers to purchase certain dissolved houses, 1 Aug., 1540. 1217 Journal 14, fo. 129; Letter Book P, fo. 178. 1218 Journal 14, fo. 216b; Letter Book P, fo. 220b. 1219 Repertory 10, fo. 200. M638 The City in difficulties with king and parliament, 1541-1542. 1220 Journal 14, fo. 269. 1221 Wriothesley, i, 129. 1222 Son of Thomas Hill, of Hodnet, co. Salop. He devoted large sums of
      money to building causeways and bridges, and erected a grammar
      school at Drayton-in-Hales, otherwise Market Drayton, in his native
      county, which he endowed by will, dated 6 April, 1551 (Cal. of
      Wills, Court of Hust., London, part ii, p. 651). See also Holinshed,
      iii, 1021. 1223 Holinshed, iii, 824; Wriothesley, i, 135. According to the Grey
      Friars Chron. (p. 45), it was the sergeant-at-arms himself whom the
      sheriffs detained. M639 Precautions against the spread of pestilence, 1543. 1224 Proclamation dated 13 Aug., 1543.--Journal 15, fo. 48b. 1225 Journal 15, fo. 55; Letter Book Q, fo. 93. 1226 Letter Book Q, fo. 92b; Grey Friars Chron., p. 45. M640 Preparation for renewal of war with France, 1544. 1227 Writ to mayor and sheriffs for proclamation of war, dat. 2 Aug.,
      1543.--Journal 15, fo. 46b. 1228 Repertory 11, fo. 32b. 1229 Repertory 11, fo. 65b. 1230 Journal 15, fo. 95; Repertory 11, fo. 74; Letter Book Q, fo. 109. M641 The re-establishment of St. Bartholomew's hospital, 23 June, 1544. 1231 "Memoranda ... relating to the Royal Hospitals," 1863, pp. 4-7. M642 The campaign in France of 1544. 1232 Repertory 11, fo. 106; Letter Book Q, fo. 116b. 1233 Repertory, 11, fo. 118b; Letter Book Q, fo. 120b. 1234 Journal 15, fo. 123; Letter Book Q, fo. 119. 1235 Journal 15, fo. 124; Letter Book Q, fo. 122. M643 City gift to the king on his return from France. 1236 Letter Book Q, fo. 120b. M644 Opposition to a benevolence in the city, 1545. 1237 Wriothesley, i, 151, 153; Grey Friars Chron., p. 48. 1238 Holinshed, iii, 346. M645 William Laxton, mayor, knighted, 8 Feb., 1545. 1239 Wriothesley, i, 151, 152. M646 A call for volunteers for the French war. April, 1545. 1240 Journal 15, fo. 239b; Letter Book Q, fo. 167b. 1241 Journal 15, fo. 240.; Letter Book Q, fo. 168; Wriothesley, i, 154. 1242 "A coarse frieze was so called from a small town in the West Riding
      of Yorkshire. An Act of 5 and 6 Edward VI (1551-2) provided that all
      "clothes commonly called Pennystones or Forest Whites ... shall
      conteyne in length beinge wett betwixt twelve and thirtene yardes." 1243 Repertory 11, fo. 193b; Letter Book Q, fo. 133; Wriothesley, i, 154. M647 The last subsidy to be forthwith paid up. 1244 Wriothesley, i, 155. M648 A force of 2,000 soldiers demanded of the City, June, 1545. 1245 Repertory 11, fos. 203, 212b. 1246 30 July.--Repertory 11, fo. 215b. The Midsummer watch had not been
      kept this year.--Wriothesley, i, 156. 1247 Repertory 11, fo. 213. 1248 Wriothesley, i, 58. M649 Boulogne threatened. 1249 Repertory 11, fo. 216b. M650 Act for confiscating chantries, &c., 1545. 1250 Stat. 37, Henry VIII, c. 4. M651 Peace with France proclaimed, 13 June, 1546. 1251 Repertory 11, fo. 299b; Letter Book Q, fo. 181; Journal 15, fo. 270;
      Wriothesley, i, 165. M652 Uniformity of religion enforced, 1546.
 M653 Recantation of the rector of St. Mary Aldermary. 1252 Holinshed, iii, 856; Grey Friars Chron., p. 50. M654 Trial and execution of Anne Ascue. 1253 Holinshed, iii, 847. 1254 Letter Book Q, fo. 181. M655 Improved water supply of the city, 1545-1546. 1255 Repertory 11, fo. 247. 1256 Journal 15, fo. 213b. 1257 Wriothesley, i, 162, 175. M656 St. Bartholomew's Hospital, &c., vested in the City, 13 Jan., 1547. 1258 Journal 15, fos. 245, 399b, _seq._ 1259 "Memoranda ... Royal Hospitals," pp. 20-45. M657 A committee appointed to investigate the recently acquired property,
      6 May, 1547. 1260 Repertory 11, fo. 349b. 1261 In Sept., 1547, the citizens were called upon to contribute half a
      fifteenth for the maintenance of the poor of St.
      Bartholomew's.--Journal 15, fo. 325b. In Dec, 1548, an annual sum of
      500 marks out of the profits of Blackwell, and in 1557 the whole of
      the same profits were set aside for the poor.--Journal 15, fos. 398,
      _seq._; Repertory 13, pt. ii, fo. 512. M658 The king's death, 28 Jan., 1547. 1262 Royal proclamation, 7 July, 1545, forbidding all pursuit of game in
      Westminster, Islington, Highgate, Hornsey and elsewhere in the
      suburbs of London.--Journal 15, fo. 240b. M659 Edward VI proclaimed king in the city, 31 Jan., 1547. 1263 Son of Christopher Huberthorne, of Waddington, co. Lane, Alderman of
      Farringdon Within. His mansion adjoined the Leadenhall. _Ob._, Oct.,
      1556. Buried in the church of St. Peter, Cornhill.--Machyn. 115, 352.
      It was in Huberthorne's mayoralty that the customary banquet to the
      aldermen, the "officers lerned" and the commoners of the city, on
      Monday next after the Feast of Epiphany, known as "Plow Monday," was
      discontinued.--Letter Book Q, fo. 191b. It was afterwards renewed and
      continues to this day in the form of a dinner given by the new mayor
      to the officers of his household and clerks engaged in various
      departments of the service of the Corporation. An attempt was at the
      same time made to put down the lord mayor's banquet
      also.--Wriothesley, i, 176. 1264 Journal 15. fos. 303b, 305b; Letter Book Q, os. 192b, 194;
      Wriothesley. i, 178. M660 Distribution of gowns of black livery. 1265 Journal 15, fo. 304; Letter Book Q, fo. 195; Repertory 11, fo. 335b. M661 Accession and coronation of Edward VI, 1547. 1266 "The lord mayor of London, Henry Hobulthorne, was called fourth, who
      kneeling before the king, his majestie tooke the sworde of the Lord
      Protector and made him knight, which was the first that eaver he
      made."--Wriothesley's Chron. (Camd. Soc, N.S., No. 11.), i, 181. 1267 This mace is still in possession of the Corporation. It is only
      brought out for use on such occasions as a coronation, when it is
      carried by the lord mayor as on the occasion narrated above, and at
      the annual election of the chief magistrate of the city, when it is
      formally handed by the Chamberlain to the lord mayor elect. The mace
      consists of a tapering shaft of rock crystal mounted in gold, with a
      coroneted head also of gold, adorned with pearls and large jewels.
      Its age is uncertain. Whilst some hazard the conjecture that it may
      be of Saxon origin, there are others who are of opinion that the
      head of it at least cannot be earlier than the 15th century. 1268 Journal 15, fo. 305; Letter Book Q, fos. 195b-196; Repertory 11, fo.
      334b. M662 Opposition in the city to the sacrament of the mass, 1547-1548. 1269 "All these chyldren shall every Chyldermasse day come to Paulis
      Church and here the chylde bisshoppis sermon, and after be at the
      hye masse, and eche of them offer a 1d. to the childe bisshop and
      with theme the maisters and surveyors of the scole."--Statutes of St.
      Paul's School, printed in Lupton's "Life of Dean Colet," p. 278b. 1270 Letter Book P, fo. 172b. 1271 Journal 14, fo. 158b; Letter Book P, fo. 197. 1272 See Brewer's Introd. to Cal. Letters and Papers For. and Dom., vol.
      iv, pp. dcli-dcliii. 1273 Letter Book P, fo. 153. 1274 Letter Book Q, fo. 102. 1275 "Also this same tyme [Nov., 1547] was moche spekying agayne the
      sacrament of the auter, that some callyd it Jacke of the boxe, with
      divers other shamefulle names... And at this tyme [Easter, 1548] was
      more prechyng agayne the masse."--Grey Friars Chron., p. 55. 1276 Letter Book Q, fo. 250b. 1277 Repertory 11, fo. 423. 1278 "After the redyng of the preposycioun made yesterday in the Sterre
      Chamber by the lorde chaunceler and ye declaracioun made by my lorde
      mayer of suche comunicacioun as his lordshyp had wt the Bysshop of
      Caunterburye concernyng the demeanor of certein prechers and other
      dysobedyent persones yt was ordered and agreyd that my lorde mayer
      and all my maisters thaldermen shall this afternone att ij of ye
      clok repayre to my lorde protectors grace and the hole counseill and
      declare unto theim the seid mysdemeanor and that thei shall mete att
      Saint Martyns in the Vyntrey att one of the clok."--Repertory 11, fo.
      456b. 1279 Repertory 11, fo. 465. M663 Act for abolition of chantries, 1547. 1280 A proclamation against the evil behaviour of citizens and others
      against priests, 12 Nov., 1547.--Letter Book Q. fo. 218; Journal 15,
      fo. 335b. M664 Redemption of charges for superstitious uses by the city and
      companies, 1550. 1281 By letters patent dated 14 July, 1550 (preserved at the Guildhall,
      Box 17). 1282 Letter Book R, fo. 166b; Wriothesley's Chron. (Camden Soc., N.S.,
      No. 20), ii, 35. See also exemplification of Act of Parl. passed a°
      5 Edward VI, in accordance with the terms of this petition (Box 29). M665 Order for demolition of images, pictures, &c., Aug., 1547. 1283 Journal 15, fo. 322; Letter Book Q, fo. 210b. 1284 Repertory 11. fo. 373; Letter Book Q, fo. 214. 1285 Grey Friars Chron., 54, 55; Wriothesley. ii, 1. 1286 Grey Friars Chron., p. 58. In May (1548) the duke applied to the
      City for water to be laid on to Stronde House, afterwards known as
      Somerset House.--Repertory 11, fos. 462b, 484; Journal 15. fo. 383b;
      Letter Book Q, fo. 253b. 1287 Grey Friars Chron., p. 55. 1288 Wriothesley, ii, 29. Touching the ceremony of visiting the tomb of
      the Bishop of London, to whom the citizens were indebted for the
      charter of William the Conqueror, see chap. i, p. 35. M666 The citizens and the Grey Friars Church, 1547. 1289 Letter Book Q, fos. 232, 234b; Repertory 11, fos. 356, 415, 431,
      444b, 511b. 1290 "Item, at this same tyme [_circ._ Sept., 1547] was pullyd up alle
      the tomes, grett stones, alle the auteres, with stalles and walles
      of the qweer and auters in the church that was some tyme the Gray
      freeres, and solde and the qweer made smaller."--Grey Friars Chron.,
      p. 54. M667 The "communion" substituted for the mass, 1548. 1291 "At Ester followyng there began the commonion, and confession but of
      thoys that wolde, as the boke dothe specifythe."--Grey Friars Chron.,
      p. 55; _Cf._ Wriothesley (Camd. Soc, N.S., No. 20), ii, 2. 1292 The Guildhall college, chapel and library were restored to the City
      in 1550, by Edward VI, on payment of £456 13_s._ 4_d._,--Pat. Roll 4
      Edward VI, p. 9m. (32) 20; Letter Book R, fo. 64b. 1293 Repertory 11, fo. 493b. 1294 -_Id._, fo. 455. (431 pencil mark); Letter Book Q, fo. 237. "This
      yeare in the Whitson holidaies my lord maior [Sir John Gresham]
      caused three notable sermons to be made at Sainct Marie Spittell,
      according as they are kept at Easter.... And the sensing in Poules
      cleene put downe."--Wriothesley, ii, 2, 3. The processions were kept
      up in 1554, "but there was no sensynge."--Grey Friars Chron., p. 89. M668 The "tuning of the pulpits." 1295 -_Cf._ Journal 15, fo. 352b; Letter Book Q, fos. 230-252b. "This
      yeare [1548] the xxviiith daie of September, proclamation was made
      to inhibite all preachers generallie till the kinges further
      pleasure. After which daie all sermons seasede at Poules Crosse and
      in all other places."--Wriothesley, ii, 6. 1296 Grey Friars Chron., pp. 59, 62. Occasionally the chronicler is
      overcome by his feelings, and cries out, "Almyghty God helpe it whan
      hys wylle ys!" _Id._, p. 67. M669 The insurrections of 1549. 1297 In some cases the new owners may have experienced some difficulty in
      fixing a fair rent, as appears to have been the case with the City
      of London and its recently acquired property of Bethlehem. When the
      Chamberlain reported that the rents demanded for houses in the
      precincts of the hospital were far too high, he was at once
      authorised to reduce them at discretion.--Letter Book R, fo. 10b. 1298 Letter Book R, fo. 11b. 1299 Grey Friars Chron., p. 60; Wriothesley, ii, 15, 16. M670 Cranmer at St. Paul's, 21 July, 1549. 1300 Wriothesley, ii, 16, 17; Grey Friars Chron., p. 60. M671 The king passes through the city, 23 July. 1301 Wriothesley, ii, 19. M672 Ket's rebellion in Norfolk. 1549. 1302 Wriothesley, ii, 20; Grey Friars Chron., p. 61. 1303 Holinshed, iii, 982-984. M673 The fall of Somerset, 1549.
 M674 Letter from lords of the council to the City accusing the Protector,
      6 Oct. 1304 Letter Book R, fo. 40; Journal 16, fo. 36. M675 Letter from Somerset to the mayor, 6 Oct., 1549. 1305 Letter Book R, fo. 39b. M676 Conference between the lords and the City at Ely Place, 6 Oct.,
      1549. 1306 Acts of the Privy Council, ii, 331-332; Wriothesley, ii, 24-25;
      Holinshed, iii, 1014; Repertory 12, pt. i, fos. 149-150. M677 Removal of the king to Windsor. 1307 Holinshed, iii, 1014-1015; Acts of Privy Council, ii, 333. M678 The City joins the lords against Somerset, 7 Oct., 1549. 1308 Acts of Privy Council, ii, fos. 333-336. 1309 Repertory 12, pt. i, fo. 150b. 1310 Letter Book R, fo. 40b. M679 The lords attend a Common Council, 8 Oct., 1549. 1311 -_Id._, fos. 43-43b. 1312 Acts of Privy Council, ii, 336, 337. M680 A meeting at Sheriff York's house, 9 Oct.
 M681 The City agrees to furnish a contingent of soldiers to aid the
      lords. 1313 Wriothesley, ii, 26. 1314 Acts of Privy Council, ii, 337-342. 1315 Letter Book R, fos. 41-42; Journal 16, fos. 37, 37b. According to
      Holinshed (iii, 1017, 1018), considerable opposition was made by a
      member of the Common Council named [COMPANION_B] Stadlow to any force at
      all being sent by the city. He reminded the court of the evils that
      had arisen in former times from the city rendering support to the
      barons against Henry III, and how the city lost its liberties in
      consequence. The course he recommended was that the city should join
      the lords in making a humble representation to the king as to the
      Protector's conduct. 1316 Wriothesley, ii, 26, 27. M682 The effect of the City's adhesion to the lords.
 M683 Somerset brought to the Tower, 14 Oct. 1317 Letter Book R, fo. 37; Journal 16, fo. 34; Wriothesley, ii, 26. 1318 Stow's "Summarie of the Chronicles of England" (ed. 1590), p. 545;
      Wriothesley, ii, 27, 28. The names are given differently in the Acts
      of the Privy Council, ii, 344. M684 Bonner deprived of bishopric of London, 1 Oct., 1549. 1319 Grey Friars Chron., pp. 63, 64; _Cf._ Wriothesley, ii, 24. M685 The king entertained by Sheriff York, Oct., 1549. 1320 Wriothesley, ii, 28. M686 Somerset released on parole, 6 Feb., 1550. 1321 Acts of Privy Council, ii, 384; Wriothesley, ii, 33. M687 Warwick and the reformers, 1550. 1322 For more than a week he had been compelled to lie on nothing but
      straw, his bed having been taken away by order of the knight marshal
      for refusing to pay an extortionate fee.--Grey Friars Chron., p. 65. 1323 Thomas Thurlby, the last abbot of Westminster, became the first and
      only bishop of the see. Upon the union of the see with that of
      London Thurlby became bishop of Norwich. Among the archives of the
      city there is a release by him, in his capacity as bishop of
      Westminster, and the dean and chapter of the same, to the City of
      London of the parish church of St. Nicholas, Shambles. The document
      is dated 14 March, 1549, and has the seals of the bishopric and of
      the dean and chapter, in excellent preservation, appended. 1324 For objecting to the prescribed vestments, he was committed to the
      Fleet by order of the Privy Council, 27 Jan., 1551, and was not
      consecrated until the following 8th March.--Hooper to Bullinger, 1
      Aug., 1551 ("Original Letters relative to the English Reformation."
      ed. for Parker Society, 1846, p. 91). M688 The City and the borough of Southwark, 1550. 1325 Their respective boundaries are set out in the Report of
      Commissioners on Municipal Corporations (1837), p. 3. 1326 Charter dated 6 March, 1 Edward III. 1327 Charter dated 9 Nov., 2 Edward IV. 1328 Letter Book Q, fos. 239b-241b. M689 Charter to the City, 23 April, 1550. 1329 Letter Book R, fo. 58b. 1330 Dated 23 April, 1550. A fee of £6 "and odde money" was paid for the
      enrolment of this charter in the Exchequer.--Repertory 12, pt. ii,
      fo. 458. This fee appears to have been paid, notwithstanding the
      express terms of the charter that no fee great or small should be
      paid or made or by any means given to the hanaper to the king's use.
      According to Wriothesley (ii, 36), the "purchase" of Southwark cost
      the city 1,000 marks, "so that nowe they shall have all the whole
      towne of Southwarke by letters patent as free as they have the City
      of London, the Kinges Place [_i.e._ Southwark Place or Suffolk
      House] and the two prison houses of the Kinges Bench and the
      Marshalsea excepted." 1331 Wriothesley, ii, 38. M690 The ward of Bridge Without. 1332 Letter Book R, fo. 80; Journal 16, fo. 82b. 1333 The custom in the city was for the inhabitants of a vacant ward to
      nominate four persons for the Court of Aldermen to select one.  As
      there were no means of enforcing the above ordinance it was repealed
      by Act of Co. Co., 16 June, 1558.--Letter Book S., fo. 167b. 1334 Letter Book R, fo. 71b. The following particulars of Aylyff and his
      family are drawn from the city's archives.  From Bridge Ward Without
      he removed to Dowgate Ward. At the time of his death, in 1556, he
      was keeper of the clothmarket at Blackwell Hall.  His widow was
      allowed to take the issues and profits of her late husband's place
      for one week, and was forgiven a quarter's rent.  Aylyff's son
      Erkenwald succeeded him at Blackwell Hall. The son died in 1561.
      After his decease he was convicted of having forged a deed.  His
      widow, Dorothy, married Henry Butler, "gentleman."--Repertory 13, pt.
      ii, fos. 442b, 443, 461; Repertory 14, fos. 446b, 477b, 478;
      Repertory 16, fo. 6b. 1335 Printed Report. Co. Co., 20 May, 1836. 1336 See Report Committee of the whole Court for General Purposes, with
      Appendix, 31 May, 1892 (_Printed_). M691 Growing unpopularity of Warwick, 1550-1551. 1337 Grey Friars Chron., p. 66. The surrender of Boulogne was "sore
      lamented of all Englishmen."--Wriothesley, ii, 37. 1338 Repertory 12, pt. ii, fo. 271b; Letter Book R, fos. 74, 85b; Journal
      16, fos. 66b, 91b. M692 The debasement of the currency, 1551. 1339 Letter Book R, fo. 115; Journal 16, fo. 118. 1340 Wriothesley, ii, 48. The price of living became so dear that the
      town clerk and the under-sheriffs asked for and obtained from the
      Common Council an increase of emoluments.--Letter Book R, fo. 117b. 1341 Wriothesley, ii, 54. 1342 Grey Friars Chron., p. 72. M693 The Duke of Somerset again arrested, 16 Oct., 1551. 1343 Wriothesley, ii, 56; Grey Friars Chron., p. 71. 1344 Grey Friars Chron., pp. 72, 73. 1345 -_Id._, pp. 71, 72. M694 Trial and execution of Somerset, 22 Jan., 1552. 1346 Wriothesley, ii, 57. 1347 Repertory 12, pt. ii, fo. 426; Letter Book R, fo. 157b. 1348 Wriothesley, ii, 63. 1349 Holinshed, iii, 1032. M695 The City and the Royal Hospitals, 1547-1553. 1350 Journal 15, fo. 325b; Letter Book Q, fo. 214b. 1351 Letter Book Q, fo. 237; Repertory 11, fo. 445b. 1352 Journal 15, fo. 384. 1353 Letter Book Q, fo. 261b; Journal 15, fos. 398, 401; Appendix vii to
      "Memoranda of the Royal Hospitals," pp. 46-51. M696 St. Thomas's Hospital. 1354 Repertory 12, pt. ii., fos. 311, 312b. 1355 Both deeds are printed in Supplement to Memoranda relating to Royal
      Hospitals, pp. 15-32. M697 Christ's Hospital. 1356 Son of Robert Dobbs, of Batley, Yorks. Alderman of Tower Ward.
      Knighted 8 May, 1552. _Ob._ 1556. Buried in Church of St. Margaret
      Moses.--Machyn, pp. 105, 269, 349; Wriothesley, ii, 69. 1357 Report, Charity Commissioners, No. 32, pt. vi, p. 75; Strype, Stow's
      "Survey," bk. i, p. 176. M698 Bridewell Hospital. 1358 Among the names of those forming the deputation appears that of
      Richard Grafton, whose printing house, from which issued "The
      Prymer"--one of the earliest books of private devotion printed in
      English as well as Latin--was situate within the precinct of the Old
      Grey Friars.--Repertory 12, p. ii., fos. 271b, 272b. 1359 Strype, Stow's "Survey," bk. i, p. 176. 1360 Wriothesley, 83; Repertory 13, fo. 60. 1361 Charter dated 26 June, 1553. M699 Northumberland's conspiracy, 1553. 1362 "Letters Patent for the limitation of the Crown," sometimes called
      the "counterfeit will" of King Edward VI.--Chron. of Q. Jane and Q.
      Mary (Camd. Soc., No. 48), pp. 91-100. 1363 Richard Hilles to Henry Bullinger, 9 July, 1553.--"Original letters
      relative to the English Reformation" (Parker Soc.), pp. 272-274. M700 Lady Jane Grey proclaimed queen, 10 July, 1553. 1364 Grey Friars Chron., pp. 78, 79. M701 Queen Mary proclaimed, 19 July. 1365 Wriothesley, ii, 88-90. M702 Northumberland sent to the Tower, 25 July. 1366 Letter Book R, fo. 262b; Repertory 13, pt. i, fo. 68. 1367 Wriothesley, ii, 90, 91; Grey Friars Chron., p. 81. M703 Queen Mary enters the city. 3 Aug. 1368 Repertory 13, pt. i, fo. 69. 1369 -_Id._, fo. 70b. 1370 Repertory 13, pt. i, fo. 69b. 1371 Wriothesley, 93-95. 1372 Chron. of Q. Jane and Q. Mary, p. 14; Wriothesley, ii, 95. M704 Mary releases the bishops and restores the mass.
 M705 Disturbances in the city. 1373 Grey Friars Chron., p. 83; Wriothesley, ii, 96-98. 1374 Chron. of Q. Jane and Q. Mary, p. 24. 1375 Letter Book R, fo. 270; Journal 16, fo. 261b. 1376 Wriothesley, ii, 99, 100; Holinshed, iv, 3. M706 Election of Thomas White mayor, 29 Sept., 1553. 1377 Citizen and Merchant Taylor. Son of William White, of Reading, and
      formerly of Rickmansworth. Founder of St. John's College, Oxford,
      and principal benefactor of Merchant Taylors' School. Alderman of
      Cornhill Ward; when first elected alderman he declined to accept
      office and was committed to Newgate for contumacy (Letter Book Q,
      fo. 109b; Repertory 11, fo. 80b). Sheriff 1547. Knighted at
      Whitehall 10 Dec., 1553 (Wriothesley, ii, 105). His first wife,
      Avice (surname unknown), died 26 Feb., 1588, and was buried in the
      church of St. Mary Aldermary. He afterwards married Joan, daughter
      of John Lake and widow of Sir Ralph Warren, twice Mayor of London.
      _Ob._ 11 Feb., 1566, at Oxford, aged 72.--Clode, "Early Hist. Guild
      of Merchant Taylors," pt. ii, chaps. x-xii; Machyn's Diary, pp. 167,
      330, 363. M707 The queen's coronation, 1 Oct. 1378 Journal 16, fo. 261; Repertory 13, pt. i, fo. 74b. 1379 Grey Friars Chron., p. 84. M708 Mary's first parliament, Oct.-Nov., 1553. 1380 Met in October, 1553. The names of the city's representatives are
      not recorded. The Court of Aldermen, according to a custom then
      prevalent, authorized the city chamberlain to make a gift of £6
      13_s._ 4_d._ to Sir John Pollard, the Speaker, "for his lawfull
      favor to be borne and shewed in the parlyment howse towardes this
      cytie and theyre affayres theire."--Repertory 13, pt. i, fo. 92. M709 Trial at the Guildhall of Lady Jane Grey, Cranmer and others, Nov.,
      1553. 1381 Grey Friars Chron., p. 85; Wriothesley, ii, 104; Chron. Q. Jane and
      Q. Mary, p. 32. There is preserved in the British Museum a small
      manual of prayers believed to have been used by Lady Jane Grey on
      the scaffold. The tiny volume (Harl. MS., 2342) measures only 3-1/2
      inches by 2-3/4 inches, and contains on the margin lines addressed
      to Sir John Gage, lieutenant of the Tower, and to her father, the
      Duke of Suffolk. M710 Outbreak of Wyatt's Rebellion. Jan., 1554. 1382 Journal 16, fo. 283. 1383 Chron. of Q. Jane and Q. Mary, 35. 1384 Wriothesley, ii, 106. M711 The city put into a state of defence. 1385 Repertory 13, pt. i, fos. 116, 116b, 117, 117b, 119-122b. 1386 Wriothesley, ii, 107. M712 The queen's speech at the Guildhall, 1 Feb., 1554. 1387 Repertory 13, pt. i, fo. 121. 1388 Foxe's "Acts and Monuments," vi, 414-415; Holinshed, iv, 16. 1389 Holinshed, iv, 15. 1390 Repertory 13, pt. i, fo. 124. M713 A force of 1,000 men raised in the city. 1391 Wriothesley, iii, 109. 1392 Stow. M714 Wyatt and his followers before Ludgate.
 M715 Wyatt made prisoner and lodged in the Tower. 1393 Foxe's "Acts and Monuments," vi, 415. 1394 Grey Friars Chron., p. 87. 1395 Chron. of Q. Jane and Q. Mary, p. 43; Wriothesley, iii, 107, 108. 1396 Grey Friars Chron., p. 87. M716 Execution of Lady Jane Grey, Wyatt and others. 1397 Machyn, 45. The gibbets remained standing till the following June,
      when they were taken down in anticipation of Philip's public entry
      into London.--Chron. of Q. Jane and Q. Mary, 76. 1398 Grey Friars Chron., p. 89. M717 Measures for preserving the peace. 1399 Journal 16, fo. 283; Letter Book R, fo. 288. 1400 Repertory 13, pt. i, fo. 131. M718 The lord mayor before the Star Chamber. 1401 Holinshed, iv, 26. 1402 Repertory 13, pt. i, fo. 153; Letter Book R, fo. 293. M719 Demand of money from the city, 1554. 1403 Repertory 13, pt. i, fo. 130; Journal 16, fo. 284b. 1404 Repertory 13, pt. i, fo. 138b. 1405 -_Id._, fos. 142b, 146b. 1406 -_Id._, fo. 147. M720 Trial at the Guildhall of Nicholas Throckmorton, 17 April. 1407 Wriothesley, ii, 115. 1408 Repertory 13, pt. i, fo. 186b. 1409 -_Id._, fo. 190b. 1410 Howell's "State Trials," i, 901, 902; Chron. of Q. Jane and Q. Mary,
      p. 75. M721 The queen's marriage, July, 1554. 1411 It sat from 2 April until 5 May.--Wriothesley, ii, 114, 115. The city
      returned the same members that had served in the last parliament of
      Edward VI, namely, Martin Bowes, Broke the Recorder, John Marsh and
      John Blundell. 1412 Journal 16, fo. 295b. 1413 Repertory 13, pt. i, fos. 165, 166, 166b, 170. M722 The passage of the king and queen through the city, 19 Aug. 1414 Chron. of Q. Jane and Q. Mary, p. 77. 1415 -_Id._, p. 78. 1416 Journal 16, fo. 263. 1417 Repertory 13, pt. i, fo. 191. A full account of the pageants, etc.,
      will be found in John Elder's letter.--Chron. of Q. Jane and Q. Mary,
      Appendix X. 1418 Chron. of Q. Jane and Q. Mary, pp. 78-79. M723 The reconciliation with Rome, 1554. 1419 Martin Bowes, of the old members, alone continued to sit for the
      city, the places of the other members being taken by Ralph
      Cholmeley, who had succeeded Broke as Recorder; Richard Grafton, the
      printer; and Richard Burnell. 1420 Chron. of Q. Jane and Q. Mary, 82; Wriothesley, 122. 1421 Repertory 13, part i, fo. 111b. 1422 -_Id._, fo. 193. 1423 Journal 16, fo. 300. Bishop Braybroke, nearly two centuries before,
      had done all he could to put down marketing within the sacred
      precincts, and to render "Paul's Walk"--as the great nave of the
      cathedral was called--less a scene of barter and frivolity. 1424 Repertory 13, pt. i, fo. 251b. 1425 In 1558, a man convicted of breaking this law was ordered to ride
      through the public market places of the city, his face towards the
      horse's tail, with a piece of beef hanging before and behind him,
      and a paper on his head setting forth his offence.--Repertory 13, fo.
      12b. 1426 Repertory 13, pt. i, fo. 193; Letter Book S, fo. 119b. M724 Opposition to the reestablishment of the old religion. 1427 Journal 16, fo. 285b; Letter Book R, fo. 290b; Repertory 13, pt. i,
      fo. 147; Wriothesley, ii, 114. 1428 Grey Friars Chron., p. 89. 1429 -_Id._, p. 95. 1430 -_Id._, _ibid._ 1431 -_Id._, p. 78n. M725 The Marian persecution, 1555. 1432 Journal 16, fo. 321b. 1433 Wriothesley, ii, 126; Grey Friars Chron., p. 94. 1434 Wriothesley, ii, 126n; Grey Friars Chron., pp. 56, 57, 95. 1435 Foxe's "Acts and Monuments," vi, 717, 737, 740, vii, 114, 115. 1436 "Item the vth day of September [1556], was browte thorrow Cheppesyde
      teyd in ropes xxiijti tayd together as herreytkes, and soo unto the
      Lowlers tower."--Grey Friars Chron., p. 98. M726 Renewed opposition to strangers in the city. 1437 "At this time [Aug., 1554] there was so many Spanyerdes in London
      that a man shoulde have mett in the stretes for one Inglisheman
      above iiij Spanyerdes, to the great discomfort of the Inglishe
      nation. The halles taken up for Spanyerdes."--Chron. Q. Jane and Q.
      Mary, p. 81. 1438 -_Id._, _ibid_. 1439 Repertory 13, pt. i, fo. 205b. 1440 By an order in council, dated Greenwich, 13 March, 1555, the
      merchants of the Steelyard were thenceforth to be allowed to buy
      cloth in warehouses adjoining the Steelyard, without hindrance from
      the mayor. The mayor was ordered to give up cloth that had been
      seized as foreign bought and sold at Blackwell Hall. He was,
      moreover, not to demand _quotam salis_ of the merchants, who were to
      be allowed to import into the city fish, corn and other provisions
      free of import.--Repertory 13, pt. ii, fo. 384b; Letter Book S, fo.
      76. 1441 Repertory 13, pt. ii, fos. 399b, 404, 406; Letter Book S, fos. 70,
      93b. 1442 Repertory 13, pt. ii, fo. 508b. 1443 Wheeler's "Treatise of Commerce" (ed. 1601), p. 100. 1444 Repertory 13, pt. ii, fos. 507b, 520b, 540. 1445 Repertory 13, pt. ii, fo. 529. 1446 -_Id._, fo. 526b. 1447 -_Id._, fo. 534b. M727 Philip leaves England, 4 Sept., 1555.
 M728 The queen obtains a City loan of £6,000, Aug., 1556.
 M729 War declared against France, 7 June, 1557. 1448 Repertory 13, pt. ii, fo. 420. 1449 Stafford had issued a proclamation from Scarborough Castle
      declaiming against Philip for introducing 12,000 foreigners into the
      country, and announcing himself as protector and governor of the
      realm. He was captured by the Earl of Westmoreland and executed on
      Tower Hill 28 May.--Journal 17, fo. 34b; Letter Book S, fo. 127b;
      Holinshed. iv, 87; Machyn's Diary, p. 137. 1450 Journal 17, fo. 37b; Letter Book S, fo. 131. 1451 Journal 17, fos. 37b, 38; Letter Book S, fo. 131b. 1452 Machyn, p. 142. M730 A City contingent joins the expedition to France. 1453 Repertory 13, pt. ii, fo. 517. 1454 "London fond v.c. men all in bluw cassokes, sum by shyppes and sum
      to Dover by land, the goodlyst men that ever whent, and best be-sene
      in change (of) apprelle."--Diary, p. 143. 1455 Merchant Taylor, son of William Offley, of Chester; alderman of
      Portsoken and Aldgate Wards. Was one of the signatories to the
      document nominating Lady Jane Grey successor to Edward VI, and was
      within a few weeks (1 Aug.) elected sheriff. Knighted with alderman
      William Chester, 7 Feb., 1557.  His mansion-house was in Lime
      Street, near the Church of St. Andrew Undershaft. _Ob._ 29 Aug,
      1582.--Machyn, pp. 125, 353; Index to Remembrancia, p. 37, note.
      Fuller, who erroneously places his death in 1580, describes him as
      the "Zaccheus of London" not "on account of his low stature, but his
      great charity in bestowing half of his estate on the poor."--Fuller's
      "Worthies," p. 191. 1456 Repertory 13, pt. ii, fos. 521b, 522; Letter Book S, fo. 134. M731 The City called upon to furnish another contingent of 1,000 men, 31
      July. 1457 Journal 17, fo. 54b. M732 The citizens make demur, but in vain. 1458 Repertory 13, pt. ii, fo. 530. 1459 Repertory 13, pt. ii, fos. 530, 532, 522b, 535; Journal 17, fo. 54. M733 The French king defeated at St. Quentin, 27 Aug., 1557. 1460 Machyn, p. 147. M734 The loss of Calais, 7 Jan., 1558.
 M735 A city force despatched, 24 Jan., 1558. 1461 Repertory 13, pt. ii, fo. 571. 1462 Journal 17, fo. 55. See Appendix. They were ordered in the first
      instance to be forwarded to Dover by the 19th Jan. at the latest,
      but on the 6th Jan. the Privy Council sent a letter to the mayor to
      the effect that "albeit he was willed to send the vc men levied in
      London to Dover, forasmuch as it is sithence considered here that
      they may with best speede be brought to the place of service by
      seas, he is willen to sende them with all speede by hoyes to
      Queenburgh, where order is given for the receavinge and placing of
      them in the shippes, to be transported with all speede
      possible."--Harl. MS. 643, fo. 198; Notes to Machyn's Diary, p. 362. 1463 Journal 17, fo. 56. 1464 Wriothesley, ii, 140. 1465 Order of the Court of Aldermen, 10 Jan.--Repertory 13, pt. ii, fo.
      582. 1466 Repertory 13, pt. ii, fo. 582b; Precept to the Companies.--Journal
      17, fo. 56b. 1467 Journal 17, fo. 57. So furious was this storm, lasting four or five
      days, that "some said that the same came to passe through
      necromancie, and that the diuell was raised vp and become French,
      the truth whereof is known (saith Master Grafton) to
      God."--Holinshed, iv, 93. 1468 Journal 17, fo. 7. 1469 Repertory 14, fo. 1b; Journal 17, fo. 58; Machyn, 164. 1470 Journal 17, fos. 59, 59b; Letter Book S, fos. 154b, 155. M736 A city loan of £20,000, March, 1558. 1471 Cal. State Papers Dom. (1547-1580), p. 100; Wriothesley, ii, 140,
      141. 1472 Stat. 5 and 6, Edward VI, c. 20, which repealed Stat. _37_, Henry
      VIII, c. 9 (allowing interest to be taken on loans at the rate of
      ten per cent.) and forbade all usury. This Statute was afterwards
      repealed (Stat. 13, Eliz., c. 8) and the Statute of Henry VIII
      re-enacted. The dispensation granted by Mary was confirmed in 1560
      by Elizabeth.--Repertory 14, fo. 404b. 1473 Repertory 14, fo. 15b; Journal 17, fo. 63. A large portion of this
      loan was repaid by Elizabeth soon after her accession.--Repertory 14,
      fos. 236b, 289. M737 Death of Mary, 17 Nov., 1558. 1474 Repertory 14, fos. 94b, 96b. M738 The ascension of Elizabeth, 17 Nov., 1558. 1475 The commemoration was eventually put down by the Stuarts as giving
      rise to tumults and disorders.--Journal 49, fo. 270b; Luttrell's
      Diary, 17 Nov., 1682. 1476 Son of Roger Leigh, of Wellington, co. Salop, an apprentice of Sir
      Rowland Hill, whose niece, Alice Barker, he married. Buried in the
      Mercers' Chapel. By his second son, William, he was ancestor of the
      Lords Leigh, of Stoneleigh, and by his third son William,
      grandfather of Francis Leigh, Earl of Chichester.--Notes to Machyn's
      Diary, p. 407. 1477 "The order of the sheryfes at the receyvyng of the quenes highenes
      in to Myddlesex."--Letter Book S, fo. 183; Repertory 14, fo. 90b. M739 The queen's coronation, 15 Jan., 1559. 1478 Letter Book S, fo. 182b; Journal 7, fo. 101b. 1479 Repertory 14, fos. 97, 98. 1480 -_Id._, fo. 99. 1481 -_Id._, fo. 102b. M740 A strike among the painters. 1482 Repertory 14, fo. 103b. M741 Elizabeth's policy of moderation, 1558. 1483 Dated 27 Dec., 1558.--Journal 17, fo. 106b. M742 The Act of Uniformity and Supremacy, 1558.
 M743 The restoration of the Prayer Book and abolition of the Mass, 1559. 1484 Wriothesley, ii, 145. 1485 -_Id._ _ibid_. 1486 Repertory 4, fo. 213b. M744 Ultra-Protestant reformers in the city, 1559. 1487 Journal 17, fos. 120b, 168; Repertory 14, fo. 152; Letter Book T,
      fo. 82b. 1488 "In some places the coapes, vestments, and aulter clothes, bookes,
      banners, sepulchers and other ornaments of the churches were burned,
      which cost above £2,000 renuinge agayne in Queen Maries time"
      (Wriothesley, ii, 146; _Cf._ Machyn, p. 298). Among the churchwarden
      accounts of the parish of St. Mary-at-Hill for the year 1558-1559
      there is a payment of one shilling for "bringing down ymages to
      Romeland (near Billingsgate) to be burnt." 1489 Proclamation, dated 19 Sept., 1559.--Journal 17, fo. 267; Letter Book
      T, fo. 5b. M745 The claims of Mary Stuart, 1559-1560. 1490 Journal 17, fo. 184b. 1491 Proclamation, dated 24 March, 1560.--Journal 17, fo. 223b. 1492 In April the city was called upon to furnish 900 soldiers, in May
      250 seamen, and in June 200 soldiers.--Repertory 14, fos. 323, 336,
      339b, 340, 340b, 344b; Journal 17, fos. 238b, 244. It is noteworthy
      that the number of able men in the city at this time serviceable for
      war, although untrained, was estimated to amount to no more than
      5,000.--Journal 17, fo. 244b. M746 The French war, 1562-1564. 1493 Journal 18, fos. 57-60b. The livery companies furnished the men
      according to allotment. The barber-surgeons claimed exemption by
      statute (32 Henry VIII, c. 42), but subsequently consented to waive
      their claim. The city also objected to supplying the soldiers with
      cloaks.--Repertory 15, fos. 110b, 113. 1494 Journal 18, fo. 66; Machyn, pp. 292, 293. 1495 Journal 18, fo. 71. M747 Soldiers for the defence of Havre. 1563. 1496 The queen to the mayor and corporation of London, 30 June,
      1563.--Journal 18, fo. 124. 1497 Repertory 15, fo. 258. 1498 -_Id._, fo. 259. 1499 -_Id._, fo. 263. 1500 The queen to the mayor, 2 Aug., 1563.--Journal 18, fo. 140. Precept
      of the mayor.--_Id._, fo. 136; Repertory 15, fo. 279b; Machyn's
      Diary, p. 312. 1501 Journal 18, fo. 128. 1502 -_Id._, fo. 119b. 1503 Repertory 15, fo. 265b. M748 The loss of Havre, July, 1563. 1504 Machyn, 312. 1505 Journal 18, fos. 139, 139b, 142, 151b, 152b, 154, 156b, 184, 189b.
      With the sickness was associated, as was so often the case, a
      scarcity of food.--Repertory 15, fos. 127, 133b, 138, 168, 178, 179b,
      etc. The rate of mortality increased to such an extent that a
      committee was appointed for the purpose of procuring more burial
      accommodation.--Repertory 15, fos. 311b, 313b, 333. 1506 Proclamation dated 1 Aug., 1563.--Journal 18, fo. 141. M749 Peace between England and France signed, 13 April, 1564. 1507 Repertory 15, fo. 284b. 1508 Journal 18, fo. 249. 1509 -_Id._, fo. 190b. 1510 Journal 18, fos. 214, 215, 227, 291b, 354b; Holinshed, iv, 224. M750 The restoration of St. Paul's Cathedral, 1561-1565. 1511 Journal 17, fos. 320, 321, 331b; Letter Book T, fos. 42, 42b;
      Repertory 14, fo. 491b. The fire caused by the lightning threatened
      the neighbouring shops, and their contents were therefore removed to
      Christchurch, Newgate and elsewhere for safety.--Journal 17, fo.
      319b; Letter Book T, fo. 42. 1512 Repertory 15, fos. 474, 478. 1513 Repertory 16, fos. 227, 241b, 274; Letter Book V, fo. 108b. 1514 Repertory 16, fos. 303b, 448. Among the Chamber Accounts of this
      period we find an item of a sum exceeding £4 paid for "Cusshens to
      be occupied at Powles by my L. Maior and thaldermen, vz:--for cloth
      for the uttorside lyning of leather feathers and for making of theym
      as by a bill appearth."--Chamber Accounts, Town Clerk's Office, vol.
      i, fo. 50b. M751 Sir Thomas Gresham and the City Burse. 1565-1566. 1515 Journal 13, fos. 417, 420, 435, 442b, 443. 1516 Cotton MS., Otho E, x. fo. 45; _Cf._ Burgon's "Life of Gresham," i,
      31-33. 1517 Journal 14, fos. 124, 124b. 1518 By Sir Richard's first wife Audrey, daughter of William Lynne, of
      Southwick, co. Northampton. Sir Thomas is supposed to have been born
      in London in 1519. Having been bound apprentice to his uncle, Sir
      John Gresham, he was admitted to the freedom of the Mercers' Company
      in 1543. Married Anne, daughter of William Ferneley, of West
      Creting, co. Suffolk, widow of William Read, mercer. 1519 The queen's business kept him so much abroad that her majesty wrote
      to the Common Council (7 March, 1563) desiring that he might be
      discharged from all municipal duties.--Journal 18, fo. 137. 1520 Printed in Burgon's "Life of Gresham," i, 409. 1521 Repertory 15, fo. 237b. 1522 Burgon, ii, 30-40. 1523 Repertory 15, fos. 406b, 407. M752 Difficulties of obtaining a site. 1524 Repertory 15, fos. 410b, 412. 1525 -_Id._, fos. 417b, 431. 1526 Repertory 16, fos. 31b, 32b, 43b; Letter Book V, fos. 5, 7b, 8, 17,
      21b. 1527 The amount of subscriptions and charges is set out in a "booke" and
      entered on the City's Journal (No. 19, fos. 12-20; _Cf._ Letter Book
      V, fos. 70b-79); see also Repertory 16, fo. 126. 1528 Journal 18. fo. 398. M753 Strong foreign element in connection with the building of the first
      Burse. 1529 Repertory 16, fo. 316. 1530 Repertory 16, fo. 406b. 1531 Repertory 15, fo. 268b. 1532 Repertory 16, fo. 229. M754 The Burse opened by Q. Elizabeth, 23 Jan., 1571.
 M755 Wanton damage done to the new Burse. 1533 "A proclamacioun concernyng the cutting of the crest conyzans and
      mantell of the arms of Sr Thomas Gresham."--Journal 19, fo. 150b;
      Letter Book V, fo. 222. 1534 Journal 20, pt. ii, fo. 341. M756 Insurance business carried on at the Royal Exchange. 1535 Repertory 18, fo. 362. 1536 "Law and Practice of Marine Insurance," by John Duer, LL.D. (New
      York, 1845), Lecture ii, p. 33. 1537 At the present day the form of policy used at Lloyds and commonly
      called the "Lloyd's policy" contains the following clause:--"and it
      is agreed by us the insurers, that this writing or policy of
      assurance shall be of as much force and effect as the surest writing
      or policy of assurance heretofore made in Lombard Street or in the
      Royal Exchange or elsewhere in London."--Arnould, "Marine Insurance"
      (6th ed.), i, 230. 1538 Repertory 18, fo. 362b. 1539 Cal. State Papers Dom. (1547-1580), p. 523. 1540 Repertory 19, fos. 166b, 168. 1541 The reader is here reminded that there is an essential difference
      between life policies and fire or marine policies of assurance. The
      latter, being policies of indemnity, recovery can be had at law only
      to the extent of the actual damage done, whereas in life policies
      the whole amount of the policy can be recovered. M757 Music and football at the Exchange. 1542 Repertory 17, fo. 300. 1543 Repertory 19, fo. 150. M758 Gresham College and Lectures. 1544 Cal. Wills, Court of Hust., London, ii, 698. 1545 Printed Report "Gresham College Trust," 29 Oct., 1885. M759 The Act of Uniformity strictly enforced, 1565.
 M760 Gresham's hospitality to Cardinal Chastillon, 1568. 1546 A return made in 1567 by the livery companies of foreigners residing
      in the city and liberties gives the number as 3,562.--Repertory 16,
      fo. 202. Another authority gives the number as 4,851, of which 3,838
      were Dutch.--Burgon's "Life of Gresham," ii, 242, citing Haynes, p.
      461. 1547 Burgon's "Life of Gresham," ii, 271-275. M761 The city crowded with refugees from the continent. 1548 Repertory 16, fo. 164. 1549 Journal 19, fo. 116. 1550 Precept of the mayor to that effect, 19 Oct., 1568.-_Id._, fo. 132b. 1551 Repertory 16, fo. 451. 1552 Journal 19, fo. 180; Letter Book V, fo. 245. 1553 Letter Book V, fo. 246.  Holinshed (iv, 234) and others give the
      whole credit of providing the cemetery to the liberality of Sir
      Thomas Rowe, the mayor. M762 The Prince of Orange receives substantial assistance from the
      citizens. 1554 Proclamation (15 July, 1568) against suspected persons landing in
      England or returning "with any furniture for mayntenaunce of ther
      rebellion or other lyke cryme" against the King of Spain.--Journal
      18, fo. 115; _Cf._ Letter Book V, fos. 181, 246b. 1555 Green, "Hist. of the English People," ii, 418. M763 The decline of Antwerp London's opportunity.
 M764 The queen applies to the merchant adventurers for a loan. 1556 Repertory 15, fos. 162, 164, 166b, 241b, 258, 267b, 297, etc. 1557 Strype, Stow's "Survey" (ed. 1720), bk. i, p. 283. M765 The first public lottery, 1567-1569. 1558 Journal II, fo. 253. 1559 Journal 19, fos. 55-58; Letter Book V, fos. 115b-117b. 1560 Price's "London Bankers" (enlarged edition), p. 51. 1561 Letter Book V, fo. 139. 1562 Cal. State Papers Dom. (1547-1580), p. 314. 1563 Clode, "Early Hist. of the Guild of Merchant Taylors," pt. ii, pp.
      229-230. 1564 Journal 19, fo. 133b. 1565 Holinshed, iv, 234. 1566 "Mesmes j'entendz que de la blanque, qu'on a tirée ces jours passés
      en ceste ville, ceste Royne retirera pour elle plus de cent mille
      livres esterlin, qui sont 33,000 escuz; de quoy le monde murumre
      assés pour la diminution qu'ilz trouvent aulx bénéfices qu'ilz
      esperoient de leurs billetz"--wrote De la Motlie Fénélon, the French
      ambassador in London.--Cooper's "Recueil des Dépéches, etc., des
      Ambassadeurs de France (Paris and London, 1838-1840)," i, 155. M766 English merchants in Antwerp arrested by order of Alva, 1568.
 M767 Elizabeth retaliates by seizing treasure on board Spanish vessels. 1567 Proclamation, 6 Jan., 1569.--Journal 19, fo. 139; Letter Book V, fo.
      210. 1568 See letter from Sir Arthur Champernowne, William Hawkins and others
      to the lords of the council. 1 Jan., 1569.--Cal. State Papers Dom.
      (1547-1580), p. 326. M768 Order to seize Flemish merchants and their goods in London, Jan.,
      1569. 1569 Cal. State Papers Dom. (1547-1580), p. 326. 1570 Cotton MS., Galba C, iii, fo. 151b. This letter was signed by John
      Gresham, Thomas Offley, John White, Roger Martyn, Leonell Duckett,
      Thomas Heaton, Richard Wheler, Thomas Aldersey and Francis Beinson. 1571 Citizen and Merchant Taylor: Alderman of the Wards of Portsoken and
      Bishopsgate; Sheriff, 1560-61. _Ob._ 2 Sept., 1570. Buried in
      Hackney Church. He bestowed the sum of £100 for the relief of
      members of his company "usinge the brode shire or ell rowinge of the
      pearch or making of garmentes" during his lifetime, and some landed
      estate in the city by his will for like purpose.--Letter Book V, fo.
      274b; Cal. of Wills, Court of Husting, ii, 686. 1572 Letter printed (from original among State Papers Dom.) in Burgon's
      "Life of Gresham," ii, 287. M769 Alva's envoy demands restitution. 1573 Sir Thomas Rowe, mayor, to Secretary Cecil. 23 Jan., 1569.--Cal.
      State Papers Dom. (1547-1580), p. 329; Burgon's "Life of Gresham,"
      ii, 295-296. 1574 -_Id._, 25 Jan. 1575 Cooper's "Dépźches, etc., des Ambassadeurs de France," i, 176-177. 1576 Burgon's "Life of Gresham," ii, 297. M770 Gresham suggests minting the Spanish treasure, 14 Aug., 1569. 1577 Lansd. MS., No. xii, fo. 16b. 1578 -_Id._, fo. 22. M771 The City Courts closed to Spanish suitors, 11 July, 1570. 1579 Repertory 17, fo. 36b. M772 Failure of efforts to effect a mutual restoration of goods seized.
 M773 Spanish goods ordered to be sold.
 M774 The respective claims of England and Spain referred to arbitration. 1580 Journal 19, fo. 247b; Letter Book V, fo. 301. 1581 Journal 19, fo. 257. 1582 -_Id._, fo. 390b. 1583 Journal 19, fo. 390b. 1584 Add. MS., No. 5, 755, fo. 58. M775 Insurrection of the Earls of Northumberland and Westmoreland, 1569. 1585 In the following year he was removed to the Charterhouse, but being
      discovered in correspondence with the deposed Queen of Scots was
      again placed in the Tower. He was tried and convicted of treason,
      and after some delay executed on Tower Hill.--Holinshed, iv, 254,
      262, 264, 267. 1586 The proclamation, which is set out in Journal 19, fo. 202b (_Cf._
      Letter Book V, fo. 267b), gives in detail the rise and progress of
      the rebellion. M776 Measures taken for safe-guarding the city. 1587 Journal 19, fo. 202; Letter Book V, fo. 267. 1588 Journal 19, fo. 202; Letter Book V, fo. 267. 1589 Letter Book V, fo. 269. 1590 Journal 19, fo. 206b; Letter Book V, fo. 270b; Repertory 16, fo.
      522b. M777 Papal Bull of excommunication against Elizabeth, 1570. 1591 Holinshed, iv, 254. M778 Rejoicing in the city after the battle of Lepanto, 7 Oct., 1571. 1592 -_Id._, 262. 1593 From Hertfordshire, alderman of Billingsgate Ward. 1594 Dated 8 Nov.--Journal 19, fo. 370b. 1595 Holinshed, iv, 263. 1596 Repertory 17, fos. 8b, 23, 27b, 29. 243, etc.; Repertory 19, fos.
      24b, 154, etc.; City Records known as "Remembrancia" (Analytical
      Index), pp. 51-55. M779 Peace and commercial prosperity, 1572. 1597 Stranger denizens, carrying on a handicraft in the city, had
      recently preferred a Bill in Parliament against several of the
      livery companies. They were persuaded, however, to drop it, and
      refer their grievance to the Court of Aldermen.--Repertory 17, fos.
      302b, 335, 337. A return made by the mayor (10 Nov., 1571) of the
      strangers then living in London and Southwark and liberties thereof
      gives the total number as 4,631.--Cal. State Papers Dom. (1547-1580),
      p. 427. 1598 Repertory 17, fo. 372. M780 The shifting policy of Elizabeth towards Spain and France,
      1572-1574. 1599 Journal 19, fos. 407-408b, 417-417b; Repertory 17, fos. 292, 298b,
      307, 308. 1600 Journal 20, pt. i, fos. 133b, 143b; Repertory 18, fo. 224b. 1601 Journal 20, pt. i, fo. 156b. M781 Piracy rampant, 1575-1576. 1602 Journal 20, pt. i, fo. 252; _Id._, pt. ii, fo. 280b. M782 A loan of£30,000, June, 1575.
 M783 A city Chamberlain dismissed from office. 1603 Journal 20, pt. i, fos. 228b, 239. 1604 Repertory 19, fo. 98. 1605 Journal 20, pt. ii, fo. 371. 1606 He was removed by order of Common Council, 13 Dec., _pre diversis
      magnis rebus dictam civitatem et negotia ejusdem
      tangentibus_.--Journal 20, pt. ii, fo. 376b. M784 The city called upon to furnish soldiers, 1578. 1607 Journal 20, pt. ii, fos. 388b, 389, 394-395b. The queen to the
      mayor, etc., of London, 12 March.--Cal. State Papers Dom.
      (1547-1580), p. 586. 1608 Journal 20, pt. ii, fo. 409b. 1609 -_Id._, fos. 404, 408b, 412. 1610 Repertory 19, fo. 346b. M785 Count Casimir at Gresham House, Jan., 1579.
 M786 Death of Sir Thomas Gresham, 21 Nov., 1579.
 M787 Count Casimir presented by the city with a gift of 500 marks. 1611 This conjecture is made from the fact of a precept having been
      issued on the 20th Jan. for certain persons to furnish themselves
      with velvet coats, chains and horses, and a suitable suite, to wait
      upon the lord mayor on the following Saturday.--Journal 20, pt. ii,
      fo. 404b. 1612 Burgon's "Life of Gresham," ii, 451-452. 1613 Journal 20, pt. ii, fos. 464, 480. 1614 Continuation of Holinshed, iv, 315. M788 The plague in the city, 1580-1583. 1615 City Records known as "Remembrancia" (Printed Analytical Index), pp.
      306, 330, 331, 350-352; Journal 20, pt. ii, fos. 373, 379, 407. 1616 Remembrancia (Index), pp. 207, 331, 334; Journal 21, fo. 235b. 1617 Remembrancia, vol. i, No. 331. M789 Preparations for war.
 M790 Troubles in Ireland, 1579-1583. 1618 A reference to this defeat is to be found in the Dublin Assembly
      Roll under the year 1581.--"Cal. of Ancient Records of Dublin" (ed.
      by John T. Gilbert, 1891), ii, 155. 1619 Bright, "Hist. of England," ii, 539. 1620 Journal 21, fos. 19, 34, 52, 53, 69b-71b, 78b, etc.; Repertory 20,
      fos. 90, 117, 117b, 119b, etc.; Remembrancia (Analytical Index), pp.
      230-236. 1621 Journal 21, fo. 329b. 1622 Among Chamber Accounts _circa_ 1585 we find the following:--"Pd. the
      x of Dec. by order of Courte to Roger Warffeld Treasuror of
      Bridewell towards the conveyinge of all the Irishe begging people in
      and nere London to the Citie of Bristowe v1."--Chamber Accounts, Town
      Clerk's Office, vol. ii, fo. 17. M791 The Jesuits in the city, 1580-1581. 1623 Repertory 16, fo. 350. 1624 Repertory 18, fo. 167. 1625 Journal 20, fo. 219b. 1626 Journal 21, fo. 81b; Repertory 20, fo. 1b. M792 The Recusancy Laws, 1581. 1627 Journal 21, fo. 90. 1628 -_Id._, fos. 114b, 135, 290, 322. 1629 Remembrancia (Analytical Index), pp. 364, 365. M793 Special preachers appointed for the city, 1581-1582. 1630 As early as 1554 students had been supported by the Corporation and
      the Companies at the Universities.--Repertory 13, fos. 144b, 148,
      150b. 1631 Rembrancia, i, 250, 256 (Analytical Index, pp. 365, 366). Another
      difference shortly occurred between the corporation and the Bishop
      of London in October of this year. A dispute arose between them as
      to who was responsible for keeping St. Paul's Cathedral in repair,
      each party endeavouring to throw the burden upon the other (_Id._,
      Analytical Index, pp. 323-327); and in the following March (1582)
      Bishop Aylmer found cause to complain by letter of unbecoming
      treatment by the mayor, both of the bishop and his clergy, and
      threatened, unless matters changed for the better, to admonish the
      mayor publicly at Paul's Cross, "where the lord mayor must sit, not
      as a judge to control, but as a scholar to learn, and the writer,
      not as John Aylmer to be thwarted, but as John London, to teach him
      and all London."--(_Id._, _ibid._, pp. 128-129). 1632 Repertory 20, fo. 282. M794 Arrest and execution of Campion.
 M795 Breach with Spain, Jan., 1584. 1633 Son of Richard Osborne, of Ashford, co. Kent. The story goes that he
      was apprenticed to Sir William Hewet, clothworker, and that he
      married his master's daughter, whom he had rescued from a watery
      grave in the Thames at London Bridge. His son, Sir Edward Osborne,
      was created a baronet by Charles I, and his grandson, Sir Thomas,
      made Duke of Leeds in 1692 by King William III. 1634 Cal. State Papers Dom. (1581-1590), p. 157. The right of holding
      musters in Southwark was again questioned; and the claim of the city
      was upheld by Sir Francis Walsingham. For this he received the
      thanks of the lord mayor by letter dated 15 Feb.--_Id._, p. 159. M796 Muster of 4,000 men in Greenwich Park, 1584. 1635 "A lettre from the quenes maty for ye mustringe of 4000 men, and
      also for the shewes on the evens of St. John Baptist and St. Peter
      thapostles."--Journal 21, fo. 421b. 1636 Contin. of Holinshed, v, 599, 600. M797 Assassination of Prince of Orange, 10 July, 1584. 1637 Journal 21, fo. 388b. M798 Dutch envoys to Elizabeth, June, 1585. 1638 Stow's Annals (ed. 1592), pp. 1198-1201. 1639 Motley, "United Netherlands," i, pp. 318-324. M799 Recruits for service in the Low Countries, July, 1585. 1640 For particulars of his life see Remembrancia (Analytical Index), p.
      284, note. 1641 Journal 21, fo. 448b. M800 The fall of Antwerp and despatch of Leicester to the Low Countries,
      1585. 1642 "Thaccompte of the saide chamberlyn for the transportacioun and
      necessary provision of MMCCCCXX soldiers into the lowe countryes of
      Flaunders."--Chamber Accounts, vol. ii, fos. 56-58b. 1643 Motley, "United Netherlands," i, 340. 1644 Chamber Accounts, ii, 134. The earl's honor of Denbigh, North Wales,
      was mortgaged to certain citizens of London, and not being redeemed,
      was afterwards purchased by the queen herself.--Repertory 22, fo.
      287. 1645 Repertory 21, fos. 308-311. 1646 For many years after the passing of the Act (1 Edw. VI, c. 14)
      confiscating property devoted to "superstitious uses," the
      corporation and the livery companies were the objects of suspicion
      of holding "concealed lands," _i.e._ lands held charged for
      superstitious uses, which they had failed to divulge. The
      appointment of a royal commission to search for such lands was
      submitted to the law officers of the city for consideration, 9
      Sept., 1567.--Repertory 16, fo. 276b. Vexatious proceedings continued
      to be taken under the Act until the year 1623, when a Statute was
      passed, entitled "An Act for the General Quiet of the Subjects
      against all Pretences of Concealment whatsoever."--Stat. 21, James I,
      c. ii. M801 The city flooded with strangers from France and Flanders. 1647 Journal 22, fo. 1. 1648 -_Id._, fos. 26, 29. 1649 Journal 22, fo. 37b; Repertory 21, fo. 288b. M802 Discovery of the Babington plot, Aug., 1586. 1650 Journal 22, fos. 52-53.  Both the queen's letter and Dalton's speech
      are printed in Stow's Continuation of Holinshed, iv, 902-904. 1651 Journal 22, fos. 48, 57b, 58; Repertory 21, fo. 327. M803 Execution of Mary Stuart, 8 Feb., 1587. 1652 Proclamation, dated Richmond, 4 Dec., 1586.--Journal 22, fo. 67b. M804 A threatened famine in the city, Nov., 1586 1653 Royal Proclamation against engrossers of corn, 2 Jan., 1587.--Journal
      22, fo. 74. 1654 Journal 22, fo. 64. 1655 Repertory 21, fo. 370b. M805 Philip's preparations for invasion, 1587. 1656 Journal 21, fo. 136b. 1657 Motley, "United Netherlands," ii, 281. M806 Preparations in England, 1587-1588. 1658 Journal 22, fos. 144, 161b, 166-167b, 170b. 1659 Journal 22, fo. 190. 1660 Only 1,000 men out of the force raised by the city went to Tilbury,
      and the earl only consented to receive this small contingent on
      condition they brought their own provisions with them, so scantily
      was the camp supplied with victuals through the queen's
      parsimony.--Remembrancia (Analytical Index), p. 244. Letter from
      Leicester to Walsingham, 26 July.--Cal. State Papers Dom.
      (1581-1590), p. 513. 1661 Leicester to Walsingham, 28 July, 1588.--State Papers Dom., vol.
      ccxiii, No. 55. 1662 William of Malmesbury bears similar testimony to the courage of
      Londoners under good leadership: _Laudandi prorsus viri et quos Mars
      ipse collata non sperneret hasta si ducem habuissent_.--Gesta Regum
      (Rolls Series, No. 90), i, 208. 1663 Repertory 22, fo. 148b. M807 The City fits out sixteen ships and four pinnaces. 1664 A list of "the London shippes" (including pinnaces), dated 19 July,
      1588, is preserved among the State Papers (Domestic) at the Public
      Record Office (vol. ccxii, No. 68), and is set out in the Appendix
      to this work. Two other lists, dated 24 July, giving the names of
      the ships (exclusive of pinnaces) are also preserved (State Papers
      Dom., vol. ccxiii, Nos. 15, 16). Each of these lists give the number
      of vessels supplied by the city against the Armada as sixteen ships
      and four pinnaces, or as twenty ships (inclusive of pinnaces). It is
      not clear what was the authority of Stow (Howes's Chron., p. 743)
      for stating that the city, having been requested to furnish fifteen
      ships of war and 5,000 men, asked for two days to deliberate, and
      then furnished thirty ships and 10,000 men. At the same time there
      does exist a list of "shipps set forth and payde upon ye charge of
      ye city of London, anno 1588" (that is to say, the ships furnished
      by the city for that whole year), and that list contains the names
      of thirty ships, with the number of men on board each vessel and the
      names of the commanders.--State Papers Dom., vol. ccxxxii, fos. 16,
      16b. 1665 Journal 22, fo. 173. The assessment was afterwards (19 April)
      settled at three shillings in the pound.--_Id._, fo. 175. 1666 Journal 22, fos. 193, 200b. M808 The fate of the Armada, July, 1588. 1667 Richard Tomson to Walsingham, 30 July, 1588.--Cal. State Papers Dom.
      (1581-1590), p. 517. 1668 Hawkins to Walsingham, 31 July, 1588.--Cal. State Papers Dom.
      (1581-1590), p. 517. 1669 Howard to the same, 21 July.--_Id._, p. 507. 1670 Sir William Wynter to Walsingham, 1 Aug., 1588.--Cal. State Papers
      Dom. (1581-1590), p. 521. 1671 Journal 22, fo. 196b. 1672 -_Id._, fo. 196. M809 Richard Tomson and the London ship _Margaret and John_. 1673 Tomson to Walsingham, 30 July, 1588.--State Papers Dom., vol. ccxiii,
      No. 67. M810 The naval engagement off Gravelines 29 July, 1588.
 M811 The Armada driven northward.
 M812 Preparations in the city for receiving sick and wounded, 29 July. 1674 Repertory 21, fo. 578. 1675 Journal 22, fo. 200b; Cal. State Papers Dom. (1581-1590), p. 510. M813 Reports as to the fate of the Armada, July-Aug., 1588. 1676 Journal 22, fo. 197. 1677 -_Id._, fo. 199b. 1678 Journal 22, fo. 200. M814 The queen attends a public thanksgiving service at St. Paul's, 24
      Nov., 1588. 1679 Nichols' "Progresses of Q. Elizabeth," ii, 537. 1680 Journal 22, fos. 233, 235. 1681 Nichols' "Progresses of Q. Elizabeth," ii, 538, 539. M815 Monuments in city churches to Frobisher, Hawkins and Martin Bond. 1682 On the 7th Feb., 1583, previously to setting out on his last
      ill-fated expedition, Gilbert addressed a letter to Walsingham from
      "his house in Redcross Street."--Cal. State Papers Dom. (1581-1590),
      p. 95. 1683 See the will of Dame Margaret Hawkins, dated 23 April, 1619.--Cal. of
      Wills, Court of Hust., London, ii, 745. The will contains many
      bequests of articles which savour of Spanish loot. 1684 Strype, Stow's "Survey" (1720), bk. ii, p. 44. M816 Disorganized state of the camp at Tilbury. 1685 Journal 22, fo. 202b. M817 City loans of £30,000 and £20,000, Sept.-Dec., 1588. 1686 Journal 22, fo. 210; Repertory 21, fos. 590b, 593; Repertory 22,
      fos. 15, 26b, 27; Cal. State Papers Dom. (1581-1590), p. 471. M818 Expedition to Spain under Norris and Drake, April-July, 1589. 1687 Journal 22, fo. 252; Repertory 22, fo. 16b. 1688 Journal 22, fos. 227b, 278. M819 Disbanded soldiers and sailors in the city. 1689 Burghley and others to the mayor, 26 July, 1589.--Journal 22, fo.
      312. M820 Soldiers ordered to return to their own homes. 1690 -_Id._, fo. 316b. 1691 Journal 22, fo. 345b; Journal 23, fo. 79. 1692 Journal 22, fo. 314. M821 Elizabeth and Henry IV of France, 1589-1591. 1693 Journal 22, fo. 321b. 1694 -_Id._, fo. 326. 1695 -_Id._, fo. 321. M822 The City and the Earl of Essex, 1591. 1696 Journal 23, fos. 35, 38. 1697 July 24, 1591.--Remembrancia. i, 599 (Analytical Index, p. 408). M823 The City agrees to fit out six ships and a pinnace, 16 June, 1591. 1698 Journal 23, fos. 31, 43b, 48b; Repertory 22, fo. 284b. 1699 Journal 23, fos. 68, 68b; _Cf._ Cal. State Papers Dom. (1591-1594),
      p. 48, where the date of the letter is given as "May." 1700 Journal 23, fos. 325b, 383b. M824 Search to be made for Spanish emissaries in disguise. 1701 Journal 23, fos. 45-46b. 1702 Journal 24, fo. 86. M825 Privateering expeditions against Spain, 1591-1592. 1703 Proclamation, dated 16 Sept., 1591.--Journal 23, fo. 47. 1704 Journal 23, fo. 73. 1705 -_Id._, fo. 71. 1706 Proclamations, dated 8 Jan. and 26 Sept., 1592.--Journal 23, fos.
      78b, 136. 1707 The queen to the lord mayor, 6 Jan., 1592.--Cal. State Papers Dom.
      (1591-1594), p. 168. The same to the same, 25 Jan.--Journal 23, fo.
      87. 1708 Journal 23, fos. 157, 167, 174, 224b; Repertory 23, fo. 29. M826 Proposal to build a pest-house for the city, 1592. 1709 It was in 1592 that bills of mortality, kept by the parish clerks,
      were for the first time published. 1710 Journal 23, fo. 204b. 1711 Journal 23, fo. 266. 1712 -_Id._, fos. 400, 402. M827 The hysterical Anne Burnell. 1713 -_Id._, fo. 153. M828 Six ships, two pinnaces and 350 men provided by the City against
      Spain, July, 1594. 1714 Journal 23, fo. 290b. The number was afterwards reduced to 350
      men.--_Id._, fo. 296b; Remembrancia, ii, 3, 27, 30. 1715 Journal 23, fo. 290. 1716 -_Id._, fo. 289. 1717 Journal 23, fo. 293. The names, tonnage and crews of the ships are
      thus given (Remembrancia, ii, 26):--The Assention, 400 tons, 100
      mariners; The Consent, 350 tons, 100 mariners; The Susan
      Bonadventure, 300 tons, 70 mariners; The Cherubim, 300 tons, 70
      mariners; The Minion, 180 tons, 50 mariners; and The Primrose, 180
      tons, 50 mariners. Only one pinnace is mentioned, of 50 tons, with
      20 mariners. M829 Sir John Spencer and his daughter. 1718 Journal 23, fo. 323b. 1719 Chamberlain's Letters, _temp._, Eliz. (Camd. Soc., No. 79), p. 50.
      The writer was a son of Richard Chamberlain, a city alderman. 1720 Alderman of Tower Ward; Sheriff 1584-5; Mayor 1597. 1721 Repertory 24, fo. 410b. 1722 Repertory 25, fo. 216b. 1723 The letter is printed _in extenso_ in Chambers' "Book of Days," i,
      464, and in Goodman's "Court of James I," ii, 127. M830 The capture of Cadiz, July, 1596. 1724 Journal 24, fos. 79b, 81, 82, 82b. 1725 -_Id._, fo. 85b. 1726 Journal 24, fos. 105, 144. 1727 -_Id._, fo. 84b. 1728 Macaulay's "Essay on Lord Bacon." 1729 Journal 24, fo. 145. 1730 -_Id._, fos. 146b, 149. M831 Calais falls into the hands of Spain, April, 1596. 1731 Journal 24, fos. 110-111, 129b.; Repertory 23, fo. 594b. 1732 Journal 24, fos. 124, 154b, 157b. M832 Reinforcements for the Netherlands, July, 1596. 1733 The queen to the mayor, 25 July; the lords of the council to the
      same, 26 July.--Journal 24, fo. 142. M833 A demand for ten ships to be furnished by the City, Dec., 1596. 1734 Journal 24, fos. 173, 175. M834 The City's reply. 1735 The same dissatisfaction at the result of the Cadiz expedition so
      far as it affected the citizens of London was displayed in a
      previous letter from the mayor to the lords of the Privy Council (3
      Nov.) in answer to a demand for 3,000 men and three ships to ride at
      Tilbury Hope and give notice of the approach of the Spanish
      fleet.--Remembrancia (Analytical Index), pp. 243, 244. 1736 Repertory 24, fo. 60b. M835 Affairs in Ireland, 1594-1599. 1737 Journal 24, fos. 210b-213b, 216, 217. 1738 Journal 24, fos. 324b, 325, 329b; Repertory 24, fos. 268, 287, 306;
      _Id._ 25, fo. 4b. Elizabeth asked for £40,000, but only succeeded in
      getting half that sum.--Chamberlain's Letters, p. 15. 1739 Journal 25, fos. 34, 47b, 48; Repertory 24, fo. 352b. In July, 1600,
      a deputation was appointed to wait upon the lords of the council
      touching the repayment of this loan.--Repertory 25, fo. 119b.  It
      still remained unpaid in Feb., 1604.--Journal 26, fo. 163b. By the
      end of 1606 £20,000 had been paid off.--Remembrancia (Analytical
      Index), p. 188; Repertory 27, fo. 278. And by July, 1607, the whole
      was repaid.--Howes's Chron., p. 890. M836 A scare in London, July-Aug., 1598. 1740 Journal 25, fos. 74b, 75, 77b-78b, 81, 81b, 82b-84, etc. 1741 Chamberlain's Letters, p. 59. 1742 Journal 25, fo. 79b. 1743 -_Id._, fos. 80, 80b. 1744 Chamberlain's Letters, p. 59. 1745 Chamberlain's Letters, p. 61; Journal 25, fos. 81, 84b. M837 The abortive insurrection of the Earl of Essex, Feb., 1601. 1746 Journal 25, fo. 238. 1747 Journal 25. fo. 245; Letter Book BB, fo. 85. He was deprived of his
      aldermanry of the Ward of Farringdon Without and debarred from ever
      becoming alderman of any other ward "for causes sufficiently made
      known" to the Court of Aldermen. 1748 Repertory 25, fos. 209b, 213. 1749 Cal. State Papers Dom. (1598-1601), p. 546. 1750 Secretary Cecil to the Lord Lieutenant of Ireland and others, 10
      Feb., 1601.--Cal. State Papers Dom. (1598-1601), p. 547. 1751 Proclamation, dated 9 Feb., 1601.--Journal 25, fo. 240b. 1752 Repertory 25, fos. 213, 246. 1753 Journal 25, fos. 242, 243, 243b. 1754 Cal. State Papers Dom. (1601-1603), pp. 16, 26, 89, 90. M838 Mountjoy's conquest of Ireland, 1600-1603. 1755 Journal 25, fos. 137, 161b, 166, 179, 189, 190, 218b, 223, 237,
      237b, 262b-265b, 293, 295, 301, 302b, 313b, 315; Journal 26, fos.
      16b-19. M839 The parliament of 1601. 1756 Repertory 25, fo. 296b. M840 The last days of Elizabeth, 1601-1603. 1757 Repertory 24, fos. 343, 354; Repertory 25, fos. 165-175. The
      Steelyard was re-opened in 1606.--Journal 27, fo. 66. 1758 Letter from Sir Christopher Hatton to the mayor, 27 Nov.,
      1583.--Remembrancia (Analytical Index), p. 407. 1759 Journal 26, fo. 42.
```

### AI Extraction
- **Primary Mechanism**: `STATUS_REVERSAL` (Detector Confidence: `0.98`)
- **Secondary Dynamics**: SOCIAL_EMBARRASSMENT, CALLBACK
- **Linguistic Craft Score**: `0.90`
- **Tone**: `DRY_WIT`
- **Setup**: Characters Append, April establish scene context: 'Book I, fo....'
- **Escalation**: Complication rises around status_reversal: '1002 -_Id._, fo....'
- **Reversal**: Expectation or status is inverted: 'M649 Boulogne threatened....'
- **Payoff**: Comedic resolution or deadpan beat lands: '42....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 10 — `the_little_nugget_ch1_02885`

**Source**: *The Little Nugget* (Chapter 1)  
**Characters Identified**: Dr Sir, Flannery, Miss Kane, Morehouse, Morgan, Mr Morehouse, Mr Morgan, Mrs Morehouse, Professor Gordon, Professor Was, Westcote  
**Dialogue Ratio**: `0.53` | **Surface Slang Isolated**: None  

### Passage
```text
PIGS IS PIGS *** Produced by An Anonymous Volunteer "PIGS IS PIGS" By Ellis Parker Butler Mike Flannery, the Westcote agent of the Interurban Express Company, leaned over the counter of the express office and shook his fist. Mr. Morehouse, angry and red, stood on the other side of the counter, trembling with rage. The argument had been long and heated, and at last Mr. Morehouse had talked himself speechless. The cause of the trouble stood on the counter between the two men. It was a soap box across the top of which were nailed a number of strips, forming a rough but serviceable cage. In it two spotted guinea-pigs were greedily eating lettuce leaves. "Do as you loike, then!" shouted Flannery, "pay for thim an' take thim, or don't pay for thim and leave thim be. Rules is rules, Misther Morehouse, an' Mike Flannery's not goin' to be called down fer breakin' of thim." "But, you everlastingly stupid idiot!" shouted Mr. Morehouse, madly shaking a flimsy printed book beneath the agent's nose, "can't you read it here-in your own plain printed rates? 'Pets, domestic, Franklin to Westcote, if properly boxed, twenty-five cents each.'" He threw the book on the counter in disgust. "What more do you want? Aren't they pets? Aren't they domestic? Aren't they properly boxed? What?" He turned and walked back and forth rapidly; frowning ferociously. Suddenly he turned to Flannery, and forcing his voice to an artificial calmness spoke slowly but with intense sarcasm. "Pets," he said "P-e-t-s! Twenty-five cents each. There are two of them. One! Two! Two times twenty-five are fifty! Can you understand that? I offer you fifty cents." Flannery reached for the book. He ran his hand through the pages and stopped at page sixty four. "An' I don't take fifty cints," he whispered in mockery. "Here's the rule for ut. 'Whin the agint be in anny doubt regardin' which of two rates applies to a shipment, he shall charge the larger. The con-sign-ey may file a claim for the overcharge.' In this case, Misther Morehouse, I be in doubt. Pets thim animals may be, an' domestic they be, but pigs I'm blame sure they do be, an' me rules says plain as the nose on yer face, 'Pigs Franklin to Westcote, thirty cints each.' An' Mister Morehouse, by me arithmetical knowledge two times thurty comes to sixty cints." Mr. Morehouse shook his head savagely. "Nonsense!" he shouted, "confounded nonsense, I tell you! Why, you poor ignorant foreigner, that rule means common pigs, domestic pigs, not guinea pigs!" Flannery was stubborn. "Pigs is pigs," he declared firmly. "Guinea-pigs, or dago pigs or Irish pigs is all the same to the Interurban Express Company an' to Mike Flannery. Th' nationality of the pig creates no differentiality in the rate, Misther Morehouse! 'Twould be the same was they Dutch pigs or Rooshun pigs. Mike Flannery," he added, "is here to tind to the expriss business and not to hould conversation wid dago pigs in sivinteen languages fer to discover be they Chinese or Tipperary by birth an' nativity." Mr. Morehouse hesitated. He bit his lip and then flung out his arms wildly. "Very well!" he shouted, "you shall hear of this! Your president shall hear of this! It is an outrage! I have offered you fifty cents. You refuse it! Keep the pigs until you are ready to take the fifty cents, but, by [COMPANION_B], sir, if one hair of those pigs' heads is harmed I will have the law on you!" He turned and stalked out, slamming the door. Flannery carefully lifted the soap box from the counter and placed it in a corner. He was not worried. He felt the peace that comes to a faithful servant who has done his duty and done it well. Mr. Morehouse went home raging. His boy, who had been awaiting the guinea-pigs, knew better than to ask him for them. He was a normal boy and therefore always had a guilty conscience when his father was angry. So the boy slipped quietly around the house. There is nothing so soothing to a guilty conscience as to be out of the path of the avenger. Mr. Morehouse stormed into the house. "Where's the ink?" he shouted at his wife as soon as his foot was across the doorsill. Mrs. Morehouse jumped, guiltily. She never used ink. She had not seen the ink, nor moved the ink, nor thought of the ink, but her husband's tone convicted her of the guilt of having borne and reared a boy, and she knew that whenever her husband wanted anything in a loud voice the boy had been at it. "I'll find Sammy," she said meekly. When the ink was found Mr. Morehouse wrote rapidly, and he read the completed letter and smiled a triumphant smile. "That will settle that crazy Irishman!" he exclaimed. "When they get that letter he will hunt another job, all right!" A week later Mr. Morehouse received a long official envelope with the card of the Interurban Express Company in the upper left corner. He tore it open eagerly and drew out a sheet of paper. At the top it bore the number A6754. The letter was short. "Subject--Rate on guinea-pigs," it said, "Dr. Sir--We are in receipt of your letter regarding rate on guinea-pigs between Franklin and Westcote addressed to the president of this company. All claims for overcharge should be addressed to the Claims Department." Mr. Morehouse wrote to the Claims Department. He wrote six pages of choice sarcasm, vituperation and argument, and sent them to the Claims Department. A few weeks later he received a reply from the Claims Department. Attached to it was his last letter. "Dr. Sir," said the reply. "Your letter of the 16th inst., addressed to this Department, subject rate on guinea-pigs from Franklin to Westcote, ree'd. We have taken up the matter with our agent at Westcote, and his reply is attached herewith. He informs us that you refused to receive the consignment or to pay the charges. You have therefore no claim against this company, and your letter regarding the proper rate on the consignment should be addressed to our Tariff Department." Mr. Morehouse wrote to the Tariff Department. He stated his case clearly, and gave his arguments in full, quoting a page or two from the encyclopedia to prove that guinea-pigs were not common pigs. With the care that characterizes corporations when they are systematically conducted, Mr. Morehouse's letter was numbered, O.K'd, and started through the regular channels. Duplicate copies of the bill of lading, manifest, Flannery's receipt for the package and several other pertinent papers were pinned to the letter, and they were passed to the head of the Tariff Department. The head of the Tariff Department put his feet on his desk and yawned. He looked through the papers carelessly. "Miss Kane," he said to his stenographer, "take this letter. 'Agent, Westcote, N. J. Please advise why consignment referred to in attached papers was refused domestic pet rates."' Miss Kane made a series of curves and angles on her note book and waited with pencil poised. The head of the department looked at the papers again. "Huh! guinea-pigs!" he said. "Probably starved to death by this time! Add this to that letter: 'Give condition of consignment at present.'" He tossed the papers on to the stenographer's desk, took his feet from his own desk and went out to lunch. When Mike Flannery received the letter he scratched his head. "Give prisint condition," he repeated thoughtfully. "Now what do thim clerks be wantin' to know, I wonder! 'Prisint condition, 'is ut? Thim pigs, praise St. Patrick, do be in good health, so far as I know, but I niver was no veternairy surgeon to dago pigs. Mebby thim clerks wants me to call in the pig docther an' have their pulses took. Wan thing I do know, howiver, which is they've glorious appytites for pigs of their soize. Ate? They'd ate the brass padlocks off of a barn door I If the paddy pig, by the same token, ate as hearty as these dago pigs do, there'd be a famine in Ireland." To assure himself that his report would be up to date, Flannery went to the rear of the office and looked into the cage. The pigs had been transferred to a larger box--a dry goods box. "Wan, -- two, -- t'ree, -- four, -- five, -- six, -- sivin, -- eight!" he counted. "Sivin spotted an' wan all black. All well an' hearty an' all eatin' loike ragin' hippypottymusses. He went back to his desk and wrote. "Mr. Morgan, Head of Tariff Department," he wrote. "Why do I say dago pigs is pigs because they is pigs and will be til you say they ain't which is what the rule book says stop your jollying me you know it as well as I do. As to health they are all well and hoping you are the same. P. S. There are eight now the family increased all good eaters. P. S. I paid out so far two dollars for cabbage which they like shall I put in bill for same what?" Morgan, head of the Tariff Department, when he received this letter, laughed. He read it again and became serious. "By [COMPANION_B]!" he said, "Flannery is right, 'pigs is pigs.' I'll have to get authority on this thing. Meanwhile, Miss Kane, take this letter: Agent, Westcote, N. J. Regarding shipment guinea-pigs, File No. A6754. Rule 83, General Instruction to Agents, clearly states that agents shall collect from consignee all costs of provender, etc., etc., required for live stock while in transit or storage. You will proceed to collect same from consignee." Flannery received this letter next morning, and when he read it he grinned. "Proceed to collect," he said softly. "How thim clerks do loike to be talkin'! Me proceed to collect two dollars and twinty-foive cints off Misther Morehouse! I wonder do thim clerks know Misther Morehouse? I'll git it! Oh, yes! 'Misther Morehouse, two an' a quarter, plaze.' 'Cert'nly, me dear frind Flannery. Delighted!' Not!" Flannery drove the express wagon to Mr. Morehouse's door. Mr. Morehouse answered the bell. "Ah, ha!" he cried as soon as he saw it was Flannery. "So you've come to your senses at last, have you? I thought you would! Bring the box in." "I hev no box," said Flannery coldly. "I hev a bill agin Misther John C. Morehouse for two dollars and twinty-foive cints for kebbages aten by his dago pigs. Wud you wish to pay ut?" "Pay--Cabbages--!" gasped Mr. Morehouse. "Do you mean to say that two little guinea-pigs--" "Eight!" said Flannery. "Papa an' mamma an' the six childer. Eight!" For answer Mr. Morehouse slammed the door in Flannery's face. Flannery looked at the door reproachfully. "I take ut the con-sign-y don't want to pay for thim kebbages," he said. "If I know signs of refusal, the con-sign-y refuses to pay for wan dang kebbage leaf an' be hanged to me!" Mr. Morgan, the head of the Tariff Department, consulted the president of the Interurban Express Company regarding guinea-pigs, as to whether they were pigs or not pigs. The president was inclined to treat the matter lightly. "What is the rate on pigs and on pets?" he asked. "Pigs thirty cents, pets twenty-five," said Morgan. "Then of course guinea-pigs are pigs," said the president. "Yes," agreed Morgan, "I look at it that way, too. A thing that can come under two rates is naturally due to be classed as the higher. But are guinea-pigs, pigs? Aren't they rabbits?" "Come to think of it," said the president, "I believe they are more like rabbits. Sort of half-way station between pig and rabbit. I think the question is this--are guinea-pigs of the domestic pig family? I'll ask professor Gordon. He is authority on such things. Leave the papers with me." The president put the papers on his desk and wrote a letter to Professor Gordon. Unfortunately the Professor was in South America collecting zoological specimens, and the letter was forwarded to him by his wife. As the Professor was in the highest Andes, where no white man had ever penetrated, the letter was many months in reaching him. The president forgot the guinea-pigs, Morgan forgot them, Mr. Morehouse forgot them, but Flannery did not. One-half of his time he gave to the duties of his agency; the other half was devoted to the guinea-pigs. Long before Professor Gordon received the president's letter Morgan received one from Flannery. "About them dago pigs," it said, "what shall I do they are great in family life, no race suicide for them, there are thirty-two now shall I sell them do you take this express office for a menagerie, answer quick." Morgan reached for a telegraph blank and wrote: "Agent, Westcote. Don't sell pigs." He then wrote Flannery a letter calling his attention to the fact that the pigs were not the property of the company but were merely being held during a settlement of a dispute regarding rates. He advised Flannery to take the best possible care of them. Flannery, letter in hand, looked at the pigs and sighed. The dry-goods box cage had become too small. He boarded up twenty feet of the rear of the express office to make a large and airy home for them, and went about his business. He worked with feverish intensity when out on his rounds, for the pigs required attention and took most of his time. Some months later, in desperation, he seized a sheet of paper and wrote "160" across it and mailed it to Morgan. Morgan returned it asking for explanation. Flannery replied: "There be now one hundred sixty of them dago pigs, for heavens sake let me sell off some, do you want me to go crazy, what." "Sell no pigs," Morgan wired. Not long after this the president of the express company received a letter from Professor Gordon. It was a long and scholarly letter, but the point was that the guinea-pig was the Cava aparoea while the common pig was the genius Sus of the family Suidae. He remarked that they were prolific and multiplied rapidly. "They are not pigs," said the president, decidedly, to Morgan. "The twenty-five cent rate applies." Morgan made the proper notation on the papers that had accumulated in File A6754, and turned them over to the Audit Department. The Audit Department took some time to look the matter up, and after the usual delay wrote Flannery that as he had on hand one hundred and sixty guinea-pigs, the property of consignee, he should deliver them and collect charges at the rate of twenty-five cents each. Flannery spent a day herding his charges through a narrow opening in their cage so that he might count them. "Audit Dept." he wrote, when he had finished the count, "you are way off there may be was one hundred and sixty dago pigs once, but wake up don't be a back number. I've got even eight hundred, now shall I collect for eight hundred or what, how about sixty-four dollars I paid out for cabbages." It required a great many letters back and forth before the Audit Department was able to understand why the error had been made of billing one hundred and sixty instead of eight hundred, and still more time for it to get the meaning of the "cabbages." Flannery was crowded into a few feet at the extreme front of the office. The pigs had all the rest of the room and two boys were employed constantly attending to them. The day after Flannery had counted the guinea-pigs there were eight more added to his drove, and by the time the Audit Department gave him authority to collect for eight hundred Flannery had given up all attempts to attend to the receipt or the delivery of goods. He was hastily building galleries around the express office, tier above tier. He had four thousand and sixty-four guinea-pigs to care for! More were arriving daily. Immediately following its authorization the Audit Department sent another letter, but Flannery was too busy to open it. They wrote another and then they telegraphed: "Error in guinea-pig bill. Collect for two guinea-pigs, fifty cents. Deliver all to consignee." Flannery read the telegram and cheered up. He wrote out a bill as rapidly as his pencil could travel over paper and ran all the way to the Morehouse home. At the gate he stopped suddenly. The house stared at him with vacant eyes. The windows were bare of curtains and he could see into the empty rooms. A sign on the porch said, "To Let." Mr. Morehouse had moved! Flannery ran all the way back to the express office. Sixty-nine guinea-pigs had been born during his absence. He ran out again and made feverish inquiries in the village. Mr. Morehouse had not only moved, but he had left Westcote. Flannery returned to the express office and found that two hundred and six guinea-pigs had entered the world since he left it. He wrote a telegram to the Audit Department. "Can't collect fifty cents for two dago pigs consignee has left town address unknown what shall I do? Flannery." The telegram was handed to one of the clerks in the Audit Department, and as he read it he laughed. "Flannery must be crazy. He ought to know that the thing to do is to return the consignment here," said the clerk. He telegraphed Flannery to send the pigs to the main office of the company at Franklin. When Flannery received the telegram he set to work. The six boys he had engaged to help him also set to work. They worked with the haste of desperate men, making cages out of soap boxes, cracker boxes, and all kinds of boxes, and as fast as the cages were completed
```

### AI Extraction
- **Primary Mechanism**: `STATUS_REVERSAL` (Detector Confidence: `0.98`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.90`
- **Tone**: `DRY_WIT`
- **Setup**: Characters Dr Sir, Flannery establish scene context: 'PIGS IS PIGS *** Produced by An Anonymous Volunteer "PIGS IS PIGS" By Ellis Park...'
- **Escalation**: Complication rises around status_reversal: 'Mr....'
- **Reversal**: Expectation or status is inverted: 'All well an' hearty an' all eatin' loike ragin' hippypottymusses....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'They worked with the haste of desperate men, making cages out of soap boxes, cra...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 11 — `the_man_upstairs_ch33_07601`

**Source**: *The Man Upstairs* (Chapter 33)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.42` | **Surface Slang Isolated**: None  

### Passage
```text
"Carwin's eyes glared and his limbs were petrified at this intelligence. No words were requisite to prove him guiltless of these enormities: at the time, however, I was nearly insensible to these exculpatory tokens. He walked to the farther end of the room, and, having recovered some degree of composure, he spoke: -," " "What!" I replied; "was not thine the voice that commanded my brother to imbrue his hands in the blood of his children? - to strangle that angel of sweetness, his wife? Has he not vowed my death, and the death of Pleyel, at thy bidding? Hast thou not made him the butcher of his family? - changed him who was the glory of his species into worse than brute? - robbed him of reason and consigned the rest of his days to fetters and stripes? I am not this villain.
```

### AI Extraction
- **Primary Mechanism**: `ESCALATION` (Detector Confidence: `0.42`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: '"Carwin's eyes glared and his limbs were petrified at this intelligence....'
- **Escalation**: Complication rises around escalation: 'He walked to the farther end of the room, and, having recovered some degree of c...'
- **Reversal**: Expectation or status is inverted: 'Has he not vowed my death, and the death of Pleyel, at thy bidding?...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'I am not this villain....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 12 — `right_ho_ch6_05876`

**Source**: *Right Ho* (Chapter 6)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.71` | **Surface Slang Isolated**: rummy, stout fellow  

### Passage
```text
"I began to see that, unless I made the thing a bit more plausible, the scheme might turn out a frost. I could guess what the old boy was thinking. He was trying to square all this prosperity with what he knew of poor old Bicky. And one had to admit that it took a lot of squaring, for dear old Bicky, though a stout fellow and absolutely unrivalled as an imitator of bull-terriers and cats, was in many ways one of the most pronounced fatheads that ever pulled on a suit of gent's underwear," " "What! Forty pounds a month! I suppose it seems rummy to you," I said, "but the fact is New York often bucks chappies up and makes them show a flash of speed that you wouldn't have imagined them capable of.
```

### AI Extraction
- **Primary Mechanism**: `ESCALATION` (Detector Confidence: `0.20`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: '"I began to see that, unless I made the thing a bit more plausible, the scheme m...'
- **Escalation**: Complication rises around escalation: 'I could guess what the old boy was thinking....'
- **Reversal**: Expectation or status is inverted: 'And one had to admit that it took a lot of squaring, for dear old Bicky, though ...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'I suppose it seems rummy to you," I said, "but the fact is New York often bucks ...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 13 — `my_man_jeeves_ch6_08030`

**Source**: *My Man Jeeves* (Chapter 6)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.71` | **Surface Slang Isolated**: rummy, stout fellow  

### Passage
```text
"I began to see that, unless I made the thing a bit more plausible, the scheme might turn out a frost. I could guess what the old boy was thinking. He was trying to square all this prosperity with what he knew of poor old Bicky. And one had to admit that it took a lot of squaring, for dear old Bicky, though a stout fellow and absolutely unrivalled as an imitator of bull-terriers and cats, was in many ways one of the most pronounced fatheads that ever pulled on a suit of gent's underwear," " "What! Forty pounds a month! I suppose it seems rummy to you," I said, "but the fact is New York often bucks chappies up and makes them show a flash of speed that you wouldn't have imagined them capable of.
```

### AI Extraction
- **Primary Mechanism**: `ESCALATION` (Detector Confidence: `0.20`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: '"I began to see that, unless I made the thing a bit more plausible, the scheme m...'
- **Escalation**: Complication rises around escalation: 'I could guess what the old boy was thinking....'
- **Reversal**: Expectation or status is inverted: 'And one had to admit that it took a lot of squaring, for dear old Bicky, though ...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'I suppose it seems rummy to you," I said, "but the fact is New York often bucks ...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 14 — `a_damsel_in_distress_ch29_04150`

**Source**: *A Damsel In Distress* (Chapter 29)  
**Characters Identified**: Ann, Jimmy, Mr Crocker, Mr Pett, Mrs Crocker, Uncle To  
**Dialogue Ratio**: `0.66` | **Surface Slang Isolated**: None  

### Passage
```text
CHAPTER XXVI EVERYBODY HAPPY Jimmy looked at Ann. They were alone. Mr. Pett had gone back to
bed, Mrs. Crocker to her hotel. Mr. Crocker was removing his
make-up in his room. A silence had followed their departure. "This is the end of a perfect day!" said Jimmy. Ann took a step towards the door. "Don't go!" Ann stopped. "Mr. Crocker!" she said. "Jimmy," he corrected. "Mr. Crocker!" repeated Ann firmly. "Or Algernon, if you prefer it." "May I ask--" Ann regarded him steadily. "May I ask." "Nearly always," said Jimmy, "when people begin with that, they
are going to say something unpleasant." "May I ask why you went to all this trouble to make a fool of me?
Why could you not have told me who you were from the start?" "Have you forgotten all the harsh things you said to me from time
to time about Jimmy Crocker? I thought that, if you knew who I
was, you would have nothing more to do with me." "You were quite right." "Surely, though, you won't let a thing that happened five years
ago make so much difference?" "I shall never forgive you!" "And yet, a little while ago, when Willie's bomb was about to go
off, you flung yourself into my arms!" Ann's face flamed. "I lost my balance." "Why try to recover it?" Ann bit her lip. "You did a cruel, heartless thing. What does it matter how long
ago it was? If you were capable of it then--" "Be reasonable. Don't you admit the possibility of reformation?
Take your own case. Five years ago you were a minor poetess. Now
you are an amateur kidnapper--a bright, lovable girl at whose
approach people lock up their children and sit on the key. As for
me, five years ago I was a heartless brute. Now I am a sober
serious business-man, specially called in by your uncle to help
jack up his tottering firm. Why not bury the dead past?
Besides--I don't want to praise myself, I just want to call your
attention to it--think what I have done for you. You admitted
yourself that it was my influence that had revolutionised your
character. But for me, you would now be doing worse than write
poetry. You would be writing _vers libre_. I saved you from that.
And you spurn me!" "I hate you!" said Ann. Jimmy went to the writing-desk and took up a small book. "Put that down!" "I just wanted to read you 'Love's Funeral!' It illustrates my
point. Think of yourself as you are now, and remember that it is
I who am responsible for the improvement. Here we are. 'Love's
Funeral.' 'My heart is dead. . . .' " Ann snatched the book from his hands and flung it away. It soared
up, clearing the gallery rails, and fell with a thud on the
gallery floor. She stood facing him with sparkling eyes. Then she
moved away. "I beg your pardon," she said stiffly. "I lost my temper." "It's your hair," said Jimmy soothingly. "You're bound to be
quick-tempered with hair of that glorious red shade. You must
marry some nice, determined fellow, blue-eyed, dark-haired,
clean-shaven, about five foot eleven, with a future in business.
He will keep you in order." "Mr. Crocker!" "Gently, of course. Kindly-lovingly. The velvet thingummy rather
than the iron what's-its-name. But nevertheless firmly." Ann was at the door. "To a girl with your ardent nature some one with whom you can
quarrel is an absolute necessity of life. You and I are
affinities. Ours will be an ideally happy marriage. You would be
miserable if you had to go through life with a human doormat with
'Welcome' written on him. You want some one made of sterner
stuff. You want, as it were, a sparring-partner, some one with
whom you can quarrel happily with the certain knowledge that he
will not curl up in a ball for you to kick, but will be there
with the return wallop. I may have my faults--" He paused
expectantly. Ann remained silent. "No, no!" he went on. "But I am
such a man. Brisk give-and-take is the foundation of the happy
marriage. Do you remember that beautiful line of Tennyson's--'We
fell out, my wife and I'? It always conjures up for me a vision
of wonderful domestic happiness. I seem to see us in our old age,
you on one side of the radiator, I on the other, warming our old
limbs and thinking up snappy stuff to hand to each
other--sweethearts still! If I were to go out of your life now,
you would be miserable. You would have nobody to quarrel with.
You would be in the position of the female jaguar of the Indian
jungle, who, as you doubtless know, expresses her affection for
her mate by biting him shrewdly in the fleshy part of the leg, if
she should snap sideways one day and find nothing there." Of all the things which Ann had been trying to say during this
discourse, only one succeeded in finding expression. To her
mortification, it was the only weak one in the collection. "Are you asking me to marry you?" "I am." "I won't!" "You think so now, because I am not appearing at my best. You see
me nervous, diffident, tongue-tied. All this will wear off,
however, and you will be surprised and delighted as you begin to
understand my true self. Beneath the surface--I speak
conservatively--I am a corker!" The door banged behind Ann. Jimmy found himself alone. He walked
thoughtfully to Mr. Pett's armchair and sat down. There was a
feeling of desolation upon him. He lit a cigarette and began to
smoke pensively. What a fool he had been to talk like that! What
girl of spirit could possibly stand it? If ever there had been a
time for being soothing and serious and pleading, it had been
these last few minutes. And he talked like that! Ten minutes passed. Jimmy sprang from his chair. He thought he
had heard a footstep. He flung the door open. The passage was
empty. He returned miserably to his chair. Of course she had not
come back. Why should she? A voice spoke. "Jimmy!" He leaped up again, and looked wildly round. Then he looked up.
Ann was leaning over the gallery rail. "Jimmy, I've been thinking it over. There's something I want to
ask you. Do you admit that you behaved abominably five years
ago?" "Yes!" shouted Jimmy. "And that you've been behaving just as badly ever since?" "Yes!" "And that you are really a pretty awful sort of person?" "Yes!" "Then it's all right. You deserve it!" "Deserve it?" "Deserve to marry a girl like me. I was worried about it, but now
I see that it's the only punishment bad enough for you!" She
raised her arm. "Here's the dead past, Jimmy! Go and bury it! Good-night!" A small book fell squashily at Jimmy's feet. He regarded it dully
for a moment. Then, with a wild yell which penetrated even to Mr.
Pett's bedroom and woke that sufferer just as he was dropping off
to sleep for the third time that night he bounded for the gallery
stairs. At the further end of the gallery a musical laugh sounded, and a
door closed. Ann had gone.
```

### AI Extraction
- **Primary Mechanism**: `ESCALATION` (Detector Confidence: `0.42`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.90`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Ann, Jimmy establish scene context: 'CHAPTER XXVI EVERYBODY HAPPY Jimmy looked at Ann....'
- **Escalation**: Complication rises around escalation: 'As for
me, five years ago I was a heartless brute....'
- **Reversal**: Expectation or status is inverted: '"To a girl with your ardent nature some one with whom you can
quarrel is an abso...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'Ann had gone....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 15 — `the_diary_of_a_nobody_ch3_03510`

**Source**: *The Diary Of A Nobody* (Chapter 3)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.53` | **Surface Slang Isolated**: None  

### Passage
```text
"day," " When he says that such and such things happened, I believe him to mean that they actually occurred and not that he imagined or dreamed them; when he says I believe he uses the word in the popular sense; when he says "made" or "created," I believe he means that they came into being by a process analogous to that which the people whom he addressed called "making" or "creating"; and I think that, unless we forget our present knowledge of nature, and, putting ourselves back into the position of a Phoenician or a Chaldaean philosopher, start from his conception of the world, we shall fail to grasp the meaning of the Hebrew writer.
```

### AI Extraction
- **Primary Mechanism**: `ESCALATION` (Detector Confidence: `0.20`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.85`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: "day," " When he says that such and such things happened, I believe him to mean that they actually occurred and not that he imagined or dreamed them; when he says I believe he uses the word in the popular sense; when he says "made" or "created," I believe he means that they came into being by a process analogous to that which the people whom he addressed called "making" or "creating"; and I think that, unless we forget our present knowledge of nature, and, putting ourselves back into the position of a Phoenician or a Chaldaean philosopher, start from his conception of the world, we shall fail to grasp the meaning of the Hebrew writer.
- **Escalation**: Comedic complication introduced.
- **Reversal**: Expectation upended.
- **Payoff**: "day," " When he says that such and such things happened, I believe him to mean that they actually occurred and not that he imagined or dreamed them; when he says I believe he uses the word in the popular sense; when he says "made" or "created," I believe he means that they came into being by a process analogous to that which the people whom he addressed called "making" or "creating"; and I think that, unless we forget our present knowledge of nature, and, putting ourselves back into the position of a Phoenician or a Chaldaean philosopher, start from his conception of the world, we shall fail to grasp the meaning of the Hebrew writer.

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 16 — `the_man_upstairs_ch18_03006`

**Source**: *The Man Upstairs* (Chapter 18)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.74` | **Surface Slang Isolated**: None  

### Passage
```text
"In this expedition to the 'Bishop's Hotel' I had been attended by Jupiter, who had, no doubt, observed, for some weeks past, the abstraction of my demeanor, and took especial care not to leave me alone. But, on the next day, getting up very early, I contrived to give him the slip, and went into the hills in search of the tree. After much toil I found it. When I came home at night my valet proposed to give me a flogging. With the rest of the adventure I believe you are as well acquainted as myself," "I suppose," said I, "you missed the spot, in the first attempt at digging, through Jupiter's stupidity in letting the bug fall through the right instead of through the left eye of the skull.
```

### AI Extraction
- **Primary Mechanism**: `DEADPAN_REACTION` (Detector Confidence: `0.30`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DEADPAN`
- **Setup**: Characters Narrator establish scene context: '"In this expedition to the 'Bishop's Hotel' I had been attended by Jupiter, who ...'
- **Escalation**: Complication rises around deadpan_reaction: 'But, on the next day, getting up very early, I contrived to give him the slip, a...'
- **Reversal**: Expectation or status is inverted: 'After much toil I found it....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'With the rest of the adventure I believe you are as well acquainted as myself," ...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 17 — `my_man_jeeves_ch6_04598`

**Source**: *My Man Jeeves* (Chapter 6)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.61` | **Surface Slang Isolated**: by jove  

### Passage
```text
"And he floated out, leaving us to discuss details. Until we started this business of floating old Chiswick as a money-making proposition I had never realized what a perfectly foul time those Stock Exchange chappies must have when the public isn't biting freely. Nowadays I read that bit they put in the financial reports about," The market opened quietly" with a sympathetic eye, for, by Jove, it certainly opened quietly for us! You'd hardly believe how difficult it was to interest the public and make them take a flutter on the old boy.
```

### AI Extraction
- **Primary Mechanism**: `DEADPAN_REACTION` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DEADPAN`
- **Setup**: Characters Narrator establish scene context: '"And he floated out, leaving us to discuss details....'
- **Escalation**: Complication rises around deadpan_reaction: 'Until we started this business of floating old Chiswick as a money-making propos...'
- **Reversal**: Expectation or status is inverted: 'Nowadays I read that bit they put in the financial reports about," The market op...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'You'd hardly believe how difficult it was to interest the public and make them t...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 18 — `right_ho_ch6_09777`

**Source**: *Right Ho* (Chapter 6)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.61` | **Surface Slang Isolated**: by jove  

### Passage
```text
"And he floated out, leaving us to discuss details. Until we started this business of floating old Chiswick as a money-making proposition I had never realized what a perfectly foul time those Stock Exchange chappies must have when the public isn't biting freely. Nowadays I read that bit they put in the financial reports about," The market opened quietly" with a sympathetic eye, for, by Jove, it certainly opened quietly for us! You'd hardly believe how difficult it was to interest the public and make them take a flutter on the old boy.
```

### AI Extraction
- **Primary Mechanism**: `DEADPAN_REACTION` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DEADPAN`
- **Setup**: Characters Narrator establish scene context: '"And he floated out, leaving us to discuss details....'
- **Escalation**: Complication rises around deadpan_reaction: 'Until we started this business of floating old Chiswick as a money-making propos...'
- **Reversal**: Expectation or status is inverted: 'Nowadays I read that bit they put in the financial reports about," The market op...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'You'd hardly believe how difficult it was to interest the public and make them t...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 19 — `a_damsel_in_distress_ch27_05213`

**Source**: *A Damsel In Distress* (Chapter 27)  
**Characters Identified**: Ann, Lord Wisbeach, Miss Trimble, Mr Crocker, Mr Peter, Mr Pett, Mrs Crocker, Mrs Pett, Peter, Pett, Skinner, Trimble, Uncle Peter  
**Dialogue Ratio**: `0.50` | **Surface Slang Isolated**: None  

### Passage
```text
CHAPTER XXIV SENSATIONAL TURNING OF A WORM To this remarkable metamorphosis in Mr. Peter Pett several causes
had contributed. In the first place, the sudden dismissal of
Jerry Mitchell had obliged him to go two days without the
physical exercises to which his system had become accustomed, and
this had produced a heavy, irritable condition of body and mind.
He had brooded on the injustice of his lot until he had almost
worked himself up to rebellion. And then, as sometimes happened
with him when he was out of sorts, a touch of gout came to add to
his troubles. Being a patient man by nature, he might have borne
up against these trials, had he been granted an adequate night's
rest. But, just as he had dropped off after tossing restlessly
for two hours, things had begun to happen noisily in the library.
He awoke to a vague realisation of tumult below. Such was the morose condition of his mind as the result of his
misfortune that at first not even the cries for help could
interest him sufficiently to induce him to leave his bed. He knew
that walking in his present state would be painful, and he
declined to submit to any more pain just because some party
unknown was apparently being murdered in his library. It was not
until the shrill barking of the dog Aida penetrated right in
among his nerve-centres and began to tie them into knots that he
found himself compelled to descend. Even when he did so, it was
in no spirit of kindness. He did not come to rescue anybody or to
interfere between any murderer and his victim. He came in a fever
of militant wrath to suppress Aida. On the threshold of the
library, however, the genius, by treading on his gouty foot, had
diverted his anger and caused it to become more general. He had
not ceased to concentrate his venom on Aida. He wanted to assail
everybody. "What's the matter here?" he demanded, red-eyed. "Isn't somebody
going to tell me? Have I got to stop here all night? Who on earth
is this?" He glared at Miss Trimble. "What's she doing with that
pistol?" He stamped incautiously with his bad foot, and emitted a
dry howl of anguish. "She is a detective, Peter," said Mrs. Pett timidly. "A detective? Why? Where did she come from?" Miss Trimble took it upon herself to explain. "Mister Pett, siz Pett sent f'r me t' watch out so's nobody
kidnapped her son." "Oggie," explained Mrs. Pett. "Miss Trimble was guarding darling
Oggie." "Why?" "To--to prevent him being kidnapped, Peter." Mr. Pett glowered at the stout boy. Then his eye was attracted by
the forlorn figure of Jerry Mitchell. He started. "Was this fellow kidnapping the boy?" he asked. "Sure," said Miss Trimble. "Caught h'm with th' goods. He w's
waiting outside there with a car. I held h'm and this other guy
up w'th a gun and brought 'em back!" "Jerry," said Mr. Pett, "it wasn't your fault that you didn't
bring it off, and I'm going to treat you right. You'd have done
it if nobody had butted in to stop you. You'll get the money to
start that health-farm of yours all right. I'll see to that. Now
you run off to bed. There's nothing to keep you here." "Say!" cried Miss Trimble, outraged. "D'ya mean t' say y' aren't
going t' pros'cute? Why, aren't I tell'ng y' I caught h'm
kidnapping th' boy?" "I told him to kidnap the boy!" snarled Mr. Pett. "Peter!" Mr. Pett looked like an under-sized lion as he faced his wife. He
bristled. The recollection of all that he had suffered from Ogden
came to strengthen his determination. "I've tried for two years to get you to send that boy to a good
boarding-school, and you wouldn't do it. I couldn't stand having
him loafing around the house any longer, so I told Jerry Mitchell
to take him away to a friend of his who keeps a dogs' hospital on
Long Island and to tell his friend to hold him there till he got
some sense into him. Well, you've spoiled that for the moment
with your detectives, but it still looks good to me. I'll give
you a choice. You can either send that boy to a boarding-school
next week, or he goes to Jerry Mitchell's friend. I'm not going
to have him in the house any longer, loafing in my chair and
smoking my cigarettes. Which is it to be?" "But, Peter!" "Well?" "If I send him to a school, he may be kidnapped." "Kidnapping can't hurt him. It's what he needs. And, anyway, if
he is I'll pay the bill and be glad to do it. Take him off to bed
now. To-morrow you can start looking up schools. Great Godfrey!"
He hopped to the writing-desk and glared disgustedly at the
_debris_ on it. "Who's been making this mess on my desk? It's hard!
It's darned hard! The only room in the house that I ask to have
for my own, where I can get a little peace, and I find it turned
into a beer-garden, and coffee or some damned thing spilled all
over my writing-desk!" "That isn't coffee, Peter," said Mrs. Pett mildly. This cave-man
whom she had married under the impression that he was a gentle
domestic pet had taken all the spirit out of her. "It's Willie's
explosive." "Willie's explosive?" "Lord Wisbeach--I mean the man who pretended to be Lord
Wisbeach--dropped it there." "Dropped it there? Well, why didn't it explode and blow the place
to Hoboken, then?" Mrs. Pett looked helplessly at Willie, who thrust his fingers
into his mop of hair and rolled his eyes. "There was fortunately some slight miscalculation in my formula,
uncle Peter," he said. "I shall have to look into it to-morrow.
Whether the trinitrotoluol--" Mr. Pett uttered a sharp howl. He beat the air with his clenched
fists. He seemed to be having a brain-storm. "Has this--this _fish_ been living on me all this time--have I been
supporting this--this _buzzard_ in luxury all these years while he
fooled about with an explosive that won't explode! He pointed an
accusing finger at the inventor. Look into it tomorrow, will you?
Yes, you can look into it to-morrow after six o'clock! Until then
you'll be working--for the first time in your life--working in my
office, where you ought to have been all along." He surveyed the
crowded room belligerently. "Now perhaps you will all go back to
bed and let people get a little sleep. Go home!" he said to the
detective. Miss Trimble stood her ground. She watched Mrs. Pett pass away
with Ogden, and Willie Partridge head a stampede of geniuses, but
she declined to move. "Y' gotta cut th' rough stuff, 'ster Pett," she said calmly. "I
need my sleep, j'st 's much 's everyb'dy else, but I gotta stay
here. There's a lady c'ming right up in a taxi fr'm th' Astorbilt
to identify this gook. She's after'm f'r something." "What! Skinner?" "'s what he calls h'mself." "What's he done?" "I d'no. Th' lady'll tell us that." There was a violent ringing at the front door bell. "I guess that's her," said Miss Trimble. "Who's going to let 'r
in? I can't go." "I will," said Ann. Mr. Pett regarded Mr. Crocker with affectionate encouragement. "I don't know what you've done, Skinner," he said, "but I'll
stand by you. You're the best fan I ever met, and if I can keep
you out of the penitentiary, I will." "It isn't the penitentiary!" said Mr. Crocker unhappily. A tall, handsome, and determined-looking woman came into the
room. She stood in the doorway, looking about her. Then her eyes
rested on Mr. Crocker. For a moment she gazed incredulously at
his discoloured face. She drew a little nearer, peering. "D'yo 'dentify 'm, ma'am?" said Miss Trimble. "Bingley!" "Is 't th' guy y' wanted?" "It's my husband!" said Mrs. Crocker. "Y' can't arrest 'm f'r _that!_" said Miss Trimble disgustedly. She thrust her revolver back into the hinterland of her costume. "Guess I'll be beatin' it," she said with a sombre frown. She was
plainly in no sunny mood. "'f all th' hunk jobs I was ever on,
this is th' hunkest. I'm told off 't watch a gang of crooks, and
after I've lost a night's sleep doing it, it turns out 't's a
nice, jolly fam'ly party!" She jerked her thumb towards Jimmy.
"Say, this guy says he's that guy's son. I s'pose it's all
right?" "That is my step-son, James Crocker." Ann uttered a little cry, but it was lost in Miss Trimble's
stupendous snort. The detective turned to the window. "I guess I'll beat 't," she observed caustically, "before it
turns out that I'm y'r l'il daughter Genevieve."
```

### AI Extraction
- **Primary Mechanism**: `DEADPAN_REACTION` (Detector Confidence: `0.74`)
- **Secondary Dynamics**: PHYSICAL_COMPLICATION
- **Linguistic Craft Score**: `0.90`
- **Tone**: `DEADPAN`
- **Setup**: Characters Ann, Lord Wisbeach establish scene context: 'CHAPTER XXIV SENSATIONAL TURNING OF A WORM To this remarkable metamorphosis in M...'
- **Escalation**: Complication rises around deadpan_reaction: 'Pett glowered at the stout boy....'
- **Reversal**: Expectation or status is inverted: 'To-morrow you can start looking up schools....'
- **Payoff**: Comedic resolution or deadpan beat lands: '"I guess I'll beat 't," she observed caustically, "before it
turns out that I'm ...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 20 — `jill_the_reckless_ch4_07514`

**Source**: *Jill The Reckless* (Chapter 4)  
**Characters Identified**: And, Coadjutor, Croisette, Lord Of, Madame, Marie, Vidame  
**Dialogue Ratio**: `0.20` | **Surface Slang Isolated**: None  

### Passage
```text
CHAPTER IV. ENTRAPPED! There was a long silence.  We stood glaring at him, and he smiled upon
us--as a cat smiles.  Croisette told me afterwards that he could have
died of mortification--of shame and anger that we had been so
outwitted.  For myself I did not at once grasp the position.  I did not
understand.  I could not disentangle myself in a moment from the belief
in which I had entered the house--that it was Louis de Pavannes' house.
But I seemed vaguely to suspect that Bezers had swept him aside and
taken his place.  My first impulse therefore--obeyed on the
instant--was to stride to the Vidame's side and grasp his arm.  "What
have you done?"  I cried, my voice sounding hoarsely even in my own
ears.  "What have you done with M. de Pavannes?  Answer me!" He showed just a little more of his sharp white teeth as he looked down
at my face--a flushed and troubled face doubtless. "Nothing--yet," he
replied very mildly.  And he shook me off. "Then," I retorted, "how do you come here?" He glanced at Croisette and shrugged his shoulders, as if I had been a
spoiled child.  "M. Anne does not seem to understand," he said with
mock courtesy, "that I have the honour to welcome him to my house the
Hotel Bezers, Rue de Platriere." "The Hotel Bezers!  Rue de Platriere!"  I cried confusedly.  "But
Blaise Bure told us that this was the Rue St. Antoine!" "Ah!"  he replied as if slowly enlightened--the hypocrite!  "Ah! I
see!"  and he smiled grimly.  "So you have made the acquaintance of
Blaise Bure, my excellent master of the horse! Worthy Blaise! Indeed,
indeed, now I understand.  And you thought, you whelps," he continued,
and as he spoke his tone changed strangely, and he fixed us suddenly
with angry eyes, "to play a rubber with me!  With me, you imbeciles!
You thought the wolf of Bezers could be hunted down like any hare!
Then listen, and I will tell you the end of it.  You are now in my
house and absolutely at my mercy.  I have two score men within call who
would cut the throats of three babes at the breast, if I bade them!
Ay," he, added, a wicked exultation shining in his eyes, "they would,
and like the job!" He was going on to say more, but I interrupted him.  The rage I felt,
caused as much by the thought of our folly as by his arrogance, would
let me be silent no longer.  "First, M. de Bezers, first," I broke out
fiercely, my words leaping over one another in my haste, "a word with
you!  Let me tell you what I think of you!  You are a treacherous
hound, Vidame!  A cur!  a beast!  And I spit upon you!  Traitor and
assassin!"  I shouted, "is that not enough?  Will nothing provoke you?
If you call yourself a gentleman, draw!" He shook his head; he was still smiling, still unmoved.  "I do not do
my own dirty work," he said quietly, "nor stint my footmen of their
sport, boy." "Very well!"  I retorted.  And with the words I drew my sword, and
sprang as quick as lightning to the curtain by which he had entered.
"Very well, we will kill you first!"  I cried wrathfully, my eye on his
eye, and every savage passion in my breast aroused, "and take our
chance with the lackeys afterwards! Marie!  Croisette!"  I cried
shrilly, "on him, lads!" But they did not answer!  They did not move or draw.  For the moment
indeed the man was in my power.  My wrist was raised, and I had my
point at his breast, I could have run him through by a single thrust.
And I hated him.  Oh, how I hated him!  But he did not stir.  Had he
spoken, had he moved so much as an eyelid, or drawn back his foot, or
laid his hand on his hilt, I should have killed him there.  But he did
not stir and I could not do it.  My hand dropped.  "Cowards!"  I cried,
glancing bitterly from him to them--they had never failed me before.
"Cowards!"  I muttered, seeming to shrink into myself as I said the
word.  And I flung my sword clattering on the floor. "That is better!"  he drawled quite unmoved, as if nothing more than
words had passed, as if he had not been in peril at all. "It was what I
was going to ask you to do.  If the other young gentlemen will follow
your example, I shall be obliged.  Thank you.  Thank you." Croisette, and a minute later Marie, obeyed him to the letter!  I could
not understand it.  I folded my arms and gave up the game in despair,
and but for very shame I could have put my hands to my face and cried.
He stood in the middle under the lamp, a head taller than the tallest
of us; our master.  And we stood round him trapped, beaten, for all the
world like children.  Oh, I could have cried!  This was the end of our
long ride, our aspirations, our knight-errantry! "Now perhaps you will listen to me," he went on smoothly, "and hear
what I am going to do.  I shall keep you here, young gentlemen, until
you can serve me by carrying to mademoiselle, your cousin, some news of
her betrothed.  Oh, I shall not detain you long," he added with an evil
smile.  "You have arrived in Paris at a fortunate moment.  There is
going to be a--well, there is a little scheme on foot appointed for
to-night--singularly lucky you are!--for removing some objectionable
people, some friends of ours perhaps among them, M. Anne.  That is all.
You will hear shots, cries, perhaps screams.  Take no notice.  You will
be in no danger.  For M. de Pavannes," he continued, his voice sinking,
"I think that by morning I shall be able to give you a--a more
particular account of him to take to Caylus--to Mademoiselle, you
understand." For a moment the mask was off.  His face took a sombre brightness.  He
moistened his lips with his tongue as though he saw his vengeance
worked out then and there before him, and were gloating over the
picture.  The idea that this was so took such a hold upon me that I
shrank back, shuddering; reading too in Croisette's face the same
thought--and a late repentance.  Nay, the malignity of Bezers' tone,
the savage gleam of joy in his eyes appalled me to such an extent that
I fancied for a moment I saw in him the devil incarnate! He recovered his composure very quickly, however; and turned carelessly
towards the door.  "If you will follow me," he said, "I will see you
disposed of.  You may have to complain of your lodging--I have other
things to think of to-night than hospitality, But you shall not need to
complain of your supper." He drew aside the curtain as he spoke, and passed into the next room
before us, not giving a thought apparently to the possibility that we
might strike him from behind.  There certainly was an odd quality
apparent in him at times which seemed to contradict what we knew of him. The room we entered was rather long than wide, hung with tapestry, and
lighted by silver lamps.  Rich plate, embossed, I afterwards learned,
by Cellini the Florentine--who died that year I remember--and richer
glass from Venice, with a crowd of meaner vessels filled with meats and
drinks covered the table; disordered as by the attacks of a numerous
party.  But save a servant or two by the distant dresser, and an
ecclesiastic at the far end of the table, the room was empty. The priest rose as we entered, the Vidame saluting him as if they had
not met that day.  "You are welcome M. le Coadjuteur," he said; saying
it coldly, however, I thought.  And the two eyed one another with
little favour; rather as birds of prey about to quarrel over the spoil,
than as host and guest.  Perhaps the Coadjutor's glittering eyes and
great beak-like nose made me think of this. "Ho!  ho!"  he said, looking piercingly at us--and no doubt we must
have seemed a miserable and dejected crew enough.  "Who are these?  Not
the first-fruits of the night, eh?" The Vidame looked darkly at him.  "No," he answered brusquely. "They
are not.  I am not particular out of doors, Coadjutor, as you know, but
this is my house, and we are going to supper. Perhaps you do not
comprehend the distinction.  Still it exists--for me," with a sneer. This was as good as Greek to us.  But I so shrank from the priest's
malignant eyes, which would not quit us, and felt so much disgust
mingled with my anger that when Bezers by a gesture invited me to sit
down, I drew back.  "I will not eat with you," I said sullenly;
speaking out of a kind of dull obstinacy, or perhaps a childish
petulance. It did not occur to me that this would pierce the Vidame's armour.  Yet
a dull red showed for an instant in his cheek, and he eyed me with a
look, that was not all ferocity, though the veins in his great temples
swelled.  A moment, nevertheless, and he was himself again.  "Armand,"
he said quietly to the servant, "these gentlemen will not sup with me.
Lay for them at the other end." Men are odd.  The moment he gave way to me I repented of my words.  It
was almost with reluctance that I followed the servant to the lower
part of the table.  More than this, mingled with the hatred I felt for
the Vidame, there was now a strange sentiment towards him--almost of
admiration; that had its birth I think in the moment, when I held his
life in my hand, and he had not flinched. We ate in silence; even after Croisette by grasping my hand under the
table had begged me not to judge him hastily.  The two at the upper end
talked fast, and from the little that reached us, I judged that the
priest was pressing some course on his host, which the latter declined
to take. Once Bezers raised his voice.  "I have my own ends to serve!"  he broke
out angrily, adding a fierce oath which the priest did not rebuke, "and
I shall serve them.  But there I stop.  You have your own.  Well, serve
them, but do not talk to me of the cause! The cause?  To hell with the
cause!  I have my cause, and you have yours, and my lord of Guise has
his!  And you will not make me believe that there is any other!" "The king's?"  suggested the priest, smiling sourly. "Say rather the Italian woman's!"  the Vidame answered
recklessly--meaning the queen-mother, Catharine de' Medici, I supposed. "Well, then, the cause of the Church?"  the priest persisted. "Bah!  The Church?  It is you, my friend!"  Bezers rejoined, rudely
tapping his companion--at that moment in the act of crossing
himself--on the chest.  "The Church?"  he continued; "no, no, my
friend.  I will tell you what you are doing.  You want me to help you
to get rid of your branch, and you offer in return to aid me with
mine--and then, say you, there will be no stick left to beat either of
us.  But you may understand once for all"--and the Vidame struck his
hand heavily down among the glasses--"that I will have no interference
with my work, master Clerk!  None!  Do you hear?  And as for yours, it
is no business of mine.  That is plain speaking, is it not?" The priest's hand shook as he raised a full glass to his lips, but he
made no rejoinder, and the Vidame, seeing we had finished, rose.
"Armand!"  he cried, his face still dark, "take these gentlemen to
their chamber.  You understand?" We stiffly acknowledged his salute--the priest taking no notice of
us--and followed the servant from the room; going along a corridor and
up a steep flight of stairs, and seeing enough by the way to be sure
that resistance was hopeless.  Doors opened silently as we passed, and
grim fellows, in corslets and padded coats, peered out.  The clank of
arms and murmur of voices sounded continuously about us; and as we
passed a window the jingle of bits, and the hollow clang of a restless
hoof on the flags below, told us that the great house was for the time
a fortress.  I wondered much.  For this was Paris, a city with gates
and guards; the night a short August night.  Yet the loneliest manor in
Quercy could scarcely have bristled with more pikes and musquetoons, on
a winter's night and in time of war. No doubt these signs impressed us all; and Croisette not least. For
suddenly I heard him stop, as he followed us up the narrow staircase,
and begin without warning to stumble down again as fast as he could.  I
did not know what he was about; but muttering something to Marie, I
followed the lad to see.  At the foot of the flight of stairs I looked
back, Marie and the servant were standing in suspense, where I had left
them.  I heard the latter bid us angrily to return. But by this time Croisette was at the end of the corridor; and
reassuring the fellow by a gesture I hurried on, until brought to a
standstill by a man opening a door in my face.  He had heard our
returning footsteps, and eyed me suspiciously; but gave way after a
moment with a grunt of doubt I hastened on, reaching the door of the
room in which we had supped in time to see something which filled me
with grim astonishment; so much so that I stood rooted where I was, too
proud at any rate to interfere. Bezers was standing, the leering priest at his elbow.  And Croisette
was stooping forward, his hands stretched out in an attitude of
supplication. "Nay, but M. le Vidame," the lad cried, as I stood, the door in my
hand, "it were better to stab her at once than break her heart!  Have
pity on her!  If you kill him, you kill her!" The Vidame was silent, seeming to glower on the boy.  The priest
sneered.  "Hearts are soon mended--especially women's," he said. "But not Kit's!"  Croisette said passionately--otherwise ignoring him.
"Not Kit's!  You do not know her, Vidame!  Indeed you do not!" The remark was ill-timed.  I saw a spasm of anger distort Bezers' face.
"Get up, boy!"  he snarled, "I wrote to Mademoiselle what I would do,
and that I shall do!  A Bezers keeps his word.  By the God above us--if
there be a God, and in the devil's name I doubt it to-night!--I shall
keep mine!  Go!" His great face was full of rage.  He looked over Croisette's head as he
spoke, as if appealing to the Great Registrar of his vow, in the very
moment in which he all but denied Him.  I turned and stole back the way
I had come; and heard Croisette follow. That little scene completed my misery.  After that I seemed to take no
heed of anything or anybody until I was aroused by the grating of our
gaoler's key in the lock, and became aware that he was gone, and that
we were alone in a small room under the tiles. He had left the candle
on the floor, and we three stood round it. Save for the long shadows we
cast on the walls and two pallets hastily thrown down in one corner,
the place was empty.  I did not look much at it, and I would not look
at the others.  I flung myself on one of the pallets and turned my face
to the wall, despairing.  I thought bitterly of the failure we had made
of it, and of the Vidame's triumph.  I cursed St. Croix especially for
that last touch of humiliation he had set to it.  Then, forgetting
myself as my anger abated, I thought of Kit so far away at Caylus--of
Kit's pale, gentle face, and her sorrow.  And little by little I
forgave Croisette.  After all he had not begged for us--he had not
stooped for our sakes, but for hers. I do not know how long I lay at see-saw between these two moods. Or
whether during that time the others talked or were silent, moved about
the room or lay still.  But it was Croisette's hand on my shoulder,
touching me with a quivering eagerness that instantly communicated
itself to my limbs, which recalled me to the room and its shadows.
"Anne!"  he cried.  "Anne!  Are you awake?" "What is it?"  I said, sitting up and looking at him. "Marie," he began, "has--" But there was no need for him to finish.  I saw that Marie was standing
at the far side of the room by the unglazed window; which, being in a
sloping part of the roof, inclined slightly also.  He had raised the
shutter which closed it, and on his tip-toes--for the sill was almost
his own height from the floor--was peering out.  I looked sharply at
Croisette.  "Is there a gutter outside?"  I whispered, beginning to
tingle all over as the thought of escape for the first time occurred to
me. "No," he answered in the same tone.  "But Marie says he can see a beam
below, which he thinks we can reach." I sprang up, promptly displaced Marie, and looked out.  When my eyes
grew accustomed to the gloom I discerned a dark chaos of roofs and
gables stretching as far as I could see before me. Nearer, immediately
under the window, yawned a chasm--a narrow street.  Beyond this was a
house rather lower than that in which we were, the top of its roof not
quite reaching the level of my eyes. "I see no beam," I said. "Look below!"  quoth Marie, stolidly, I did so, and then saw that fifteen or sixteen feet below our window
there was a narrow beam which ran from our house to the opposite
one--for the support of both, as is common in towns.  In the shadow
near the far end of this--it was so directly under our window that I
could only see the other end of it--I made out a casement, faintly
illuminated from within. I shook my head. "We cannot get down to it," I said, measuring the distance to the beam
and the depth below it, and shivering. "Marie says we can, with a short rope," Croisette replied.  His eyes
were glistening with excitement. "But we have no rope!"  I retorted.  I was dull--as usual.  Marie made
no answer.  Surely he was the most stolid and silent of brothers.  I
turned to him.  He was taking off his waistcoat and neckerchief. "Good!"  I cried.  I began to see now.  Off came our scarves and
kerchiefs also, and fortunately they were of home make, long and
strong.  And Marie had a hank of four-ply yarn in his pocket as it
turned out, and I had some stout new garters, and two or three yards of
thin cord, which I had brought to mend the girths, if need should
arise.  In five minutes we had fastened them cunningly together. "I am the lightest," said Croisette. "But Marie has the steadiest head," I objected.  We had learned that
long ago--that Marie could walk the coping-stones of the battlements
with as little concern as we paced a plank set on the ground. "True," Croisette had to admit.  "But he must come last, because
whoever does so will have to let himself down." I had not thought of that, and I nodded.  It seemed that the lead was
passing out of my hands and I might resign myself.  Still one thing I
would have.  As Marie was to come last, I would go first. My weight
would best test the rope.  And accordingly it was so decided. There was no time to be lost.  At any moment we might be interrupted.
So the plan was no sooner conceived than carried out.  The rope was
made fast to my left wrist.  Then I mounted on Marie's shoulders, and
climbed--not without quavering--through the window, taking as little
time over it as possible, for a bell was already proclaiming midnight. All this I had done on the spur of the moment.  But outside, hanging by
my hands in the darkness, the strokes of the great bell in my ears, I
had a moment in which to think.  The sense of the vibrating depth below
me, the airiness, the space and gloom around, frightened me.  "Are you
ready?"  muttered Marie, perhaps with a little impatience.  He had not
a scrap of imagination, had Marie. "No!  wait a minute!"  I blurted out, clinging to the sill, and taking
a last look at the bare room, and the two dark figures between me and
the light.  "No!"  I added, hurriedly. "Croisette--boys, I called you
cowards just now.  I take it back! I did not mean it!  That is all!"  I
gasped.  "Let go!" A warm touch on my hand.  Something like a sob. The next moment I felt myself sliding down the face of the house, down
into the depth.  The light shot up.  My head turned giddily. I clung,
oh, how I clung to that rope!  Half way down the thought struck me that
in case of accident those above might not be strong enough to pull me
up again.  But it was too late to think of that, and in another second
my feet touched the beam.  I breathed again.  Softly, very gingerly, I
made good my footing on the slender bridge, and, disengaging the rope,
let it go.  Then, not without another qualm, I sat down astride of the
beam, and whistled in token of success.  Success so far! It was a strange position, and I have often dreamed of it since. In the
darkness about me Paris lay to all seeming asleep.  A veil, and not the
veil of night only, was stretched between it and me; between me, a mere
lad, and the strange secrets of a great city; stranger, grimmer, more
deadly that night than ever before or since.  How many men were
watching under those dimly-seen roofs, with arms in their hands?  How
many sat with murder at heart?  How many were waking, who at dawn would
sleep for ever, or sleeping who would wake only at the knife's edge?
These things I could not know, any more than I could picture how many
boon-companions were parting at that instant, just risen from the dice,
one to go blindly--the other watching him--to his death?  I could not
imagine, thank Heaven for it, these secrets, or a hundredth part of the
treachery and cruelty and greed that lurked at my feet, ready to burst
all bounds at a pistol-shot.  It had no significance for me that the
past day was the 23rd of August, or that the morrow was St.
Bartholomew's feast! No.  Yet mingled with the jubilation which the possibility of triumph
over our enemy raised in my breast, there was certainly a foreboding.
The Vidame's hints, no less than his open boasts, had pointed to
something to happen before morning--something wider than the mere
murder of a single man.  The warning also which the Baron de Rosny had
given us at the inn occurred to me with new meaning.  And I could not
shake the feeling off.  I fancied, as I sat in the darkness astride of
my beam, that I could see, closing the narrow vista of the street, the
heavy mass of the Louvre; and that the murmur of voices and the tramp
of men assembling came from its courts, with now and again the stealthy
challenge of a sentry, the restrained voice of an officer. Scarcely a
wayfarer passed beneath me:  so few, indeed, that I had no fear of
being detected from below.  And yet unless I was mistaken, a furtive
step, a subdued whisper were borne to me on every breeze, from every
quarter.  And the night was full of phantoms. Perhaps all this was mere nervousness, the outcome of my position.  At
any rate I felt no more of it when Croisette joined me.  We had our
daggers, and that gave me some comfort.  If we could once gain entrance
to the house opposite, we had only to beg, or in the last resort force
our way downstairs and out, and then to hasten with what speed we might
to Pavannes' dwelling. Clearly it was a question of time only now;
whether Bezers' band or we should first reach it.  And struck by this I
whispered Marie to be quick.  He seemed to be long in coming. He scrambled down hand over hand at last, and then I saw that he had
not lingered above for nothing.  He had contrived after getting out of
the window to let down the shutter.  And more he had at some risk
lengthened our rope, and made a double line of it, so that it ran round
a hinge of the shutter; and when he stood beside us, he took it by one
end and disengaged it.  Good, clever Marie! "Bravo!"  I said softly, clapping him on the back.  "Now they will not
know which way the birds have flown!" So there we all were, one of us, I confess, trembling.  We slid easily
enough along the beam to the opposite house.  But once there in a row
one behind the other with our faces to the wall, and the night air
blowing slantwise--well I am nervous on a height and I gasped.  The
window was a good six feet above the beam, The casement--it was
unglazed--was open, veiled by a thin curtain, and alas!  protected by
three horizontal bars--stout bars they looked. Yet we were bound to get up, and to get in; and I was preparing to rise
to my feet on the giddy bridge as gingerly as I could, when Marie
crawled quickly over us, and swung himself up to the narrow sill, much
as I should mount a horse on the level.  He held out his foot to me,
and making an effort I reached the same dizzy perch.  Croisette for the
time remained below. A narrow window-ledge sixty feet above the pavement, and three bars to
cling to!  I cowered to my holdfasts, envying even Croisette.  My legs
dangled airily, and the black chasm of the street seemed to yawn for
me.  For a moment I turned sick.  I recovered from that to feel
desperate.  I remembered that go forward we must, bars or no bars.  We
could not regain our old prison if we would. It was equally clear that we could not go forward if the inmates should
object.  On that narrow perch even Marie was helpless. The bars of the
window were close together.  A woman, a child, could disengage our
hands, and then--I turned sick again.  I thought of the cruel stones.
I glued my face to the bars, and pushing aside a corner of the curtain,
looked in. There was only one person in the room--a woman, who was moving about
fully dressed, late as it was.  The room was a mere attic, the
counterpart of that we had left.  A box-bed with a canopy roughly
nailed over it stood in a corner.  A couple of chairs were by the
hearth, and all seemed to speak of poverty and bareness.  Yet the woman
whom we saw was richly dressed, though her silks and velvets were
disordered.  I saw a jewel gleam in her hair, and others on her hands.
When she turned her face towards us--a wild, beautiful face, perplexed
and tear-stained--I knew her instantly for a gentlewoman, and when she
walked hastily to the door, and laid her hand upon it, and seemed to
listen--when she shook the latch and dropped her hands in despair and
went back to the hearth, I made another discovery I knew at once,
seeing her there, that we were likely but to change one prison for
another.  Was every house in Paris then a dungeon?  And did each roof
cover its tragedy? "Madame!"  I said, speaking softly, to attract her attention. "Madame!" She started violently, not knowing whence the sound came, and looked
round, at the door first.  Then she moved towards the window, and with
an affrighted gesture drew the curtain rapidly aside. Our eyes met.  What if she screamed and aroused the house?  What,
indeed?  "Madame," I said again, speaking hurriedly, and striving to
reassure her by the softness of my voice, "we implore your help!
Unless you assist us we are lost." "You!  Who are you?"  she cried, glaring at us wildly, her hand to her
head.  And then she murmured to herself, "Mon Dieu!  what will become
of me?" "We have been imprisoned in the house opposite," I hastened to explain,
disjointedly I am afraid.  "And we have escaped.  We cannot get back if
we would.  Unless you let us enter your room and give us shelter--" "We shall be dashed to pieces on the pavement," supplied Marie, with
perfect calmness--nay, with apparent enjoyment. "Let you in here?"  she answered, starting back in new terror; "it is
impossible." She reminded me of our cousin, being, like her pale and dark-haired.
She wore her hair in a coronet, disordered now.  But though she was
still beautiful, she was older than Kit, and lacked her pliant grace.
I saw all this, and judging her nature, I spoke out of my despair.
"Madame," I said piteously, "we are only boys.  Croisette!  Come up!"
Squeezing myself still more tightly into my corner of the ledge, I made
room for him between us.  "See, Madame," I cried, craftily, "will you
not have pity on three boys?" St. Crois's boyish face and fair hair arrested her attention, as I had
expected.  Her expression grew softer, and she murmured, "Poor boy!" I caught at the opportunity.  "We do but seek a passage through your
room," I said fervently.  Good heavens, what had we not at stake!  What
if she should remain obdurate?  "We are in trouble--in despair," I
panted.  "So, I believe, are you.  We will help you if you will first
save us.  We are boys, but we can fight for you." "Whom am I to trust?"  she exclaimed, with a shudder.  "But heaven
forbid," she continued, her eyes on Croisette's face, "that, wanting
help, I should refuse to give it.  Come in, if you will." I poured out my thanks, and had forced my head between the bars--at
imminent risk of its remaining there--before the words were well out of
her mouth.  But to enter was no easy task after all. Croisette did,
indeed, squeeze through at last, and then by force pulled first one and
then the other of us after him.  But only necessity and that chasm
behind could have nerved us, I think, to go through a process so
painful.  When I stood, at length on the floor, I seemed to be one
great abrasion from head to foot.  And before a lady, too! But what a joy I felt, nevertheless.  A fig for Bezers now.  He had
called us boys; and we were boys.  But he should yet find that we could
thwart him.  It could be scarcely half-an-hour after midnight; we might
still be in time.  I stretched myself and trod the level door
jubilantly, and then noticed, while doing so, that our hostess had
retreated to the door and was eyeing us timidly--half-scared. I advanced to her with my lowest bow--sadly missing my sword. "Madame,"
I said, "I am M. Anne de Caylus, and these are my brothers.  And we are
at your service." "And I," she replied, smiling faintly--I do not know why--"am Madame de
Pavannes, I gratefully accept your offers of service." "De Pavannes?"  I exclaimed, amazed and overjoyed.  Madame de Pavannes!
Why, she must be Louis' kinswoman!  No doubt she could tell us where he
was lodged, and so rid our task of half its difficulty.  Could anything
have fallen out more happily?  "You know then M. Louis de Pavannes?"  I
continued eagerly. "Certainly," she answered, smiling with a rare shy sweetness this time.
"Very well indeed.  He is my husband."
```

### AI Extraction
- **Primary Mechanism**: `DEADPAN_REACTION` (Detector Confidence: `0.66`)
- **Secondary Dynamics**: MISUNDERSTANDING, STATUS_REVERSAL
- **Linguistic Craft Score**: `0.75`
- **Tone**: `DEADPAN`
- **Setup**: Characters And, Coadjutor establish scene context: 'CHAPTER IV....'
- **Escalation**: Complication rises around deadpan_reaction: 'But save a servant or two by the distant dresser, and an
ecclesiastic at the far...'
- **Reversal**: Expectation or status is inverted: 'I do not know how long I lay at see-saw between these two moods....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'He is my husband."...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 21 — `the_man_upstairs_ch27_02543`

**Source**: *The Man Upstairs* (Chapter 27)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.46` | **Surface Slang Isolated**: None  

### Passage
```text
"Coward! stand aside, and see me do it. I will grasp her throat; I will do her business in an instant; she shall not have time so much as to groan," Presently, another voice, but equally near me, was heard whispering in answer, "Why not? I will draw a trigger in this business; but perdition be my lot if I do more!" To this the first voice returned, in a tone which rage had heightened in a small degree above a whisper, What wonder that I was petrified by sounds so dreadful! Murderers lurked in my closet.
```

### AI Extraction
- **Primary Mechanism**: `SOCIAL_EMBARRASSMENT` (Detector Confidence: `0.25`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: '"Coward!...'
- **Escalation**: Complication rises around social_embarrassment: 'stand aside, and see me do it....'
- **Reversal**: Expectation or status is inverted: 'I will grasp her throat; I will do her business in an instant; she shall not hav...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'Murderers lurked in my closet....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 22 — `right_ho_ch17_06755`

**Source**: *Right Ho* (Chapter 17)  
**Characters Identified**: Aunt Isabel  
**Dialogue Ratio**: `0.59` | **Surface Slang Isolated**: None  

### Passage
```text
"that roused dear old Rocky like a trumpet call. It must have brought home to him the realisation that a miracle had come off and saved him from being cut out of Aunt Isabel's. At any rate, as she said it he perked up, let go of the table, and faced her with gleaming eyes," Won't you, for my sake, try, [FRIEND]? Won't you go back to the country to-morrow and begin the struggle? Little by little, if you use your will - - " I can't help thinking it must have been that word "will Do you want me to go back to the country, Aunt Isabel?" "Yes.
```

### AI Extraction
- **Primary Mechanism**: `SOCIAL_EMBARRASSMENT` (Detector Confidence: `0.25`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Aunt Isabel establish scene context: '"that roused dear old Rocky like a trumpet call....'
- **Escalation**: Complication rises around social_embarrassment: 'It must have brought home to him the realisation that a miracle had come off and...'
- **Reversal**: Expectation or status is inverted: 'At any rate, as she said it he perked up, let go of the table, and faced her wit...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'Little by little, if you use your will - - " I can't help thinking it must have ...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 23 — `my_man_jeeves_ch17_04507`

**Source**: *My Man Jeeves* (Chapter 17)  
**Characters Identified**: Aunt Isabel, Rocky  
**Dialogue Ratio**: `0.73` | **Surface Slang Isolated**: None  

### Passage
```text
"said Rocky. And so the merry party began. It was one of those jolly, happy, bread-crumbling parties where you cough twice before you speak, and then decide not to say it after all. After we had had an hour of this wild dissipation, Aunt Isabel said she wanted to go home. In the light of what Rocky had been telling me, this struck me as sinister. I had gathered that at the beginning of her visit she had had to be dragged home with ropes. It must have hit Rocky the same way, for he gave me a pleading look," What'll you have? You'll come along, won't you, [PROTAGONIST], and have a drink at the flat?" I had a feeling that this wasn't in the contract, but there wasn't anything to be done.
```

### AI Extraction
- **Primary Mechanism**: `SOCIAL_EMBARRASSMENT` (Detector Confidence: `0.25`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Aunt Isabel, Rocky establish scene context: '"said Rocky....'
- **Escalation**: Complication rises around social_embarrassment: 'It was one of those jolly, happy, bread-crumbling parties where you cough twice ...'
- **Reversal**: Expectation or status is inverted: 'In the light of what Rocky had been telling me, this struck me as sinister....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'You'll come along, won't you, [PROTAGONIST], and have a drink at the flat?" I ha...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 24 — `jill_the_reckless_ch11_03908`

**Source**: *Jill The Reckless* (Chapter 11)  
**Characters Identified**: About, All, Anne, Bure, Captain Answered, Croisette, Louis, Pavannes, Uncle Might  
**Dialogue Ratio**: `0.64` | **Surface Slang Isolated**: None  

### Passage
```text
CHAPTER XI. A NIGHT OF SORROW. "Louis!  Louis!" He turned with a start at the sound of my voice, joy and
bewilderment--and no wonder--in his countenance.  He had not supposed
us to be within a hundred leagues of him.  And lo!  here we were, knee
to knee, hand meeting hand in a long grasp, while his eyes, to which
tears sprang unbidden, dwelt on my face as though they could read in it
the features of his sweetheart. Some one had furnished him with a hat,
and enabled him to put his dress in order, and wash his wound, which
was very slight, and these changes had improved his appearance; so that
the shadow of grief and despondency passing for a moment from him in
the joy of seeing me, he looked once more his former self:  as he had
looked in the old days at Caylus on his return from hawking, or from
some boyish escapade among the hills.  Only, alas!  he wore no sword. "And now tell me all," he cried, after his first exclamation of wonder
had found vent.  "How on earth do you come here?  Here, of all places,
and by my side?  Is all well at Caylus?  Surely Mademoiselle is not--" "Mademoiselle is well!  perfectly well!  And thinking of you, I swear!"
I answered passionately.  "For us," I went on, eager for the moment to
escape that subject--how could I talk of it in the daylight and under
strange eyes?--"Marie and Croisette are behind.  We left Caylus eight
days ago.  We reached Paris yesterday evening.  We have not been to
bed!  We have passed, Louis, such a night as I never--" He stopped me with a gesture.  "Hush!"  he said, raising his hand.
"Don't speak of it, Anne!"  and I saw that the fate of his friends was
still too recent, the horror of his awakening to those dreadful sights
and sounds was still too vivid for him to bear reference to them.  Yet
after riding for a time in silence--though his lips moved--he asked me
again what had brought us up. "We came to warn you--of him," I answered, pointing to the solitary,
moody figure of the Vidame, who was riding ahead of the party.  "He--he
said that Kit should never marry you, and boasted of what he would do
to you, and frightened her.  So, learning he was going to Paris, we
followed him--to put you on your guard, you know."  And I briefly
sketched our adventures, and the strange circumstances and mistakes
which had delayed us hour after hour, through all that strange night,
until the time had gone by when we could do good. His eyes glistened and his colour rose as I told the story.  He wrung
my hand warmly, and looked back to smile at Marie and Croisette.  "It
was like you!"  he ejaculated with emotion.  "It was like her cousins!
Brave, brave lads!  The Vicomte will live to be proud of you!  Some day
you will all do great things!  I say it!" "But oh, Louis!"  I exclaimed sorrowfully, though my heart was bounding
with pride at his words, "if we had only been in time! If we had only
come to you two hours earlier!" "You would have spoken to little purpose then, I fear," he replied,
shaking his head.  "We were given over as a prey to the enemy.
Warnings?  We had warnings in plenty.  De Rosny warned us, and we
scoffed at him.  The king's eye warned us, and we trusted him.  But--"
and Louis' form dilated and his hand rose as he went on, and I thought
of his cousin's prediction--"it will never be so again in France, Anne!
Never!  No man will after this trust another!  There will be no honour,
no faith, no quarter, and no peace!  And for the Valois who has done
this, the sword will never depart from his house!  I believe it!  I do
believe it!" How truly he spoke we know now.  For two-and-twenty years after that
twenty-fourth of August, 1572, the sword was scarcely laid aside in
France for a single month.  In the streets of Paris, at Arques, and
Coutras, and Ivry, blood flowed like water that the blood of the St.
Bartholomew might be forgotten--that blood which, by the grace of God,
Navarre saw fall from the dice box on the eve of the massacre.  The
last of the Valois passed to the vaults of St. Denis:  and a greater
king, the first of all Frenchmen, alive or dead, the bravest, gayest,
wisest of the land, succeeded him:  yet even he had to fall by the
knife, in a moment most unhappy for his country, before France,
horror-stricken, put away the treachery and evil from her. Talking with Louis as we rode, it was not unnatural--nay, it was the
natural result of the situation--that I should avoid one subject.  Yet
that subject was the uppermost in my thoughts. What were the Vidame's
intentions?  What was the meaning of this strange journey?  What was to
be Louis' fate?  I shrank with good reason from asking him these
questions.  There could be so little room for hope, even after that
smile which I had seen Bezers smile, that I dared not dwell upon them.
I should but torture him and myself. So it was he who first spoke about it.  Not at that time, but after
sunset, when the dusk had fallen upon us, and found us still plodding
southward with tired horses; a link outwardly like other links in the
long chain of riders, toiling onwards.  Then he said suddenly, "Do you
know whither we are going, Anne?" I started, and found myself struggling with a strange confusion before
I could reply.  "Home," I suggested at random. "Home?  No.  And yet nearly home.  To Cahors," he answered with an odd
quietude.  "Your home, my boy, I shall never see again, Nor Kit!  Nor
my own Kit!"  It was the first time I had heard him call her by the
fond name we used ourselves.  And the pathos in his tone as of the
past, not the present, as of pure memory--I was very thankful that I
could not in the dusk see his face--shook my self-control.  I wept.
"Nay, my lad," he went on, speaking softly and leaning from his saddle
so that he could lay his hand on my shoulder "we are all men together.
We must be brave.  Tears cannot help us, so we should leave them to
the--women." I cried more passionately at that.  Indeed his own voice quavered over
the last word.  But in a moment he was talking to me coolly and
quietly.  I had muttered something to the effect that the Vidame would
not dare--it would be too public. "There is no question of daring in it," he replied.  "And the more
public it is, the better he will like it.  They have dared to take
thousands of lives since yesterday.  There is no one to call him to
account since the king--our king forsooth!--has declared every Huguenot
an outlaw, to be killed wherever he be met with.  No, when Bezers
disarmed me yonder," he pointed as he spoke to his wound, "I looked of
course for instant death.  Anne! I saw blood in his eyes!  But he did
not strike." "Why not?"  I asked in suspense. "I can only guess," Louis answered with a sigh.  "He told me that my
life was in his hands, but that he should take it at his own time.
Further that if I would not give my word to go with him without trying
to escape, he would throw me to those howling dogs outside.  I gave my
word.  We are on the road together.  And oh, Anne!  yesterday, only
yesterday, at this time I was riding home with Teligny from the Louvre,
where we had been playing at paume with the king!  And the world--the
world was very fair." "I saw you, or rather Croisette did," I muttered as his sorrow--not for
himself, but his friends--forced him to stop.  "Yet how, Louis, do you
know that we are going to Cahors?" "He told me, as we passed through the gates, that he was appointed
Lieutenant-Governor of Quercy to carry out the edict against the
religion.  Do you not see, Anne?"  my companion added bitterly, "to
kill me at once were too small a revenge for him! He must torture
me--or rather he would if he could--by the pains of anticipation. "Besides, my execution will so finely open his bed of justice. Bah!"
and Pavannes raised his head proudly, "I fear him not!  I fear him not
a jot!" For a moment he forgot Kit, the loss of his friends, his own doom.  He
snapped his fingers in derision of his foe. But my heart sank miserably.  The Vidame's rage I remembered had been
directed rather against my cousin than her lover; and now by the light
of his threats I read Bezers' purpose more clearly than Louis could.
His aim was to punish the woman who had played with him.  To do so he
was bringing her lover from Paris that he might execute him--AFTER
GIVING HER NOTICE!  That was it:  after giving her notice, it might be
in her very presence!  He would lure her to Cahors, and then-- I shuddered.  I well might feel that a precipice was opening at my
feet.  There was something in the plan so devilish, yet so accordant
with those stories I had heard of the Wolf, that I felt no doubt of my
insight.  I read his evil mind, and saw in a moment why he had troubled
himself with us.  He hoped to draw Mademoiselle to Cahors by our means. Of course I said nothing of this to Louis.  I hid my feelings as well
as I could.  But I vowed a great vow that at the eleventh hour we would
baulk the Vidame.  Surely if all else failed we could kill him, and,
though we died ourselves, spare Kit this ordeal.  My tears were dried
up as by a fire.  My heart burned with a great and noble rage:  or so
it seemed to me! I do not think that there was ever any journey so strange as this one
of ours.  We met with the same incidents which had pleased us on the
road to Paris.  But their novelty was gone.  Gone too were the cosy
chats with old rogues of landlords and good-natured dames.  We were
travelling now in such force that our coming was rather a terror to the
innkeeper than a boon.  How much the Lieutenant-Governor of Quercy,
going down to his province, requisitioned in the king's name; and for
how much he paid, we could only judge from the gloomy looks which
followed us as we rode away each morning.  Such looks were not solely
due I fear to the news from Paris, although for some time we were the
first bearers of the tidings. Presently, on the third day of our journey I think, couriers from the
Court passed us:  and henceforth forestalled us.  One of these
messengers--who I learned from the talk about me was bound for Cahors
with letters for the Lieutenant-Governor and the Count-Bishop--the
Vidame interviewed and stopped.  How it was managed I do not know, but
I fear the Count-Bishop never got his letters, which I fancy would have
given him some joint authority. Certainly we left the messenger--a
prudent fellow with a care for his skin--in comfortable quarters at
Limoges, whence I do not doubt he presently returned to Paris at his
leisure. The strangeness of the journey however arose from none of these things,
but from the relations of our party to one another. After the first day
we four rode together, unmolested, so long as we kept near the centre
of the straggling cavalcade.  The Vidame always rode alone, and in
front, brooding with bent head and sombre face over his revenge, as I
supposed.  He would ride in this fashion, speaking to no one and giving
no orders, for a day together.  At times I came near to pitying him.
He had loved Kit in his masterful way, the way of one not wont to be
thwarted, and he had lost her--lost her, whatever might happen.  He
would get nothing after all by his revenge.  Nothing but ashes in the
mouth.  And so I saw in softer moments something inexpressibly
melancholy in that solitary giant-figure pacing always alone. He seldom spoke to us.  More rarely to Louis.  When he did, the
harshness of his voice and his cruel eyes betrayed the gloomy hatred in
which he held him.  At meals he ate at one end of the table:  we four
at the other, as three of us had done on that first evening in Paris.
And sometimes the covert looks, the grim sneer he shot at his
rival--his prisoner--made me shiver even in the sunshine.  Sometimes,
on the other hand, when I took him unawares, I found an expression on
his face I could not read. I told Croisette, but warily, my suspicions of his purpose.  He heard
me, less astounded to all appearance than I had expected. Presently I
learned the reason.  He had his own view.  "Do you not think it
possible, Anne?"  he suggested timidly--we were of course alone at the
time--"that he thinks to make Louis resign Mademoiselle?" "Resign her!"  I exclaimed obtusely.  "How?" "By giving him a choice--you understand?" I did understand I saw it in a moment.  I had been dull not to see it
before.  Bezers might put it in this way:  let M. de Pavannes resign
his mistress and live, or die and lose her. "I see," I answered.  "But Louis would not give her up.  Not to him!" "He would lose her either way," Croisette answered in a low tone. "That
is not however the worst of it.  Louis is in his power. Suppose he
thinks to make Kit the arbiter, Anne, and puts Louis up to ransom,
setting Kit for the price?  And gives her the option of accepting
himself, and saving Louis' life; or refusing, and leaving Louis to die?" "St. Croix!"  I exclaimed fiercely.  "He would not be so base!" And yet
was not even this better than the blind vengeance I had myself
attributed to him? "Perhaps not," Croisette answered, while he gazed onwards through the
twilight.  We were at the time the foremost of the party save the
Vidame; and there was nothing to interrupt our view of his gigantic
figure as he moved on alone before us with bowed shoulders.  "Perhaps
not," Croisette repeated thoughtfully. "Sometimes I think we do not
understand him; and that after all there may be worse people in the
world than Bezers." I looked hard at the lad, for that was not what I had meant. "Worse?"
I said.  "I do not think so.  Hardly!" "Yes, worse," he replied, shaking his head.  "Do you remember lying
under the curtain in the box-bed at Mirepoix's?" "Of course I do!  Do you think I shall ever forget it?" "And Madame d'O coming in?" "With the Coadjutor?"  I said with a shudder.  "Yes." "No, the second time," he answered, "when she came back alone. It was
pretty dark, you remember, and Madame de Pavannes was at the window,
and her sister did not see her?" "Well, well, I remember," I said impatiently.  I knew from the tone of
his voice that he had something to tell me about Madame d'O, and I was
not anxious to hear it.  I shrank, as a wounded man shrinks from the
cautery, from hearing anything about that woman; herself so beautiful,
yet moving in an atmosphere of suspicion and horror.  Was it shame, or
fear, or some chivalrous feeling having its origin in that moment when
I had fancied myself her knight?  I am not sure, for I had not made up
my mind even now whether I ought to pity or detest her; whether she had
made a tool of me, or I had been false to her. "She came up to the bed, you remember, Anne?"  Croisette went on. "You
were next to her.  She saw you indistinctly, and took you for her
sister.  And then I sprang from the bed." "I know you did!"  I exclaimed sharply.  All this time I had forgotten
that grievance.  "You nearly frightened her out of her wits, St. Croix.
I cannot think what possessed you--why you did it?" "To save your life, Anne," he answered solemnly, "and her from a crime!
an unutterable, an unnatural crime.  She had come back to I can hardly
tell it you--to murder her sister.  You start.  You do not believe me.
It sounds too horrible.  But I could see better than you could.  She
was exactly between you and the light.  I saw the knife raised.  I saw
her wicked face!  If I had not startled her as I did, she would have
stabbed you.  She dropped the knife on the floor, and I picked it up
and have it. See!" I looked furtively, and turned away again, shivering.  "Why," I
muttered, "why did she do it?" "She had failed you know to get her sister back to Pavannes' house,
where she would have fallen an easy victim.  Bezers, who knew Madame
d'O, prevented that.  Then that fiend slipped back with her knife;
thinking that in the common butchery the crime would be overlooked, and
never investigated, and that Mirepoix would be silent!" I said nothing.  I was stunned.  Yet I believed the story.  When I went
over the facts in my mind I found that a dozen things, overlooked at
the time and almost forgotten in the hurry of events, sprang up to
confirm it.  M. de Pavannes'--the other M. de Pavannes'--suspicions had
been well founded.  Worse than Bezers was she?  Ay!  worse a hundred
times.  As much worse as treachery ever is than violence; as the
pitiless fraud of the serpent is baser than the rage of the wolf. "I thought," Croisette added softly, not looking at me, "when I
discovered that you had gone off with her, that I should never see you
again, Anne.  I gave you up for lost.  The happiest moment of my life I
think was when I saw you come back." "Croisette," I whispered piteously, my cheeks burning, "let us never
speak of her again." And we never did--for years.  But how strange is life.  She and the
wicked man with whom her fate seemed bound up had just crossed our
lives when their own were at the darkest.  They clashed with us, and,
strangers and boys as we were, we ruined them.  I have often asked
myself what would have happened to me had I met her at some earlier and
less stormy period--in the brilliance of her beauty.  And I find but
one answer.  I should bitterly have rued the day.  Providence was good
to me.  Such men and such women, we may believe have ceased to exist
now.  They flourished in those miserable days of war and divisions, and
passed away with them like the foul night-birds of the battle-field. To return to our journey.  In the morning sunshine one could not but be
cheerful, and think good things possible.  The worst trial I had came
with each sunset.  For then--we generally rode late into the
evening--Louis sought my side to talk to me of his sweetheart.  And how
he would talk of her!  How many thousand messages he gave me for her!
How often he recalled old days among the hills, with each laugh and
jest and incident, when we five had been as children!  Until I would
wonder passionately, the tears running down my face in the darkness,
how he could--how he could talk of her in that quiet voice which
betrayed no rebellion against fate, no cursing of Providence!  How he
could plan for her and think of her when she should be alone! Now I understand it.  He was still labouring under the shock of his
friends' murder.  He was still partially stunned.  Death seemed natural
and familiar to him, as to one who had seen his allies and companions
perish without warning or preparation. Death had come to be normal to
him, life the exception; as I have known it seem to a child brought
face to face with a corpse for the first time. One afternoon a strange thing happened.  We could see the Auvergne
hills at no great distance on our left--the Puy de Dome above them--and
we four were riding together.  We had fallen--an unusual thing--to the
rear of the party.  Our road at the moment was a mere track running
across moorland, sprinkled here and there with gorse and brushwood.
The main company had straggled on out of sight.  There were but half a
dozen riders to be seen an eighth of a league before us, a couple
almost as far behind. I looked every way with a sudden surging of the
heart.  For the first time the possibility of flight occurred to me.
The rough Auvergne hills were within reach.  Supposing we could get a
lead of a quarter of a league, we could hardly be caught before
darkness came and covered us.  Why should we not put spurs to our
horses and ride off? "Impossible!"  said Pavannes quietly, when I spoke. "Why?"  I asked with warmth. "Firstly," he replied, "because I have given my word to go with the
Vidame to Cahors." My face flushed hotly.  But I cried, "What of that?  You were taken by
treachery!  Your safe conduct was disregarded.  Why should you be
scrupulous?  Your enemies are not.  This is folly?" "I think not.  Nay," Louis answered, shaking his head, "you would not
do it yourself in my place." "I think I should," I stammered awkwardly. "No, you would not, lad," he said smiling.  "I know you too well. But
if I would do it, it is impossible."  He turned in the saddle and,
shading his eyes with his hand from the level rays of the sun, looked
back intently.  "It is as I thought," he continued. "One of those men
is riding grey Margot, which Bure said yesterday was the fastest mare
in the troop.  And the man on her is a light weight.  The other fellow
has that Norman bay horse we were looking at this morning.  It is a
trap laid by Bezers, Anne. If we turned aside a dozen yards, those two
would be after us like the wind." "Do you mean," I cried, "that Bezers has drawn his men forward on
purpose?" "Precisely;" was Louis's answer.  "That is the fact.  Nothing would
please him better than to take my honour first, and my life afterwards.
But, thank God, only the one is in his power." And when I came to look at the horsemen, immediately before us, they
confirmed Louis's view.  They were the best mounted of the party:  all
men of light weight too.  One or other of them was constantly looking
back.  As night fell they closed in upon us with their usual care.
When Bure joined us there was a gleam of intelligence in his bold eyes,
a flash of conscious trickery.  He knew that we had found him out, and
cared nothing for it. And the others cared nothing.  But the thought that if left to myself I
should have fallen into the Vidame's cunning trap filled me with new
hatred towards him; such hatred and such fear--for there was
humiliation mingled with them--as I had scarcely felt before.  I
brooded over this, barely noticing what passed in our company for
hours--nay, not until the next day when, towards evening, the cry arose
round me that we were within sight of Cahors.  Yes, there it lay below
us, in its shallow basin, surrounded by gentle hills.  The domes of the
cathedral, the towers of the Vallandre Bridge, the bend of the Lot,
where its stream embraces the town--I knew them all.  Our long journey
was over. And I had but one idea.  I had some time before communicated to
Croisette the desperate design I had formed--to fall upon Bezers and
kill him in the midst of his men in the last resort.  Now the time had
come if the thing was ever to be done:  if we had not left it too long
already.  And I looked about me.  There was some confusion and jostling
as we halted on the brow of the hill, while two men were despatched
ahead to announce the governor's arrival, and Bure, with half a dozen
spears, rode out as an advanced guard. The road where we stood was narrow, a shallow cutting winding down the
declivity of the hills.  The horses were tired, It was a bad time and
place for my design, and only the coming night was in my favour.  But I
was desperate. Yet before I moved or gave a signal which nothing could recall, I
scanned the landscape eagerly, scrutinizing in turn the small, rich
plain below us, warmed by the last rays of the sun, the bare hills here
glowing, there dark, the scattered wood-clumps and spinneys that filled
the angles of the river, even the dusky line of helm-oaks that crowned
the ridge beyond--Caylus way.  So near our own country there might be
help!  If the messenger whom we had despatched to the Vicomte before
leaving home had reached him, our uncle might have returned, and even
be in Cahors to meet us. But no party appeared in sight:  and I saw no place where an ambush
could be lying.  I remembered that no tidings of our present plight or
of what had happened could have reached the Vicomte.  The hope faded
out of life as soon as despair had given it birth.  We must fend for
ourselves and for Kit. That was my justification.  I leaned from my saddle towards
Croisette--I was riding by his side--and muttered, as I felt my horse's
head and settled myself firmly in the stirrups, "You remember what I
said?  Are you ready?" He looked at me in a startled way, with a face showing white in the
shadow:  and from me to the one solitary figure seated like a pillar a
score of paces in front with no one between us and it. "There need be
but two of us," I muttered, loosening my sword. "Shall it be you or
Marie?  The others must leap their horses out of the road in the
confusion, cross the river at the Arembal Ford if they are not
overtaken, and make for Caylus." He hesitated.  I do not know whether it had anything to do with his
hesitation that at that moment the cathedral bell in the town below us
began to ring slowly for Vespers.  Yes, he hesitated. He--a Caylus.
Turning to him again, I repeated my question impatiently.  "Which shall
it be?  A moment, and we shall be moving on, and it will be too late." He laid his hand hurriedly on my bridle, and began a rambling answer.
Rambling as it was I gathered his meaning.  It was enough for me!  I
cut him short with one word of fiery indignation, and turned to Marie
and spoke quickly.  "Will you, then?"  I said. But Marie shook his head in perplexity, and answering little, said the
same.  So it happened a second time. Strange!  Yet strange as it seemed, I was not greatly surprised. Under
other circumstances I should have been beside myself with anger at the
defection.  Now I felt as if I had half expected it, and without
further words of reproach I dropped my head and gave it up.  I passed
again into the stupor of endurance.  The Vidame was too strong for me.
It was useless to fight against him.  We were under the spell.  When
the troop moved forward, I went with them, silent and apathetic. We passed through the gate of Cahors, and no doubt the scene was worthy
of note; but I had only a listless eye for it--much such an eye as a
man about to be broken on the wheel must have for that curious
instrument, supposing him never to have seen it before.  The whole
population had come out to line the streets through which we rode, and
stood gazing, with scarcely veiled looks of apprehension, at the
procession of troopers and the stern face of the new governor. We dismounted passively in the courtyard of the castle, and were for
going in together, when Bure intervened.  "M. de Pavannes," he said,
pushing rather rudely between us, "will sup alone to-night.  For you,
gentlemen, this way, if you please." I went without remonstrance.  What was the use?  I was conscious that
the Vidame from the top of the stairs leading to the grand entrance was
watching us with a wolfish glare in his eyes.  I went quietly.  But I
heard Croisette urging something with passionate energy. We were led through a low doorway to a room on the ground floor; a
place very like a cell.  Were we took our meal in silence. When it was
over I flung myself on one of the beds prepared for us, shrinking from
my companions rather in misery than in resentment. No explanation had passed between us.  Still I knew that the other two
from time to time eyed me doubtfully.  I feigned therefore to be
asleep, but I heard Bure enter to bid us good-night--and see that we
had not escaped.  And I was conscious too of the question Croisette put
to him, "Does M. de Pavannes lie alone to-night, Bure?" "Not entirely," the captain answered with gloomy meaning.  Indeed he
seemed in bad spirits himself, or tired.  "The Vidame is anxious for
his soul's welfare, and sends a priest to him." They sprang to their feet at that.  But the light and its bearer, who
so far recovered himself as to chuckle at his master's pious thought,
had disappeared.  They were left to pace the room, and reproach
themselves and curse the Vidame in an agony of late repentance.  Not
even Marie could find a loop-hole of escape from here.  The door was
double-locked; the windows so barred that a cat could scarcely pass
through them; the walls were of solid masonry. Meanwhile I lay and feigned to sleep, and lay feigning through long,
long hours; though my heart like theirs throbbed in response to the
dull hammering that presently began without, and not far from us, and
lasted until daybreak.  From our windows, set low and facing a wall, we
could see nothing.  But we could guess what the noise meant, the dull,
earthy thuds when posts were set in the ground, the brisk, wooden
clattering when one plank was laid to another.  We could not see the
progress of the work, or hear the voices of the workmen, or catch the
glare of their lights.  But we knew what they were doing.  They were
raising the scaffold.
```

### AI Extraction
- **Primary Mechanism**: `SOCIAL_EMBARRASSMENT` (Detector Confidence: `0.91`)
- **Secondary Dynamics**: STATUS_REVERSAL, CALLBACK
- **Linguistic Craft Score**: `0.90`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters About, All establish scene context: 'CHAPTER XI....'
- **Escalation**: Complication rises around social_embarrassment: '"I can only guess," Louis answered with a sigh....'
- **Reversal**: Expectation or status is inverted: 'Was it shame, or
fear, or some chivalrous feeling having its origin in that mome...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'They were
raising the scaffold....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 25 — `a_damsel_in_distress_ch1_05755`

**Source**: *A Damsel In Distress* (Chapter 1)  
**Characters Identified**: Ann, Aunt As, Aunt Finds, Aunt Has, Aunt Nesta, Aunt Wouldn, Celestine, Child, Jerry, Jerry Mitchell, Lord Wisbeach, Miss Ann, Mitchell, Mr Chester, Mr Crocker, Mr Ford, Mr Mcgraw, Mr Peter, Mr Pett, Mr Smethurst, Mr Smithers, Mrs Nesta, Mrs Pett, Nesta, Ogden, Peter, Pett, Uncle In, Uncle Peter  
**Dialogue Ratio**: `0.42` | **Surface Slang Isolated**: None  

### Passage
```text
CHAPTER I A RED-HAIRED GIRL The residence of Mr. Peter Pett, the well-known financier, on
Riverside Drive is one of the leading eyesores of that breezy and
expensive boulevard. As you pass by in your limousine, or while
enjoying ten cents worth of fresh air on top of a green omnibus,
it jumps out and bites at you. Architects, confronted with it,
reel and throw up their hands defensively, and even the lay
observer has a sense of shock. The place resembles in almost
equal proportions a cathedral, a suburban villa, a hotel and a
Chinese pagoda. Many of its windows are of stained glass, and
above the porch stand two terra-cotta lions, considerably more
repulsive even than the complacent animals which guard New York's
Public Library. It is a house which is impossible to overlook:
and it was probably for this reason that Mrs. Pett insisted on
her husband buying it, for she was a woman who liked to be
noticed. Through the rich interior of this mansion Mr. Pett, its nominal
proprietor, was wandering like a lost spirit. The hour was about
ten of a fine Sunday morning, but the Sabbath calm which was upon
the house had not communicated itself to him. There was a look of
exasperation on his usually patient face, and a muttered oath,
picked up no doubt on the godless Stock Exchange, escaped his
lips. "Darn it!" He was afflicted by a sense of the pathos of his position. It was
not as if he demanded much from life. He asked but little here
below. At that moment all that he wanted was a quiet spot where
he might read his Sunday paper in solitary peace, and he could
not find one. Intruders lurked behind every door. The place was
congested. This sort of thing had been growing worse and worse ever since
his marriage two years previously. There was a strong literary
virus in Mrs. Pett's system. She not only wrote voluminously
herself--the name Nesta Ford Pett is familiar to all lovers of
sensational fiction--but aimed at maintaining a salon. Starting,
in pursuance of this aim, with a single specimen,--her nephew,
Willie Partridge, who was working on a new explosive which would
eventually revolutionise war--she had gradually added to her
collections, until now she gave shelter beneath her terra-cotta
roof to no fewer than six young and unrecognised geniuses. Six
brilliant youths, mostly novelists who had not yet started and
poets who were about to begin, cluttered up Mr. Pett's rooms on
this fair June morning, while he, clutching his Sunday paper,
wandered about, finding, like the dove in Genesis, no rest. It
was at such times that he was almost inclined to envy his wife's
first husband, a business friend of his named Elmer Ford, who had
perished suddenly of an apoplectic seizure: and the pity which he
generally felt for the deceased tended to shift its focus. Marriage had certainly complicated life for Mr. Pett, as it
frequently does for the man who waits fifty years before trying
it. In addition to the geniuses, Mrs. Pett had brought with her
to her new home her only son, Ogden, a fourteen-year-old boy of a
singularly unloveable type. Years of grown-up society and the
absence of anything approaching discipline had given him a
precocity on which the earnest efforts of a series of private
tutors had expended themselves in vain. They came, full of
optimism and self-confidence, to retire after a brief interval,
shattered by the boy's stodgy resistance to education in any form
or shape. To Mr. Pett, never at his ease with boys, Ogden Ford
was a constant irritant. He disliked his stepson's personality,
and he more than suspected him of stealing his cigarettes. It
was an additional annoyance that he was fully aware of the
impossibility of ever catching him at it. Mr. Pett resumed his journey. He had interrupted it for a moment
to listen at the door of the morning-room, but, a remark in a
high tenor voice about the essential Christianity of the poet
Shelley filtering through the oak, he had moved on. Silence from behind another door farther down the passage
encouraged him to place his fingers on the handle, but a crashing
chord from an unseen piano made him remove them swiftly. He
roamed on, and a few minutes later the process of elimination had
brought him to what was technically his own private library--a
large, soothing room full of old books, of which his father had
been a great collector. Mr. Pett did not read old books himself,
but he liked to be among them, and it is proof of his pessimism
that he had not tried the library first. To his depressed mind it
had seemed hardly possible that there could be nobody there. He stood outside the door, listening tensely. He could hear
nothing. He went in, and for an instant experienced that ecstatic
thrill which only comes to elderly gentlemen of solitary habit
who in a house full of their juniors find themselves alone at
last. Then a voice spoke, shattering his dream of solitude. "Hello, pop!" Ogden Ford was sprawling in a deep chair in the shadows. "Come in, pop, come in. Lots of room." Mr. Pett stood in the doorway, regarding his step-son with a
sombre eye. He resented the boy's tone of easy patronage, all the
harder to endure with philosophic calm at the present moment from
the fact that the latter was lounging in his favourite chair.
Even from an aesthetic point of view the sight of the bulging
child offended him. Ogden Ford was round and blobby and looked
overfed. He had the plethoric habit of one to whom wholesome
exercise is a stranger and the sallow complexion of the confirmed
candy-fiend. Even now, a bare half hour after breakfast, his jaws
were moving with a rhythmical, champing motion. "What are you eating, boy?" demanded Mr. Pett, his disappointment
turning to irritability. "Candy." "I wish you would not eat candy all day." "Mother gave it to me," said Ogden simply. As he had anticipated,
the shot silenced the enemy's battery. Mr. Pett grunted, but made
no verbal comment. Ogden celebrated his victory by putting
another piece of candy in his mouth. "Got a grouch this morning, haven't you, pop?" "I will not be spoken to like that!" "I thought you had," said his step-son complacently. "I can
always tell. I don't see why you want to come picking on me,
though. I've done nothing." Mr. Pett was sniffing suspiciously. "You've been smoking." "Me!!" "Smoking cigarettes." "No, sir!" "There are two butts in the ash-tray." "I didn't put them there." "One of them is warm." "It's a warm day." "You dropped it there when you heard me come in." "No, sir! I've only been here a few minutes. I guess one of the
fellows was in here before me. They're always swiping your
coffin-nails. You ought to do something about it, pop. You ought
to assert yourself." A sense of helplessness came upon Mr. Pett. For the thousandth
time he felt himself baffled by this calm, goggle-eyed boy who
treated him with such supercilious coolness. "You ought to be out in the open air this lovely morning," he
said feebly. "All right. Let's go for a walk. I will if you will." "I--I have other things to do," said Mr. Pett, recoiling from the
prospect. "Well, this fresh-air stuff is overrated anyway. Where's the
sense of having a home if you don't stop in it?" "When I was your age, I would have been out on a morning like
this--er--bowling my hoop." "And look at you now!" "What do you mean?" "Martyr to lumbago." "I am not a martyr to lumbago," said Mr. Pett, who was touchy on
the subject. "Have it your own way. All I know is--" "Never mind!" "I'm only saying what mother . . ." "Be quiet!" Ogden made further researches in the candy box. "Have some, pop?" "No." "Quite right. Got to be careful at your age." "What do you mean?" "Getting on, you know. Not so young as you used to be. Come in,
pop, if you're coming in. There's a draft from that door." Mr. Pett retired, fermenting. He wondered how another man would
have handled this situation. The ridiculous inconsistency of the
human character infuriated him. Why should he be a totally
different man on Riverside Drive from the person he was in Pine
Street? Why should he be able to hold his own in Pine Street with
grown men--whiskered, square-jawed financiers--and yet be unable
on Riverside Drive to eject a fourteen-year-old boy from an easy
chair? It seemed to him sometimes that a curious paralysis of the
will came over him out of business hours. Meanwhile, he had still to find a place where he could read his
Sunday paper. He stood for a while in thought. Then his brow cleared, and he
began to mount the stairs. Reaching the top floor, he walked
along the passage and knocked on a door at the end of it. From
behind this door, as from behind those below, sounds proceeded,
but this time they did not seem to discourage Mr. Pett. It was
the tapping of a typewriter that he heard, and he listened to it
with an air of benevolent approval. He loved to hear the sound of
a typewriter: it made home so like the office. "Come in," called a girl's voice. The room in which Mr. Pett found himself was small but cosy, and
its cosiness--oddly, considering the sex of its owner--had that
peculiar quality which belongs as a rule to the dens of men. A
large bookcase almost covered one side of it, its reds and blues
and browns smiling cheerfully at whoever entered. The walls were
hung with prints, judiciously chosen and arranged. Through a
window to the left, healthfully open at the bottom, the sun
streamed in, bringing with it the pleasantly subdued whirring of
automobiles out on the Drive. At a desk at right angles to this
window, her vivid red-gold hair rippling in the breeze from the
river, sat the girl who had been working at the typewriter. She
turned as Mr. Pett entered, and smiled over her shoulder. Ann Chester, Mr. Pett's niece, looked her best when she smiled.
Although her hair was the most obviously striking feature of her
appearance, her mouth was really the most individual thing about
her. It was a mouth that suggested adventurous possibilities. In
repose, it had a look of having just finished saying something
humorous, a kind of demure appreciation of itself. When it
smiled, a row of white teeth flashed out: or, if the lips did not
part, a dimple appeared on the right cheek, giving the whole face
an air of mischievous geniality. It was an enterprising,
swashbuckling sort of mouth, the mouth of one who would lead
forlorn hopes with a jest or plot whimsically lawless
conspiracies against convention. In its corners and in the firm
line of the chin beneath it there lurked, too, more than a hint
of imperiousness. A physiognomist would have gathered, correctly,
that Ann Chester liked having her own way and was accustomed to
get it. "Hello, uncle Peter," she said. "What's the trouble?" "Am I interrupting you, Ann?" "Not a bit. I'm only copying out a story for aunt Nesta. I
promised her I would. Would you like to hear some of it?" Mr. Pett said he would not. "You're missing a good thing," said Ann, turning the pages. "I'm
all worked up over it. It's called 'At Dead of Night,' and it's
full of crime and everything. You would never think aunt Nesta
had such a feverish imagination. There are detectives and
kidnappers in it and all sorts of luxuries. I suppose it's the
effect of reading it, but you look to me as if you were trailing
something. You've got a sort of purposeful air." Mr. Pett's amiable face writhed into what was intended to be a
bitter smile. "I'm only trailing a quiet place to read in. I never saw such a
place as this house. It looks big enough outside for a regiment.
Yet, when you're inside, there's a poet or something in every
room." "What about the library? Isn't that sacred to you?" "The boy Ogden's there." "What a shame!" "Wallowing in my best chair," said Mr. Pett morosely. "Smoking
cigarettes." "Smoking? I thought he had promised aunt Nesta he wouldn't smoke." "Well, he said he wasn't, of course, but I know he had been. I
don't know what to do with that boy. It's no good my talking to
him. He--he patronises me!" concluded Mr. Pett indignantly.
"Sits there on his shoulder blades with his feet on the table
and talks to me with his mouth full of candy as if I were his
grandson." "Little brute." Ann was sorry for Mr. Pett. For many years now, ever since the
death of her mother, they had been inseparable. Her father, who
was a traveller, explorer, big-game hunter, and general sojourner
in the lonelier and wilder spots of the world and paid only
infrequent visits to New York, had left her almost entirely in
Mr. Pett's care, and all her pleasantest memories were associated
with him. Mr. Chester's was in many ways an admirable character,
but not a domestic one; and his relations with his daughter were
confined for the most part to letters and presents. In the past
few years she had come almost to regard Mr. Pett in the light of
a father. Hers was a nature swiftly responsive to kindness; and
because Mr. Pett besides being kind was also pathetic she pitied
as well as loved him. There was a lingering boyishness in the
financier, the boyishness of the boy who muddles along in an
unsympathetic world and can never do anything right: and this
quality called aloud to the youth in her. She was at the valiant
age when we burn to right wrongs and succour the oppressed, and
wild rebel schemes for the reformation of her small world came
readily to her. From the first she had been a smouldering
spectator of the trials of her uncle's married life, and if Mr.
Pett had ever asked her advice and bound himself to act on it he
would have solved his domestic troubles in explosive fashion. For
Ann in her moments of maiden meditation had frequently devised
schemes to that end which would have made his grey hair stand
erect with horror. "I've seen a good many boys," she said, "but Ogden is in a class
by himself. He ought to be sent to a strict boarding-school, of
course." "He ought to be sent to Sing-Sing," amended Mr. Pett. "Why don't you send him to school?" "Your aunt wouldn't hear of it. She's afraid of his being
kidnapped. It happened last time he went to school. You can't
blame her for wanting to keep her eye on him after that." Ann ran her fingers meditatively over the keys. "I've sometimes thought . . ." "Yes?" "Oh, nothing. I must get on with this thing for aunt Nesta." Mr. Pett placed the bulk of the Sunday paper on the floor beside
him, and began to run an appreciative eye over the comic
supplement. That lingering boyishness in him which endeared him
to Ann always led him to open his Sabbath reading in this
fashion. Grey-headed though he was, he still retained both in art
and in real life a taste for the slapstick. No one had ever known
the pure pleasure it had given him when Raymond Green, his wife's
novelist protege, had tripped over a loose stair-rod one morning
and fallen an entire flight. From some point farther down the corridor came a muffled
thudding. Ann stopped her work to listen. "There's Jerry Mitchell punching the bag." "Eh?" said Mr. Pett. "I only said I could hear Jerry Mitchell in the gymnasium." "Yes, he's there." Ann looked out of the window thoughtfully for a moment. Then she
swung round in her swivel-chair. "Uncle Peter." Mr. Pett emerged slowly from the comic supplement. "Eh?" "Did Jerry Mitchell ever tell you about that friend of his who
keeps a dogs' hospital down on Long Island somewhere? I forget
his name. Smithers or Smethurst or something. People--old ladies,
you know, and people--bring him their dogs to be cured when they
get sick. He has an infallible remedy, Jerry tells me. He makes a
lot of money at it." "Money?" Pett, the student, became Pett, the financier, at the
magic word. "There might be something in that if one got behind
it. Dogs are fashionable. There would be a market for a really
good medicine." "I'm afraid you couldn't put Mr. Smethurst's remedy on the
market. It only works when the dog has been overeating himself
and not taking any exercise." "Well, that's all these fancy dogs ever have the matter with
them. It looks to me as if I might do business with this man.
I'll get his address from Mitchell." "It's no use thinking of it, uncle Peter. You couldn't do
business with him--in that way. All Mr. Smethurst does when any
one brings him a fat, unhealthy dog is to feed it next to
nothing--just the simplest kind of food, you know--and make it
run about a lot. And in about a week the dog's as well and happy
and nice as he can possibly be." "Oh," said Mr. Pett, disappointed. Ann touched the keys of her machine softly. "Why I mentioned Mr. Smethurst," she said, "it was because we had
been talking of Ogden. Don't you think his treatment would be
just what Ogden needs?" Mr. Pett's eyes gleamed. "It's a shame he can't have a week or two of it!" Ann played a little tune with her finger-tips on the desk. "It would do him good, wouldn't it?" Silence fell upon the room, broken only by the tapping of the
typewriter. Mr. Pett, having finished the comic supplement,
turned to the sporting section, for he was a baseball fan of no
lukewarm order. The claims of business did not permit him to see
as many games as he could wish, but he followed the national
pastime closely on the printed page and had an admiration for the
Napoleonic gifts of Mr. McGraw which would have gratified that
gentleman had he known of it. "Uncle Peter," said Ann, turning round again. "Eh?" "It's funny you should have been talking about Ogden getting
kidnapped. This story of aunt Nesta's is all about an
angel-child--I suppose it's meant to be Ogden--being stolen and
hidden and all that. It's odd that she should write stories like
this. You wouldn't expect it of her." "Your aunt," said Mr. Pett, "lets her mind run on that sort of
thing a good deal. She tells me there was a time, not so long
ago, when half the kidnappers in America were after him. She sent
him to school in England--or, rather, her husband did. They were
separated then--and, as far as I can follow the story, they all
took the next boat and besieged the place." "It's a pity somebody doesn't smuggle him away now and keep him
till he's a better boy." "Ah!" said Mr. Pett wistfully. Ann looked at him fixedly, but his eyes were once more on his
paper. She gave a little sigh, and turned to her work again. "It's quite demoralising, typing aunt Nesta's stories," she said.
"They put ideas into one's head." Mr. Pett said nothing. He was reading an article of medical
interest in the magazine section, for he was a man who ploughed
steadily through his Sunday paper, omitting nothing. The
typewriter began tapping again. "Great Godfrey!" Ann swung round, and gazed at her uncle in concern. He was
staring blankly at the paper. "What's the matter?" The page on which Mr. Pett's attention was concentrated was
decorated with a fanciful picture in bold lines of a young man in
evening dress pursuing a young woman similarly clad along what
appeared to be a restaurant supper-table. An enjoyable time was
apparently being had by both. Across the page this legend ran: PICCADILLY JIM ONCE MORE The Recent Adventures of Young Mr. Crocker of New York and London It was not upon the title, however, nor upon the illustration
that Mr. Pett's fascinated eye rested. What he was looking at was
a small reproduction of a photograph which had been inserted in
the body of the article. It was the photograph of a woman in the
early forties, rather formidably handsome, beneath which were
printed the words: Mrs. Nesta Ford Pett Well-Known Society Leader and Authoress Ann had risen and was peering over his shoulder. She frowned as
she caught sight of the heading of the page. Then her eye fell
upon the photograph. "Good gracious! Why have they got aunt Nesta's picture there?" Mr. Pett breathed a deep and gloomy breath. "They've found out she's his aunt. I was afraid they would. I
don't know what she will say when she sees this." "Don't let her see it." "She has the paper downstairs. She's probably reading it now." Ann was glancing through the article. "It seems to be much the same sort of thing that they have
published before. I can't understand why the _Chronicle_ takes such
an interest in Jimmy Crocker." "Well, you see he used to be a newspaper man, and the _Chronicle_
was the paper he worked for." Ann flushed. "I know," she said shortly. Something in her tone arrested Mr. Pett's attention. "Yes, yes, of course," he said hastily. "I was forgetting." There was an awkward silence. Mr. Pett coughed. The matter of
young Mr. Crocker's erstwhile connection with the New York
_Chronicle_ was one which they had tacitly decided to refrain from
mentioning. "I didn't know he was your nephew, uncle Peter." "Nephew by marriage," corrected Mr. Pett a little hurriedly.
"Nesta's sister Eugenia married his father." "I suppose that makes me a sort of cousin." "A distant cousin." "It can't be too distant for me." There was a sound of hurried footsteps outside the door. Mrs.
Pett entered, holding a paper in her hand. She waved it before
Mr. Pett's sympathetic face. "I know, my dear," he said backing. "Ann and I were just talking
about it." The little photograph had not done Mrs. Pett justice. Seen
life-size, she was both handsomer and more formidable than she
appeared in reproduction. She was a large woman, with a fine
figure and bold and compelling eyes, and her personality crashed
disturbingly into the quiet atmosphere of the room. She was the
type of woman whom small, diffident men seem to marry
instinctively, as unable to help themselves as cockleshell boats
sucked into a maelstrom. "What are you going to do about it?" she demanded, sinking
heavily into the chair which her husband had vacated. This was an aspect of the matter which had not occurred to Mr.
Pett. He had not contemplated the possibility of actually doing
anything. Nature had made him out of office hours essentially a
passive organism, and it was his tendency, when he found himself
in a sea of troubles, to float plaintively, not to take arms
against it. To pick up the slings and arrows of outrageous
fortune and fling them back was not a habit of his. He scratched
his chin and said nothing. He went on saying nothing. "If Eugenia had had any sense, she would have foreseen what would
happen if she took the boy away from New York where he was
working too hard to get into mischief and let him run loose in
London with too much money and nothing to do. But, if she had had
any sense, she would never have married that impossible Crocker
man. As I told her." Mrs. Pett paused, and her eyes glowed with reminiscent fire. She
was recalling the scene which had taken place three years ago
between her sister and herself, when Eugenia had told her of her
intention to marry an obscure and middle-aged actor named Bingley
Crocker. Mrs. Pett had never seen Bingley Crocker, but she had
condemned the proposed match in terms which had ended definitely
and forever her relations with her sister. Eugenia was not a
woman who welcomed criticism of her actions. She was cast in the
same formidable mould as Mrs. Pett and resembled her strikingly
both in appearance and character. Mrs. Pett returned to the present. The past could look after
itself. The present demanded surgery. "One would have thought it would have been obvious even to
Eugenia that a boy of twenty-one needed regular work." Mr. Pett was glad to come out of his shell here. He was the
Apostle of Work, and this sentiment pleased him. "That's right," he said. "Every boy ought to have work." "Look at this young Crocker's record since he went to live in
London. He is always doing something to make himself notorious.
There was that breach-of-promise case, and that fight at the
political meeting, and his escapades at Monte Carlo, and--and
everything. And he must be drinking himself to death. I think
Eugenia's insane. She seems to have no influence over him at
all." Mr. Pett moaned sympathetically. "And now the papers have found out that I am his aunt, and I
suppose they will print my photograph whenever they publish an
article about him." She ceased and sat rigid with just wrath. Mr. Pett, who always
felt his responsibilities as chorus keenly during these wifely
monologues, surmised that a remark from him was indicated. "It's tough," he said. Mrs. Pett turned on him like a wounded tigress. "What is the use of saying that? It's no use saying anything." "No, no," said Mr. Pett, prudently refraining from pointing out
that she had already said a good deal. "You must do something." Ann entered the conversation for the first time. She was not very
fond of her aunt, and liked her least when she was bullying Mr.
Pett. There was something in Mrs. Pett's character with which the
imperiousness which lay beneath Ann's cheerful attitude towards
the world was ever at war. "What can uncle Peter possibly do?" she inquired. "Why, get the boy back to America and make him work. It's the
only possible thing." "But is it possible?" "Of course it is." "Assuming that Jimmy Crocker would accept an invitation to come
over to America, what sort of work could he do here? He couldn't
get his place on the _Chronicle_ back again after dropping out for
all these years and making a public pest of himself all that
while. And outside of newspaper work what is he fit for?" "My dear child, don't make difficulties." "I'm not. These are ready-made." Mr. Pett interposed. He was always nervously apprehensive of a
clash between these two. Ann had red hair and the nature which
generally goes with red hair. She was impulsive and quick of
tongue, and--as he remembered her father had always been--a
little too ready for combat. She was usually as quickly
remorseful as she was quickly pugnacious, like most persons of
her colour. Her offer to type the story which now lay on her desk
had been the amende honourable following on just such a scene
with her aunt as this promised to be. Mr. Pett had no wish to see
the truce thus consummated broken almost before it had had time
to operate. "I could give the boy a job in my office," he suggested. Giving young men jobs in his office was what Mr. Pett liked doing
best. There were six brilliant youths living in his house and
bursting with his food at that very moment whom he would have
been delighted to start addressing envelopes down-town. Notably his wife's nephew, Willie Partridge, whom he looked on as
a specious loafer. He had a stubborn disbelief in the explosive
that was to revolutionise war. He knew, as all the world did,
that Willie's late father had been a great inventor, but he did
not accept the fact that Willie had inherited the dead man's
genius. He regarded the experiments on Partridgite, as it was to
be called, with the profoundest scepticism, and considered that
the only thing Willie had ever invented or was likely to invent
was a series of ingenious schemes for living in fatted idleness
on other people's money. "Exactly," said Mrs. Pett, delighted at the suggestion. "The very
thing." "Will you write and suggest it?" said Mr. Pett, basking in the
sunshine of unwonted commendation. "What would be the use of writing? Eugenia would pay no
attention. Besides, I could not say all I wished to in a letter.
No, the only thing is to go over to England and see her. I shall
speak very plainly to her. I shall point out what an advantage it
will be to the boy to be in your office and to live here. . . ." Ann started. "You don't mean live here--in this house?" "Of course. There would be no sense in bringing the boy all the
way over from England if he was to be allowed to run loose when
he got here." Mr. Pett coughed deprecatingly. "I don't think that would be very pleasant for Ann, dear." "Why in the name of goodness should Ann object?" Ann moved towards the door. "Thank you for thinking of it, uncle Peter. You're always a dear.
But don't worry about me. Do just as you want to. In any case I'm
quite certain that you won't be able to get him to come over
here. You can see by the paper he's having far too good a time in
London. You can call Jimmy Crockers from the vasty deep, but will
they come when you call for them?" Mrs. Pett looked at the door as it closed behind her, then at her
husband. "What do you mean, Peter, about Ann? Why wouldn't it be pleasant
for her if this Crocker boy came to live with us?" Mr. Pett hesitated. "Well, it's like this, Nesta. I hope you won't tell her I told
you. She's sensitive about it, poor girl. It all happened before
you and I were married. Ann was much younger then. You know what
schoolgirls are, kind of foolish and sentimental. It was my fault
really, I ought to have . . ." "Good Heavens, Peter! What are you trying to tell me?" "She was only a child." Mrs. Pett rose in slow horror. "Peter! Tell me! Don't try to break it gently." "Ann wrote a book of poetry and I had it published for her." Mrs. Pett sank back in her chair. "Oh!" she said--it would have been hard to say whether with
relief or disappointment. "Whatever did you make such a fuss for?
Why did you want to be so mysterious?" "It was all my fault, really," proceeded Mr. Pett. "I ought to
have known better. All I thought of at the time was that it would
please the child to see the poems in print and be able to give
the book to her friends. She did give it to her friends," he went
on ruefully, "and ever since she's been trying to live it down.
I've seen her bite a young fellow's head off when he tried to
make a grand-stand play with her by quoting her poems which he'd
found in his sister's book-shelf." "But, in the name of goodness, what has all this to do with young
Crocker?" "Why, it was this way. Most of the papers just gave Ann's book a
mention among 'Volumes Received,' or a couple of lines that
didn't amount to anything, but the _Chronicle_ saw a Sunday feature
in it, as Ann was going about a lot then and was a well-known
society girl. They sent this Crocker boy to get an interview from
her, all about her methods of work and inspirations and what not.
We never suspected it wasn't the straight goods. Why, that very
evening I mailed an order for a hundred copies to be sent to me
when the thing appeared. And--" pinkness came upon Mr. Pett at
the recollection "it was just a josh from start to finish. The
young hound made a joke of the poems and what Ann had told him
about her inspirations and quoted bits of the poems just to kid
the life out of them. . . . I thought Ann would never get over
it. Well, it doesn't worry her any more--she's grown out of the
school-girl stage--but you can bet she isn't going to get up and
give three cheers and a tiger if you bring young Crocker to live
in the same house." "Utterly ridiculous!" said Mrs. Pett. "I certainly do not intend
to alter my plans because of a trivial incident that happened
years ago. We will sail on Wednesday." "Very well, my dear," said Mr. Pett resignedly. "Just as you say. Er--just you and I?" "And Ogden, of course." Mr. Pett controlled a facial spasm with a powerful effort of the
will. He had feared this. "I wouldn't dream of leaving him here while I went away, after
what happened when poor dear Elmer sent him to school in England
that time." The late Mr. Ford had spent most of his married life
either quarrelling with or separated from his wife, but since
death he had been canonised as 'poor dear Elmer.' "Besides, the
sea voyage will do the poor darling good. He has not been looking
at all well lately." "If Ogden's coming, I'd like to take Ann." "Why?" "She can--" he sought for a euphemism. "Keep in order" was the expression he wished to avoid. To his
mind Ann was the only known antidote for Ogden, but he felt it
would be impolitic to say so."--look after him on the boat," he
concluded. "You know you are a bad sailor." "Very well. Bring Ann--Oh, Peter, that reminds me of what I
wanted to say to you, which this dreadful thing in the paper
drove completely out of my mind. Lord Wisbeach has asked Ann to
marry him!" Mr. Pett looked a little hurt. "She didn't tell me." Ann usually
confided in him. "She didn't tell me, either. Lord Wisbeach told me. He said Ann
had promised to think it over, and give him his answer later.
Meanwhile, he had come to me to assure himself that I approved. I
thought that so charming of him." Mr. Pett was frowning. "She hasn't accepted him?" "Not definitely." "I hope she doesn't." "Don't be foolish, Peter. It would be an excellent match." Mr. Pett shuffled his feet. "I don't like him. There's something too darned smooth about that
fellow." "If you mean that his manners are perfect, I agree with you. I
shall do all in my power to induce Ann to accept him." "I shouldn't," said Mr. Pett, with more decision than was his
wont. "You know what Ann is if you try to force her to do
anything. She gets her ears back and won't budge. Her father is
just the same. When we were boys together, sometimes--" "Don't be absurd, Peter. As if I should dream of trying to force
Ann to do anything." "We don't know anything of this fellow. Two weeks ago we didn't
know he was on the earth." "What do we need to know beyond his name?" Mr. Pett said nothing, but he was not convinced. The Lord
Wisbeach under discussion was a pleasant-spoken and presentable
young man who had called at Mr. Pett's office a short while
before to consult him about investing some money. He had brought
a letter of introduction from Hammond Chester, Ann's father, whom
he had met in Canada, where the latter was at present engaged in
the comparatively mild occupation of bass-fishing. With their
business talk the acquaintance would have begun and finished, if
Mr. Pett had been able to please himself, for he had not taken a
fancy to Lord Wisbeach. But he was an American, with an
American's sense of hospitality, and, the young man being a
friend of Hammond Chester, he had felt bound to invite him to
Riverside Drive--with misgivings which were now, he felt,
completely justified. "Ann ought to marry," said Mrs. Pett. "She gets her own way too
much now. However, it is entirely her own affair, and there is
nothing that we can do." She rose. "I only hope she will be
sensible." She went out, leaving Mr. Pett gloomier than she had found him.
He hated the idea of Ann marrying Lord Wisbeach, who, even if he
had had no faults at all, would be objectionable in that he would
probably take her to live three thousand miles away in his own
country. The thought of losing Ann oppressed Mr. Pett sorely. Ann, meanwhile, had made her way down the passage to the gymnasium
which Mr. Pett, in the interests of his health, had caused to be
constructed in a large room at the end of the house--a room designed
by the original owner, who had had artistic leanings, for a studio.
The _tap-tap-tap_ of the leather bag had ceased, but voices from
within told her that Jerry Mitchell, Mr. Pett's private physical
instructor, was still there. She wondered who was his companion, and
found on opening the door that it was Ogden. The boy was leaning
against the wall and regarding Jerry with a dull and supercilious
gaze which the latter was plainly finding it hard to bear. "Yes, sir!" Ogden was saying, as Ann entered. "I heard Biggs
asking her to come for a joyride." "I bet she turned him down," said Jerry Mitchell sullenly. "I bet she didn't. Why should she? Biggs is an awful good-looking
fellow." "What are you talking about, Ogden?" said Ann. "I was telling him that Biggs asked Celestine to go for a ride in
the car with him." "I'll knock his block off," muttered the incensed Jerry. Ogden laughed derisively. "Yes, you will! Mother would fire you if you touched him. She
wouldn't stand for having her chauffeur beaten up." Jerry Mitchell turned an appealing face to Ann. Ogden's
revelations and especially his eulogy of Biggs' personal
appearance had tormented him. He knew that, in his wooing of Mrs.
Pett's maid, Celestine, he was handicapped by his looks,
concerning which he had no illusions. No Adonis to begin with, he
had been so edited and re-edited during a long and prosperous
ring career by the gloved fists of a hundred foes that in affairs
of the heart he was obliged to rely exclusively on moral worth
and charm of manner. He belonged to the old school of fighters
who looked the part, and in these days of pugilists who resemble
matinee idols he had the appearance of an anachronism. He was a
stocky man with a round, solid head, small eyes, an undershot
jaw, and a nose which ill-treatment had reduced to a mere
scenario. A narrow strip of forehead acted as a kind of
buffer-state, separating his front hair from his eyebrows, and he
bore beyond hope of concealment the badge of his late employment,
the cauliflower ear. Yet was he a man of worth and a good
citizen, and Ann had liked him from their first meeting. As for
Jerry, he worshipped Ann and would have done anything she asked
him. Ever since he had discovered that Ann was willing to listen
to and sympathise with his outpourings on the subject of his
troubled wooing, he had been her slave. Ann came to the rescue in characteristically direct fashion. "Get out, Ogden," she said. Ogden tried to meet her eye mutinously, but failed. Why he should
be afraid of Ann he had never been able to understand, but it was
a fact that she was the only person of his acquaintance whom he
respected. She had a bright eye and a calm, imperious stare which
never failed to tame him. "Why?" he muttered. "You're not my boss." "Be quick, Ogden." "What's the big idea--ordering a fellow--" "And close the door gently behind you," said Ann. She turned to
Jerry, as the order was obeyed. "Has he been bothering you, Jerry?" Jerry Mitchell wiped his forehead. "Say, if that kid don't quit butting in when I'm working in the
gym--You heard what he was saying about Maggie, Miss Ann?" Celestine had been born Maggie O'Toole, a name which Mrs. Pett
stoutly refused to countenance in any maid of hers. "Why on earth do you pay any attention to him, Jerry? You must
have seen that he was making it all up. He spends his whole time
wandering about till he finds some one he can torment, and then
he enjoys himself. Maggie would never dream of going out in the
car with Biggs." Jerry Mitchell sighed a sigh of relief. "It's great for a fellow to have you in his corner, Miss Ann." Ann went to the door and opened it. She looked down the passage,
then, satisfied as to its emptiness, returned to her seat. "Jerry, I want to talk to you. I have an idea. Something I want
you to do for me." "Yes, Miss Ann?" "We've got to do something about that child, Ogden. He's been
worrying uncle Peter again, and I'm not going to have it. I
warned him once that, if he did it again, awful things would
happen to him, but he didn't believe me. I suppose, Jerry--what
sort of a man is your friend, Mr. Smethurst?" "Do you mean Smithers, Miss Ann?" "I knew it was either Smithers or Smethurst. The dog man, I mean.
Is he a man you can trust?" "With my last buck. I've known him since we were kids." "I don't mean as regards money. I am going to send Ogden to him
for treatment, and I want to know if I can rely on him to help
me." "For the love of Mike." Jerry Mitchell, after an instant of stunned bewilderment, was
looking at her with worshipping admiration. He had always known
that Miss Ann possessed a mind of no common order, but this, he
felt, was genius. For a moment the magnificence of the idea took
his breath away. "Do you mean that you're going to kidnap him, Miss Ann?" "Yes. That is to say, _you_ are--if I can persuade you to do
it for me." "Sneak him away and send him to Bud Smithers' dog-hospital?" "For treatment. I like Mr. Smithers' methods. I think they would
do Ogden all the good in the world." Jerry was enthusiastic. "Why, Bud would make him part-human. But, say, isn't it taking
big chances? Kidnapping's a penitentiary offence." "This isn't that sort of kidnapping." "Well, it's mighty like it." "I don't think you need be afraid of the penitentiary. I can't
see aunt Nesta prosecuting, when it would mean that she would
have to charge us with having sent Ogden to a dogs' hospital. She
likes publicity, but it has to be the right kind of publicity.
No, we do run a risk, but it isn't that one. You run the risk of
losing your job here, and I should certainly be sent to my
grandmother for an indefinite sentence. You've never seen my
grandmother, have you, Jerry? She's the only person in the world
I'm afraid of! She lives miles from anywhere and has family
prayers at seven-thirty sharp every morning. Well, I'm ready to
risk her, if you're ready to risk your job, in such a good cause.
You know you're just as fond of uncle Peter as I am, and Ogden is
worrying him into a breakdown. Surely you won't refuse to help
me, Jerry?" Jerry rose and extended a calloused hand. "When do we start?" Ann shook the hand warmly. "Thank you, Jerry. You're a jewel. I envy Maggie. Well, I don't
think we can do anything till they come back from England, as
aunt Nesta is sure to take Ogden with her." "Who's going to England?" "Uncle Peter and aunt Nesta were talking just now of sailing to
try and persuade a young man named Crocker to come back here." "Crocker? Jimmy Crocker? Piccadilly Jim?" "Yes. Why, do you know him?" "I used to meet him sometimes when he was working on the
_Chronicle_ here. Looks as if he was cutting a wide swathe in dear
old London. Did you see the paper to-day?" "Yes, that's what made aunt Nesta want to bring him over. Of
course, there isn't the remotest chance that she will be able to
make him come. Why should he come?" "Last time I saw Jimmy Crocker," said Jerry, "it was a couple of
years ago, when I went over to train Eddie Flynn for his go with
Porky Jones at the National. I bumped into him at the N. S. C. He
was a good deal tanked." "He's always drinking, I believe." "He took me to supper at some swell joint where they all had the
soup-and-fish on but me. I felt like a dirty deuce in a clean
deck. He used to be a regular fellow, Jimmy Crocker, but from
what you read in the papers it begins to look as if he was
hitting it up too swift. It's always the way with those boys when
you take them off a steady job and let them run around loose with
their jeans full of mazuma." "That's exactly why I want to do something about Ogden. If he's
allowed to go on as he is at present, he will grow up exactly
like Jimmy Crocker." "Aw, Jimmy Crocker ain't in Ogden's class," protested Jerry. "Yes, he is. There's absolutely no difference between them." "Say! You've got it in for Jim, haven't you, Miss Ann?" Jerry
looked at her wonderingly. "What's your kick against him?" Ann bit her lip. "I object to him on principle," she said. "I
don't like his type. . . . Well, I'm glad we've settled this
about Ogden, Jerry. I knew I could rely on you. But I won't let
you do it for nothing. Uncle Peter shall give you something for
it--enough to start that health-farm you talk about so much.
Then you can marry Maggie and live happily ever afterwards." "Gee! Is the boss in on this, too?" "Not yet. I'm going to tell him now. Hush! There's some one
coming." Mr. Pett wandered in. He was still looking troubled. "Oh, Ann--good morning, Mitchell--your aunt has decided to go to
England. I want you to come, too." "You want me? To help interview Jimmy Crocker?" "No, no. Just to come along and be company on the voyage. You'll
be such a help with Ogden, Ann. You can keep him in order. How
you do it, I don't know. You seem to make another boy of him." Ann stole a glance at Jerry, who answered with an encouraging
grin. Ann was constrained to make her meaning plainer than by the
language of the eye. "Would you mind just running away for half a moment, Jerry?" she
said winningly. "I want to say something to uncle Peter." "Sure. Sure." Ann turned to Mr. Pett as the door closed. "You'd like somebody to make Ogden a different boy, wouldn't you,
uncle Peter?" "I wish it was possible." "He's been worrying you a lot lately, hasn't he?" asked Ann
sympathetically. "Yes," sighed Mr. Pett. "Then that's all right," said Ann briskly. "I was afraid that you
might not approve. But, if you do, I'll go right ahead." Mr. Pett started violently. There was something in Ann's voice
and, as he looked at her, something in her face which made him
fear the worst. Her eyes were flashing with an inspired light of
a highly belligerent nature, and the sun turned the red hair to
which she owed her deplorable want of balance to a mass of flame.
There was something in the air. Mr. Pett sensed it with every
nerve of his apprehensive person. He gazed at Ann, and as he did
so the years seemed to slip from him and he was a boy again,
about to be urged to lawless courses by the superior will of his
boyhood's hero, Hammond Chester. In the boyhood of nearly every
man there is a single outstanding figure, some one youthful
hypnotic Napoleon whose will was law and at whose bidding his
better judgment curled up and died. In Mr. Pett's life Ann's
father had filled this role. He had dominated Mr. Pett at an age
when the mind is most malleable. And now--so true is it that
though Time may blunt our boyish memories the traditions of
boyhood live on in us and an emotional crisis will bring them to
the surface as an explosion brings up the fish that lurk in the
nethermost mud--it was as if he were facing the youthful Hammond
Chester again and being irresistibly impelled to some course of
which he entirely disapproved but which he knew that he was
destined to undertake. He watched Ann as a trapped man might
watch a ticking bomb, bracing himself for the explosion and
knowing that he is helpless. She was Hammond Chester's daughter,
and she spoke to him with the voice of Hammond Chester. She was
her father's child and she was going to start something. "I've arranged it all with Jerry," said Ann. "He's going to help
me smuggle Ogden away to that friend of his I told you about who
keeps the dog-hospital: and the friend is going to keep him until
he reforms. Isn't it a perfectly splendid idea?" Mr. Pett blanched. The frightfulness of reality had exceeded
anticipation. "But, Ann!" The words came from him in a strangled bleat. His whole being was
paralysed by a clammy horror. This was beyond the uttermost limit
of his fears. And, to complete the terror of the moment, he knew,
even while he rebelled against the insane lawlessness of her
scheme, that he was going to agree to it, and--worst of all--that
deep, deep down in him there was a feeling toward it which did
not dare to come to the surface but which he knew to be approval. "Of course Jerry would do it for nothing," said Ann, "but I
promised him that you would give him something for his trouble.
You can arrange all that yourselves later." "But, Ann! . . . But, Ann! . . . Suppose your aunt finds out who
did it!" "Well, there will be a tremendous row!" said Ann composedly.
"And you will have to assert yourself. It will be a splendid
thing for you. You know you are much too kind to every one, uncle
Peter. I don't think there's any one who would put up with what
you do. Father told me in one of his letters that he used to call
you Patient Pete as a boy." Mr. Pett started. Not for many a day had a nickname which he
considered the most distasteful of all possible nicknames risen
up from its grave to haunt him. Patient Pete! He had thought the
repulsive title buried forever in the same tomb as his dead
youth. Patient Pete! The first faint glimmer of the flame of
rebellion began to burn in his bosom. "Patient Pete!" "Patient Pete!" said Ann inexorably. "But, Ann,"--there was pathos in Mr. Pett's voice--"I like a
peaceful life." "You'll never have one if you don't stand up for yourself. You
know quite well that father is right. You do let every one
trample on you. Do you think father would let Ogden worry him and
have his house filled with affected imitation geniuses so that he
couldn't find a room to be alone in?" "But, Ann, your father is different. He likes fusses. I've known
your father contradict a man weighing two hundred pounds out of
sheer exuberance. There's a lot of your father in you, Ann. I've
often noticed it." "There is! That's why I'm going to make you put your foot down
sooner or later. You're going to turn all these loafers out of
the house. And first of all you're going to help us send Ogden
away to Mr. Smithers." There was a long silence. "It's your red hair!" said Mr. Pett at length, with the air of a
man who has been solving a problem. "It's your red hair that
makes you like this, Ann. Your father has red hair, too." Ann laughed. "It's not my fault that I have red hair, uncle Peter. It's my
misfortune." Mr. Pett shook his head. "Other people's misfortune, too!" he said.
```

### AI Extraction
- **Primary Mechanism**: `SOCIAL_EMBARRASSMENT` (Detector Confidence: `0.69`)
- **Secondary Dynamics**: PHYSICAL_COMPLICATION, ESCALATION
- **Linguistic Craft Score**: `0.90`
- **Tone**: `LIGHT_SATIRICAL`
- **Setup**: Characters Ann, Aunt As establish scene context: 'CHAPTER I A RED-HAIRED GIRL The residence of Mr....'
- **Escalation**: Complication rises around social_embarrassment: 'Pett had ever asked her advice and bound himself to act on it he
would have solv...'
- **Reversal**: Expectation or status is inverted: 'These are ready-made." Mr....'
- **Payoff**: Comedic resolution or deadpan beat lands: '"Other people's misfortune, too!" he said....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 26 — `the_man_upstairs_ch37_02024`

**Source**: *The Man Upstairs* (Chapter 37)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.55` | **Surface Slang Isolated**: None  

### Passage
```text
"And the poor girl advanced a step toward the alchemist. He grew deathly pale, and staggered as if about to fall. The next instant, though, he recovered himself, and burst into a horrible sardonic laugh. Then he said, in tones full of the bitterest irony:," You'll forgive me, won't you? A conspiracy, is it? Well done, doctor! You think to reconcile me with this wretched girl by trumping up this story that I have been for two years a dupe of her filial piety.
```

### AI Extraction
- **Primary Mechanism**: `VERBAL_WIT` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DRY_WIT`
- **Setup**: Characters Narrator establish scene context: '"And the poor girl advanced a step toward the alchemist....'
- **Escalation**: Complication rises around verbal_wit: 'He grew deathly pale, and staggered as if about to fall....'
- **Reversal**: Expectation or status is inverted: 'Then he said, in tones full of the bitterest irony:," You'll forgive me, won't y...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'You think to reconcile me with this wretched girl by trumping up this story that...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 27 — `their_mutual_child_ch19_00178`

**Source**: *Their Mutual Child* (Chapter 19)  
**Characters Identified**: Lord Macaulay, Lord Robert, Mr Adams, Mr Boutwell, Mr Fish, Mr Mcculloch, Mrs Grant  
**Dialogue Ratio**: `0.01` | **Surface Slang Isolated**: None  

### Passage
```text
CHAPTER XVII PRESIDENT GRANT (1869) THE first effect of this leap into the unknown was a fit of low
spirits new to the young man's education; due in part to the
overpowering beauty and sweetness of the Maryland autumn, almost
unendurable for its strain on one who had toned his life down to the
November grays and browns of northern Europe. Life could not go on so
beautiful and so sad. Luckily, no one else felt it or knew it. He bore
it as well as he could, and when he picked himself up, winter had come,
and he was settled in bachelor's quarters, as modest as those of a
clerk in the Departments, far out on G Street, towards Georgetown,
where an old Finn named Dohna, who had come out with the Russian
Minister Stoeckel long before, had bought or built a new house.
Congress had met. Two or three months remained to the old
administration, but all interest centred in the new one. The town began
to swarm with office-seekers, among whom a young writer was lost. He
drifted among them, unnoticed, glad to learn his work under cover of
the confusion. He never aspired to become a regular reporter; he knew
he should fail in trying a career so ambitious and energetic; but he
picked up friends on the press--Nordhoff, Murat Halstead, Henry
Watterson, Sam Bowles--all reformers, and all mixed and jumbled
together in a tidal wave of expectation, waiting for General Grant to
give orders. No one seemed to know much about it. Even Senators had
nothing to say. One could only make notes and study finance. In waiting, he amused himself as he could. In the amusements of
Washington, education had no part, but the simplicity of the amusements
proved the simplicity of everything else, ambitions, interests,
thoughts, and knowledge. Proverbially Washington was a poor place for
education, and of course young diplomats avoided or disliked it, but,
as a rule, diplomats disliked every place except Paris, and the world
contained only one Paris. They abused London more violently than
Washington; they praised no post under the sun; and they were merely
describing three-fourths of their stations when they complained that
there were no theatres, no restaurants, no monde, no demi-monde, no
drives, no splendor, and, as Mme. de Struve used to say, no grandezza.
This was all true; Washington was a mere political camp, as transient
and temporary as a camp-meeting for religious revival, but the
diplomats had least reason to complain, since they were more sought for
there than they would ever be elsewhere. For young men Washington was
in one way paradise, since they were few, and greatly in demand. After
watching the abject unimportance of the young diplomat in London
society, Adams found himself a young duke in Washington. He had ten
years of youth to make up, and a ravenous appetite. Washington was the
easiest society he had ever seen, and even the Bostonian became simple,
good-natured, almost genial, in the softness of a Washington spring.
Society went on excellently well without houses, or carriages, or
jewels, or toilettes, or pavements, or shops, or grandezza of any sort;
and the market was excellent as well as cheap. One could not stay there
a month without loving the shabby town. Even the Washington girl, who
was neither rich nor well-dressed nor well-educated nor clever, had
singular charm, and used it. According to Mr. Adams the father, this
charm dated back as far as Monroe's administration, to his personal
knowledge. Therefore, behind all the processes of political or financial
or newspaper training, the social side of Washington was to be taken
for granted as three-fourths of existence. Its details matter nothing.
Life ceased to be strenuous, and the victim thanked God for it.
Politics and reform became the detail, and waltzing the profession.
Adams was not alone. Senator Sumner had as private secretary a young
man named Moorfield Storey, who became a dangerous example of
frivolity. The new Attorney-General, E. R. Hoar, brought with him from
Concord a son, Sam Hoar, whose example rivalled that of Storey. Another
impenitent was named Dewey, a young naval officer. Adams came far down
in the list. He wished he had been higher. He could have spared a world
of superannuated history, science, or politics, to have reversed better
in waltzing. He had no adequate notion how little he knew, especially of
women, and Washington offered no standard of comparison. All were
profoundly ignorant together, and as indifferent as children to
education. No one needed knowledge. Washington was happier without
style. Certainly Adams was happier without it; happier than he had ever
been before; happier than any one in the harsh world of strenuousness
could dream of. This must be taken as background for such little
education as he gained; but the life belonged to the eighteenth
century, and in no way concerned education for the twentieth. In such an atmosphere, one made no great pretence of hard work.
If the world wants hard work, the world must pay for it; and, if it
will not pay, it has no fault to find with the worker. Thus far, no one
had made a suggestion of pay for any work that Adams had done or could
do; if he worked at all, it was for social consideration, and social
pleasure was his pay. For this he was willing to go on working, as an
artist goes on painting when no one buys his pictures. Artists have
done it from the beginning of time, and will do it after time has
expired, since they cannot help themselves, and they find their return
in the pride of their social superiority as they feel it. Society
commonly abets them and encourages their attitude of contempt. The
society of Washington was too simple and Southern as yet, to feel
anarchistic longings, and it never read or saw what artists produced
elsewhere, but it good-naturedly abetted them when it had the chance,
and respected itself the more for the frailty. Adams found even the
Government at his service, and every one willing to answer his
questions. He worked, after a fashion; not very hard, but as much as
the Government would have required of him for nine hundred dollars a
year; and his work defied frivolity. He got more pleasure from writing
than the world ever got from reading him, for his work was not amusing,
nor was he. One must not try to amuse moneylenders or investors, and
this was the class to which he began by appealing. He gave three months
to an article on the finances of the United States, just then a subject
greatly needing treatment; and when he had finished it, he sent it to
London to his friend Henry Reeve, the ponderous editor of the Edinburgh
Review. Reeve probably thought it good; at all events, he said so; and
he printed it in April. Of course it was reprinted in America, but in
England such articles were still anonymous, and the author remained
unknown. The author was not then asking for advertisement, and made no
claim for credit. His object was literary. He wanted to win a place on
the staff of the Edinburgh Review, under the vast shadow of Lord
Macaulay; and, to a young American in 1868, such rank seemed
colossal--the highest in the literary world--as it had been only
five-and-twenty years before. Time and tide had flowed since then, but
the position still flattered vanity, though it brought no other
flattery or reward except the regular thirty pounds of pay--fifty
dollars a month, measured in time and labor. The Edinburgh article finished, he set himself to work on a
scheme for the North American Review. In England, Lord Robert Cecil had
invented for the London Quarterly an annual review of politics which he
called the "Session." Adams stole the idea and the name--he thought he
had been enough in Lord Robert's house, in days of his struggle with
adversity, to excuse the theft--and began what he meant for a permanent
series of annual political reviews which he hoped to make, in time, a
political authority. With his sources of information, and his social
intimacies at Washington, he could not help saying something that would
command attention. He had the field to himself, and he meant to give
himself a free hand, as he went on. Whether the newspapers liked it or
not, they would have to reckon with him; for such a power, once
established, was more effective than all the speeches in Congress or
reports to the President that could be crammed into the Government
presses. The first of these "Sessions" appeared in April, but it could
not be condensed into a single article, and had to be supplemented in
October by another which bore the title of "Civil Service Reform," and
was really a part of the same review. A good deal of authentic history
slipped into these papers. Whether any one except his press associates
ever read them, he never knew and never greatly cared. The difference
is slight, to the influence of an author, whether he is read by five
hundred readers, or by five hundred thousand; if he can select the five
hundred, he reaches the five hundred thousand. The fateful year 1870
was near at hand, which was to mark the close of the literary epoch,
when quarterlies gave way to monthlies; letter-press to illustration;
volumes to pages. The outburst was brilliant. Bret Harte led, and
Robert Louis Stevenson followed. Guy de Maupassant and Rudyard Kipling
brought up the rear, and dazzled the world. As usual, Adams found
himself fifty years behind his time, but a number of belated wanderers
kept him company, and they produced on each other the effect or
illusion of a public opinion. They straggled apart, at longer and
longer intervals, through the procession, but they were still within
hearing distance of each other. The drift was still superficially
conservative. Just as the Church spoke with apparent authority, or the
quarterlies laid down an apparent law, and no one could surely say
where the real authority, or the real law, lay. Science did not know.
Truths a priori held their own against truths surely relative.
According to Lowell, Right was forever on the scaffold, Wrong was
forever on the Throne; and most people still thought they believed it.
Adams was not the only relic of the eighteenth century, and he could
still depend on a certain number of listeners--mostly respectable, and
some rich. Want of audience did not trouble him; he was well enough off in
that respect, and would have succeeded in all his calculations if this
had been his only hazard. Where he broke down was at a point where he
always suffered wreck and where nine adventurers out of ten make their
errors. One may be more or less certain of organized forces; one can
never be certain of men. He belonged to the eighteenth century, and the
eighteenth century upset all his plans. For the moment, America was
more eighteenth century than himself; it reverted to the stone age. As education--of a certain sort--the story had probably a
certain value, though he could never see it. One seldom can see much
education in the buck of a broncho; even less in the kick of a mule.
The lesson it teaches is only that of getting out of the animal's way.
This was the lesson that Henry Adams had learned over and over again in
politics since 1860. At least four-fifths of the American people--Adams among the
rest--had united in the election of General Grant to the Presidency,
and probably had been more or less affected in their choice by the
parallel they felt between Grant and Washington. Nothing could be more
obvious. Grant represented order. He was a great soldier, and the
soldier always represented order. He might be as partisan as he
pleased, but a general who had organized and commanded half a million
or a million men in the field, must know how to administer. Even
Washington, who was, in education and experience, a mere cave-dweller,
had known how to organize a government, and had found Jeffersons and
Hamiltons to organize his departments. The task of bringing the
Government back to regular practices, and of restoring moral and
mechanical order to administration, was not very difficult; it was
ready to do it itself, with a little encouragement. No doubt the
confusion, especially in the old slave States and in the currency, was
considerable, but, the general disposition was good, and every one had
echoed that famous phrase: "Let us have peace." Adams was young and easily deceived, in spite of his diplomatic
adventures, but even at twice his age he could not see that this
reliance on Grant was unreasonable. Had Grant been a Congressman one
would have been on one's guard, for one knew the type. One never
expected from a Congressman more than good intentions and public
spirit. Newspaper-men as a rule had no great respect for the lower
House; Senators had less; and Cabinet officers had none at all. Indeed,
one day when Adams was pleading with a Cabinet officer for patience and
tact in dealing with Representatives, the Secretary impatiently broke
out: "You can't use tact with a Congressman! A Congressman is a hog!
You must take a stick and hit him on the snout!" Adams knew far too
little, compared with the Secretary, to contradict him, though he
thought the phrase somewhat harsh even as applied to the average
Congressman of 1869--he saw little or nothing of later ones--but he
knew a shorter way of silencing criticism. He had but to ask: "If a
Congressman is a hog, what is a Senator?" This innocent question, put
in a candid spirit, petrified any executive officer that ever sat a
week in his office. Even Adams admitted that Senators passed belief.
The comic side of their egotism partly disguised its extravagance, but
faction had gone so far under Andrew Johnson that at times the whole
Senate seemed to catch hysterics of nervous bucking without apparent
reason. Great leaders, like Sumner and Conkling, could not be
burlesqued; they were more grotesque than ridicule could make them;
even Grant, who rarely sparkled in epigram, became witty on their
account; but their egotism and factiousness were no laughing matter.
They did permanent and terrible mischief, as Garfield and Blaine, and
even McKinley and John Hay, were to feel. The most troublesome task of
a reform President was that of bringing the Senate back to decency. Therefore no one, and Henry Adams less than most, felt hope
that any President chosen from the ranks of politics or politicians
would raise the character of government; and by instinct if not by
reason, all the world united on Grant. The Senate understood what the
world expected, and waited in silence for a struggle with Grant more
serious than that with Andrew Johnson. Newspaper-men were alive with
eagerness to support the President against the Senate. The
newspaper-man is, more than most men, a double personality; and his
person feels best satisfied in its double instincts when writing in one
sense and thinking in another. All newspaper-men, whatever they wrote,
felt alike about the Senate. Adams floated with the stream. He was
eager to join in the fight which he foresaw as sooner or later
inevitable. He meant to support the Executive in attacking the Senate
and taking away its two-thirds vote and power of confirmation, nor did
he much care how it should be done, for he thought it safer to effect
the revolution in 1870 than to wait till 1920. With this thought in his mind, he went to the Capitol to hear
the names announced which should reveal the carefully guarded secret of
Grant's Cabinet. To the end of his life, he wondered at the suddenness
of the revolution which actually, within five minutes, changed his
intended future into an absurdity so laughable as to make him ashamed
of it. He was to hear a long list of Cabinet announcements not much
weaker or more futile than that of Grant, and none of them made him
blush, while Grant's nominations had the singular effect of making the
hearer ashamed, not so much of Grant, as of himself. He had made
another total misconception of life--another inconceivable false start.
Yet, unlikely as it seemed, he had missed his motive narrowly, and his
intention had been more than sound, for the Senators made no secret of
saying with senatorial frankness that Grant's nominations betrayed his
intent as plainly as they betrayed his incompetence. A great soldier
might be a baby politician. Adams left the Capitol, much in the same misty mental condition
that he recalled as marking his railway journey to London on May 13,
1861; he felt in himself what Gladstone bewailed so sadly, "the
incapacity of viewing things all round." He knew, without absolutely
saying it, that Grant had cut short the life which Adams had laid out
for himself in the future. After such a miscarriage, no thought of
effectual reform could revive for at least one generation, and he had
no fancy for ineffectual politics. What course could he sail next? He
had tried so many, and society had barred them all! For the moment, he
saw no hope but in following the stream on which he had launched
himself. The new Cabinet, as individuals, were not hostile.
Subsequently Grant made changes in the list which were mostly welcome
to a Bostonian--or should have been--although fatal to Adams. The name
of Hamilton Fish, as Secretary of State, suggested extreme conservatism
and probable deference to Sumner. The name of [COMPANION_B] S. Boutwell, as
Secretary of the Treasury, suggested only a somewhat lugubrious joke;
Mr. Boutwell could be described only as the opposite of Mr. McCulloch,
and meant inertia; or, in plain words, total extinction for any one
resembling Henry Adams. On the other hand, the name of Jacob D. Cox, as
Secretary of the Interior, suggested help and comfort; while that of
Judge Hoar, as Attorney-General, promised friendship. On the whole, the
personal outlook, merely for literary purposes, seemed fairly cheerful,
and the political outlook, though hazy, still depended on Grant
himself. No one doubted that Grant's intention had been one of reform;
that his aim had been to place his administration above politics; and
until he should actually drive his supporters away, one might hope to
support him. One's little lantern must therefore be turned on Grant.
One seemed to know him so well, and really knew so little. By chance it happened that Adam Badeau took the lower suite of
rooms at Dohna's, and, as it was convenient to have one table, the two
men dined together and became intimate. Badeau was exceedingly social,
though not in appearance imposing. He was stout; his face was red, and
his habits were regularly irregular; but he was very intelligent, a
good newspaper-man, and an excellent military historian. His life of
Grant was no ordinary book. Unlike most newspaper-men, he was a
friendly critic of Grant, as suited an officer who had been on the
General's staff. As a rule, the newspaper correspondents in Washington
were unfriendly, and the lobby sceptical. From that side one heard
tales that made one's hair stand on end, and the old West Point army
officers were no more flattering. All described him as vicious, narrow,
dull, and vindictive. Badeau, who had come to Washington for a
consulate which was slow to reach him, resorted more or less to whiskey
for encouragement, and became irritable, besides being loquacious. He
talked much about Grant, and showed a certain artistic feeling for
analysis of character, as a true literary critic would naturally do.
Loyal to Grant, and still more so to Mrs. Grant, who acted as his
patroness, he said nothing, even when far gone, that was offensive
about either, but he held that no one except himself and Rawlins
understood the General. To him, Grant appeared as an intermittent
energy, immensely powerful when awake, but passive and plastic in
repose. He said that neither he nor the rest of the staff knew why
Grant succeeded; they believed in him because of his success. For
stretches of time, his mind seemed torpid. Rawlins and the others would
systematically talk their ideas into it, for weeks, not directly, but
by discussion among themselves, in his presence. In the end, he would
announce the idea as his own, without seeming conscious of the
discussion; and would give the orders to carry it out with all the
energy that belonged to his nature. They could never measure his
character or be sure when he would act. They could never follow a
mental process in his thought. They were not sure that he did think. In all this, Adams took deep interest, for although he was not,
like Badeau, waiting for Mrs. Grant's power of suggestion to act on the
General's mind in order to germinate in a consulate or a legation, his
portrait gallery of great men was becoming large, and it amused him to
add an authentic likeness of the greatest general the world had seen
since Napoleon. Badeau's analysis was rather delicate; infinitely
superior to that of Sam Ward or Charles Nordhoff. Badeau took Adams to the White House one evening and introduced
him to the President and Mrs. Grant. First and last, he saw a dozen
Presidents at the White House, and the most famous were by no means the
most agreeable, but he found Grant the most curious object of study
among them all. About no one did opinions differ so widely. Adams had
no opinion, or occasion to make one. A single word with Grant satisfied
him that, for his own good, the fewer words he risked, the better. Thus
far in life he had met with but one man of the same intellectual or
unintellectual type--Garibaldi. Of the two, Garibaldi seemed to him a
trifle the more intellectual, but, in both, the intellect counted for
nothing; only the energy counted. The type was pre-intellectual,
archaic, and would have seemed so even to the cave-dwellers. Adam,
according to legend, was such a man. In time one came to recognize the type in other men, with
differences and variations, as normal; men whose energies were the
greater, the less they wasted on thought; men who sprang from the soil
to power; apt to be distrustful of themselves and of others; shy;
jealous; sometimes vindictive; more or less dull in outward appearance;
always needing stimulants, but for whom action was the highest
stimulant--the instinct of fight. Such men were forces of nature,
energies of the prime, like the Pteraspis, but they made short work of
scholars. They had commanded thousands of such and saw no more in them
than in others. The fact was certain; it crushed argument and intellect
at once. Adams did not feel Grant as a hostile force; like Badeau he saw
only an uncertain one. When in action he was superb and safe to follow;
only when torpid he was dangerous. To deal with him one must stand
near, like Rawlins, and practice more or less sympathetic habits.
Simple-minded beyond the experience of Wall Street or State Street, he
resorted, like most men of the same intellectual calibre, to
commonplaces when at a loss for expression: "Let us have peace!" or,
"The best way to treat a bad law is to execute it"; or a score of such
reversible sentences generally to be gauged by their sententiousness;
but sometimes he made one doubt his good faith; as when he seriously
remarked to a particularly bright young woman that Venice would be a
fine city if it were drained. In Mark Twain, this suggestion would have
taken rank among his best witticisms; in Grant it was a measure of
simplicity not singular. Robert E. Lee betrayed the same intellectual
commonplace, in a Virginian form, not to the same degree, but quite
distinctly enough for one who knew the American. What worried Adams was
not the commonplace; it was, as usual, his own education. Grant fretted
and irritated him, like the Terebratula, as a defiance of first
principles. He had no right to exist. He should have been extinct for
ages. The idea that, as society grew older, it grew one-sided, upset
evolution, and made of education a fraud. That, two thousand years
after Alexander the Great and Julius Caesar, a man like Grant should be
called--and should actually and truly be--the highest product of the
most advanced evolution, made evolution ludicrous. One must be as
commonplace as Grant's own commonplaces to maintain such an absurdity.
The progress of evolution from President Washington to President Grant,
was alone evidence enough to upset Darwin. Education became more perplexing at every phase. No theory was
worth the pen that wrote it. America had no use for Adams because he
was eighteenth-century, and yet it worshipped Grant because he was
archaic and should have lived in a cave and worn skins. Darwinists
ought to conclude that America was reverting to the stone age, but the
theory of reversion was more absurd than that of evolution. Grant's
administration reverted to nothing. One could not catch a trait of the
past, still less of the future. It was not even sensibly American. Not
an official in it, except perhaps Rawlins whom Adams never met, and who
died in September, suggested an American idea. Yet this administration, which upset Adams's whole life, was
not unfriendly; it was made up largely of friends. Secretary Fish was
almost kind; he kept the tradition of New York social values; he was
human and took no pleasure in giving pain. Adams felt no prejudice
whatever in his favor, and he had nothing in mind or person to attract
regard; his social gifts were not remarkable; he was not in the least
magnetic; he was far from young; but he won confidence from the start
and remained a friend to the finish. As far as concerned Mr. Fish, one
felt rather happily suited, and one was still better off in the
Interior Department with J. D. Cox. Indeed, if Cox had been in the
Treasury and Boutwell in the Interior, one would have been quite
satisfied as far as personal relations went, while, in the
Attorney-General's Office, Judge Hoar seemed to fill every possible
ideal, both personal and political. The difficulty was not the want of friends, and had the whole
government been filled with them, it would have helped little without
the President and the Treasury. Grant avowed from the start a policy of
drift; and a policy of drift attaches only barnacles. At thirty, one
has no interest in becoming a barnacle, but even in that character
Henry Adams would have been ill-seen. His friends were reformers,
critics, doubtful in party allegiance, and he was himself an object of
suspicion. Grant had no objects, wanted no help, wished for no
champions. The Executive asked only to be let alone. This was his
meaning when he said: "Let us have peace!" No one wanted to go into opposition. As for Adams, all his
hopes of success in life turned on his finding an administration to
support. He knew well enough the rules of self-interest. He was for
sale. He wanted to be bought. His price was excessively cheap, for he
did not even ask an office, and had his eye, not on the Government, but
on New York. All he wanted was something to support; something that
would let itself be supported. Luck went dead against him. For once, he
was fifty years in advance of his time.
```

### AI Extraction
- **Primary Mechanism**: `VERBAL_WIT` (Detector Confidence: `0.44`)
- **Secondary Dynamics**: CALLBACK
- **Linguistic Craft Score**: `0.65`
- **Tone**: `DRY_WIT`
- **Setup**: Characters Lord Macaulay, Lord Robert establish scene context: 'CHAPTER XVII PRESIDENT GRANT (1869) THE first effect of this leap into the unkno...'
- **Escalation**: Complication rises around verbal_wit: 'He gave three months
to an article on the finances of the United States, just th...'
- **Reversal**: Expectation or status is inverted: 'Therefore no one, and Henry Adams less than most, felt hope
that any President c...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'For once, he
was fifty years in advance of his time....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 28 — `three_men_in_a_boat_ch15_04970`

**Source**: *Three Men In A Boat* (Chapter 15)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.24` | **Surface Slang Isolated**: None  

### Passage
```text
"[COMPANION_B] retorted on [COMPANION_A];," "Well, I don't see how _you_ can know much about it, one way or the
other, for I'm blest if you haven't been
asleep half the time.
```

### AI Extraction
- **Primary Mechanism**: `VERBAL_WIT` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.50`
- **Tone**: `DRY_WIT`
- **Setup**: "[COMPANION_B] retorted on [COMPANION_A];," "Well, I don't see how _you_ can know much about it, one way or the
other, for I'm blest if you haven't been
asleep half the time.
- **Escalation**: Comedic complication introduced.
- **Reversal**: Expectation upended.
- **Payoff**: "[COMPANION_B] retorted on [COMPANION_A];," "Well, I don't see how _you_ can know much about it, one way or the
other, for I'm blest if you haven't been
asleep half the time.

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 29 — `love_among_the_chickens_chNone_03766`

**Source**: *Love Among The Chickens* (Chapter None)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.15` | **Surface Slang Isolated**: None  

### Passage
```text
He looked askance at the floor and said gruffly:  "Look! How dirty he has made it!"  Tsiganok retorted quickly:  "You've made the whole world dirty, you fat-face, and yet I haven't said anything to you
```

### AI Extraction
- **Primary Mechanism**: `VERBAL_WIT` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.50`
- **Tone**: `DRY_WIT`
- **Setup**: He looked askance at the floor and said gruffly:  "Look!
- **Escalation**: How dirty he has made it!"  Tsiganok retorted quickly:  "You've made the whole world dirty, you fat-face, and yet I haven't said anything to you
- **Reversal**: Expectation upended.
- **Payoff**: How dirty he has made it!"  Tsiganok retorted quickly:  "You've made the whole world dirty, you fat-face, and yet I haven't said anything to you

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 30 — `the_inimitable_jeeves_chNone_08774`

**Source**: *The Inimitable Jeeves* (Chapter None)  
**Characters Identified**: Lady Jane  
**Dialogue Ratio**: `0.00` | **Surface Slang Isolated**: None  

### Passage
```text
By the strange irony of fortune, it fell to the lot of Thomas Offley to perform the duties of sheriff at Dudley's execution, although he had himself been one of the supporters of the Lady Jane in her claim to the crown
```

### AI Extraction
- **Primary Mechanism**: `VERBAL_WIT` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.40`
- **Tone**: `DRY_WIT`
- **Setup**: By the strange irony of fortune, it fell to the lot of Thomas Offley to perform the duties of sheriff at Dudley's execution, although he had himself been one of the supporters of the Lady Jane in her claim to the crown
- **Escalation**: Comedic complication introduced.
- **Reversal**: Expectation upended.
- **Payoff**: By the strange irony of fortune, it fell to the lot of Thomas Offley to perform the duties of sheriff at Dudley's execution, although he had himself been one of the supporters of the Lady Jane in her claim to the crown

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 31 — `right_ho_ch10_06631`

**Source**: *Right Ho* (Chapter 10)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.65` | **Surface Slang Isolated**: None  

### Passage
```text
"Well, we shall have to make it an exterior set instead of an interior. We can easily corner her on the beach somewhere, when we're ready. Meanwhile, we must get the kid letter-perfect. First rehearsal for lines and business eleven sharp to-morrow," Poor old Freddie was in such a gloomy state of mind that we decided not to tell him the idea till we had finished coaching the kid.
```

### AI Extraction
- **Primary Mechanism**: `DRAMATIC_IRONY` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.75`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: '"Well, we shall have to make it an exterior set instead of an interior....'
- **Escalation**: Complication rises around dramatic_irony: 'We can easily corner her on the beach somewhere, when we're ready....'
- **Reversal**: Expectation or status is inverted: 'Meanwhile, we must get the kid letter-perfect....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'First rehearsal for lines and business eleven sharp to-morrow," Poor old Freddie...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 32 — `my_man_jeeves_ch10_02075`

**Source**: *My Man Jeeves* (Chapter 10)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.65` | **Surface Slang Isolated**: None  

### Passage
```text
"Well, we shall have to make it an exterior set instead of an interior. We can easily corner her on the beach somewhere, when we're ready. Meanwhile, we must get the kid letter-perfect. First rehearsal for lines and business eleven sharp to-morrow," Poor old Freddie was in such a gloomy state of mind that we decided not to tell him the idea till we had finished coaching the kid.
```

### AI Extraction
- **Primary Mechanism**: `DRAMATIC_IRONY` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.75`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: '"Well, we shall have to make it an exterior set instead of an interior....'
- **Escalation**: Complication rises around dramatic_irony: 'We can easily corner her on the beach somewhere, when we're ready....'
- **Reversal**: Expectation or status is inverted: 'Meanwhile, we must get the kid letter-perfect....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'First rehearsal for lines and business eleven sharp to-morrow," Poor old Freddie...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 33 — `the_inimitable_jeeves_ch36_00522`

**Source**: *The Inimitable Jeeves* (Chapter 36)  
**Characters Identified**: Lady Jane  
**Dialogue Ratio**: `0.12` | **Surface Slang Isolated**: None  

### Passage
```text
"that wolde a been qwene," In the meanwhile the aged Cranmer and the youthful Lady Jane Grey--she her husband and two of her husband's brothers
had been brought to trial at the Guildhall (13 Nov).
```

### AI Extraction
- **Primary Mechanism**: `DRAMATIC_IRONY` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.50`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: "that wolde a been qwene," In the meanwhile the aged Cranmer and the youthful Lady Jane Grey--she her husband and two of her husband's brothers
had been brought to trial at the Guildhall (13 Nov).
- **Escalation**: Comedic complication introduced.
- **Reversal**: Expectation upended.
- **Payoff**: "that wolde a been qwene," In the meanwhile the aged Cranmer and the youthful Lady Jane Grey--she her husband and two of her husband's brothers
had been brought to trial at the Guildhall (13 Nov).

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 34 — `their_mutual_child_ch6_10268`

**Source**: *Their Mutual Child* (Chapter 6)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.05` | **Surface Slang Isolated**: None  

### Passage
```text
"Capital," He could not
afterwards remember to have heard the name of Karl Marx mentioned, or
the title of He was equally ignorant of Auguste Comte.
```

### AI Extraction
- **Primary Mechanism**: `DRAMATIC_IRONY` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.40`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: "Capital," He could not
afterwards remember to have heard the name of Karl Marx mentioned, or
the title of He was equally ignorant of Auguste Comte.
- **Escalation**: Comedic complication introduced.
- **Reversal**: Expectation upended.
- **Payoff**: "Capital," He could not
afterwards remember to have heard the name of Karl Marx mentioned, or
the title of He was equally ignorant of Auguste Comte.

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 35 — `the_man_upstairs_ch42_03950`

**Source**: *The Man Upstairs* (Chapter 42)  
**Characters Identified**: And, Lady Arched  
**Dialogue Ratio**: `0.66` | **Surface Slang Isolated**: None  

### Passage
```text
"I made some commonplace reply. The old lady arched her eyebrows," "A nice room, my dear, and I ought to be much obliged to you for it, since my maid tells me it is yours," said her ladyship; "but I am pretty sure you repent your generosity to me, after all those ghost stories, and tremble to think of a strange bed and chamber, eh? Where have they put you, child?" she asked; "in some cock-loft of the turrets, eh? or in a lumber-room - a regular ghost-trap? I can hear your heart beating with fear this moment.
```

### AI Extraction
- **Primary Mechanism**: `DIALOGUE_SUBTEXT` (Detector Confidence: `0.25`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters And, Lady Arched establish scene context: '"I made some commonplace reply....'
- **Escalation**: Complication rises around dialogue_subtext: 'The old lady arched her eyebrows," "A nice room, my dear, and I ought to be much...'
- **Reversal**: Expectation or status is inverted: 'Where have they put you, child?" she asked; "in some cock-loft of the turrets, e...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'I can hear your heart beating with fear this moment....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 36 — `something_fresh_ch8_10471`

**Source**: *Something Fresh* (Chapter 8)  
**Characters Identified**: Ashe, Mr Peters, Professor Muldoon  
**Dialogue Ratio**: `0.50` | **Surface Slang Isolated**: ripping  

### Passage
```text
CHAPTER VIII "'Put the butter or drippings in a kettle on the range, and when
hot add the onions and fry them; add the veal and cook until
brown. Add the water, cover closely, and cook very slowly until
the meat is tender; then add the seasoning and place the potatoes
on top of the meat. Cover and cook until the potatoes are tender,
but not falling to pieces.'" "Sure," said Mr. Peters--"not falling to pieces. That's right.
Go on." "'Then add the cream and cook five minutes longer'" read Ashe. "Is that all?" "That's all of that one." Mr. Peters settled himself more comfortably in bed. "Read me the piece where it tells about curried lobster." Ashe cleared his throat. "'Curried Lobster,'" he read. "'Materials: Two one-pound
lobsters, two teaspoonfuls lemon juice, half a spoonful curry
powder, two tablespoonfuls butter, a tablespoonful flour, one
cupful scalded milk, one cupful cracker crumbs, half teaspoonful
salt, quarter teaspoonful pepper.'" "Go on." "'Way of Preparing: Cream the butter and flour and add the
scalded milk; then add the lemon juice, curry powder, salt and
pepper. Remove the lobster meat from the shells and cut into
half-inch cubes.'" "Half-inch cubes," sighed Mr. Peters wistfully. "Yes?" "'Add the latter to the sauce.'" "You didn't say anything about the latter. Oh, I see; it means
the half-inch cubes. Yes?" "'Refill the lobster shells, cover with buttered crumbs, and bake
until the crumbs are brown. This will serve six persons.'" "And make them feel an hour afterward as though they had
swallowed a live wild cat," said Mr. Peters ruefully. "Not necessarily," said Ashe. "I could eat two portions of that
at this very minute and go off to bed and sleep like a little
child." Mr. Peters raised himself on his elbow and stared at him. They
were in the millionaire's bedroom, the time being one in the
morning, and Mr. Peters had expressed a wish that Ashe should
read him to sleep. He had voted against Ashe's novel and produced
from the recesses of his suitcase a much-thumbed cookbook. He
explained that since his digestive misfortunes had come on him he
had derived a certain solace from its perusal. It may be that to some men sorrow's crown of sorrow is
remembering happier things; but Mr. Peters had not found that to
be the case. In his hour of affliction it soothed him to read of
Hungarian Goulash and escaloped brains, and to remember that he,
too, the nut-and-grass eater of today, had once dwelt in Arcadia. The passage of the days, which had so sapped the stamina of the
efficient Baxter, had had the opposite effect on Mr. Peters. His
was one of those natures that cannot deal in half measures.
Whatever he did, he did with the same driving energy. After the
first passionate burst of resistance he had settled down into a
model pupil in Ashe's one-man school of physical culture. It had
been the same, now that he came to look back on it, at Muldoon's. Now that he remembered, he had come away from White Plains
hoping, indeed, never to see the place again, but undeniably a
different man physically. It was not the habit of Professor
Muldoon to let his patients loaf; but Mr. Peters, after the
initial plunge, had needed no driving. He had worked hard at his
cure then, because it was the job in hand. He worked hard now,
under the guidance of Ashe, because, once he had begun, the thing
interested and gripped him. Ashe, who had expected continued reluctance, had been astonished
and delighted at the way in which the millionaire had behaved.
Nature had really intended Ashe for a trainer; he identified
himself so thoroughly with his man and rejoiced at the least
signs of improvement. In Mr. Peters' case there had been distinct improvement already.
Miracles do not happen nowadays, and it was too much to expect
one who had maltreated his body so consistently for so many years
to become whole in a day; but to an optimist like Ashe signs were
not wanting that in due season Mr. Peters would rise on
stepping-stones of his dead self to higher things, and though
never soaring into the class that devours lobster a la Newburg
and smiles after it, might yet prove himself a devil of a fellow
among the mutton chops. "You're a wonder!" said Mr. Peters. "You're fresh, and you have
no respect for your elders and betters; but you deliver the
goods. That's the point. Why, I'm beginning to feel great! Say,
do you know I felt a new muscle in the small of my back this
morning? They are coming out on me like a rash." "That's the Larsen Exercises. They develop the whole body." "Well, you're a pretty good advertisement for them if they need
one. What were you before you came to me--a prize-fighter?" "That's the question everybody I have met since I arrived here
has asked me. I believe it made the butler think I was some sort
of crook when I couldn't answer it. I used to write stories--
detective stories." "What you ought to be doing is running a place over here in
England like Muldoon has back home. But you will be able to write
one more story out of this business here, if you want to. When
are you going to have another try for my scarab?" "To-night." "To-night? How about Baxter?" "I shall have to risk Baxter." Mr. Peters hesitated. He had fallen out of the habit of being
magnanimous during the past few years, for dyspepsia brooks no
divided allegiance and magnanimity has to take a back seat when
it has its grip on you. "See here," he said awkwardly; "I've been thinking this over
lately--and what's the use? It's a queer thing; and if anybody
had told me a week ago that I should be saying it I wouldn't have
believed him; but I am beginning to like you. I don't want to get
you into trouble. Let the old scarab go. What's a scarab anyway?
Forget about it and stick on here as my private Muldoon. If it's
the five thousand that's worrying you, forget that too. I'll give
it to you as your fee." Ashe was astounded. That it could really be his peppery employer
who spoke was almost unbelievable. Ashe's was a friendly nature
and he could never be long associated with anyone without trying
to establish pleasant relations; but he had resigned himself in
the present case to perpetual warfare. He was touched; and if he had ever contemplated abandoning his
venture, this, he felt, would have spurred him on to see it
through. This sudden revelation of the human in Mr. Peters was
like a trumpet call. "I wouldn't think of it," he said. "It's great of you to suggest
such a thing; but I know just how you feel about the thing, and
I'm going to get it for you if I have to wring Baxter's neck.
Probably Baxter will have given up waiting as a bad job by now if
he has been watching all this while. We've given him ten nights
to cool off. I expect he is in bed, dreaming pleasant dreams.
It's nearly two o'clock. I'll wait another ten minutes and then
go down." He picked up the cookbook. "Lie back and make yourself
comfortable, and I'll read you to sleep first." "You're a good boy," said Mr. Peters drowsily. "Are you ready? 'Pork Tenderloin Larded. Half pound fat pork--'"
A faint smile curved Mr. Peters' lips. His eyes were closed and
he breathed softly. Ashe went on in a low voice: "'four large
pork tenderloins, one cupful cracker crumbs, one cupful boiling
water, two tablespoonfuls butter, one teaspoonful salt, half
teaspoonful pepper, one teaspoonful poultry seasoning.'" A little sigh came from the bed. "'Way of Preparing: Wipe the tenderloins with a damp cloth. With
a sharp knife make a deep pocket lengthwise in each tenderloin.
Cut your pork into long thin strips and, with a needle, lard each
tenderloin. Melt the butter in the water, add the seasoning and
the cracker crumbs, combining all thoroughly. Now fill each
pocket in the tenderloin with this stuffing. Place the
tenderloins--'" A snore sounded from the pillows, punctuating the recital like a
mark of exclamation. Ashe laid down the book and peered into the
darkness beyond the rays of the bed lamp. His employer slept. Ashe switched off the light and crept to the door. Out in the
passage he stopped and listened. All was still. He stole
downstairs.
```

### AI Extraction
- **Primary Mechanism**: `DIALOGUE_SUBTEXT` (Detector Confidence: `0.25`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.90`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Ashe, Mr Peters establish scene context: 'CHAPTER VIII "'Put the butter or drippings in a kettle on the range, and when
ho...'
- **Escalation**: Complication rises around dialogue_subtext: 'It may be that to some men sorrow's crown of sorrow is
remembering happier thing...'
- **Reversal**: Expectation or status is inverted: 'Say,
do you know I felt a new muscle in the small of my back this
morning?...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'He stole
downstairs....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 37 — `the_little_nugget_ch1_10395`

**Source**: *The Little Nugget* (Chapter 1)  
**Characters Identified**: Mr Morehouse, Professor Gordon, Professor Was  
**Dialogue Ratio**: `0.76` | **Surface Slang Isolated**: None  

### Passage
```text
"The president put the papers on his desk and wrote a letter to Professor Gordon. Unfortunately the Professor was in South America collecting zoological specimens, and the letter was forwarded to him by his wife. As the Professor was in the highest Andes, where no white man had ever penetrated, the letter was many months in reaching him. The president forgot the guinea-pigs, Morgan forgot them, Mr. Morehouse forgot them, but Flannery did not. One-half of his time he gave to the duties of his agency; the other half was devoted to the guinea-pigs. Long before Professor Gordon received the president's letter Morgan received one from Flannery," About them dago pigs," it said, "what shall I do they are great in family life, no race suicide for them, there are thirty-two now shall I sell them do you take this express office for a menagerie, answer quick.
```

### AI Extraction
- **Primary Mechanism**: `DIALOGUE_SUBTEXT` (Detector Confidence: `0.25`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.80`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Mr Morehouse, Professor Gordon establish scene context: '"The president put the papers on his desk and wrote a letter to Professor Gordon...'
- **Escalation**: Complication rises around dialogue_subtext: 'Unfortunately the Professor was in South America collecting zoological specimens...'
- **Reversal**: Expectation or status is inverted: 'The president forgot the guinea-pigs, Morgan forgot them, Mr....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'Long before Professor Gordon received the president's letter Morgan received one...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 38 — `right_ho_ch11_02254`

**Source**: *Right Ho* (Chapter 11)  
**Characters Identified**: Harold, Voules  
**Dialogue Ratio**: `0.79` | **Surface Slang Isolated**: None  

### Passage
```text
"as they say, which after considerable difficulty, I identified as Voules's. I hardly recognized it. In his official capacity Voules talks exactly like you'd expect a statue to talk, if it could. In private, however, he evidently relaxed to some extent, and to have that sort of thing going on in my midst at that hour was too much for me," The chief ingredients were a female voice that sobbed and said: "Oh, Harold!" and a male voice "raised in anger, Voules!" I yelled.
```

### AI Extraction
- **Primary Mechanism**: `DIALOGUE_SUBTEXT` (Detector Confidence: `0.25`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.80`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Harold, Voules establish scene context: '"as they say, which after considerable difficulty, I identified as Voules's....'
- **Escalation**: Complication rises around dialogue_subtext: 'I hardly recognized it....'
- **Reversal**: Expectation or status is inverted: 'In his official capacity Voules talks exactly like you'd expect a statue to talk...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'In private, however, he evidently relaxed to some extent, and to have that sort ...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 39 — `my_man_jeeves_ch10_05135`

**Source**: *My Man Jeeves* (Chapter 10)  
**Characters Identified**: Angela, Jimmy, Marie  
**Dialogue Ratio**: `0.88` | **Surface Slang Isolated**: old top  

### Passage
```text
"This stone is the girl. This bit of seaweed's the child. This nutshell is Freddie. Dialogue leading up to child's line. Child speaks like, 'Boofer lady, does i'oo love dadda?' Business of outstretched hands. Hold picture for a moment. Freddie crosses L., takes girl's hand. Business of swallowing lump in throat. Then big speech. 'Ah, Marie,' or whatever her name is - Jane - Agnes - Angela? Very well. 'Ah, Angela, has not this gone on too long? A little child rebukes us! Angela!' And so on. Freddie must work up his own part. I'm just giving you the general outline. And we must get a good line for the child. 'Boofer lady, does 'oo love dadda?' isn't definite enough. We want something more - ah! 'Kiss Freddie,' that's it. Short, crisp, and has the punch," "But, Jimmy, old top," I said, "the only objection is, don't you know, that there's no way of getting the girl to the cottage.
```

### AI Extraction
- **Primary Mechanism**: `DIALOGUE_SUBTEXT` (Detector Confidence: `0.25`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.80`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Angela, Jimmy establish scene context: '"This stone is the girl....'
- **Escalation**: Complication rises around dialogue_subtext: 'Hold picture for a moment....'
- **Reversal**: Expectation or status is inverted: 'Very well....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'Short, crisp, and has the punch," "But, Jimmy, old top," I said, "the only objec...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 40 — `my_man_jeeves_ch16_00207`

**Source**: *My Man Jeeves* (Chapter 16)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.75` | **Surface Slang Isolated**: ripping  

### Passage
```text
"I went back to the sitting-room. She hadn't moved an inch. She was still bolt upright on the edge of her chair, gripping her umbrella like a hammer-thrower. She gave me another of those looks as I came in. There was no doubt about it; for some reason she had taken a dislike to me. I suppose because I wasn't [COMPANION_B] M. Cohan. It was a bit hard on a chap," This is a surprise, what?" I said, after about five minutes' restful silence, trying to crank the conversation up again.
```

### AI Extraction
- **Primary Mechanism**: `CALLBACK` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: '"I went back to the sitting-room....'
- **Escalation**: Complication rises around callback: 'She was still bolt upright on the edge of her chair, gripping her umbrella like ...'
- **Reversal**: Expectation or status is inverted: 'There was no doubt about it; for some reason she had taken a dislike to me....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'It was a bit hard on a chap," This is a surprise, what?" I said, after about fiv...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 41 — `right_ho_ch16_05676`

**Source**: *Right Ho* (Chapter 16)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.75` | **Surface Slang Isolated**: ripping  

### Passage
```text
"I went back to the sitting-room. She hadn't moved an inch. She was still bolt upright on the edge of her chair, gripping her umbrella like a hammer-thrower. She gave me another of those looks as I came in. There was no doubt about it; for some reason she had taken a dislike to me. I suppose because I wasn't [COMPANION_B] M. Cohan. It was a bit hard on a chap," This is a surprise, what?" I said, after about five minutes' restful silence, trying to crank the conversation up again.
```

### AI Extraction
- **Primary Mechanism**: `CALLBACK` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: '"I went back to the sitting-room....'
- **Escalation**: Complication rises around callback: 'She was still bolt upright on the edge of her chair, gripping her umbrella like ...'
- **Reversal**: Expectation or status is inverted: 'There was no doubt about it; for some reason she had taken a dislike to me....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'It was a bit hard on a chap," This is a surprise, what?" I said, after about fiv...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 42 — `the_man_upstairs_ch9_08161`

**Source**: *The Man Upstairs* (Chapter 9)  
**Characters Identified**: Dick  
**Dialogue Ratio**: `0.47` | **Surface Slang Isolated**: None  

### Passage
```text
"The woman's voice rose, it was loud and shrill. The man turned slowly round without looking up, and stretched out his arms toward the woman. She stopped and looked down at him. The fire glittered for a moment and then died out of her eyes, her bosom heaved and her lips began to tremble. With a cry she flung herself into his arms, caught him around the neck, and pressed his face up close against her cheek," They shall hang you! Do you hear me? They shall hang you! Oh! Dick, Dick," she sobbed, "I do love you so! I can't live without you! Not another hour, Dick! I do want you so much, so much, Dick!" The man shifted his right arm quickly, slipped a great Mexican knife out of his sleeve, and passed his fingers slowly up the woman's side until he felt the heart beat under his hand, then he raised the knife, gripped the handle tight, and drove the keen blade into the woman's bosom.
```

### AI Extraction
- **Primary Mechanism**: `CALLBACK` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Dick establish scene context: '"The woman's voice rose, it was loud and shrill....'
- **Escalation**: Complication rises around callback: 'The fire glittered for a moment and then died out of her eyes, her bosom heaved ...'
- **Reversal**: Expectation or status is inverted: 'They shall hang you!...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'I do want you so much, so much, Dick!" The man shifted his right arm quickly, sl...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 43 — `the_little_nugget_ch2_06202`

**Source**: *The Little Nugget* (Chapter 2)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.31` | **Surface Slang Isolated**: None  

### Passage
```text
they filled them with guinea-pigs and expressed them to Franklin. Day after day the cages of guineapigs flowed in a steady stream from Westcote to Franklin, and still Flannery and his six helpers ripped and nailed and packed--relentlessly and feverishly. At the end of the week they had shipped two hundred and eighty cases of guinea-pigs, and there were in the express office seven hundred and four more pigs than when they began packing them. "Stop sending pigs. Warehouse full," came a telegram to Flannery. He stopped packing only long enough to wire back, "Can't stop," and kept on sending them. On the next train up from Franklin came one of the company's inspectors. He had instructions to stop the stream of guinea-pigs at all hazards. As his train drew up at Westcote station he saw a cattle car standing on the express company's siding. When he reached the express office he saw the express wagon backed up to the door. Six boys were carrying bushel baskets full of guinea-pigs from the office and dumping them into the wagon. Inside the room Flannery, with' his coat and vest off, was shoveling guinea-pigs into bushel baskets with a coal scoop. He was winding up the guinea-pig episode. He looked up at the inspector with a snort of anger. "Wan wagonload more an, I'll be quit of thim, an' niver will ye catch Flannery wid no more foreign pigs on his hands. No, sur! They near was the death o' me. Nixt toime I'll know that pigs of whaiver nationality is domistic pets--an' go at the lowest rate." He began shoveling again rapidly, speaking quickly between breaths. "Rules may be rules, but you can't fool Mike Flannery twice wid the same thrick--whin ut comes to live stock, dang the rules. So long as Flannery runs this expriss office--pigs is pets--an' cows is pets--an' horses is pets--an' lions an' tigers an' Rocky Mountain goats is pets--an' the rate on thim is twinty-foive cints." He paused long enough to let one of the boys put an empty basket in the place of the one he had just filled. There were only a few guinea-pigs left. As he noted their limited number his natural habit of looking on the bright side returned. "Well, annyhow," he said cheerfully, "'tis not so bad as ut might be. What if thim dago pigs had been elephants!"
```

### AI Extraction
- **Primary Mechanism**: `CALLBACK` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DOMESTIC_ABSURDITY`
- **Setup**: Characters Narrator establish scene context: 'they filled them with guinea-pigs and expressed them to Franklin....'
- **Escalation**: Complication rises around callback: 'On the next train up from Franklin came one of the company's inspectors....'
- **Reversal**: Expectation or status is inverted: 'He was winding up the guinea-pig episode....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'What if thim dago pigs had been elephants!"...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 44 — `a_damsel_in_distress_ch19_03486`

**Source**: *A Damsel In Distress* (Chapter 19)  
**Characters Identified**: Doctor Briginshaw, Gee, Lord Wisbeach, Mr Sturgis, Mrs Ford, Mrs Peter, Mrs Pett, Ogden  
**Dialogue Ratio**: `0.30` | **Surface Slang Isolated**: None  

### Passage
```text
CHAPTER XVI MRS. PETT TAKES PRECAUTIONS Mrs. Pett, on leaving the luncheon-table, had returned to the
drawing-room to sit beside the sick-settee of her stricken child.
She was troubled about Ogden. The poor lamb was not at all
himself to-day. A bowl of clear soup, the midday meal prescribed
by Doctor Briginshaw, lay untasted at his side. She crossed the room softly, and placed a cool hand on her son's
aching brow. "Oh, Gee," said Ogden wearily. "Are you feeling a little better, Oggie darling?" "No," said Ogden firmly. "I'm feeling a lot worse." "You haven't drunk your nice soup." "Feed it to the cat." "Could you eat a nice bowl of bread-and-milk, precious?" "Have a heart," replied the sufferer. Mrs. Pett returned to her seat, sorrowfully. It struck her as an
odd coincidence that the poor child was nearly always like this
on the morning after she had been entertaining guests; she put it
down to the reaction from the excitement working on a
highly-strung temperament. To his present collapse the brutal
behaviour of Jerry Mitchell had, of course, contributed. Every
drop of her maternal blood boiled with rage and horror whenever
she permitted herself to contemplate the excesses of the late
Jerry. She had always mistrusted the man. She had never liked his
face--not merely on aesthetic grounds but because she had seemed
to detect in it a lurking savagery. How right events had proved
this instinctive feeling. Mrs. Pett was not vulgar enough to
describe the feeling, even to herself, as a hunch, but a hunch it
had been; and, like every one whose hunches have proved correct,
she was conscious in the midst of her grief of a certain
complacency. It seemed to her that hers must be an intelligence
and insight above the ordinary. The peace of the early afternoon settled upon the drawing-room.
Mrs. Pett had taken up a book; Ogden, on the settee, breathed
stentorously. Faint snores proceeded from the basket in the
corner where Aida, the Pomeranian, lay curled in refreshing
sleep. Through the open window floated sounds of warmth and
Summer. Yielding to the drowsy calm, Mrs. Pett was just nodding into a
pleasant nap, when the door opened and Lord Wisbeach came in. Lord Wisbeach had been doing some rapid thinking. Rapid thought
is one of the essentials in the composition of men who are known
as Gentleman Jack to the boys and whose livelihood is won only by
a series of arduous struggles against the forces of Society and
the machinations of Potter and his gang. Condensed into capsule
form, his lordship's meditations during the minutes after he had
left Jimmy in the dining-room amounted to the realisation that
the best mode of defence is attack. It is your man who knows how
to play the bold game on occasion who wins. A duller schemer than
Lord Wisbeach might have been content to be inactive after such a
conversation as had just taken place between himself and Jimmy.
His lordship, giving the matter the concentrated attention of his
trained mind, had hit on a better plan, and he had come to the
drawing-room now to put it into effect. His entrance shattered the peaceful atmosphere. Aida, who had
been gurgling apoplectically, sprang snarling from the basket,
and made for the intruder open-mouthed. Her shrill barking rang
through the room. Lord Wisbeach hated little dogs. He hated and feared them. Many
men of action have these idiosyncrasies. He got behind a chair
and said "There, there." Aida, whose outburst was mere sound and
fury and who had no intention whatever of coming to blows,
continued the demonstration from a safe distance, till Mrs. Pett,
swooping down, picked her up and held her in her lap, where she
consented to remain, growling subdued defiance. Lord Wisbeach
came out from behind his chair and sat down warily. "Can I have a word with you, Mrs. Pett?" "Certainly, Lord Wisbeach." His lordship looked meaningly at Ogden. "In private, you know." He then looked meaningly at Mrs. Pett. "Ogden darling," said Mrs. Pett, "I think you had better go to
your room and undress and get into bed. A little nice sleep might
do you all the good in the world." With surprising docility, the boy rose. "All right," he said. "Poor Oggie is not at all well to-day," said Mrs. Pett, when he
was gone. "He is very subject to these attacks. What do you want
to tell me, Lord Wisbeach?" His lordship drew his chair a little closer. "Mrs. Pett, you remember what I told you yesterday?" "Of course." "Might I ask what you know of this man who has come here calling
himself Jimmy Crocker?" Mrs. Pett started. She remembered that she had used almost that
very expression to Ann. Her suspicions, which had been lulled by
the prompt recognition of the visitor by Skinner and Lord
Wisbeach, returned. It is one of the effects of a successful
hunch that it breeds other hunches. She had been right about
Jerry Mitchell; was she to be proved right about the self-styled
Jimmy Crocker? "You have seen your nephew, I believe?" "Never. But--" "That man," said Lord Wisbeach impassively, "is not your nephew." Mrs. Pett thrilled all down her spine. She had been right. "But you--" "But I pretended to recognise him? Just so. For a purpose. I
wanted to make him think that I suspected nothing." "Then you think--?" "Remember what I said to you yesterday." "But Skinner--the butler--recognised him?" "Exactly. It goes to prove that what I said about Skinner was
correct. They are working together. The thing is self-evident.
Look at it from your point of view. How simple it is. This man
pretends to an intimate acquaintance with Skinner. You take that
as evidence of Skinner's honesty. Skinner recognises this man.
You take that as proof that this man is really your nephew. The
fact that Skinner recognised as Jimmy Crocker a man who is not
Jimmy Crocker condemns him." "But why did you--?" "I told you that I pretended to accept this man as the real Jimmy
Crocker for a purpose. At present there is nothing that you can
do. Mere impersonation is not a crime. If I had exposed him when
we met, you would have gained nothing beyond driving him from the
house. Whereas, if we wait, if we pretend to suspect nothing, we
shall undoubtedly catch him red-handed in an attempt on your
nephew's invention." "You are sure that that is why he has come?" "What other reason could he have?" "I thought he might be trying to kidnap Ogden." Lord Wisbeach frowned thoughtfully. He had not taken this
consideration into account. "It is possible," he said. "There have been several attempts
made, have there not, to kidnap your son?" "At one time," said Mrs. Pett proudly, "there was not a child in
America who had to be more closely guarded. Why, the kidnappers
had a special nick-name for Oggie. They called him the Little
Nugget." "Of course, then, it is quite possible that that may be the man's
object. In any case, our course must be the same. We must watch
every move he makes." He paused. "I could help--pardon my
suggesting it--I could help a great deal more if you were to
invite me to live in the house. You were kind enough to ask me to
visit you in the country, but it will be two weeks before you go
to the Country, and in those two weeks--" "You must come here at once, Lord Wisbeach. To-night. To-day." "I think that would be the best plan." "I cannot tell you how grateful I am for all you are doing." "You have been so kind to me, Mrs. Pett," said Lord Wisbeach with
feeling, "that it is surely only right that I should try to make
some return. Let us leave it at this then. I will come here
to-night and will make it my business to watch these two men. I
will go and pack my things and have them sent here." "It is wonderful of you, Lord Wisbeach." "Not at all," replied his lordship. "It will be a pleasure." He held out his hand, drawing it back rapidly as the dog Aida
made a snap at it. Substituting a long-range leave-taking for the
more intimate farewell, he left the room. When he had gone, Mrs. Pett remained for some minutes, thinking.
She was aflame with excitement. She had a sensational mind, and
it had absorbed Lord Wisbeach's revelations eagerly. Her
admiration for his lordship was intense, and she trusted him
utterly. The only doubt that occurred to her was whether, with
the best intentions in the world, he would be able unassisted to
foil a pair of schemers so distant from each other geographically
as the man who called himself Jimmy Crocker and the man who had
called himself Skinner. That was a point on which they had not
touched, the fact that one impostor was above stairs, the other
below. It seemed to Mrs. Pett impossible that Lord Wisbeach, for
all his zeal, could watch Skinner without neglecting Jimmy or
foil Jimmy without taking his attention off Skinner. It was
manifestly a situation that called for allies. She felt that she
must have further assistance. To Mrs. Pett, doubtless owing to her hobby of writing sensational
fiction, there was a magic in the word detective which was shared
by no other word in the language. She loved detectives--their
keen eyes, their quiet smiles, their Derby hats. When they came
on the stage, she leaned forward in her orchestra chair; when
they entered her own stories, she always wrote with a greater
zest. It is not too much to say that she had an almost spiritual
attachment for detectives, and the idea of neglecting to employ
one in real life, now that circumstances had combined to render
his advent so necessary, struck her as both rash and inartistic.
In the old days, when Ogden had been kidnapped, the only thing
which had brought her balm had been the daily interviews with the
detectives. She ached to telephone for one now. The only consideration that kept her back was a regard for Lord
Wisbeach's feelings. He had been so kind and so shrewd that to
suggest reinforcing him with outside assistance must infallibly
wound him deeply. And yet the situation demanded the services of
a trained specialist. Lord Wisbeach had borne himself during
their recent conversation in such a manner as to leave no doubt
that he considered himself adequate to deal with the matter
single-handed: but admirable though he was he was not a
professional exponent of the art of espionage. He needed to be
helped in spite of himself. A happy solution struck Mrs. Pett. There was no need to tell him.
She could combine the installation of a detective with the nicest
respect for her ally's feelings by the simple process of engaging
one without telling Lord Wisbeach anything about it. The telephone stood at her elbow, concealed--at the express
request of the interior decorator who had designed the room--in
the interior of what looked to the casual eye like a stuffed owl.
On a table near at hand, handsomely bound in morocco to resemble
a complete works of Shakespeare, was the telephone book. Mrs.
Pett hesitated no longer. She had forgotten the address of the
detective agency which she had employed on the occasion of the
kidnapping of Ogden, but she remembered the name, and also the
name of the delightfully sympathetic manager or proprietor or
whatever he was who had listened to her troubles then. She unhooked the receiver, and gave a number. "I want to speak to Mr. Sturgis," she said. "Oh, Mr. Sturgis," said Mrs. Pett. "I wonder if you could
possibly run up here--yes, now. This is Mrs. Peter Pett speaking.
You remember we met some years ago when I was Mrs. Ford. Yes, the
mother of Ogden Ford. I want to consult--You will come up at
once? Thank you so much. Good-bye." Mrs. Pett hung up the receiver.
```

### AI Extraction
- **Primary Mechanism**: `CALLBACK` (Detector Confidence: `0.44`)
- **Secondary Dynamics**: ESCALATION
- **Linguistic Craft Score**: `0.90`
- **Tone**: `LIGHT_SATIRICAL`
- **Setup**: Characters Doctor Briginshaw, Gee establish scene context: 'CHAPTER XVI MRS....'
- **Escalation**: Complication rises around callback: 'Lord Wisbeach hated little dogs....'
- **Reversal**: Expectation or status is inverted: 'This man
pretends to an intimate acquaintance with Skinner....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'Pett hung up the receiver....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 45 — `the_man_upstairs_ch9_06983`

**Source**: *The Man Upstairs* (Chapter 9)  
**Characters Identified**: Dick  
**Dialogue Ratio**: `0.31` | **Surface Slang Isolated**: None  

### Passage
```text
"she sobbed," "Oh! Dick, Dick, I do love you so! I can't live without you! Not another hour, Dick! I do want you so much, so much, Dick!" The man shifted his right arm quickly, slipped a great Mexican knife out of his sleeve, and passed his fingers slowly up the woman's side until he felt the heart beat under his hand, then he raised the knife, gripped the handle tight, and drove the keen blade into the woman's bosom.
```

### AI Extraction
- **Primary Mechanism**: `PHYSICAL_COMPLICATION` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `FARCE`
- **Setup**: Characters Dick establish scene context: '"she sobbed," "Oh!...'
- **Escalation**: Complication rises around physical_complication: 'Dick, Dick, I do love you so!...'
- **Reversal**: Expectation or status is inverted: 'I can't live without you!...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'I do want you so much, so much, Dick!" The man shifted his right arm quickly, sl...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 46 — `right_ho_ch15_04270`

**Source**: *Right Ho* (Chapter 15)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.82` | **Surface Slang Isolated**: None  

### Passage
```text
"To have to come and live in New York! To have to leave my little cottage and take a stuffy, smelly, over-heated hole of an apartment in this Heaven-forsaken, festering Gehenna. To have to mix night after night with a mob who think that life is a sort of St. Vitus's dance, and imagine that they're having a good time because they're making enough noise for six and drinking too much for ten. I loathe New York, [PROTAGONIST]. I wouldn't come near the place if I hadn't got to see editors occasionally. There's a blight on it. It's got moral delirium tremens. It's the limit. The very thought of staying more than a day in it makes me sick. And you call this thing pretty soft for me!," I felt rather like Lot's friends must have done when they dropped in for a quiet chat and their genial host began to criticise the Cities of the Plain.
```

### AI Extraction
- **Primary Mechanism**: `PHYSICAL_COMPLICATION` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.80`
- **Tone**: `FARCE`
- **Setup**: Characters Narrator establish scene context: '"To have to come and live in New York!...'
- **Escalation**: Complication rises around physical_complication: 'To have to mix night after night with a mob who think that life is a sort of St....'
- **Reversal**: Expectation or status is inverted: 'I wouldn't come near the place if I hadn't got to see editors occasionally....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'And you call this thing pretty soft for me!," I felt rather like Lot's friends m...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 47 — `my_man_jeeves_ch15_09914`

**Source**: *My Man Jeeves* (Chapter 15)  
**Characters Identified**: Narrator  
**Dialogue Ratio**: `0.82` | **Surface Slang Isolated**: None  

### Passage
```text
"To have to come and live in New York! To have to leave my little cottage and take a stuffy, smelly, over-heated hole of an apartment in this Heaven-forsaken, festering Gehenna. To have to mix night after night with a mob who think that life is a sort of St. Vitus's dance, and imagine that they're having a good time because they're making enough noise for six and drinking too much for ten. I loathe New York, [PROTAGONIST]. I wouldn't come near the place if I hadn't got to see editors occasionally. There's a blight on it. It's got moral delirium tremens. It's the limit. The very thought of staying more than a day in it makes me sick. And you call this thing pretty soft for me!," I felt rather like Lot's friends must have done when they dropped in for a quiet chat and their genial host began to criticise the Cities of the Plain.
```

### AI Extraction
- **Primary Mechanism**: `PHYSICAL_COMPLICATION` (Detector Confidence: `0.22`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.80`
- **Tone**: `FARCE`
- **Setup**: Characters Narrator establish scene context: '"To have to come and live in New York!...'
- **Escalation**: Complication rises around physical_complication: 'To have to mix night after night with a mob who think that life is a sort of St....'
- **Reversal**: Expectation or status is inverted: 'I wouldn't come near the place if I hadn't got to see editors occasionally....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'And you call this thing pretty soft for me!," I felt rather like Lot's friends m...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 48 — `love_among_the_chickens_ch21_04764`

**Source**: *Love Among The Chickens* (Chapter 21)  
**Characters Identified**: Sergey, Seryozha  
**Dialogue Ratio**: `0.17` | **Surface Slang Isolated**: None  

### Passage
```text
CHAPTER VIII THERE IS DEATH AS WELL AS LIFE Sergey Golovin never thought of death, as though it were something not
to be considered, something that did not concern him in the least. He
was a strong, healthy, cheerful youth, endowed with that calm, clear
joy of living which causes every evil thought and feeling that might
injure life to disappear from the organism without leaving any trace.
Just as all cuts, wounds and stings on his body healed rapidly, so all
that weighed upon his soul and wounded it immediately rose to the
surface and disappeared. And he brought into every work, even into his
enjoyments, the same calm and optimistic seriousness, - it mattered not
whether he was occupied with photography, with bicycling or with
preparations for a terroristic act. Everything in life was joyous,
everything in life was important, everything should be done well. And he did everything well: he was an excellent sailor, an expert shot
with the revolver. He was as faithful in friendship as in love, and a
fanatic believer in the "word of honor." His comrades laughed at him,
saying that if the most notorious spy told him upon his word of honor
that he was not a spy, Sergey would believe him and would shake hands
with him as with any comrade. He had one fault, - he was convinced that
he could sing well, whereas in fact he had no ear for music and even
sang the revolutionary songs out of tune, and felt offended when his
friends laughed at him. "Either you are all asses, or I am an ass," he would declare seriously
and even angrily. And all his friends as seriously declared: "You are
an ass. We can tell by your voice." But, as is sometimes the case with good people, he was perhaps liked
more for this little foible than for his good qualities. He feared death so little and thought of it so little that on the fatal
morning, before leaving the house of Tanya Kovalchuk, he was the only
one who had breakfasted properly, with an appetite. He drank two
glasses of tea with milk, and a whole five-copeck roll of bread. Then
he glanced at Werner's untouched bread and said: "Why don't you eat? Eat. We must brace up." "I don't feel like eating." "Then I'll eat it. May I?" "You have a fine appetite, Seryozha." Instead of answering, Sergey, his mouth full, began to sing in a dull
voice, out of tune: "Hostile whirlwinds are blowing over us..." After the arrest he at first grew sad; the work had not been done well,
they had failed; but then he thought: "There is something else now that
must be done well - and that is, to die," and he cheered up again. And
however strange it may seem, beginning with the second morning in the
fortress, he commenced devoting himself to gymnastics according to the
unusually rational system of a certain German named Müller, which
absorbed his interest. He undressed himself completely and, to the
alarm and astonishment of the guard who watched him, he carefully went
through all the prescribed eighteen exercises. The fact that the guard
watched him and was apparently astonished, pleased him as a
propagandist of the Müller system; and although he knew that he would
get no answer he nevertheless spoke to the eye staring in the little
window: "It's a good system, my friend, it braces you up. It should be
introduced in your regiment," he shouted convincingly and kindly, so as
not to frighten the soldier, not suspecting that the guard considered
him a harmless lunatic. The fear of death came over him gradually. It was as if somebody were
striking his heart a powerful blow with the fist from below. This
sensation was rather painful than terrible. Then the sensation was
forgotten, but it returned again a few hours later, and each time it
grew more intense and of longer duration, and thus it began to assume
vague outlines of some great, even unbearable fear. "Is it possible that I am afraid?" thought Sergey in astonishment.
"What nonsense!" It was not he who was afraid, - it was his young, sound, strong body,
which could not be deceived either by the exercises prescribed by the
Müller system, or by the cold rub-downs. On the contrary, the stronger
and the fresher his body became after the cold water, the keener and
the more unbearable became the sensations of his recurrent fear. And
just at those moments when, during his freedom, he had felt a special
influx of the joy and power of life, - in the mornings after he had slept
soundly and gone through his physical exercises, - now there appeared
this deadening fear which was so foreign to his nature. He noticed this
and thought: "It is foolish, Sergey! To die more easily, you should weaken the body
and not strengthen it. It is foolish!" So he dropped his gymnastics and the rub-downs. To the soldier he
shouted, as if to explain and justify himself: "Never mind that I have stopped. It's a good thing, my friend, - but not
for those who are to be hanged. But it's very good for all others." And, indeed, he began to feel somewhat better. He tried also to eat
less, so as to grow still weaker, but notwithstanding the lack of pure
air and exercises, his appetite was very good, - it was difficult for him
to control it, and he ate everything that was brought to him. Then he
began to manage differently - before starting to eat he would pour out
half into the pail, and this seemed to work. A dull drowsiness and
faintness came over him. "I'll show you what I can do!" he threatened his body, and at the same
time sadly, yet tenderly he felt his flabby, softened muscles with his
hand. Soon, however, his body grew accustomed to this regime as well, and the
fear of death appeared again - not so keen, nor so burning, but more
disgusting, somewhat akin to a nauseating sensation. "It's because they
are dragging it out so long," thought Sergey. "It would be a good idea
to sleep all the time till the day of the execution," and he tried to
sleep as much as possible. At first he succeeded, but later, either
because he had slept too much, or for some other reason, insomnia
appeared. And with it came eager, penetrating thoughts and a longing
for life. "I am not afraid of this devil!" he thought of Death. "I simply feel
sorry for my life. It is a splendid thing, no matter what the
pessimists say about it. What if they were to hang a pessimist? Ah, I
feel sorry for life, very sorry! And why does my beard grow now? It
didn't grow before, but suddenly it grows - why?" He shook his head mournfully, heaving long, painful sighs. Silence - then
a sigh; then a brief silence again - followed by a longer, deeper sigh. Thus it went on until the trial and the terrible meeting with his
parents. When he awoke in his cell the next day he realized clearly
that everything between him and life was ended, that there were only a
few empty hours of waiting and then death would come, - and a strange
sensation took possession of him. He felt as though he had been
stripped, stripped entirely, - as if not only his clothes, but the sun,
the air, the noise of voices and his ability to do things had been
wrested from him. Death was not there as yet, but life was there no
longer, - there was something new, something astonishing, inexplicable,
not entirely reasonable and yet not altogether without
meaning, - something so deep and mysterious and supernatural that it was
impossible to understand. "Fie, you devil!" wondered Sergey, painfully. "What is this? Where am
I? I - who am I?" He examined himself attentively, with interest, beginning with his
large prison slippers, ending with his stomach where his coat
protruded. He paced the cell, spreading out his arms and continuing to
survey himself like a woman in a new dress which is too long for her.
He tried to turn his head, and it turned. And this strange, terrible,
uncouth creature was he, Sergey Golovin, and soon he would be no more! Everything became strange. He tried to walk across the cell - and it seemed strange to him that he
could walk. He tried to sit down - and it seemed strange to him that he
could sit. He tried to drink some water - and it seemed strange to him
that he could drink, that he could swallow, that he could hold the cup,
that he had fingers and that those fingers were trembling. He choked,
began to cough and while coughing, thought: "How strange it is that I
am coughing." "Am I losing my reason?" thought Sergey, growing cold. "Am I coming to
that, too? The devil take them!" He rubbed his forehead with his hand, and this also seemed strange to
him. And then he remained breathless, motionless, petrified for hours,
suppressing every thought, all loud breathing, all motion, - for every
thought seemed to him but madness, every motion - madness. Time was no
more; it appeared transformed into space, airless and transparent, into
an enormous square upon which all were there - the earth and life and
people. He saw all that at one glance, all to the very end, to the
mysterious abyss - Death. And he was tortured not by the fact that Death
was visible, but that both Life and Death were visible at the same
time. The curtain which through eternity has hidden the mystery of life
and the mystery of death was pushed aside by a sacrilegious hand, and
the mysteries ceased to be mysteries - yet they remained
incomprehensible, like the Truth written in a foreign tongue. There
were no conceptions in his human mind, no words in his human language
that could define what he saw. And the words "I am afraid" were uttered
by him only because there were no other words, because no other
conceptions existed, nor could other conceptions exist which would
grasp this new, un-human condition. Thus would it be with a man if,
while remaining within the bounds of human reason, experience and
feelings, he were suddenly to see God Himself. He would see Him but
would not understand, even though he knew that it was God, and he would
tremble with inconceivable sufferings of incomprehension. "There is Müller for you!" he suddenly uttered loudly, with extreme
conviction, and shook his head. And with that unexpected break in his
feelings, of which the human soul is so capable, he laughed heartily
and cheerfully. "Oh, Müller! My dear Müller! Oh, you splendid German! After all you are
right, Müller, and I am an ass!" He paced the cell quickly several times and to the great astonishment
of the soldier who was watching him through the peephole, he quickly
undressed himself and cheerfully went through all the eighteen
exercises with the greatest care. He stretched and expanded his young,
somewhat emaciated body, sat down for a moment, drew deep breaths of
air and exhaled it, stood up on tip-toe, stretched his arms and his
feet. And after each exercise he announced, with satisfaction: "That's it! That's the real way, Müller!" His cheeks flushed; drops of
warm, pleasant perspiration came from the pores of his body, and his
heart beat soundly and evenly. "The fact is, Müller," philosophized Sergey, expanding his chest so
that the ribs under his thin, tight skin were outlined clearly, - "the
fact is, that there is a nineteenth exercise - to hang by the neck
motionless. That is called execution. Do you understand, Müller? They
take a live man, let us say Sergey Golovin, they swaddle him as a doll
and they hang him by the neck until he is dead. It is a foolish
exercise, Müller, but it can't be helped, - we have to do it." He bent over on the right side and repeated: "We have to do it, Müller."
```

### AI Extraction
- **Primary Mechanism**: `PHYSICAL_COMPLICATION` (Detector Confidence: `0.44`)
- **Secondary Dynamics**: MISUNDERSTANDING
- **Linguistic Craft Score**: `0.75`
- **Tone**: `FARCE`
- **Setup**: Characters Sergey, Seryozha establish scene context: 'CHAPTER VIII THERE IS DEATH AS WELL AS LIFE Sergey Golovin never thought of deat...'
- **Escalation**: Complication rises around physical_complication: 'This
sensation was rather painful than terrible....'
- **Reversal**: Expectation or status is inverted: 'It is a splendid thing, no matter what the
pessimists say about it....'
- **Payoff**: Comedic resolution or deadpan beat lands: 'It is a foolish
exercise, Müller, but it can't be helped, - we have to do it." H...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 49 — `something_fresh_ch2_07118`

**Source**: *Something Fresh* (Chapter 2)  
**Characters Identified**: Dickie, Freddie, Frederick, Lord Emsworth, Mr Lloyd, Mr Peters, Threepwood  
**Dialogue Ratio**: `0.23` | **Surface Slang Isolated**: old top, dash it, deuced, ripping, corking  

### Passage
```text
CHAPTER II In a bedroom on the fourth floor of the Hotel Guelph in
Piccadilly, the Honorable Frederick Threepwood sat in bed, with
his knees drawn up to his chin, and glared at the day with the
glare of mental anguish. He had very little mind, but what he had
was suffering. He had just remembered. It is like that in this life. You wake
up, feeling as fit as a fiddle; you look at the window and see
the sun, and thank Heaven for a fine day; you begin to plan a
perfectly corking luncheon party with some of the chappies you
met last night at the National Sporting Club; and then--you
remember. "Oh, dash it!" said the Honorable Freddie. And after a moment's
pause: "And I was feeling so dashed happy!" For the space of some minutes he remained plunged in sad
meditation; then, picking up the telephone from the table at his
side, he asked for a number. "Hello!" "Hello!" responded a rich voice at the other end of the wire. "Oh, I say! Is that you, Dickie?" "Who is that?" "This is Freddie Threepwood. I say, Dickie, old top, I want to
see you about something devilish important. Will you be in at
twelve?" "Certainly. What's the trouble?" "I can't explain over the wire; but it's deuced serious." "Very well. By the way, Freddie, congratulations on the
engagement." "Thanks, old man. Thanks very much, and so on--but you won't
forget to be in at twelve, will you? Good-by." He replaced the receiver quickly and sprang out of bed, for he
had heard the door handle turn. When the door opened he was
giving a correct representation of a young man wasting no time in
beginning his toilet for the day. An elderly, thin-faced, bald-headed, amiably vacant man entered.
He regarded the Honorable Freddie with a certain disfavor. "Are you only just getting up, Frederick?" "Hello, gov'nor. Good morning. I shan't be two ticks now." "You should have been out and about two hours ago. The day is
glorious." "Shan't be more than a minute, gov'nor, now. Just got to have a
tub and then chuck on a few clothes." He disappeared into the bathroom. His father, taking a chair,
placed the tips of his fingers together and in this attitude
remained motionless, a figure of disapproval and suppressed
annoyance. Like many fathers in his rank of life, the Earl of Emsworth had
suffered much through that problem which, with the exception of
Mr. Lloyd-[COMPANION_B], is practically the only fly in the British
aristocratic amber--the problem of what to do with the younger
sons. It is useless to try to gloss over the fact--in the aristocratic
families of Great Britain the younger son is not required. Apart, however, from the fact that he was a younger son, and, as
such, a nuisance in any case, the honorable Freddie had always
annoyed his father in a variety of ways. The Earl of Emsworth was
so constituted that no man or thing really had the power to
trouble him deeply; but Freddie had come nearer to doing it than
anybody else in the world. There had been a consistency, a
perseverance, about his irritating performances that had acted on
the placid peer as dripping water on a stone. Isolated acts of
annoyance would have been powerless to ruffle his calm; but
Freddie had been exploding bombs under his nose since he went to
Eton. He had been expelled from Eton for breaking out at night and
roaming the streets of Windsor in a false mustache. He had been
sent down from Oxford for pouring ink from a second-story window
on the junior dean of his college. He had spent two years at an
expensive London crammer's and failed to pass into the army. He
had also accumulated an almost record series of racing debts,
besides as shady a gang of friends--for the most part vaguely
connected with the turf--as any young man of his age ever
contrived to collect. These things try the most placid of parents; and finally Lord
Emsworth had put his foot down. It was the only occasion in his
life when he had acted with decision, and he did it with the
accumulated energy of years. He stopped his son's allowance,
haled him home to Blandings Castle, and kept him there so
relentlessly that until the previous night, when they had come up
together by an afternoon train, Freddie had not seen London for
nearly a year. Possibly it was the reflection that, whatever his secret
troubles, he was at any rate once more in his beloved metropolis
that caused Freddie at this point to burst into discordant song.
He splashed and warbled simultaneously. Lord Emsworth's frown deepened and he began to tap his fingers
together irritably. Then his brow cleared and a pleased smile
flickered over his face. He, too, had remembered. What Lord Emsworth remembered was this: Late in the previous
autumn the next estate to Blandings had been rented by an
American, a Mr. Peters--a man with many millions, chronic
dyspepsia, and one fair daughter--Aline. The two families had
met. Freddie and Aline had been thrown together; and, only a few
days before, the engagement had been announced. And for Lord
Emsworth the only flaw in this best of all possible worlds had
been removed. Yes, he was glad Freddie was engaged to be married to Aline
Peters. He liked Aline. He liked Mr. Peters. Such was the relief
he experienced that he found himself feeling almost affectionate
toward Freddie, who emerged from the bathroom at this moment,
clad in a pink bathrobe, to find the paternal wrath evaporated,
and all, so to speak, right with the world. Nevertheless, he wasted no time about his dressing. He was always
ill at ease in his father's presence and he wished to be
elsewhere with all possible speed. He sprang into his trousers
with such energy that he nearly tripped himself up. As he
disentangled himself he recollected something that had slipped
his memory. "By the way, gov'nor, I met an old pal of mine last night and
asked him down to Blandings this week. That's all right, isn't
it? He's a man named Emerson, an American. He knows Aline quite
well, he says--has known her since she was a kid." "I do not remember any friend of yours named Emerson." "Well, as a matter of fact, I met him last night for the first
time. But it's all right. He's a good chap, don't you know!
--and all that sort of rot." Lord Emsworth was feeling too benevolent to raise the objections
he certainly would have raised had his mood been less sunny. "Certainly; let him come if he wishes." "Thanks, gov'nor." Freddie completed his toilet. "Doing anything special this morning, gov'nor? I rather thought
of getting a bit of breakfast and then strolling round a bit.
Have you had breakfast?" "Two hours ago. I trust that in the course of your strolling you
will find time to call at Mr. Peters' and see Aline. I shall be
going there directly after lunch. Mr. Peters wishes to show me
his collection of--I think scarabs was the word he used." "Oh, I'll look in all right! Don't you worry! Or if I don't I'll
call the old boy up on the phone and pass the time of day. Well,
I rather think I'll be popping off and getting that bit of
breakfast--what?" Several comments on this speech suggested themselves to Lord
Emsworth. In the first place, he did not approve of Freddie's
allusion to one of America's merchant princes as "the old boy."
Second, his son's attitude did not strike him as the ideal
attitude of a young man toward his betrothed. There seemed to be
a lack of warmth. But, he reflected, possibly this was simply
another manifestation of the modern spirit; and in any case it
was not worth bothering about; so he offered no criticism. Presently, Freddie having given his shoes a flick with a silk
handkerchief and thrust the latter carefully up his sleeve, they
passed out and down into the main lobby of the hotel, where they
parted--Freddie to his bit of breakfast; his father to potter
about the streets and kill time until luncheon. London was always
a trial to the Earl of Emsworth. His heart was in the country and
the city held no fascinations for him.
```

### AI Extraction
- **Primary Mechanism**: `PHYSICAL_COMPLICATION` (Detector Confidence: `0.44`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.75`
- **Tone**: `FARCE`
- **Setup**: Characters Dickie, Freddie establish scene context: 'CHAPTER II In a bedroom on the fourth floor of the Hotel Guelph in
Piccadilly, t...'
- **Escalation**: Complication rises around physical_complication: 'Good morning....'
- **Reversal**: Expectation or status is inverted: 'Lord Emsworth's frown deepened and he began to tap his fingers
together irritabl...'
- **Payoff**: Comedic resolution or deadpan beat lands: 'His heart was in the country and
the city held no fascinations for him....'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---

## Example 50 — `right_ho_ch18_07025`

**Source**: *Right Ho* (Chapter 18)  
**Characters Identified**: Aunt Off, Sir It  
**Dialogue Ratio**: `0.74` | **Surface Slang Isolated**: None  

### Passage
```text
and I was back in the old flat, lying in the old arm-chair, with my feet upon the good old table. I had just come from seeing dear old Rocky off to his country cottage, and an hour before he had seen his aunt off to whatever hamlet it was that she was the curse of; so we were alone at last. "[COMPANION], there's no place like home - what?" "Very true, sir." "The jolly old roof-tree, and all that sort of thing - what?" "Precisely, sir." I lit another cigarette. "[COMPANION]." "Sir?" "Do you know, at one point in the business I really thought you were baffled." "Indeed, sir?" "When did you get the idea of taking Miss [FRIEND] to the meeting? It was pure genius!" "Thank you, sir. It came to me a little suddenly, one morning when I was thinking of my aunt, sir." "Your aunt? The hansom cab one?" "Yes, sir. I recollected that, whenever we observed one of her attacks coming on, we used to send for the clergyman of the parish. We always found that if he talked to her a while of higher things it diverted her mind from hansom cabs. It occurred to me that the same treatment might prove efficacious in the case of Miss [FRIEND]." I was stunned by the man's resource. "It's brain," I said; "pure brain! What do you do to get like that, [COMPANION]? I believe you must eat a lot of fish, or something. Do you eat a lot of fish, [COMPANION]?" "No, sir." "Oh, well, then, it's just a gift, I take it; and if you aren't born that way there's no use worrying." "Precisely, sir," said [COMPANION]. "If I might make the suggestion, sir, I should not continue to wear your present tie. The green shade gives you a slightly bilious air. I should strongly advocate the blue with the red domino pattern instead, sir." "All right, [COMPANION]." I said humbly. "You know!" THE END
```

### AI Extraction
- **Primary Mechanism**: `STATUS_REVERSAL` (Detector Confidence: `0.57`)
- **Secondary Dynamics**: None
- **Linguistic Craft Score**: `0.95`
- **Tone**: `DRY_WIT`
- **Setup**: Characters Aunt Off, Sir It establish scene context: 'and I was back in the old flat, lying in the old arm-chair, with my feet upon th...'
- **Escalation**: Complication rises around status_reversal: 'It was pure genius!" "Thank you, sir....'
- **Reversal**: Expectation or status is inverted: 'It occurred to me that the same treatment might prove efficacious in the case of...'
- **Payoff**: Comedic resolution or deadpan beat lands: '"You know!" THE END...'

### Human Verification Form
```text
[ ] AGREEMENT VERDICT       : [ AGREE | PARTIAL | DISAGREE ]
[ ] HUMAN PRIMARY MECHANISM : _________________________
[ ] HUMAN SECONDARY MECHS   : [ List comma-separated secondary mechanisms ]
[ ] HUMAN SETUP ACCURATE    : [ YES | NO | PARTIAL ]
[ ] HUMAN ESCALATION ACCURATE: [ YES | NO | PARTIAL ]
[ ] HUMAN REVERSAL ACCURATE : [ YES | NO | PARTIAL ]
[ ] HUMAN PAYOFF ACCURATE   : [ YES | NO | PARTIAL ]
[ ] HUMAN LITERARY QUALITY  : [ 1 - 10 ] (How good is the prose as comedy)
[ ] HUMAN TRAINING VALUE    : [ 1 - 10 ] (How transferable is the comic construction)
[ ] HUMAN MECHANISM CERTAINTY: [ 1 - 10 ]
[ ] DISAGREEMENT CATEGORY   : [ A_DETECTOR_FAILURE | B_TAXONOMY_AMBIGUITY | C_HUMAN_DISAGREEMENT | D_SOURCE_AMBIGUITY | E_COMPETING_MECHANISMS | F_REJECT_EXAMPLE ]
[ ] HUMAN AUDIT NOTES       : _________________________
```

---
