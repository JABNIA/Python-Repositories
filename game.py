import random



#1. in this project we input our level of difficulty for this game
level = int(input("Level: "))

#2. next depending on this level we measure range for random numbers
    
random_int = random.randint(1, level)


#3. afther that we input our number and implement conditions, if our input is more, less or 
#   equal to random number. depending on result, we continiue or finish our program
def user_input():
        user_choice = input("Enter number: ")
        if user_choice.isalpha():
              user_input()
        elif user_choice.isnumeric():
            formated_ui = int(user_choice)
            if formated_ui > 0:
            
                if formated_ui > random_int:
                    print("Too large!")
                    user_input()
                elif formated_ui < random_int: 
                    print("Too small!")
                    user_input()
                else:
                    print("Just right!")
        else: 
              user_input()

user_input()