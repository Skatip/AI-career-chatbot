from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer

def evaluate_response(reference_text, generated_text):
    bleu = sentence_bleu(
        [reference_text.split()],
        generated_text.split(),
        smoothing_function=SmoothingFunction().method1
    )
    rouge = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    rouge_scores = rouge.score(reference_text, generated_text)
    return {"bleu": bleu, "rouge": rouge_scores}
