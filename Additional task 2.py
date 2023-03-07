import random


greetingVariants = ["Hello", "Greetings", "Nice to meet you", "Welcome", "Wats up"]
randomGreeting = greetingVariants[random.randrange(0,4)] 

print(randomGreeting, input("What is your name?"))