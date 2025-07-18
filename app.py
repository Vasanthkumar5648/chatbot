import os
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from streamlit.components.v1 import html

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Custom CSS for chat interface
def inject_custom_css():
    st.markdown("""
    <style>
        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 20px;
        }
        .user-message {
            align-self: flex-end;
            background-color: #DCF8C6;
            border-radius: 15px 15px 0 15px;
            padding: 10px 15px;
            max-width: 70%;
            margin-left: 30%;
        }
        .bot-message {
            align-self: flex-start;
            background-color: #ECECEC;
            border-radius: 15px 15px 15px 0;
            padding: 10px 15px;
            max-width: 70%;
            margin-right: 30%;
        }
        .avatar {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            margin-right: 10px;
            object-fit: cover;
        }
        .message-header {
            display: flex;
            align-items: center;
            margin-bottom: 5px;
        }
        .clear-btn {
            margin-bottom: 20px !important;
        }
    </style>
    """, unsafe_allow_html=True)

intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"],
        "responses": ["Hi there 👋", "Hello!", "Hey! How can I help?", "I'm fine, thank you!", "Nothing much. How about you?"],
        "avatar": "👋"
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Take care"],
        "responses": ["Goodbye! 👋", "See you later!", "Take care! 😊", "Have a great day! 🌞"],
        "avatar": "👋"
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"],
        "responses": ["You're welcome! 😊", "No problem!", "Glad I could help! 👍", "Anytime! 😄"],
        "avatar": "🙏"
    },
    {
        "tag": "about",
        "patterns": ["What can you do", "Who are you", "What are you", "What is your purpose"],
        "responses": [
            "I'm a **smart chatbot** 🤖 designed to help with various questions.", 
            "My purpose is to **assist you** with information and conversation.", 
            "I can answer questions, provide suggestions, and more!"
        ],
        "avatar": "🤖"
    },
    {
        "tag": "help",
        "patterns": ["Help", "I need help", "Can you help me", "What should I do"],
        "responses": [
            "Sure! What do you need help with? 💡", 
            "I'm here to help. What's the problem? 🛠️", 
            "How can I assist you today? 🤔"
        ],
        "avatar": "🆘"
    },
    {
        "tag": "age",
        "patterns": ["How old are you", "What's your age"],
        "responses": [
            "I don't have an age - I'm a chatbot! 🤖", 
            "I was just born in the **digital world** 🌐", 
            "Age is just a number for me! 🔢"
        ],
        "avatar": "🎂"
    },
    {
        "tag": "weather",
        "patterns": ["What's the weather like", "How's the weather today"],
        "responses": [
            "I can't check real-time weather, but you can try [Weather.com](https://weather.com) 🌦️", 
            "For weather updates, check your favorite weather app! ☀️🌧️"
        ],
        "avatar": "🌤️"
    },
    {
        "tag": "budget",
        "patterns": ["How can I make a budget", "What's a good budgeting strategy", "How do I create a budget"],
        "responses": [
            "Here's a simple budgeting method:\n\n1. Track income & expenses\n2. Categorize spending\n3. Set financial goals\n4. Review regularly\n\nTry apps like **Mint** or **YNAB**! 💰", 
            "The **50/30/20 rule** works well:\n- 50% needs\n- 30% wants\n- 20% savings/debt\n\n[Learn more](https://www.nerdwallet.com/article/finance/nerdwallet-budget-guide)"
        ],
        "avatar": "💵"
    },
    {
        "tag": "credit_score",
        "patterns": ["What is a credit score", "How do I check my credit score", "How can I improve my credit score"],
        "responses": [
            "A **credit score** (300-850) shows your creditworthiness. Key factors:\n- Payment history (35%)\n- Amounts owed (30%)\n- Credit history length (15%)\n\nCheck free at [Credit Karma](https://www.creditkarma.com)", 
            "To **improve your credit score**:\n1. Pay bills on time\n2. Keep balances low\n3. Don't close old accounts\n4. Limit new credit applications"
        ],
        "avatar": "📊"
    }
]

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Train the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            avatar = intent['avatar']
            return response, avatar

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
if 'show_goodbye' not in st.session_state:
    st.session_state.show_goodbye = False

# Inject custom CSS
inject_custom_css()

# App title and description
st.title("🤖 Smart Chatbot")
st.markdown("""
Welcome to your personal assistant! Ask me about:
- Budgeting 💰
- Credit scores 📊
- General questions ❓
...or just say hello! 👋
""")

# Clear conversation button
if st.button("🗑️ Clear Conversation", key="clear_btn", help="Clear all messages"):
    st.session_state.conversation = []
    st.session_state.show_goodbye = False
    st.experimental_rerun()

# Display conversation
chat_container = st.container()

with chat_container:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    for exchange in st.session_state.conversation:
        if exchange['sender'] == 'user':
            st.markdown(f"""
            <div class="user-message">
                <div class="message-header">
                    <strong>You</strong>
                </div>
                {exchange['message']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="bot-message">
                <div class="message-header">
                    <span style="font-size: 1.5em;">{exchange['avatar']}</span>
                    <strong>Chatbot</strong>
                </div>
                {exchange['message']}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Goodbye message if needed
if st.session_state.show_goodbye:
    st.success("Thank you for chatting with me. Have a great day!")
    st.stop()

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to conversation
    st.session_state.conversation.append({
        'sender': 'user',
        'message': user_input,
        'avatar': ''
    })
    
    # Get bot response
    bot_response, avatar = chatbot(user_input)
    
    # Add bot response to conversation
    st.session_state.conversation.append({
        'sender': 'bot',
        'message': bot_response,
        'avatar': avatar
    })
    
    # Check for goodbye
    if any(word in bot_response.lower() for word in ['goodbye', 'bye', 'see you']):
        st.session_state.show_goodbye = True
    
    # Rerun to update the display
    st.experimental_rerun()
