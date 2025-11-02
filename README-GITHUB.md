# 🎓 Campus AI Assistant

> An intelligent AI-powered assistant that helps students with internships, jobs, courses, and study abroad programs with **context-aware conversations** and **advanced features**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

---

## ✨ Features

### 🤖 AI Capabilities
- **Context-Aware Conversations**: Remembers previous messages and understands follow-up questions
- **Smart Follow-ups**: Responds to "why?", "compare them", "which is best?" without asking clarification
- **Real-time Responses**: Powered by Google Gemini 2.0 Flash AI
- **Clickable Links**: Automatically formats URLs in responses

### 🎨 User Interface
- **Beautiful Gradient Design**: Modern, professional UI with smooth animations
- **Perfect Mobile Responsive**: Works flawlessly on phones, tablets, and desktops
- **Voice Input Support**: Hands-free operation with speech recognition
- **Quick Question Buttons**: Fast access to common queries
- **One-Line Input**: Mic, text field, and send button always in one horizontal row

### 📊 Advanced Features (in Settings Menu ⋮)
1. **Clear Chat**: Reset conversation and show welcome screen
2. **Export Chat**: Download conversation as text file
3. **Dark Mode**: Toggle between light and dark themes
4. **Statistics Dashboard**: View message counts, session time, context memory status
5. **Search History**: Full-text search through all chat messages with highlighting

---

## 🚀 Tech Stack

**Backend:**
- Python 3.8+
- Flask (Web framework)
- Flask-CORS (Cross-origin support)
- Google Generative AI (Gemini 2.0)
- Python-dotenv (Environment variables)

**Frontend:**
- Pure HTML5, CSS3, JavaScript (No frameworks!)
- CSS Grid & Flexbox (Responsive layout)
- Web Speech API (Voice input)
- LocalStorage (Statistics tracking)

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Google API Key ([Get one here](https://makersuite.google.com/app/apikey))
- Modern web browser (Chrome, Edge, Firefox, Safari)

### Step 1: Clone Repository
```bash
git clone https://github.com/YOUR-USERNAME/campus-ai-assistant.git
cd campus-ai-assistant
```

### Step 2: Backend Setup
```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

### Step 3: Frontend Setup
```bash
# No installation needed! Just open the file
# frontend/index.html in your browser
```

---

## 🎯 Usage

### Starting the Backend
```bash
cd backend
python app.py
```

You should see:
```
======================================================================
🎓 CAMPUS AI ASSISTANT - CONTEXT-AWARE VERSION v3.1
======================================================================
✅ Remembers conversation context like a human
✅ Understands follow-up questions (why, which, compare)
✅ Handles pronouns (they/these/that) intelligently
======================================================================
🚀 Server running on: http://localhost:5000
```

### Opening the Frontend
1. **Option 1**: Double-click `frontend/index.html`
2. **Option 2**: Right-click → Open with → Your Browser
3. **Option 3**: Drag and drop into browser window

### Using the App
1. **Type or Speak**: Use text input or click 🎙️ for voice
2. **Quick Questions**: Click suggested topics for instant queries
3. **Follow-up**: Ask "why?", "compare them", "which is best?" naturally
4. **Settings**: Click ⋮ (three dots) for advanced features

---

## 📂 Project Structure

```
campus-ai-assistant/
├── backend/
│   ├── app.py                 # Flask backend with context memory
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # API keys (create this)
├── frontend/
│   └── index.html             # Complete single-page app
├── docs/
│   ├── SETUP.md              # Detailed setup guide
│   └── API.md                # API documentation
├── .gitignore                # Git ignore rules
├── README.md                 # This file
└── LICENSE                   # MIT License
```

---

## 🔧 Configuration

### Environment Variables (.env)
```env
GOOGLE_API_KEY=your_google_api_key_here
```

### Frontend API URL
If deploying backend separately, update API_URL in `frontend/index.html`:
```javascript
const API_URL = 'http://localhost:5000'; // Change this to your deployed backend URL
```

---

## 🌐 Deployment

### Deploy Backend (Render.com)
1. Create account on [Render.com](https://render.com)
2. Connect GitHub repository
3. Create new Web Service
4. Set environment variable: `GOOGLE_API_KEY`
5. Deploy!

### Deploy Frontend (Vercel)
1. Create account on [Vercel.com](https://vercel.com)
2. Import GitHub repository
3. Update `API_URL` to your backend URL
4. Deploy!

---

## 📸 Screenshots

### Desktop View
![Desktop Interface](screenshots/desktop.png)

### Mobile View
![Mobile Interface](screenshots/mobile.png)

### Settings Menu
![Settings Menu](screenshots/settings.png)

### Statistics Dashboard
![Statistics](screenshots/stats.png)

---

## 🎓 How It Works

### Context Memory System
The AI maintains conversation context by:
1. **Extracting Key Items**: Captures course names, internships, etc. from responses
2. **Sending Context**: Includes previous context with each new message
3. **Smart Understanding**: Backend recognizes follow-up questions

### Example Conversation:
```
You: "Best free courses for data science"
AI: [Lists IBM, Harvard, freeCodeCamp courses]

You: "why are they best?"
AI: "Those data science courses I mentioned are excellent because..." ✅
```

---

## 🛠️ Development

### Running in Development Mode
```bash
# Backend (with auto-reload)
cd backend
python app.py

# Frontend (any local server)
# Or just open index.html directly
```

### Adding New Features
1. **Backend**: Edit `backend/app.py`
2. **Frontend**: Edit `frontend/index.html`
3. **Test**: Verify context memory still works
4. **Commit**: Push changes to GitHub

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 API Documentation

### POST /api/chat
Send message to AI with context.

**Request:**
```json
{
  "message": "your question here",
  "previous_context": "optional context from previous response"
}
```

**Response:**
```json
{
  "success": true,
  "response": "AI response with HTML formatting",
  "model": "gemini-2.0-flash-exp"
}
```

### GET /api/health
Check backend status.

**Response:**
```json
{
  "status": "healthy",
  "ai_model": "gemini-2.0-flash-exp",
  "mode": "context-aware"
}
```

---

## 🐛 Troubleshooting

### Backend won't start
- Check Python version: `python --version` (need 3.8+)
- Verify .env file exists with valid `GOOGLE_API_KEY`
- Install dependencies: `pip install -r requirements.txt`

### Frontend can't connect
- Ensure backend is running on http://localhost:5000
- Check browser console for errors
- Verify CORS is enabled (already configured)

### Voice input not working
- Use Chrome or Edge browser (best support)
- Allow microphone permissions
- Check browser console for errors

### Context memory not working
- Verify backend v3.1 is running
- Check if `previous_context` is being sent (Network tab)
- Clear browser cache and reload

---

## 📊 Features Roadmap

### ✅ Completed
- Context-aware conversations
- Voice input support
- Statistics dashboard
- Search history
- Dark mode
- Export chat
- Mobile responsive design

### 🔄 In Progress
- User authentication
- Database integration
- Multi-language support

### 📋 Planned
- PWA (Progressive Web App)
- Email notifications
- Calendar integration
- Advanced analytics
- API rate limiting
- User profiles

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Google Gemini AI for powerful language model
- Flask team for excellent web framework
- All open-source contributors

---

## ⭐ Star This Repo!

If you find this project helpful, please give it a ⭐️ on GitHub!

---

**Made with ❤️ for students worldwide**
