import re
import sys

try: 
    lines_count = 0
    
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        argument = re.findall(".py$", sys.argv[1])
        if argument:
            with open(sys.argv[1], "r") as file: 
                for line in file:
                    if line.startswith("#") or line == "\n":
                        continue
                    else:
                        lines_count += 1
            print(lines_count)
        else: 
            print("Not a python file")        
            
        # for line in file_lines:
        #     if line == "" :
        #         file_lines.remove(line)
        #     elif line.startswith("#"):
        #         file_lines.remove(line)
        
except FileNotFoundError:
    print("File does not exist")