#First 10 natural numbers
def natural_no():
    for i in range(1,11,1):
        print(i)
print(natural_no())

#Sum of first n natural no.
def sum_of_natural_no():
    n=int(input("Enter the value of n to get the sum of first n natural= "))
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print(sum)
print(sum_of_natural_no())

#Function to reverse a no.
def reversing_number():
    n=int(input("Enter a no. to get its reversed no.="))
    while(n>0):
        dig=n%10
        print(dig,end="")
        n=n//10
print(reversing_number())

#Function to count digits in a no.
def counting_numbers():
    n=int(input("enter a no.:"))
    sum=0
    while(n>0):
        dig=n%10
        n=n//10
        sum=sum+1
    print("Digits are=",sum)    
print(counting_numbers())

#function to check whether the number is palindrome or not
def reversing_number():
    reversed_number=0
    n=int(input("Enter a no. to get its reversed no.="))
    original=n
    while(n>0):
        dig=n%10
        reversed_number=reversed_number*10 +dig
        n=n//10
    if (reversed_number==original):
        print("Entered no. is a Palidrome no.")
    else:
        print("Entered no. is not a Palidrome no.")
print(reversing_number())

#function to generate fibonacci series
def fibonacci():
    n = int(input("How many terms? "))
    a = 0
    b = 1
    count = 0
    while count < n:
        print(a, end=" ")
        c = a + b    # next number
        a = b        # shift
        b = c        # shift
        count += 1
fibonacci()

# Functions to perform calculations
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b

def calculator():
    # Step 1: User selects operation
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Select operation (1/2/3/4): "))   
    # Step 2: Take input from user
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    # Step 3: Perform calculation and display result
    if choice == 1:
        print("Result =", add(a, b))
    elif choice == 2:
        print("Result =", subtract(a, b))
    elif choice == 3:
        print("Result =", multiply(a, b))
    elif choice == 4:
        print("Result =", divide(a, b))
    else:
        print("Invalid choice!")
# Calling the calculator function
calculator()

#Creating a text file using pandas
import pandas as pd
data={"Name":["pari","preeti","ritu","muskan","tanu","isha"],
      "Roll no.":[90,98,104,82,87,45],
      "course":['B.Tech','B.Tech','B.Tech','B.Tech','B.A','Bsc']}
df=pd.DataFrame(data)
print(df)
pd.to_csv("students_detail.csv")

# Function to display all students
def show_students():
    df = pd.read_csv("students_detail.csv")
    print("\n===== All Students =====")
    print(df)
show_students()

# Function to perform division
def divide():
    try:
        # Step 1: Take input from user
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        # Step 2: Perform division
        result = a / b
        # Step 3: Display result
        print("Result =", result)
    except ZeroDivisionError:
        # Step 4: Handle division by zero
        print("Error! Cannot divide by zero")
    except ValueError:
        # Handle invalid input
        print("Error! Please enter a valid number")
# Calling the function
divide()

# Creating a student class
class Student:
    # Step 1: Initialize student details
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    # Step 2: Display student details
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
    # Step 3: Check if student passed or failed
    def result(self):
        if self.marks >= 40:
            print(self.name, "is Passed ✅")
        else:
            print(self.name, "is Failed ❌")
# Creating student objects
s1 = Student("Rahul", 85)
s2 = Student("Priya", 35)
# Calling functions
s1.display()
s1.result()
print("---------------------")
s2.display()
s2.result()
