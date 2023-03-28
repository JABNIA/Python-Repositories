menu ={
     "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    } 
global total_price    

order_items = []


try:
    
    def main():
        order = input("Item: ").title()
        if order not in menu:
            main()
        else:
            order_items.append(menu[order])
            print("total:", sum(order_items))
            main()

    main()

except EOFError:
    ...