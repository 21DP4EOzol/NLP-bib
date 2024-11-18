import re

text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

# output
cleaned_text = re.sub(r'@\w+|http\S+|[^a-zA-Zā-žĀ-Ž\s]', '', text).lower().strip()
print(cleaned_text)
