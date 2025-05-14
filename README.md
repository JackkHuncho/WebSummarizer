# Web Summarizer

A lightweight CLI tool that scrapes a website’s main content and generates a concise Markdown summary using a local Ollama language model.

---

## 🔍 Features

- **Website scraping**: Removes navigation, scripts, styles, images, and inputs to focus on core text.
- **AI-powered summaries**: Leverages a local Ollama model (e.g., `llama3.2`) to produce readable, Markdown-formatted summaries.
- **Interactive CLI**: Simple prompt-driven interface—enter URLs one at a time, or quit with `q`.
- **Minimal dependencies**: Pure Python, no Jupyter required.

---

## ⚙️ Prerequisites

- **Python 3.8+**
- **Ollama CLI** installed and on your system `$PATH` (see: https://ollama.com/docs#install)

---

## 🚀 Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourname/web-summarizer.git
cd web-summarizer

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Pull the Ollama model
ollama pull llama3.2
```

---

## 💻 Usage

```bash
# Run the summarizer script
python WebSummarizer.py

# Or, make it executable:
chmod +x WebSummarizer.py
./WebSummarizer.py
```

1. **Enter a URL** at the prompt and press **Enter**.
2. Wait for the AI to fetch, analyze, and print a Markdown summary.
3. To quit, type **`q`** or **`quit`**.

---

## 📦 requirements.txt

```text
requests
beautifulsoup4
ipython
```

---

## 🤝 Contributing

1. Fork this repository.
2. Create a feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request and describe your changes.

Please follow the existing code style and write clear commit messages.

---

