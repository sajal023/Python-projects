import random

x=input("enter the names: ")
name=x.split(", ")
n=len(name)
r_name=random.randint(0,n-1)
choice=name[r_name]
print(f"{choice} is going to pay the bill")