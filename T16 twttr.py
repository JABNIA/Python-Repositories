text = input("Input your text here: ")
short_text = ""

for i in text:
    if (i == "a" or i == "A" or i == "e" or i == "E"
        or i == "i" or i == "I" or i == "o" or i == "O"
        or i == "u" or i == "U"):
        continue
    else:
        short_text += i

print(short_text)