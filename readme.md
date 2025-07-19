# 🤖 Smart Chatbot - Financial Assistant & General Helper

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

A conversational AI chatbot that provides financial advice and answers general questions using natural language processing.

![Chatbot Demo](images/demo.jpg)

## Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Examples](#-example-queries)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## 🌟 Features
- **Natural Language Understanding** using NLTK and scikit-learn
- **Financial Guidance** on budgeting and credit scores
- **Interactive Web Interface** built with Streamlit
- **Easy Customization** through simple intent configuration

## 🚀 Installation:
### Prerequisites
- Python 3.8+
- pip

### Steps
# Clone the repository
git clone https://github.com/Vasanthkumar5648/chatbot.git
cd smart-chatbot
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
# Install dependencies
pip install -r requirements.txt
# Download NLTK data
python -c "import nltk; nltk.download('punkt', download_dir='./nltk_data')"

### 💻 Usage
'''bash
streamlit run chatbot.py

## ⚙️ Configuration:
intents = [
    {
        "tag": "new_topic",
        "patterns": ["sample question"],
        "responses": ["sample response"],
        "avatar": "🎯"
    }
]

## 💡 Example Queries:
Try asking:

"How do I create a budget?"

"What affects my credit score?"

"What can you do?"

## 🛠 Troubleshooting:
NLTK Data Issues:
nltk.data.path.append(os.path.abspath("nltk_data"))
SSL Errors:
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

##📜 License
Distributed under the MIT License. See LICENSE for more information.

Created with ❤️ by [Vasantha kumar]

### GitHub-Specific Enhancements:
1. **Shields.io Badges** - Visual indicators for Python version, license, and Streamlit
2. **Table of Contents** - Auto-linked sections for better navigation
3. **Code Fences** - Properly formatted installation commands
4. **Relative Paths** - Assets linked using relative paths for GitHub display
5. **GitHub-Flavored Markdown** - Optimized for GitHub's renderer
