from transformers import MarianMTModel, MarianTokenizer


model_name = "Helsinki-NLP/opus-mt-lv-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)


texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

# Translate texts
for text in texts:
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    translation = tokenizer.decode(translated[0], skip_special_tokens=True)
    print(f"Original: {text}")
    print(f"Translated: {translation}")
