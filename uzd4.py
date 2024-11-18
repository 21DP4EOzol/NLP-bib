
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

for sentence in sentences:
    result = classifier(sentence)
    print(f"Sentence: {sentence} - Sentiment: {result[0]['label']} ({result[0]['score']:.2f})")
