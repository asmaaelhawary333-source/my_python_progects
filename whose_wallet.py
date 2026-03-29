import random
print("""
welcome to'whose wallet'
you will give me a list of names, and i will pick a person to pay
""")
user_name=input(" if you ready, enter the nmes separated by a comma... \n")
names=user_name.split(", ")
payer=random.choice(names)
print(f"please ask {payer} to take his wallet out. dinner is on him")
