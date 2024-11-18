from collections import Counter
import re

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."


text = text.lower()
words = re.findall(r'\b\w+\b', text)  # izraksta vardus 

# skaita
word_counts = Counter(words)
print(word_counts)
