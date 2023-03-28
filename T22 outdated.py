months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
new_format = ""

def date_formater():
    
    date = input("Date: ")
    if "/" in date: 
        new_format = date.split("/")
        print(f"Date: {new_format[2]}-{new_format[0]}-{new_format[1]}" )
    
    elif " " in date:   
        new_format = date.split(" ")
        
        if new_format[0].isnumeric():
            date_formater()
        else:        
            date_in_month = int(new_format[1].replace(",", ""))
            month_index = months.index(new_format[0].title())
            
            if new_format[0].title() in months:
                if date_in_month <= 9 and month_index >= 10:
                    print(f"Date: {new_format[2]}-0{date_in_month}-{months.index(new_format[0].title()) + 1}")
                elif month_index >= 9 and month_index <= 10:
                    print(f"Date: {new_format[2]}-{date_in_month}-0{months.index(new_format[0].title()) + 1}")
                elif date_in_month <= 9 and month_index <= 9:
                    print(f"Date: {new_format[2]}-0{date_in_month}-0{months.index(new_format[0].title()) + 1}")
                else: 
                    print(f"Date: {new_format[2]}-{date_in_month}-{months.index(new_format[0].title()) + 1}")

        
date_formater()
