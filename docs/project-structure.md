# Campus AI Assistant - Project Structure

## 📁 Complete Folder Structure

```
campus-ai-assistant/
├── frontend/
│   ├── index.html
│   ├── css/
│   │   ├── main.css
│   │   ├── responsive.css
│   │   └── themes.css
│   ├── js/
│   │   ├── app.js
│   │   ├── ai-handler.js
│   │   ├── offline.js
│   │   └── voice.js
│   ├── assets/
│   │   ├── icons/
│   │   └── images/
│   └── manifest.json (PWA)
│
├── backend/
│   ├── app.py (Flask main file)
│   ├── config.py
│   ├── requirements.txt
│   ├── models/
│   │   ├── ai_model.py
│   │   └── data_retriever.py
│   ├── routes/
│   │   ├── api.py
│   │   ├── internships.py
│   │   ├── jobs.py
│   │   ├── courses.py
│   │   └── study_abroad.py
│   ├── data/
│   │   ├── internships.json
│   │   ├── jobs.json
│   │   ├── courses.json
│   │   ├── colleges.json
│   │   └── study_abroad.json
│   └── utils/
│       ├── rag_engine.py
│       ├── vector_db.py
│       └── cache.py
│
├── ai_training/
│   ├── knowledge_base/
│   ├── fine_tune_data/
│   └── model_config.json
│
├── tests/
│   ├── test_api.py
│   ├── test_ai_accuracy.py
│   └── test_performance.py
│
├── docs/
│   ├── API_DOCS.md
│   ├── SETUP.md
│   └── FEATURES.md
│
├── .gitignore
├── .env.example
├── README.md
├── LICENSE
└── setup.sh
```

## 🎯 Technology Stack (Confirmed)

### Frontend (Lightweight)
- **HTML5** - Semantic structure
- **Vanilla CSS** - No frameworks (< 50KB total)
- **Vanilla JavaScript** - No jQuery/React (modular ES6+)
- **PWA** - Service workers for offline mode
- **Total Size Target**: < 500KB initial load

### Backend (Python)
- **Flask** - Lightweight Python framework
- **Google Generative AI (Gemini)** - Main AI engine
- **ChromaDB** - Vector database for RAG
- **SQLite** - Lightweight database
- **Flask-CORS** - API access
- **Flask-Caching** - Performance optimization

### AI/ML Components
- **RAG (Retrieval-Augmented Generation)** - For accuracy >97%
- **LangChain** - AI orchestration
- **Sentence Transformers** - Text embeddings
- **FAISS** - Fast similarity search

### Hosting & Deployment
- **Frontend**: GitHub Pages (Free)
- **Backend**: Render/Railway (Free tier)
- **Database**: SQLite (local) → PostgreSQL (production)
- **CDN**: Cloudflare (Free)

## 📊 Performance Targets

| Metric | Target | Strategy |
|--------|--------|----------|
| AI Accuracy | >97% | RAG + Verified data sources |
| Initial Load | <2s | Code splitting, lazy loading |
| Memory Usage | <100MB | Efficient caching, lightweight code |
| CPU Usage | <10% idle | Async operations, web workers |
| Storage | <50MB | Compressed data, IndexedDB |
| Mobile Support | All devices | Progressive enhancement |

## 🔐 Security Considerations

1. **API Keys**: Environment variables only (.env)
2. **CORS**: Whitelist specific domains
3. **Rate Limiting**: Prevent abuse
4. **Input Sanitization**: Prevent injection attacks
5. **HTTPS Only**: Secure data transmission
6. **GitHub Secrets**: For CI/CD deployment

## 📦 Development Phases

### Phase 1: Foundation (Current - STEP 1)
- Project structure setup
- Basic HTML/CSS/JS
- Flask API skeleton
- Git repository initialization

### Phase 2: Core AI Integration (STEP 2)
- Google Gemini API integration
- RAG implementation
- Knowledge base creation
- Basic query-response system

### Phase 3: Data Integration (STEP 3)
- Internships database
- Jobs aggregation
- Courses catalog
- Study abroad programs
- Top colleges list

### Phase 4: Unique Features (STEP 4)
- Voice query support
- Offline mode
- Smart match score
- Deadline tracker
- AI Study Buddy

### Phase 5: Advanced Features (STEP 5)
- Interview prep bot
- Document scanner
- Peer connect
- AR campus tours (if feasible)
- Resource optimizer

### Phase 6: Testing & Optimization (STEP 6)
- Accuracy testing (>97%)
- Performance optimization
- Cross-device testing
- Load testing

### Phase 7: Deployment & Documentation (STEP 7)
- GitHub repository setup
- README documentation
- API documentation
- Deployment guides
- Video demo

## 🎨 UI Design Concept

**Theme**: Modern Glassmorphism + Neumorphism Hybrid

**Color Palette**:
- Primary: #6366f1 (Indigo)
- Secondary: #8b5cf6 (Purple)
- Accent: #06b6d4 (Cyan)
- Background: Linear gradient
- Text: High contrast for accessibility

**Typography**:
- Headings: Inter/Poppins (Google Fonts CDN)
- Body: System fonts (performance)

**Layout**:
- Mobile-first design
- Card-based interface
- Floating action button for AI chat
- Bottom navigation (mobile)
- Sidebar navigation (desktop)

## 🚀 Next Steps (After STEP 1 Complete)

1. ✅ Initialize Git repository
2. ✅ Create all folder structure
3. ✅ Setup virtual environment
4. ✅ Install dependencies
5. ✅ Create basic HTML/CSS/JS files
6. ✅ Setup Flask backend skeleton
7. ✅ Test local development server
8. ✅ First commit to GitHub

---

**Once STEP 1 is complete, we'll move to STEP 2: AI Integration**
