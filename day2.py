a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("sum:", a + b)
print("difference:", a - b)
print("product:", a * b)
print("division:", a / b)


age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age <=19:
    print("You are a teenager.")
else:
    print("You are an adult.")


a= int(input("Enter a number: "))
if a>0:
    print("positive number")
elif a<0:    
    print("negative number")
else:    
     print("zero")

b=int(input("Enter a number: "))
if b%2==0:
    print("even number")
else:
    print("odd number")


a = int(input("Enter a number: "))    
b = int(input("Enter another number: "))
if a>b:
    print(a, "is greater than", b)
elif a<b:
    print(b, "is greater than", a)    
else:
    print(a, "is equal to", b)


c=int(input("Enter a number: "))    
if c > 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")    


name = input("Enter your name: ")
mark1 = float(input("Enter mark1: "))
mark2 = float(input("Enter mark2: "))
mark3 = float(input("Enter mark3: "))
total = mark1 + mark2 + mark3
average = total / 3
print("name:", name)
print("total:", total)
print("average:", average)
if average >= 90:
    print("Grade: A")
elif average >= 80:    
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:   
    print("Grade: D")
elif average >= 50:         
    print("Grade: E")
else:
    print("Grade: F")