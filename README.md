# 🎓 AI-Powered Career Guidance Chatbot Using RAG

A Retrieval-Augmented Generation (RAG) based chatbot that provides personalized career guidance to students using semantic retrieval and open-source language models.

Built by **Team 02** for academic research and practical deployment in low-resource environments.
You-Tube: https://youtu.be/AZv0E7ubstM

---

## Project Highlights

-  Semantic document retrieval using **FAISS**
-  Open-source LLMs: `Phi-2`, `GPT-2`, and `Falcon-RW-1B`
-  Chain-of-Thought (CoT) prompting to improve reasoning
-  BLEU & ROUGE-based evaluation of model output
-  Gradio web interface for user-friendly interaction

---

## Project Structure

career-rag-chatbot/
├── app/
│ ├── retrieve.py # Retrieve Top-k relevant documents
│ ├── prompt_builder.py # Build prompts with CoT
│ ├── generator.py # Generate answer from selected model
│ ├── compare_models.py # Compare all LLMs
│ └── evaluate.py # BLEU and ROUGE scoring
├── data/
│ └── career_articles.json # Domain-specific articles
├── embeddings/
│ ├── career_index.faiss # FAISS index file
│ └── embeddings.npy # Numpy array of embeddings
├── ui/
│ └── gradio_ui.py # Chatbot UI
├── notebooks/
│ └── Team02_Demo.ipynb # Main development notebook (add manually)
├── requirements.txt
├── README.md
├── Project_Report.docx
└── Project_Slides.pptx



---

##  Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/career-rag-chatbot.git
cd career-rag-chatbot
Install required packages

bash
Copy
Edit
pip install -r requirements.txt
Run the chatbot

bash
Copy
Edit
python ui/gradio_ui.py
📌 Make sure career_index.faiss and embeddings.npy are already generated using the notebook.

🔬 Evaluation & Metrics
We evaluated model responses using:

BLEU Score — n-gram similarity

ROUGE-L — longest common subsequence

Model	BLEU Score	ROUGE-L	Style
Phi-2	0.68	0.73	Accurate, Safe
GPT-2	0.61	0.70	Fluent, Creative
Falcon-RW	0.64	0.71	Balanced, Clear

Sample Queries
What skills are required for a cybersecurity analyst?

How can I transition from engineering to product management?

Is a UX/UI design career good in 2025?

What certifications are helpful for digital marketing?

🌐 Gradio UI
Run gradio_ui.py to launch a browser-based chatbot with support for real-time model inference and BLEU score evaluation.

📄 Resources
Project_Report.docx — Final research paper

Project_Slides.pptx — Presentation slides

Team02_Demo.ipynb — All code, explanation, embedding generation

✍️ Authors
Team 02 – University of [Your University Name]

NLP Course – [Course Title or Professor Name]

📬 License
This project is licensed under an open-source academic use license.
