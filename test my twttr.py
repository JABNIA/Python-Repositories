from isVowel import is_vowel
user_input = input("what i have to shorten?")

def main():
    
    print(shorten(user_input))

def shorten(word):
        return is_vowel(word)

if __name__ == "__main__":
    main()