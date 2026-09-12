// AI Author Studio — Local Editor Frontend Script

document.addEventListener("DOMContentLoaded", () => {
  let currentBookSlug = "";
  let currentChapterIndex = null;

  // DOM Elements
  const bookSelector = document.getElementById("book-selector");
  const chapterList = document.getElementById("chapter-list");
  const chapterHeading = document.getElementById("chapter-heading");
  const wordCountBadge = document.getElementById("word-count-badge");
  const chapterTextarea = document.getElementById("chapter-textarea");
  const btnSaveChapter = document.getElementById("btn-save-chapter");
  const btnExport = document.getElementById("btn-export");
  const btnRunAI = document.getElementById("btn-run-ai");
  const btnInsertAI = document.getElementById("btn-insert-ai");
  const aiTaskSelect = document.getElementById("ai-task");
  const aiInstructionInput = document.getElementById("ai-instruction");
  const aiOutputBox = document.getElementById("ai-output");

  const storyInfo = document.getElementById("story-info");
  const characterInfo = document.getElementById("character-info");
  const plotInfo = document.getElementById("plot-info");

  // Tab Navigation
  document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));

      btn.classList.add("active");
      document.getElementById(btn.dataset.tab).classList.add("active");
    });
  });

  // Fetch Available Books
  async function loadBooks() {
    try {
      const res = await fetch("/api/books");
      const books = await res.json();

      bookSelector.innerHTML = "";
      if (books.length === 0) {
        bookSelector.innerHTML = '<option value="">No books found</option>';
        return;
      }

      books.forEach(b => {
        const opt = document.createElement("option");
        opt.value = b.slug;
        opt.textContent = `${b.title} (${b.total_chapters} chaps)`;
        bookSelector.appendChild(opt);
      });

      currentBookSlug = books[0].slug;
      loadBookDetails(currentBookSlug);
    } catch (e) {
      console.error("Failed to load books", e);
    }
  }

  bookSelector.addEventListener("change", (e) => {
    currentBookSlug = e.target.value;
    if (currentBookSlug) {
      loadBookDetails(currentBookSlug);
    }
  });

  // Load Book Details & Knowledge Panels
  async function loadBookDetails(slug) {
    try {
      const res = await fetch(`/api/books/${slug}`);
      const data = await res.json();

      renderChapterList(data.chapters || []);
      renderStoryKnowledge(data.story_analysis);
      renderCharacterKnowledge(data.character_analysis);
      renderPlotKnowledge(data.plot_analysis);

      if (data.chapters && data.chapters.length > 0) {
        loadChapter(slug, data.chapters[0].index);
      }
    } catch (e) {
      console.error("Failed to load book details", e);
    }
  }

  function renderChapterList(chapters) {
    chapterList.innerHTML = "";
    if (chapters.length === 0) {
      chapterList.innerHTML = '<li class="empty-state">No chapters found.</li>';
      return;
    }

    chapters.forEach(c => {
      const li = document.createElement("li");
      li.textContent = `${c.title || 'Chapter ' + c.index} (${c.word_count || 0} w)`;
      li.dataset.index = c.index;
      li.addEventListener("click", () => {
        document.querySelectorAll("#chapter-list li").forEach(l => l.classList.remove("active"));
        li.classList.add("active");
        loadChapter(currentBookSlug, c.index);
      });
      chapterList.appendChild(li);
    });

    chapterList.children[0].classList.add("active");
  }

  // Load Single Chapter
  async function loadChapter(slug, index) {
    currentChapterIndex = index;
    try {
      const res = await fetch(`/api/books/${slug}/chapters/${index}`);
      const data = await res.json();

      chapterHeading.textContent = data.chapter_title || `Chapter ${index}`;
      
      const paragraphs = [];
      (data.scenes || []).forEach(scene => {
        (scene.paragraphs || []).forEach(p => paragraphs.push(p.text));
      });

      const fullText = paragraphs.join("\n\n");
      chapterTextarea.value = fullText;
      updateWordCount(fullText);
    } catch (e) {
      console.error("Failed to load chapter", e);
    }
  }

  function updateWordCount(text) {
    const words = text.trim() ? text.trim().split(/\s+/).length : 0;
    wordCountBadge.textContent = `${words} Words`;
  }

  chapterTextarea.addEventListener("input", () => {
    updateWordCount(chapterTextarea.value);
  });

  // Save Edits
  btnSaveChapter.addEventListener("click", async () => {
    if (!currentBookSlug || !currentChapterIndex) return;

    try {
      const res = await fetch(`/api/books/${currentBookSlug}/chapters/${currentChapterIndex}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: chapterTextarea.value }),
      });

      if (res.ok) {
        alert(`Successfully saved Chapter ${currentChapterIndex}!`);
        loadBookDetails(currentBookSlug);
      }
    } catch (e) {
      alert("Failed to save chapter.");
    }
  });

  // Render Knowledge Panels
  function renderStoryKnowledge(sa) {
    if (!sa) {
      storyInfo.innerHTML = '<div class="empty-state">No story analysis available.</div>';
      return;
    }
    storyInfo.innerHTML = `
      <div class="item-list">
        <li><strong>POV:</strong> ${sa.narrative_pov?.value || 'N/A'}</li>
        <li><strong>Tone:</strong> ${sa.overall_tone?.value || 'N/A'}</li>
        <li><strong>Pacing:</strong> ${sa.overall_pacing?.value || 'N/A'}</li>
      </div>
    `;
  }

  function renderCharacterKnowledge(ca) {
    if (!ca || !ca.characters) {
      characterInfo.innerHTML = '<div class="empty-state">No character analysis available.</div>';
      return;
    }

    characterInfo.innerHTML = ca.characters.map(c => `
      <div class="item-list margin-top">
        <li><strong>${c.name}</strong></li>
        <li><em>Traits:</em> ${(c.personality || []).map(p => p.value).join(', ')}</li>
      </div>
    `).join('');
  }

  function renderPlotKnowledge(pa) {
    if (!pa || !pa.plot_points) {
      plotInfo.innerHTML = '<div class="empty-state">No plot analysis available.</div>';
      return;
    }

    const points = pa.plot_points;
    plotInfo.innerHTML = Object.keys(points).map(k => `
      <div class="item-list margin-top">
        <li><strong>${k.replace('_', ' ').toUpperCase()}:</strong> ${points[k].value}</li>
      </div>
    `).join('');
  }

  // AI Assistant Execution
  btnRunAI.addEventListener("click", async () => {
    const task = aiTaskSelect.value;
    const instruction = aiInstructionInput.value;
    const text = chapterTextarea.value;

    aiOutputBox.textContent = "AI is thinking...";

    try {
      const res = await fetch("/api/ai_assist", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task, instruction, text }),
      });

      const data = await res.json();
      aiOutputBox.textContent = data.result || "No response generated.";
    } catch (e) {
      aiOutputBox.textContent = "Error executing AI command.";
    }
  });

  btnInsertAI.addEventListener("click", () => {
    const suggestion = aiOutputBox.textContent;
    if (suggestion && !suggestion.startsWith("Select an AI") && !suggestion.startsWith("Error")) {
      chapterTextarea.value += "\n\n" + suggestion;
      updateWordCount(chapterTextarea.value);
    }
  });

  // Export Manuscript
  btnExport.addEventListener("click", async () => {
    if (!currentBookSlug) return;
    try {
      const res = await fetch(`/api/books/${currentBookSlug}/export`, { method: "POST" });
      const data = await res.json();
      alert(`Manuscript exported to: ${data.export_path}`);
    } catch (e) {
      alert("Failed to export manuscript.");
    }
  });

  // Init
  loadBooks();
});
