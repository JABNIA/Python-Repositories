import sys
#open list file and reformate strings
def main(list):
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3: 
        sys.exit("Too many command-line arguments")
    elif sys.argv[1] != "list.csv":
        raise FileNotFoundError
    else:   
        new_list = []
        with open(list) as file:
            for line in file:
                #split line in to 3 diffrent strings
                form = line.split(",")
                clear_form = []
                if len(form) < 3 :
                    continue
                else:
                #format words separately and delete " ", '"' and "\n" elements from words
                    for word in form:
                        clear_word = ""
                        for let in word:
                            if let.isalpha():
                                clear_word += let
                        clear_form.append(clear_word)
                    #here we add clear list for each student into new joined list     
                new_list.append(clear_form)
            reformate(new_list)
            
            

def reformate(list):
    #Function creates new file after.csv and writes down all names and houses from previous list
    f = open(f"{sys.argv[2]}", "a")
    for li in list: 
        f.write(f"\"{li[1]} {li[0]}\", {li[2]}\n")
    return f


try: 
    main(sys.argv[1])

except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}")