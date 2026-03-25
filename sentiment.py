import random
from textblob import TextBlob

class SentimentChatbot:
    def __init__(self):
        # Define specific rules for Greetings and FAQs
        self.greetings = {
            "hello", "hi", "hey", "good morning", "good evening", "greetings"
        }
        
        self.farewells = {
            "bye", "goodbye", "see you", "exit", "quit"
        }
        
        self.faqs = {
            "what is your name": "I am SentimentBot, your friendly emotional companion.",
            "how are you": "I'm just code, but I'm running smoothly! How are you?",
            "what can you do": "I can detect your mood and chat with you. Try telling me how you feel!"
        }

        # Response pools based on sentiment
        self.positive_responses = [
            "That’s great to hear! 😃",
            "I'm so happy for you! Keep that positive energy! ✨",
            "Wonderful! It's always nice to have good news.",
            "Awesome! You seem to be having a good day."
        ]
        
        self.negative_responses = [
            "I’m sorry to hear that. Hope things get better soon. 🙁",
            "Oh no, that sounds tough. I'm here if you want to talk.",
            "Sending you a virtual hug. 🤗",
            "I understand. Tomorrow is a new day. Stay strong."
        ]
        
        self.neutral_responses = [
            "I see. Tell me more.",
            "Interesting. How can I help you with that?",
            "Got it. Is there anything specific on your mind?"
        ]

    def get_response(self, user_input):
        # 1. Normalize input
        user_input_lower = user_input.lower().strip()

        # 2. Check for Greetings
        if user_input_lower in self.greetings:
            return random.choice(["Hello! 👋", "Hi there!", "Greetings! How can I help?"])

        # 3. Check for Farewells
        if user_input_lower in self.farewells:
            return "Goodbye! Have a wonderful day! 👋"

        # 4. Check for FAQs (Keyword matching)
        for question, answer in self.faqs.items():
            if question in user_input_lower:
                return answer

        # 5. Sentiment Analysis
        # If no rules matched, analyze sentiment
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        if polarity > 0.2:
            return random.choice(self.positive_responses)
        elif polarity < -0.2:
            return random.choice(self.negative_responses)
        else:
            return random.choice(self.neutral_responses)

# ==========================================
# Run the Chatbot
# ==========================================
def run_chatbot():
    bot = SentimentChatbot()
    print("Chatbot is ready! (Type 'exit' to stop)")
    print("-" * 30)
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print(f"Bot: {bot.get_response('bye')}")
            break
            
        response = bot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    run_chatbot()
