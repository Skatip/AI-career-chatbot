def build_prompt(query, retrieved_docs):
    context = "\n\n".join([doc["content"] for doc in retrieved_docs])
    prompt = (
        f"You are a career counselor assisting students.\n\n"
        f"Context:\n{context}\n\n"
        f"Let's think step-by-step:\n"
        f"1. Understand the student's question.\n"
        f"2. Reference the context facts.\n"
        f"3. Provide clear, actionable career advice.\n\n"
        f"Question: {query}\nAnswer:"
    )
    return prompt
