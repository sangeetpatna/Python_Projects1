sum= 0
while (True):
    ItemInput=input("Enter number of the item or press e to exit : ")
    if ItemInput!='e':
        PriceInput=input("Enter price of the item or press e to exit : ")
        if PriceInput!='e':
            sum=sum+(int(ItemInput) * int(PriceInput))
            print(f"Total Bill till this item is : {sum}")
            continue
        else:
            print(f"Total bill is {sum}.")
            break
    else:
        print(f"Total bill is {sum}.")
        print("Thanks for using the calculator!")
        break