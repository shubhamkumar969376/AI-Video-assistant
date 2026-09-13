# 🎥 AI Video Assistant

An AI-powered video assistant that converts video/audio content into **searchable, understandable, and interactive knowledge**.

The project processes video content, extracts the audio, generates a transcript, and uses **AI + Retrieval-Augmented Generation (RAG)** to allow users to ask questions about the content.

---

## 🚀 Features

* 🎬 **Video/Audio Processing** — Process video and audio files.
* 🎙️ **Speech-to-Text** — Convert spoken content into text.
* 📝 **Automatic Summarization** — Generate concise summaries from long videos.
* 🔍 **Semantic Search** — Find relevant information from the transcript.
* 💬 **AI Q&A** — Ask questions about the video and get context-aware answers.
* 🧠 **RAG Pipeline** — Retrieves relevant transcript information before generating answers.
* 📚 **Long Video Support** — Break large transcripts into smaller chunks for efficient retrieval.
* ⚡ **AI-powered Analysis** — Extract useful information from unstructured video content.

---

## 🧠 How It Works

The application follows an AI-powered processing pipeline:

```text
             Video / Audio
                   │
                   ▼
          Audio Extraction
                   │
                   ▼
          Speech-to-Text
                   │
                   ▼
             Transcript
                   │
                   ▼
           Text Chunking
                   │
                   ▼
          Vector Embeddings
                   │
                   ▼
           Vector Database
                   │
                   ▼
             User Question
                   │
                   ▼
        Similarity Retrieval
                   │
                   ▼
             LLM + Context
                   │
                   ▼
             AI Answer
```

The RAG architecture helps the assistant answer questions using information from the actual video instead of relying only on the model's general knowledge.

---

## 🛠️ Tech Stack

### AI / Machine Learning

* Python
* Speech-to-Text
* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Embeddings
* Semantic Search

### Backend / Processing

* Python
* Audio/Video Processing
* LangChain

### Database / Retrieval

* Vector Database
* Vector Embeddings
* Similarity Search

### Tools

* Git
* GitHub
* FFmpeg

---

## 📂 Project Structure

```text
AI-Video-assistant/
│
├── core/
│   ├── ...
│   └── ...
│
├── utils/
│   └── ...
│
├── downloads/
│
├── test.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/shubhamkumar969376/AI-Video-assistant.git
```

```bash
cd AI-Video-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Keys

Create a `.env` file and add the required API credentials.

```env
API_KEY=your_api_key
```

> Never commit your `.env` file or API keys to GitHub.

---

## ▶️ Running the Project

After installing the dependencies, run the application using the appropriate Python entry point.

```bash
python test.py
```

---

## 💡 Example Use Cases

This project can be useful for:

* 🎓 **Educational Videos** — Quickly understand long lectures.
* 🧑‍💼 **Meetings** — Search conversations and retrieve important information.
* 🎙️ **Podcasts** — Ask questions about podcast episodes.
* 📺 **YouTube Videos** — Summarize and interact with video content.
* 📚 **Research** — Search large amounts of spoken information.
* 📝 **Interviews** — Extract relevant information from recorded interviews.

---

## 🔥 Why RAG?

A normal LLM may not know the specific information contained inside a user's video.

RAG solves this problem by:

1. Converting the video into text.
2. Splitting the transcript into smaller chunks.
3. Creating vector embeddings for those chunks.
4. Storing the embeddings in a vector database.
5. Finding the most relevant chunks for a user's question.
6. Sending the retrieved context to the LLM.
7. Generating an answer based on the video content.

This makes the assistant **context-aware and grounded in the uploaded content**.

---

## 📈 Future Improvements

* [ ] Add a web-based frontend
* [ ] Support multiple video formats
* [ ] Improve multilingual transcription
* [ ] Add timestamp-based answers
* [ ] Add video chapter generation
* [ ] Add automatic action-item extraction
* [ ] Add speaker identification
* [ ] Add conversation history
* [ ] Deploy the application online
* [ ] Improve RAG retrieval accuracy

---

## 👨‍💻 Author

**Shubham Kumar**

GitHub: [@shubhamkumar969376](https://github.com/shubhamkumar969376)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

Contributions, suggestions, and improvements are welcome!
