# 🚀 Campus AI Assistant - Quick Start Guide

## ✅ What You Have Now

Your project is ready with these files:

1. **app-backend.py** - Flask backend with Google Gemini AI
2. **campus-ai-frontend.html** - Beautiful chat interface
3. **.env** - Your API key configuration
4. **All packages installed** ✅

---

## 🎯 STEP-BY-STEP: Run Your AI Assistant

### Step 1: Save the Backend File

1. Download **app-backend.py** (I just created it)
2. Save it as `app.py` in your **backend** folder:
   - Location: `Desktop\Campus-Ai-Assistant\backend\app.py`

### Step 2: Save the Frontend File

1. Download **campus-ai-frontend.html** (I just created it)
2. Save it as `index.html` in your **frontend** folder:
   - Location: `Desktop\Campus-Ai-Assistant\frontend\index.html`

### Step 3: Start the Backend Server

Open Command Prompt in your project folder:

```bash
# Make sure you're in the project folder
cd Desktop\Campus-Ai-Assistant

# Activate virtual environment
venv\Scripts\activate

# Go to backend folder
cd backend

# Run the server
python app.py
```

You should see:
```
==================================================
🚀 Campus AI Assistant - Backend Server
==================================================
✅ API Key Configured: True
✅ AI Model: gemini-pro
✅ Server starting on: http://localhost:5000
==================================================
```

**✅ Keep this window open!** The server must run for the AI to work.

### Step 4: Open the Frontend

1. Go to your **frontend** folder in File Explorer
2. Find `index.html`
3. **Double-click** to open in your browser

OR

Right-click `index.html` → Open with → Your browser (Chrome/Edge)

---

## 🎉 TEST YOUR AI ASSISTANT!

Once both are running:

1. You'll see a beautiful purple interface
2. Try these questions:
   - "Find me software engineering internships"
   - "Best free courses for data science"
   - "Study abroad programs in USA"
   - "Entry-level jobs for fresh graduates"

3. The AI will respond with detailed information!

---

## 📁 Your Final Folder Structure

```
Desktop/Campus-Ai-Assistant/
├── backend/
│   ├── app.py ⭐ (the backend file you saved)
│   └── requirements.txt
├── frontend/
│   └── index.html ⭐ (the frontend file you saved)
├── .env (with your API key)
├── .gitignore
└── README.md
```

---

## ✅ Verification Checklist

- [ ] Backend running (Command Prompt shows "Server starting...")
- [ ] Frontend open in browser
- [ ] Can see the chat interface
- [ ] Can type messages
- [ ] AI responds to questions

---

## 🆘 Troubleshooting

### Problem 1: "GOOGLE_API_KEY not found"
**Solution**: Check your `.env` file has:
```
GOOGLE_API_KEY=AIzaSyC_z5XnMPxrqq0XPIskq9bHAeCw2xlBXWU
```

### Problem 2: "Could not connect to server"
**Solution**: 
- Make sure backend is running (`python app.py`)
- Check it says "Server starting on: http://localhost:5000"

### Problem 3: Frontend shows error
**Solution**:
- Make sure backend is running BEFORE opening frontend
- Try refreshing the browser (F5)

### Problem 4: No response from AI
**Solution**:
- Check Command Prompt for errors
- Verify API key is correct in .env file
- Try restarting the backend server

---

## 🎯 Next Steps After It Works

Once your AI assistant is working:

1. ✅ Test with different questions
2. ✅ Upload to GitHub (I'll guide you)
3. ✅ Add more features (voice input, offline mode, etc.)
4. ✅ Deploy online (make it accessible from anywhere)

---

## 📞 TELL ME WHEN READY

Reply with your status:

**Option A**: "✅ Both running - AI is responding!"

**Option B**: "❌ Stuck at [which step]" (tell me the error)

**Option C**: "❓ Where do I save the files?" (I'll guide you)

---

## 💡 Quick Commands Reference

```bash
# Activate virtual environment
venv\Scripts\activate

# Start backend
cd backend
python app.py

# Stop backend
Press Ctrl+C in Command Prompt
```

---

**You're almost there! Just save the two files and run them!** 🚀
