item_list = dict()

def main(list_of, item):
        
        if item in list_of:
            list_of[item] += 1
        else:
             list_of[item] = 1
        print(list_of)

while True:
    try:
        product = input("product: ").upper()
        main(item_list, product)


    except EOFError:
        for item, count in item_list.items():
             count = item_list[item]
             print(count, item)
        break
