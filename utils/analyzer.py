import os
import google.generativeai as genai

# Configure Gemini API key from environment
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def analyze_resume(text):
    prompt = f"""
    Analyze the following resume and return a structured JSON with:

    - "ats_score": number 0 to 100
    - "missing_skills": list of missing important skills
    - "grammar_issues": list of grammar/readability issues
    - "summary": short summary about the resume strength

    Resume:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text
