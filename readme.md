# 🤖 Smart Chatbot - Financial Assistant & General Helper

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

A conversational AI chatbot that provides financial advice and answers general questions using natural language processing.

![Chatbot Demo](assets/demo.gif)

## Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Examples](#-example-queries)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## 🌟 Features
- **Natural Language Understanding** using NLTK and scikit-learn
- **Financial Guidance** on budgeting and credit scores
- **Interactive Web Interface** built with Streamlit
- **Easy Customization** through simple intent configuration

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip

### Steps
```bash
# Clone the repository
git clone https://github.com/yourusername/smart-chatbot.git
cd smart-chatbot

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt', download_dir='./nltk_data')"
