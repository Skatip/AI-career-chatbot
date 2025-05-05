from transformers import pipeline
from app.retrieve import hybrid_retrieve
from app.prompt_builder import build_prompt

def load_model(model_name="microsoft/phi-2"):
    return pipeline("text-generation", model=model_name, max_new_tokens=300)

def generate_answer(query, model_name="microsoft/phi-2"):
    retrieved_docs = hybrid_retrieve(query)
    prompt = build_prompt(query, retrieved_docs)
    model = load_model(model_name)
    output = model(prompt)[0]["generated_text"]
    answer = output[len(prompt):].strip()
    return answer
