import random
x=int(input("enter lower range :"))
y=int(input("enter higher range:"))
k=random.randint(x,y)
print(k)

def guess():
    z=int(input("enter the number you have guessed:"))
    if z!=k:
        print("entered number is not the guessed number")
        guess()
    else:
        print("you have guessed correctly")
        exit()

guess()

