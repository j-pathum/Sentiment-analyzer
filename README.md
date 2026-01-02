# Sentiment-analyzer# Vibe Check - Sentiment Analysis App 🎭

An intermediate full-stack application that demonstrates communication between a Python backend and a JavaScript frontend.

## 🛠 Architecture
This project uses a **Microservice Architecture**:
1.  **Backend (Python/Flask):** Processes natural language and calculates a sentiment score.
2.  **Frontend (Vanilla JS):** Collects user input and dynamically updates the UI based on the API response.

## 🚀 How to Run
You need to run both the Backend and the Frontend simultaneously.

### Step 1: Start the Backend
1.  Open a terminal in the project folder.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the server:
    ```bash
    python app.py
    ```
    *You should see: "Running on http://127.0.0.1:5000"*

### Step 2: Open the Frontend
1.  Simply double-click `index.html` to open it in your browser.
2.  Type a sentence (e.g., "I hate rainy days" or "I love coding") and click **Analyze**.

## 💻 Tech Stack
- **Python (Flask):** REST API creation.
- **TextBlob:** Natural Language Processing (NLP).
- **JavaScript (ES6):** Async/Await & Fetch API.
- **CORS:** Handling cross-origin security.
