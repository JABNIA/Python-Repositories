
def main():
    getText()
    
        
def getText(): 
    userText = input("Input your text: ")
    if userText !="":
        print("Text recived by user is", userText, "and it is", len(userText), "characters long" )
    else:
        print("Text is required!")
        getText()



main()