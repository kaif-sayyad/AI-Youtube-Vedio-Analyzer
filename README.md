# 🎥 AI YouTube Video Analyzer

An Agentic AI application that analyzes YouTube videos and generates intelligent summaries, key insights, and takeaways using Large Language Models (LLMs). Built with the Agno Framework for AI agent orchestration and Streamlit for an interactive user interface.

---

## 🚀 Features

- 🔗 Analyze any public YouTube video using its URL
- 🤖 AI-powered video understanding and summarization
- 📝 Generates concise summaries
- 💡 Extracts key insights and important points
- ⚡ Fast inference using Groq API
- 🎨 Clean and interactive Streamlit UI
- 🧠 Agent-based architecture using Agno Framework

---

## 🛠️ Tech Stack

- **Framework:** Agno
- **Language:** Python
- **UI:** Streamlit
- **LLM:** Qwen/Qwen3-32B
- **Inference API:** Groq API (OpenAI-Compatible)
- **Environment:** Python Virtual Environment

---

## 📂 Project Structure

```
AI-YouTube-Video-Analyzer/
│
├── agent.py          # AI Agent implementation
├── ui.py             # Streamlit frontend
├── .env
├── README.md

```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-YouTube-Video-Analyzer.git

cd AI-YouTube-Video-Analyzer
```



## 🔑 Environment Variables

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run ui.py
```

The application will open automatically in your browser.

---

## 🖥️ Demo

1. Paste a YouTube video URL.
2. Click **Analyze**.
3. Wait for the AI agent to process the video.
4. View the generated summary and insights.

---

## 🧠 How It Works

1. User enters a YouTube video URL.
2. The Agno AI Agent processes the request.
3. The agent sends the prompt to **Qwen/Qwen3-32B** through the **Groq API**.
4. The LLM analyzes the video content.
5. The generated summary and insights are displayed in the Streamlit interface.

---


---

## 🔮 Future Improvements

- Chat with the analyzed video
- PDF report generation
- Multi-video comparison
- Support for playlists
- Voice interaction
- Export analysis as PDF or Markdown

---



**Kaif Sayyad**

If you found this project helpful, feel free to ⭐ the repository and connect with me on LinkedIn!
