import random


try:
    def main():
    
        level = input("level: ")

        if level == "1" or level == "2" or level == "3":
            professor()    
        else: 
            main()  
        
    def professor():
                errors = 0
                score = 0
                for _ in range(10):
                    x = random.randint(0, 10)
                    y = random.randint(0, 10)
                    summary = x + y   
                    answer = get_value(x, y)     
                    if answer.isalpha():
                        while answer.isalpha():
                            print("EEE")
                            get_value(x, y)
                            errors += 1
                            if errors == 2:
                                print("EEE")
                                print(f"{x} + {y} = {summary}")
                                errors -= 2
                                break
                    elif int(answer) != summary:
                        while int(answer) != summary:
                            print("EEE")
                            errors += 1
                            answer = int(input(f"{x} + {y} = "))
                            if errors == 2:
                                print("EEE")
                                print(f"{x} + {y} = {summary}")
                                errors -= 2
                                break
                    else: 
                        score += 1
                print(f"Your score is {score}")           

    def get_value(rand1, rand2):
        answer = input(f"{rand1} + {rand2} = ") 
        return answer

                
    main()
except ValueError:
    main()