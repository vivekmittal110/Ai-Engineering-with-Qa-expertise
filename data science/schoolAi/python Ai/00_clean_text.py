import re

def clean_text(text):
    text = re.sub(r"[^\w\s]","",text)
    text = " ".join(text.split())
    return text.lower()

input_text = "Hello vivek  mittal,!!.... How are yOu?..."
cleaned = clean_text(input_text)
print(cleaned)