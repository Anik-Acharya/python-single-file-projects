# Prints primes between two given numbers
# By:- Anik Acharya 

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

print(f"primes between {a} and {b} are (including {a} and {b}):")
for i in range(a,b+1):
    if isPrime(i):
        print(i)