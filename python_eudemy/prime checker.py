def prime_checker(num):
    f=0
    for i in range(2,num):
            if num%i == 0:
                f=1
                break
    if f==1:
        print("It's not a prime number")
    else:
        print("It's a prime number")

n=int(input("enter the number: "))
prime_checker(n)

