def isPrime(num):
    if num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True

a=int(input("enter the lower bound: "))
b=int(input("enter the upper bound: "))

for i in range(a,b+1):
    if isPrime(i):
        print(i)