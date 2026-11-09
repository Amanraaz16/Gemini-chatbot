# 🤖 Gemini Chatbot

A conversational AI chatbot built in Python that allows you to chat naturally from your terminal. Powered by Google's Gemini API, this project is lightweight, easy to set up, and perfect for experimenting with AI conversations.

---

## 🚀 Features

- 💬 **Interactive Terminal Chat** – type your message and get instant responses.
- 🏃 **Exit Command** – type `exit` to end the chat session.
- 🔒 **Secure API Key** – uses `.env` to keep your Gemini API key safe.
- ⚡ **Easy Setup** – clone the repo, install dependencies, and start chatting.
- 🌐 **Cross-Platform** – works on Windows, Mac, and Linux.

---

## 🎬 Demo

**Example terminal session:**


🤖 Gemini Chatbot (type 'exit' to quit)

You: Hello Gemini!

Gemini: Hello! How can I help you today?

You: exit

Gemini: Bye! 👋


---
## 🛠️ Tech Stack

- Python 3.11+
- [python-dotenv](https://pypi.org/project/python-dotenv/) – for environment variables
- Gemini API – natural language responses

---

## ⚡ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/Amanraaz16/Gemini-chatbot.git
cd Gemini-chatbot
Create and activate a virtual environment
```
2. **Create and activate a virtual environment**
```bash
python -m venv venv
.\venv\Scripts\activate   # Windows PowerShell
# OR
source venv/bin/activate  # Linux/Mac
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up your Gemini API key**

Create a .env file in the project root with your key:
```bash
GEMINI_API_KEY=your_api_key_here
```

5. **Run the chatbot**

```bash

python chatbot.py
```
📝 Usage
- Type any message to interact with the chatbot.

- Type exit to end the conversation.

- Responses appear instantly in the terminal.

📂 Project Structure
```bash

Gemini-chatbot/
├── chatbot.py          # Main chatbot script
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignored files (venv, .env)
├── README.md           # Project documentation
└── venv/               # Virtual environment (not tracked in Git)
```
🔐 Security
- Keep your .env file private to protect your API key.

- .env is included in .gitignore by default.

💡 Contributing
Contributions are welcome!

1. Fork the repository.

2. Create a new branch: git checkout -b feature-name.

3. Make your changes and commit: git commit -m "Add new feature".

4. Push your branch: git push origin feature-name.

5. Open a Pull Request.

🤝 Contact

more modification coming soon.

Aman Raj

GitHub: https://github.com/Amanraaz16

Email: amanraazgupta@gmail.com
Email: amanraazgupta@gmail.com

