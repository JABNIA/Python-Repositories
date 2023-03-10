def main():
    text = input('')
    makeFace(text)


def makeFace(Text):
    if ":)" in Text or ":(" in Text:
        print(Text.replace(":)", "🙂").replace(":(", "😟" )) 


main()


