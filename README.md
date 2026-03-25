# sentiment-chatbot

```markdown
# 🤖 Sentiment Chatbot

A simple yet intelligent Python chatbot that combines **Rule-Based Logic** with **Sentiment Analysis** to provide empathetic and context-aware responses.

Unlike traditional chatbots that only reply based on specific keywords, this bot detects the emotional tone of the user's message (Positive, Negative, or Neutral) and adapts its personality accordingly.

---

## 🌟 Features

- **Hybrid Architecture:** Combines hard-coded rules (for greetings/FAQs) with Machine Learning-based sentiment analysis.
- **Emotion Detection:** Uses `TextBlob` to analyze the polarity of user text.
- **Dynamic Responses:** 
  - 😃 **Positive Mood:** Responds with cheer and encouragement.
  - 🙁 **Negative Mood:** Responds with support and empathy.
  - 😐 **Neutral Mood:** Keeps the conversation going with follow-up questions.
- **Easy to Extend:** Simple dictionary structure allows for easy addition of new FAQs or response pools.

---

## 🛠️ Installation

### Prerequisites
- Python 3.x
- [TextBlob](https://textblob.readthedocs.io/en/dev/) (NLP library)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/sentiment-chatbot.git
   cd sentiment-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install textblob
   ```

---

## 🚀 Usage

1. Run the Python script:
   ```bash
   python chatbot.py
   ```

2. Interact with the bot in the terminal:
   ```text
   You: Hello
   Bot: Hello! 👋

   You: I am so happy today
   Bot: That’s great to hear! 😃

   You: I feel really sad
   Bot: I’m sorry to hear that. Hope things get better soon. 🙁

   You: exit
   Bot: Goodbye! Have a wonderful day! 👋
   ```

---

## ⚙️ How It Works

The chatbot follows a **priority hierarchy** to determine the best response:

1.  **Greeting Check:** Checks if input matches known greetings (e.g., "hi", "hello").
2.  **FAQ Check:** Checks if input contains specific keywords for pre-defined answers.
3.  **Sentiment Analysis:** If no rules match, it uses `TextBlob` to calculate the **polarity** of the text:
    *   **Polarity > 0.2:** Triggers **Positive** response pool.
    *   **Polarity < -0.2:** Triggers **Negative** (Supportive) response pool.
    *   **Otherwise:** Triggers **Neutral** response pool.

---

## 📁 Project Structure

```text
sentiment-chatbot/
│
├── chatbot.py        # Main logic for the chatbot
└── README.md         # Project documentation
```

---

## 🔮 Future Improvements

*   [ ] Integrate a GUI using `Tkinter` or `Streamlit`.
*   [ ] Use `NLTK` or `SpaCy` for more advanced text preprocessing (lemmatization).
*   [ ] Add logging to remember previous conversations.
*   [ ] Implement a Deep Learning model (LSTM/BERT) for more accurate sentiment detection.

---

## 📄 License

This project is open-source and available under the MIT License.
```
