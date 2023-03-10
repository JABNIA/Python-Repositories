greeting = input("Your greeting: ")


if "Hello" in greeting or "hello" in greeting:
    print("$0")
elif greeting != "Hello" or greeting != "hello" and "h" in greeting:
    print("$20")
else:
    print("$100")