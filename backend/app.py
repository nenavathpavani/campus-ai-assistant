"""
Campus AI Assistant - FINAL VERSION WITH CONTEXT MEMORY
Human-like AI that remembers conversation context
"""

import os
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file!")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# SMART SYSTEM PROMPT WITH CONTEXT AWARENESS
SYSTEM_PROMPT = """You are a friendly Campus AI Assistant - like a helpful friend who remembers what you just talked about.

**CRITICAL CONTEXT RULE:**
When users say "they", "these", "that", "it", "why", "compare", "which one" immediately after you've provided a list, they are referring to THOSE SPECIFIC ITEMS you just mentioned. Don't ask for clarification - use the context!

**YOUR PERSONALITY:**
- Warm, conversational, and supportive (not robotic)
- You remember the context of previous messages
- Understanding of student budgets and real-world constraints
- Proactive in suggesting helpful options

**WHAT YOU HELP WITH:**
1. Internships - Paid/unpaid, remote/on-site, all fields
2. Jobs - Entry-level to experienced, full-time/freelance
3. Colleges - Rankings, fees, scholarships, free education
4. Study Abroad - Countries, costs, scholarships, visa help
5. Courses - Free certifications, paid programs, bootcamps
6. Career Guidance - Paths, skills, resume help, interview prep

**FORMAT FOR LISTINGS:**
When providing courses, internships, colleges, etc., use this format:

**[Number]. [Name]** - [Brief description]
• Requirement: [What's needed]
• Cost: [FREE / Paid / Scholarship info]
• Link: [Actual working URL]
• Deadline/Duration: [Timeline]
• **Why this rocks:** [Key benefit]

**IMPORTANT CONVERSATION RULES:**
1. If previous context exists and user says "why/which/compare/they/these":
   - Assume they're asking about items you just listed
   - DON'T ask "what are you referring to?"
   - Directly explain/compare those items

2. Be conversational:
   - Start: "Great choice!", "I can help with that!", "Perfect!"
   - End: "Need more details?", "Want me to explain more?"

3. Always include REAL working links, never placeholders

Remember: You're a knowledgeable friend who pays attention and remembers what you just talked about!
"""


def format_response(text):
    """Convert markdown to HTML with clickable links"""
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    
    # URLs (not in brackets)
    text = re.sub(
        r'(?<!\()(https?://[^\s<>"\']+?)(?=[.,;:!?)]?\s|[.,;:!?)]?$|<br>|</)',
        r'<a href="\1" target="_blank" rel="noopener noreferrer">\1</a>',
        text
    )
    
    # Markdown links [text](url)
    text = re.sub(
        r'\[([^\]]+)\]\((https?://[^\s<>"\']+?)\)',
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        text
    )
    
    # Line breaks
    text = text.replace('\n', '<br>')
    
    return text


@app.route('/')
def home():
    return jsonify({
        'status': 'active',
        'version': '3.1 - Context Memory',
        'message': '🎓 Human-like Campus AI with Conversation Memory!'
    })


@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'ai_model': 'gemini-2.0-flash-exp',
        'mode': 'context-aware'
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        previous_context = data.get('previous_context', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Build context-aware prompt
        context_block = ""
        if previous_context:
            context_block = f"""

PREVIOUS CONTEXT (what you just mentioned to the user):
{previous_context}

IMPORTANT: If the user asks "why", "which one", "compare them", "they", "these", "that", or similar follow-up questions, they are referring to the items in the PREVIOUS CONTEXT above. Use that context to answer - don't ask for clarification!
"""
        
        full_prompt = f"{SYSTEM_PROMPT}{context_block}\n\nStudent Question: {user_message}\n\nYour friendly response:"
        
        # Generate response
        response = model.generate_content(full_prompt)
        ai_response = response.text
        
        # Format with links
        formatted_response = format_response(ai_response)
        
        return jsonify({
            'success': True,
            'response': formatted_response,
            'model': 'gemini-2.0-flash-exp'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    print("=" * 70)
    print("🎓 CAMPUS AI ASSISTANT - CONTEXT-AWARE VERSION v3.1")
    print("=" * 70)
    print("✅ Remembers conversation context like a human")
    print("✅ Understands follow-up questions (why, which, compare)")
    print("✅ Handles pronouns (they/these/that) intelligently")
    print("=" * 70)
    print("\n🚀 Server running on: http://localhost:5000\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
