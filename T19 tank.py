try:
    def main():
        tank = input("Fraction: ")
        values = []

        for i in tank:
            if i == "." or i.isalpha():
                raise ValueError
            elif i == "/":
                    values = tank.split(i)

        x = values[0]
        y = values[1]

        tank_amount = int(x) / int(y)
            

        if float(tank_amount) <= 1.00: 

            if float(tank_amount) >= 0.99:
                    print("F")
            elif 0.01 <= float(tank_amount) <= 1.00:
                print(str(int(100 * float(tank_amount))) + "%")
            elif float(tank_amount) <= 0.01:
                print("E")
        else:
            main()
    
    main()
except ValueError:
        print("Value error")
        main()
except ZeroDivisionError:
        print("Zero division error")
        main()