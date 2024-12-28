import random
import string

letters = string.ascii_letters
numbers = []
for i in range(0, 10):
    a = numbers.append(i)
symbols = string.punctuation
print("welcome to password generator!")
nr_letters = int(input("how many letters do you want?: "))
nr_numbers = int(input("how many numbers do you want?: "))
nr_symbols = int(input("how many symbols do you want?: "))

password = ""
comb = letters + str(symbols) + str(numbers)
length = nr_symbols + nr_numbers + nr_letters

for i in range(1, length):
    x = random.choice(comb)
    password += x
print(password)

'''#2nd approach:-\
password_list=[]
for i in range(1,nr_letters+1):
   password_list+=random.choice(letters)

for i in range(1,nr_symbols+1):
   password_list+=random.choice(symbols)

for i in range(1,nr_numbers+1):
   password_list+=str(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for i in password_list:
    password+=i

print(password)
'''