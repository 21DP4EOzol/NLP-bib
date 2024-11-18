import spacy

nlp = spacy.load("en_core_web_md")

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."


doc = nlp(text)

for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")
