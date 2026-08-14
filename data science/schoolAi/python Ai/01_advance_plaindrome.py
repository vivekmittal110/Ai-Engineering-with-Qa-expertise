def plaindrome(text):
    # text = "".join(i.lower() for i in text if i.isalnum())
    return text == text[::-1]

x = plaindrome("A man, a plan, a canal, panama")
y = plaindrome("nitin")
print(x)
print(y)