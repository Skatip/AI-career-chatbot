import gradio as gr
from app.generator import generate_answer

def chat_with_rag(query):
    try:
        return generate_answer(query)
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.Interface(
    fn=chat_with_rag,
    inputs=gr.Textbox(lines=2, placeholder="Ask your career question here..."),
    outputs=gr.Textbox(label="Career Advice"),
    title="🎓 AI-Powered Career Guidance Chatbot",
    description="Built using Retrieval-Augmented Generation (RAG)"
)

demo.launch(share=True)
