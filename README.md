# Gen AI Meeting Agenda Builder 📅

A Generative AI-powered web application that helps you create structured, time-boxed meeting agendas automatically. Built with Python, Streamlit, and the Anthropic Claude API.

## 🚀 Features

- **Topic & Goal Driven**: Generate an agenda based on your specific meeting topic and objectives.
- **Time-Boxed**: Automatically estimates time durations for each agenda item so you never run over time.
- **Exportable**: Easily download the generated agenda as a Markdown (`.md`) file to share with attendees.
- **Beautiful UI**: A clean, modern interface built using Streamlit.

## 🛠️ Project Structure

```text
agenda_builder/
│
├── app.py                  # Main Streamlit web application
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables (API keys)
├── .gitignore              # Files to be ignored by git
├── README.md               # Project documentation
│
└── utils/
    ├── __init__.py         # Makes utils a Python module
    └── generator.py        # Core logic for communicating with the Anthropic API
```

## ⚙️ Setup Instructions

### 1. Prerequisites
- Python 3.9 or higher installed on your machine.
- An [Anthropic API Key](https://console.anthropic.com/).

### 2. Installation
Clone the repository (or copy the files) and set up a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt
```

### 3. Environment Variables
Create a new file named `.env` in the root directory (you can copy `.env.example`) and add your API key:
```env
ANTHROPIC_API_KEY=your_actual_api_key_here
```

### 4. Running the App
Once everything is installed, start the local server:
```bash
streamlit run app.py
```
The application will automatically open in your default browser at `http://localhost:8501`.

## 🤝 Contributing
Feel free to fork this project, submit pull requests, or open issues to propose new features or bug fixes.
