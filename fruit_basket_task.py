basket=[["apples", "bananas"], ["milk", "juice"]]
print(basket)
change=input("press enter to change the contact ...")
if change=="":
    basket[0].insert(0, "oranges")
    basket[0].append("kiwi")
    basket[1].insert(1,"coffee" )
    basket[1].append("tea")
    basket.append([1,2,3])
    # basket[1].remove("milk")
    print(f"here is updated basket {basket}")
