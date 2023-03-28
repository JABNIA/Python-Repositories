#1. import all nercesary modules: sys, figlet and random
#2. Create user input, where user gives us string which we must translate to figlet
#3. Check for command line arguments amounth and decide what actions will take place




from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = list(figlet.getFonts())
cl_arguments = list(sys.argv)
random_font = fonts[random.randint(0, len(fonts) - 1)]


def main():
   
    if len(sys.argv) == 1:
        user_input = input("Write something: ") 
        figlet.setFont(font = random_font)
        print(figlet.renderText(user_input))    
    elif (len(sys.argv) == 3 and sys.argv[1] =="-f" and sys.argv[2] in fonts 
        or len(sys.argv) == 3 and sys.argv[1] == "--fonts" and sys.argv[2] in fonts):
        user_input = input("Write something: ") 
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(user_input))
    else: 
        print("Invalid Usage")  

main()