from app.retrieve import hybrid_retrieve
from app.prompt_builder import build_prompt
from transformers import pipeline

MODELS = {
    "phi-2": "microsoft/phi-2",
    "gpt2": "gpt2",
    "falcon": "tiiuae/falcon-rw-1b"
}

def load_model(model_name):
    return pipeline("text-generation", model=model_name, max_new_tokens=300)

def compare_models(query, k=5):
    retrieved_docs = hybrid_retrieve(query, k)
    prompt = build_prompt(query, retrieved_docs)
    responses = {}

    for label, model_name in MODELS.items():
        model = load_model(model_name)
        output = model(prompt)[0]["generated_text"]
        answer = output[len(prompt):].strip()
        responses[label] = answer

    return responses
