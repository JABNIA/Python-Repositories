import emoji

#define main function, wich asks user to input emoji name
def main():
    emoji = input("Enter emoji string: ")
#Call for emojisation
    print(emojize(emoji))


#define emojisation function
def emojize(string):
    emoji_in_string = emoji.emojize(string)
    return emoji_in_string

main()