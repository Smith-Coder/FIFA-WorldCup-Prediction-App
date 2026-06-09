# ⚽ FIFA Prediction Chatbot

An AI-powered full-stack chatbot that delivers intelligent FIFA match predictions using real-time football data and Large Language Models (LLMs).

> Note: This project is for educational purposes. Contributions, improvements, and bug reports are welcome — feel free to open issues or submit pull requests.

Built with **FastAPI**, **React**, **API-Football**, and **Gemini/OpenAI-compatible APIs**, the application provides a conversational experience similar to ChatGPT for football fans and analysts.

---

## 🚀 Features

### 🤖 AI-Powered Match Predictions

Generate insightful match predictions using advanced LLMs such as Gemini or any OpenAI-compatible model.

### ⚽ Real-Time Football Data

Fetch live and upcoming match information using API-Football.

### 💬 Chat-Based User Experience

Interactive ChatGPT-style interface for seamless football-related conversations.

### 📝 Markdown Response Rendering

Display AI-generated predictions and analysis with rich markdown formatting.

### 🧠 Intelligent Query Handling

Supports natural language queries such as:

* `Today's matches`
* `Tomorrow's matches`
* `Predict Brazil vs Germany`
* `Predict all matches today`
* `Show upcoming FIFA fixtures`

---

## 🏗️ Tech Stack

### Backend

* FastAPI (Python)
* OpenAI-Compatible Client
* Google Gemini API
* API-Football (Fixtures & Match Data)

### Frontend

* React
* Axios
* react-markdown

---

## 🔑 APIs Used

### 1. Large Language Model (LLM)

The application uses Gemini by default but can easily be configured to work with any OpenAI-compatible provider.

#### Environment Variable

```env
GOOGLE_API_KEY=your_llm_api_key
```

#### Switching to Another LLM

Simply update:

* `base_url`
* `model`

No major code changes are required.

---

### 2. API-Football

Provides real-time football fixtures, match schedules, and live data.

#### Sign Up

https://www.api-football.com/

#### Environment Variable

```env
API_FOOTBALL_KEY=your_api_football_key
```

---

## ⚙️ Installation & Setup

### Backend Setup

#### 1. Navigate to Backend Directory

```bash
cd backend
```

#### 2. Create Virtual Environment

```bash
python -m venv venv
```

#### 3. Activate Virtual Environment

##### macOS / Linux

```bash
source venv/bin/activate
```

##### Windows

```bash
venv\Scripts\activate
```

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 5. Create `.env` File

```env
GOOGLE_API_KEY=your_gemini_api_key
API_FOOTBALL_KEY=your_api_football_key
```

#### 6. Start Backend Server

```bash
uvicorn main:app --reload
```

Backend will be available at:

```text
http://127.0.0.1:8000
```

---

## ⚛️ Frontend Setup

#### 1. Navigate to Frontend Directory

```bash
cd frontend
```

#### 2. Install Dependencies

```bash
npm install
```

#### 3. Start Development Server

```bash
npm start
```

Frontend will be available at:

```text
http://localhost:3000
```

---

## 🔗 Backend API Configuration

Ensure the React application points to the correct backend endpoint:

```javascript
const API_URL = "http://127.0.0.1:8000/chat";
```

Update this URL as needed for production deployments.

---

## 🔄 System Workflow

```text
User
 │
 ▼
React Frontend
 │
 ▼
FastAPI Backend
 │
 ├── Detect User Intent
 ├── Fetch Match Data (API-Football)
 └── Build AI Prompt
         │
         ▼
    Gemini / LLM
         │
         ▼
Prediction Response
         │
         ▼
Markdown Rendering
         │
         ▼
       User
```

---

## 📂 Project Structure

```text
fifa-prediction-chatbot/
│
├── backend/
│   ├── main.py
│   ├── services/
│   ├── utils/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── .env
│
└── README.md
```

---

## ⚠️ Important Notes

### API-Football

* Free-tier plans include request rate limits.
* Consider upgrading for higher traffic and production workloads.

### LLM Usage

* AI requests consume tokens and may incur costs.
* Response quality and latency depend on model size and prompt complexity.

### Performance

* Large prediction requests may increase response time.
* Caching frequently requested fixtures is recommended for production deployments.

---

## 🎯 Final Outcome

This project provides:

* ✅ AI-powered FIFA match predictions
* ✅ Real-time football fixture integration
* ✅ Modern ChatGPT-style user interface
* ✅ FastAPI-based scalable backend
* ✅ React-powered responsive frontend
* ✅ Modular and production-ready architecture
* ✅ Easy integration with multiple LLM providers

---

## 📜 License

## 🤝 Contributing

This project is maintained for educational and learning purposes. Contributions, improvements, bug reports, and suggestions are very welcome. To contribute:

- Fork the repository
- Create a branch: `git checkout -b feature/your-feature`
- Commit your changes: `git commit -m "Add some feature"`
- Push to your branch and open a pull request

Please follow the existing code style and add tests where applicable.

---

## 📜 License

This project is intended for educational, research, and development purposes. Ensure compliance with the terms and conditions of all third-party APIs and services used.
