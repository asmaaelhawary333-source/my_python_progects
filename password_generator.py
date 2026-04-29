# ----method 1:using for loops (fundamental logic)
import random
import string
password_list=[]
print(" ***welcome to the password generator***")
total_length=int(input("enter the total number of characters in thr password \n"))
character=int(input("enter the number of the letters in the password \n"))
num=int(input("enter the number of numbers in the password \n "))
pun=int(input("enter the number of punctuation in the password \n"))
total_count=character+num+pun
if total_count!=total_length:
    print("invalid input")
else:
    for x in range(character):
        password_list.append(random.choice(string.ascii_letters))
    for i in range(num):
        password_list.append(random.choice(string.digits))
    for a in range(pun):
        password_list.append(random.choice(string.punctuation))
    random.shuffle(password_list)
    password="".join(password_list)
    print(f"your password is {password}")


# ----method 2: using random.choices (optimized method)----
import random
import string
password_list=[]
print(" ***welcome to the password generator***")
total_length=int(input("enter the total number of characters in thr password \n"))
character=int(input("enter the number of the letters in the password \n"))
num=int(input("enter the number of numbers in the password \n "))
pun=int(input("enter the number of punctuation in the password \n"))
total_count=character+num+pun
if total_count!=total_length:
    print("invalid input")
else:
    letters=string.ascii_letters
    numbers=string.digits
    symbols=string.punctuation
    
    password_chars=(
        random.choices(letters, k=character)+
        random.choices(numbers, k=num)+
        random.choices(symbols, k=pun)
    )
    random.shuffle(password_chars)
    password="".join(password_chars)
    print(f"generated password,{password}")







