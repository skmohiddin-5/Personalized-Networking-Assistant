# 🤝 Personalized Networking Assistant

An AI-powered web application that helps users generate smart, personalized conversation starters for professional and social networking events.

The assistant analyzes event descriptions and user interests to suggest meaningful conversation topics. It also provides quick fact verification using Wikipedia and stores previous conversation strategies for review.

## 🚀 Features

### 1. Smart Conversation Starters

* Generates personalized networking questions based on:

  * Event description
  * User interests
* Helps users start meaningful conversations at conferences and networking events.

### 2. Quick Fact Verification

* Provides summarized information using Wikipedia API.
* Helps users quickly research topics before attending events.

### 3. Conversation History

* Stores previously generated conversation strategies.
* Allows users to review previous networking approaches.

## 🛠️ Technologies Used

### Backend

* FastAPI
* Python
* API Integration
* Data Modeling

### Frontend

* Streamlit

### AI / NLP

* Transformers
* Generative AI
* NLP techniques

### Testing

* Pytest

## 📂 Project Structure

```
Personalized-Networking-Assistant/
│
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── wiki.py
│   ├── history.py
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
├── tests/
│
├── README.md
└── history.json
```

## ⚙️ Installation and Setup

### Clone the repository

```bash
git clone https://github.com/skmohiddin-5/Personalized-Networking-Assistant.git
```

### Install dependencies

```bash
pip install -r backend/requirements.txt
```

## ▶️ Running the Application Locally

### Start FastAPI Backend

```bash
python -m uvicorn backend.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

### Start Streamlit Frontend

Open another terminal:

```bash
python -m streamlit run frontend/app.py
```

Frontend runs at:

```
http://localhost:8501
```

## 📌 Use Cases

### Scenario 1: Generating Smart Starters

Example:

Event:

```
AI for Sustainable Cities
```

Interests:

```
Climate Change, Urban Planning
```

The assistant generates relevant conversation starters.

### Scenario 2: Quick Research

Example:

Topic:

```
Blockchain in Healthcare
```

The assistant provides a quick factual summary.

### Scenario 3: Reviewing Past Strategies

Users can access previous generated conversations through history tracking.

## 🌟 Future Improvements

* Advanced personalization using user feedback
* Improved NLP-based theme extraction
* User authentication
* Better recommendation algorithms
* Cloud-based backend deployment

## 👨‍💻 Author

Sk Mohiddin

## 📎 Links

GitHub:
https://github.com/skmohiddin-5/Personalized-Networking-Assistant

Demo:
https://personalized-networking-assistant-app6peeeqbqkdlsygkq5eah.streamlit.app/
