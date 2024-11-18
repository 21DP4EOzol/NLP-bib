from transformers import pipeline


generator = pipeline("text-generation", model="gpt2")


prompt = "Reiz kādā tālā zemē..."


generated_text = generator(prompt, max_length=50, num_return_sequences=1)
print(generated_text[0]["generated_text"])
