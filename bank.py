
def main():
    greeting = input("Your greeting: ")
    print(variants(greeting))
    
def variants(greet):    
    if "Hello" in greet or "hello" in greet:
        return "$0"
    elif greet != "Hello" and greet != "hello" and "h" in greet:
        return "$20"
    else:
        return "$100"
    
if __name__ == "__main__":
    main()