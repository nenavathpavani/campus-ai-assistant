# ⚡ QUICK START - 5 Minutes to Perfect AI

## 🎯 GOAL:
Make AI remember context so when you ask "why are they best?" it knows what "they" refers to.

---

## 📝 WHAT TO DO:

### 1️⃣ REPLACE BACKEND (2 minutes)

```bash
cd C:\Users\pavani\OneDrive\Desktop\Campus-Ai-Assistant\backend
notepad app.py
```

**Delete everything and paste the new app.py code (from first file I created)**

Save and run:
```bash
python app.py
```

---

### 2️⃣ UPDATE FRONTEND (3 minutes)

Open index.html:
```bash
notepad C:\Users\pavani\OneDrive\Desktop\Campus-Ai-Assistant\frontend\index.html
```

**ADD at top of `<script>` section:**
```javascript
let lastAIContext = '';

function extractContext(htmlResponse) {
    const temp = document.createElement('div');
    temp.innerHTML = htmlResponse;
    const items = Array.from(temp.querySelectorAll('strong'))
        .map(el => el.textContent.trim())
        .filter(text => text && text.length > 3)
        .slice(0, 10);
    return items.join(' | ');
}
```

**FIND this line in sendMessage function:**
```javascript
body: JSON.stringify({ message: message })
```

**REPLACE with:**
```javascript
body: JSON.stringify({ 
    message: message,
    previous_context: lastAIContext 
})
```

**FIND where AI message is displayed:**
```javascript
addMessage(data.response, 'ai');
```

**ADD right after it:**
```javascript
lastAIContext = extractContext(data.response);
```

Save file!

---

## ✅ TEST IT:

1. Open browser
2. Ask: "free python courses"
3. Then ask: "why are they best?"
4. AI should say: "Those Python courses I mentioned are excellent because..."

---

## 🎉 DONE!

Your AI now remembers context like a human!

**Problem?** Read IMPLEMENTATION.md for detailed steps.