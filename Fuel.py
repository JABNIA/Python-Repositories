from precentage_calculator import precentage_counter

#input expression in X/Y format
try:
    def main():
        fuel_amount = input("Fuel amount: ")
        fuel_numbers = fuel_amount.split("/")
        fuel = 0
#turn X and Y to Integers 
       
        
        if (fuel_numbers[0].isalpha() or
             fuel_numbers[1].isalpha()):
             raise ValueError
        if fuel_numbers[1] == 0:
              raise ZeroDivisionError

        X = int(fuel_numbers[0])
        Y = int(fuel_numbers[1])
        fuel = 1.3
            
        if fuel > 1.00:
            raise ValueError
        elif 0.99 <= fuel <= 1.00:
            print("F")
        elif 0.02 <= fuel < 0.98:
            print(f"{int(fuel * 100)}%")
        elif fuel <= 0.01: 
            print("E")
        
# also print F if tank is 99% or more, or E if tank is 1% or less empty
    if __name__ == "__main__":
        main()
    #We must define error messages like ValueError and ZeroDivisionError
except ValueError:
        main()
except ZeroDivisionError:
        main()
