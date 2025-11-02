"""
Campus AI Assistant - Backend Server
Main Flask application with Google Gemini AI integration
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Configure Google Gemini AI
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file!")

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the AI model
model = genai.GenerativeModel('gemini-pro')

# System prompt for Campus AI Assistant
SYSTEM_PROMPT = """You are Campus AI Assistant, an intelligent educational advisor helping students with:
- Internship opportunities (with links and deadlines)
- Job openings (entry-level to experienced)
- Study abroad programs (worldwide with dates and requirements)
- Free and paid certified courses (Coursera, Udemy, edX, etc.)
- Top colleges and universities (rankings and information)
- Career guidance and educational paths

Provide accurate, helpful, and detailed responses. Always include:
1. Direct links when possible
2. Application deadlines
3. Requirements and eligibility
4. Specific dates and timelines

Be friendly, professional, and encouraging. Help students make informed decisions."""


@app.route('/')
def home():
    """Home endpoint - API status"""
    return jsonify({
        'status': 'active',
        'message': '🎓 Campus AI Assistant API is running!',
        'version': '1.0.0',
        'endpoints': {
            '/api/chat': 'POST - Send messages to AI',
            '/api/health': 'GET - Health check'
        }
    })


@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'ai_model': 'gemini-pro',
        'api_key_configured': bool(GOOGLE_API_KEY)
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint - communicate with AI"""
    try:
        # Get user message from request
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'error': 'Message cannot be empty'
            }), 400
        
        # Create conversation with system prompt
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_message}\n\nAssistant:"
        
        # Generate AI response
        response = model.generate_content(full_prompt)
        ai_response = response.text
        
        # Return response
        return jsonify({
            'success': True,
            'message': user_message,
            'response': ai_response,
            'model': 'gemini-pro'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Failed to generate response'
        }), 500


@app.route('/api/search', methods=['POST'])
def search():
    """Search for specific opportunities"""
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        category = data.get('category', 'all')  # internships, jobs, courses, study_abroad
        
        if not query:
            return jsonify({'error': 'Query cannot be empty'}), 400
        
        # Create specialized prompt based on category
        prompts = {
            'internships': f"Find internship opportunities related to: {query}. Include company names, links, deadlines, and requirements.",
            'jobs': f"Find job opportunities related to: {query}. Include company names, positions, links, and requirements.",
            'courses': f"Find online courses related to: {query}. Include platform names (Coursera, Udemy, edX), course links, and whether they're free or paid.",
            'study_abroad': f"Find study abroad programs related to: {query}. Include countries, universities, programs, deadlines, and requirements.",
            'all': f"Find educational opportunities (internships, jobs, courses, study abroad) related to: {query}. Provide comprehensive information with links and deadlines."
        }
        
        prompt = prompts.get(category, prompts['all'])
        
        # Generate response
        response = model.generate_content(f"{SYSTEM_PROMPT}\n\n{prompt}")
        
        return jsonify({
            'success': True,
            'query': query,
            'category': category,
            'results': response.text
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/match-score', methods=['POST'])
def match_score():
    """Calculate fit score for opportunities"""
    try:
        data = request.get_json()
        user_profile = data.get('profile', {})
        opportunity = data.get('opportunity', '')
        
        if not user_profile or not opportunity:
            return jsonify({'error': 'Profile and opportunity required'}), 400
        
        prompt = f"""Analyze the match between this student profile and opportunity:

Student Profile:
- Skills: {user_profile.get('skills', 'Not provided')}
- Education: {user_profile.get('education', 'Not provided')}
- Experience: {user_profile.get('experience', 'Not provided')}
- Interests: {user_profile.get('interests', 'Not provided')}

Opportunity: {opportunity}

Provide:
1. Match score (0-100%)
2. Strengths (why they're a good fit)
3. Gaps (what they need to improve)
4. Recommendations (next steps)"""

        response = model.generate_content(prompt)
        
        return jsonify({
            'success': True,
            'analysis': response.text
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Campus AI Assistant - Backend Server")
    print("=" * 50)
    print(f"✅ API Key Configured: {bool(GOOGLE_API_KEY)}")
    print(f"✅ AI Model: gemini-pro")
    print(f"✅ Server starting on: http://localhost:5000")
    print("=" * 50)
    print("\n📝 Available Endpoints:")
    print("   GET  /              - API Status")
    print("   GET  /api/health    - Health Check")
    print("   POST /api/chat      - Chat with AI")
    print("   POST /api/search    - Search opportunities")
    print("   POST /api/match-score - Calculate match score")
    print("\n🎯 Press Ctrl+C to stop the server\n")
    
    # Run the server
    app.run(debug=True, host='0.0.0.0', port=5000)
