# For loop 

# Q.1 Print natural numbers from 1 to 10 using loop 
print("/n Natural number from 1 tp 5")
for i in range(1,6,1):
    print(i)

# Q.2 Print number from 5 to 1 in (reverse order)
print("\nReverse order")
for r in range(5,0,-1):
    print(r)

# Q.3 Print all even number from 1 to 10
print("\nEven Numbers")
for n in range(2,11,2):
    print(n)

# Q.4 Print all Odd number from 1 to 1s0
print("\n Odd Numbers")
for w in range(1, 11):
    if w % 2 !=0:
        print(w)

# Q.5 Print multiplication table of 5
print("\nMultiplication table of 5")
for v in range(1,11):
    print("5x", v, "=",5*v)

# Q.6 Calculate sum of number from 1 to 100
print("\nSum of the number from 1 to 100")
total= 0
for i in range(1,101):
    total = total+i
print("is ->",total)

# Q.7 Print numbers until user enters 0

num = int(input("\nEnter a number:"))
while num!=0:
    print("You entered:",num)
    num = int(input("Enter the number:"))

# Q.8 Count digits of a number(example: 1234 -> 4 digits)
print("\nCount digits of a numbers")
num= int(input("Enter the value:"))
count =0
while num>0:
    num = num//10
    count=count +1
print("Toatal digit:",count)

# Q.9 Check whether a number is prime or not 
print("\ncheck whether a number is prime or not")
term = int(input("Enter the number:"))
prime = True
for i in range(2,term):
    if term % i == 0:
        prime = False
        break
if prime==True:
    print("Prime Number")
else:
    print("Not prime")

# Q.10 Print the square of a number from 1 to 10 using for loop
print("\nSquare of a number from 1 o 10")
for i in range(1,11):
    square = i**2
    print(square)