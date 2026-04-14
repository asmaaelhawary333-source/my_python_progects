print("*** welcome ti ISshop calculator***")
items=[]
price=[]
shopping=int(input(" how many items are there in your basket today ? \n"))
for basket in range(shopping):
    print(" lets get to counting them...")
    products=input("tell my the name of the item \n")
    items.append(products)
    cost=int(input(f" what is the price of {products} \n"))
    price.append(cost)
print(items)
print(sum(price))
