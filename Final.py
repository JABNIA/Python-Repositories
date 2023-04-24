import sys
import random
questions = [
    {
        "question": "What is the capital of New Zealand?",
        "var1": "Warsaw",
        "var2": "Canbera",
        "var3": "Wellington",
        "var4": "Otawa"
    },
    {
        "question": "What is the smallest planet in our solar system?",
        "var1": "Mercury",
        "var2": "Venus",
        "var3": "Mars",
        "var4": "Uranus"
    },
    {
        "question": "Which popular video game franchise has released games with the subtitles World At War and Black Ops?",
        "var1": "Stalker",
        "var2": "Battlefield",
        "var3": "Arma",
        "var4": "Call of duty"
    },
    {
        "question": "Who was the head of state in Japan during the second world war?",
        "var1": "Hirohito",
        "var2": "Oda nobunaga",
        "var3": "Prince Moriyoshi",
        "var4": "Tokugawa Iesada"
    },
    {
        "question": "What was the Turkish city of Istanbul called before 1930?",
        "var1": "Percepolis",
        "var2": "Troy",
        "var3": "Constantinople",
        "var4": "Alexandria"
    }]

correct_answers = ["Wellington", "Mercury", "Call of duty", "Hirohito", "Constantinople"] 
wrong_answers = 5
number_list = []
question_index = 0
score = 0

def main():
    start = input("Type \"Yes\" if you are ready, or \"No\" if you need time: ")
    if start == "No" or start == "no":
        sys.exit("OK! please take your time and try again :)")
    elif start == "yes" or start == "Yes" or start == "YES":
        quiz()
    else:
        sys.exit("Please enter \"Yes\" or \"No\"")



def quiz():
    global score
    counter = 0
    random.shuffle(questions)
    while counter < len(questions):
        #question_choice variable is question keys/value from "question list" dictionary
        question_obj = questions[counter]
        #keys are in questio_obj variable
        obj_answers = list(question_obj) 
        #take "question" key from obj_answers list to make only answers list
        question = obj_answers.pop(0)

        print(question_obj[question])
        
        randomizer(obj_answers, question_obj)
        
        answer = user_answer(obj_answers, question_obj)
        if answer is False:
            print("❌")
        else:
            score += 1 
            print("✅")
        counter += 1
        
    print(f"Your result is {score} out of {len(questions)}")      

def randomizer(n_list, values):
    #here program switches n_list elements indexes
    random.shuffle(n_list)
    i = 1 #just for answer number nothing more
    for item in n_list:
        print(f"{i}. {values[item]}")
        i += 1 
        
    

def user_answer(n_list, values):
    global wrong_answers
    global score
    answer = input("Enter answer: ")
    #Input variants may be Words and numbers Firstr case recognizes words and the second case is for numbers
    if answer.isalpha() or " " in answer:
        cap_answer = answer.capitalize()
        valid = validate(cap_answer)
        return valid
    elif answer.isnumeric():
        #basicali program gets wich number ofanswer he tinks is corect and program adapts
        # it as correct index for answer variants list
        int_answer = int(answer) - 1
        valid = validate(values[n_list[int_answer]])
        return valid                 
    else:
        print("Wrong answer value") 
        if wrong_answers == 1:
            sys.exit("FAILURE ❌❌❌")
        else:
            while wrong_answers > 0:
                wrong_answers -= 1
                print(f"{wrong_answers} truys left")
                user_answer(n_list, values)
                return wrong_answers

def validate(answer):
    if answer in correct_answers:
        return True
    else:
        return False 

if __name__ == "__main__":
    main()