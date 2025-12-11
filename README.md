HYBRID AI — Google + Local Mistral (Glassmorphism UI)
🚀 A Futuristic Hybrid LLM System with Web Search, Local LLM, and Glass UI
<p align="center"> <img src="https://img.shields.io/badge/LLM-Mistral%20Local-blue?style=for-the-badge&logo=openai" /> <img src="https://img.shields.io/badge/Web%20Search-Google%20CSE-red?style=for-the-badge&logo=google" /> <img src="https://img.shields.io/badge/UI-Glassmorphism-purple?style=for-the-badge&logo=streamlit" /> <img src="https://img.shields.io/badge/Tech-Futuristic%20BG5-green?style=for-the-badge&logo=visualstudio" /> <img src="https://img.shields.io/badge/Mode-Hybrid%20AI-success?style=for-the-badge&logo=python" /> </p>
🌟 About the Project

Hybrid AI is a local + online hybrid intelligence system that combines:

🌍 Google Search (via Custom Search API)

🤖 Local Mistral LLM (Ollama — offline)

🧠 Smart Hybrid Mode (Google + Local combined)

⚖️ Side-by-side Comparison Mode

🎨 Glassmorphism Futuristic UI (BG5 Tech Theme)

This project allows users to ask any question and choose one of four modes:

Mode	Description
🌐 Google Answer	Fetch Google results → summarize using Mistral
💻 Local Answer	Pure offline LLM answer
⚖️ Compare Mode	Google-summary vs Local answer side-by-side
🧬 Hybrid Summary	Combine both + generate best merged answer

Perfect for:

Research

Journalism

Compliance

Fact-checking

Competitive intelligence

AI-powered R&D

✨ Features
🔹 1. Glassmorphism UI (C1)

Neon-glow buttons

Frosted glass cards

BG5 circuit-board futuristic theme

Smooth, clean interface

🔹 2. Google Search Integration

Live data

Top-ranked results

Automatic snippet extraction

Clean citation display

🔹 3. Offline Local Mistral LLM

Runs fully offline via Ollama

Fast inference

No API cost

No privacy issues

🔹 4. Hybrid Intelligence

Combines Web Signal + Local Reasoning

Best of both worlds

Smart summarization engine

📦 Tech Stack
Component	Technology
UI	Streamlit
LLM	Mistral (via Ollama)
Web Data	Google Custom Search API
Local Logic	Python
Theme	Glassmorphism + BG5 Futuristic
Deployment	Local / On-Prem
🛠 Installation
1️⃣ Clone the Repo
git clone https://github.com/yourusername/hybrid-ai-glass-ui.git
cd hybrid-ai-glass-ui

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Install & Run Ollama
ollama pull mistral
ollama run mistral

4️⃣ Set Environment Variables

Windows (PowerShell):

setx GOOGLE_API_KEY "your-key"
setx GOOGLE_CSE_ID "your-cse-id"


Restart the terminal after this.

▶️ Run the App
streamlit run app.py

🧪 Available Modes
🌐 1. Google Answer Mode

Search Google → Summarize results using Local Mistral.

💻 2. Local Answer Mode

No internet → Offline LLM → Pure reasoning.

⚖️ 3. Compare Mode

Shows both answers side-by-side.

🧬 4. Hybrid Summary Mode

Auto merges:

Google summary

Local reasoning

Produces best combined answer

📁 Folder Structure
hybrid_ai/
 ├── app.py
 ├── assets/
 │    ├── bg.png
 │    ├── style.css
 ├── hybrid_llm/
 │    ├── llm/mistral_local.py
 │    ├── web/google_search.py
 │    ├── web/web_qa_local.py
 ├── requirements.txt
 ├── README.md
