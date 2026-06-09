from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import requests
import os

# Load env
load_dotenv(override=True)

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    base_url=GEMINI_BASE_URL,
    api_key=google_api_key
)


# API-Football
API_KEY = os.getenv("API_FOOTBALL_KEY")
API_URL = "https://v3.football.api-sports.io"

app = FastAPI()

system_prompt = """
You are an advanced FIFA World Cup prediction assistant and football analytics engine.

Your responsibilities include BOTH:
1. MATCH DISCOVERY (assistant behavior)
2. MATCH PREDICTION (analytics behavior)

----------------------------------------
## 🧠 CORE CAPABILITIES

You must intelligently interpret user intent:

### 1. If user asks:
- "Today's matches"
- "Tomorrow's matches"
- "Schedule"
→ Provide a clean list of matches with:
  - Teams
  - Time (local if possible)
  - Stage (Group/Knockout)

Then ASK:
"Which match would you like me to predict?"

---

### 2. If user asks:
- "Predict today's matches"
- "Predict all matches"
- "Give predictions for tomorrow"
→ Automatically:
- Fetch/assume scheduled matches
- Generate predictions for ALL matches
- Format neatly (clear sections per match)

---

### 3. If user specifies a match:
→ Perform FULL prediction analysis immediately

---

----------------------------------------
## ⚽ PREDICTION LOGIC

For every match prediction, you MUST:

### 1. Analyze:
- Historical data
- Team strength (Elo-style reasoning)
- Head-to-head records
- Recent form (last 5 matches)
- Current FIFA World Cup performance
- Player availability (injuries/suspensions)
- Tournament stage pressure
- Live/ongoing match context (if available)

---

### 2. Output MUST include:

#### 🏟 Match:
Team A vs Team B  
Stage: (e.g., Group Stage, Quarter-final)

#### 📊 Key Analysis:
- Form comparison
- Strengths vs weaknesses
- Important context (injuries/momentum)

#### 📈 Prediction Probabilities:
- Team A Win: XX%
- Draw: XX%
- Team B Win: XX%

#### 🎯 Exact Score Prediction:
- Most Likely: X – Y

#### 🔁 Alternate Scorelines:
- X – Y
- X – Y

#### 🧠 Confidence Level:
- Low / Medium / High (explain briefly)

---

----------------------------------------
## 📋 OUTPUT FORMATTING RULES

- Use clean headings and emojis
- Separate each match clearly
- Keep it visually appealing and readable
- Avoid long paragraphs—use bullet points
- Maintain consistency across predictions

---

----------------------------------------
## ⚠️ IMPORTANT RULES

- If live data is missing → clearly mention assumptions
- NEVER guarantee results (always probabilistic)
- If no matches are available → inform user clearly
- If query is vague → guide user interactively

---

----------------------------------------
## 🎯 TONE

- Professional sports analyst
- Data-driven
- Engaging and helpful
- Slightly conversational when guiding user

"""

class ChatRequest(BaseModel):
    message: str
    history: List[Dict[str, str]] = []


#---------------------------
# FETCH MATCHES
# ---------------------------
def get_matches(date):
    url = f"{API_URL}/fixtures?date={date}"

    headers = {
        "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    matches = []

    for m in data.get("response", []):
        home = m["teams"]["home"]["name"]
        away = m["teams"]["away"]["name"]
        time = m["fixture"]["date"]

        matches.append(f"{home} vs {away} at {time}")

    if not matches:
        return "No matches found"

    return "\n".join(matches)


@app.post("/chat")
def chat(req: ChatRequest):
    msg_lower = req.message.lower()
    todays_matches = ""
    tomorrows_matches = ""
    # Detect intent BEFORE calling API
    if any(word in msg_lower for word in ["today", "todays"]):
        today = datetime.now().strftime("%Y-%m-%d")
        todays_matches = get_matches(today)

    if any(word in msg_lower for word in ["tomorrow", "tomorrows"]):
        tomorrow = (datetime.now().date() + timedelta(days=1)).strftime("%Y-%m-%d")
        tomorrows_matches = get_matches(tomorrow)

    if any(word in msg_lower for word in ["all matches", "schedule", "matches"]):
        today = datetime.now().strftime("%Y-%m-%d")
        tomorrow = (datetime.now().date() + timedelta(days=1)).strftime("%Y-%m-%d")

        todays_matches = get_matches(today)
        tomorrows_matches = get_matches(tomorrow)

    user_prompt = f"""
User Query:
{req.message}

Context Data Available:
- Today's Matches:
{todays_matches if todays_matches else "Not requested"}

- Tomorrow's Matches:
{tomorrows_matches if tomorrows_matches else "Not requested"}

Instructions:
- Understand user intent.
- If vague → guide user
- If multiple → predict all
- If specific match → predict that match
- Always structured output
"""

    messages = (
        [{"role": "system", "content": system_prompt}]
        + req.history
        + [{"role": "user", "content": user_prompt}]
    )

    response = client.chat.completions.create(
        model="gemini-3.5-flash",
        messages=messages
    )

    reply = response.choices[0].message.content

    updated_history = req.history + [
        {"role": "user", "content": req.message},
        {"role": "assistant", "content": reply},
    ]

    return {"response": reply, "history": updated_history}


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "null"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)