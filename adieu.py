try: 
    names = list()

    while True:
        ask_name = input("name: ")
        names.append(ask_name)
        names_string = ", ".join(names[0:len(names) - 1])


except EOFError:        
        if len(names) == 1:
            print(f"Adieu, adieu, {names[0]}")
        elif len(names) > 1: 
            print(f"Adieu, adieu, {names_string} and {names[len(names) - 1]}")