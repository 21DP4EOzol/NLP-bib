import spacy

# Load English language model
nlp = spacy.load("en_core_web_md")

# Words to analyze
words = ["house", "apartment", "sea"]

# Get vectors and calculate similarity
for i, word1 in enumerate(words):
    for word2 in words[i + 1:]:
        vector1 = nlp(word1).vector
        vector2 = nlp(word2).vector
        similarity = nlp(word1).similarity(nlp(word2))
        print(f"Similarity between '{word1}' and '{word2}': {similarity:.2f}")
