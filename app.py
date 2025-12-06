import gradio as gr
from utils.analyzer import analyze_resume

# Function for Gradio interface
def analyze_interface(resume_text):
    if not resume_text.strip():
        return "Please paste a resume."
    return analyze_resume(resume_text)

# Gradio UI
demo = gr.Interface(
    fn=analyze_interface,
    inputs=gr.Textbox(lines=20, placeholder="Paste your resume here..."),
    outputs="textbox",
    title="AI Resume Analyzer (Free Gemini API)",
    description="Analyze resumes: ATS score, missing skills, grammar, summary."
)

# Launch app
demo.launch()
