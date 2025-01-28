"""
#learning python starts from here
print("hello world")
#veriables

#Strings
first_name = "Sahil"
last_name = "Kumar"
email = "sahil1234@gamil.com"

#Integer
age = 19
marks = 421

#Float
price = 20.34
gpa = 8.6
distance = 12.23

#Boolean
is_student = True
is_working = False
for_sale = True

#Simple print
#with print using + for veriable.it places it without spaces and using , then it places space
print("your first name is {first_name}",first_name,"\nyour last name is {last_name}",last_name)
#print with string formated
print(f"%d",last_name," name",first_name)
print(f"first_name {first_name} last_name {last_name}")
print(f"your email is {email}")
print("your total marks is",marks)
print(f"your age is {age}")
print(f"price of one pen is ${price} and you ran {distance}km for this")
print("your gpa is",gpa)
print("you are a student",is_student)
print(f"you are employed {is_working}")

if for_sale:
    print("this car is for sale")
else:
    print("this car is not for sale")

#TypeChecking
name = "Sahil Kumar"
print(type(name))   #printing out the data type of the veriable

#TypeCasting
nums = 32
decimal = 53.98
name = "fuck you"
is_not_completed = True
just_checking = ""

nums = int(decimal)  #converting decimal number to integer by type casting it to int()
decimal = float(is_not_completed)  #converting decimal to string by type casting it to str()
name = str(is_not_completed)
is_completed = bool(name)
#nums = int(is_not_completed)   #this works just fine turned coment for convenience
just_checking = bool(just_checking)
#nums = int(name)   # cannot convert string to int or float  #it does't work

print(nums)
print(decimal)
print(name)
print(is_completed)
print(just_checking)

#accepting user input
name = input("what is your name?: ")
    #better alternative to these two lines is to just use input()
#print("what is your age?:")
#age = int(input())
    #alternative way to write these two lines and this one takes input in same line instade of next line
age = int(input("what is your age?: "))  #this is better than writing 2 lines of code only to enter age in next line
age +=1
job_status = input("did you got the job?: ")

if job_status=="yes":
    job_status = True
    job_status = bool(job_status)
else:
    job_status = False
    job_status = bool(job_status)

print() # adding new line just for fun
print(f"your name is {name}")
print(f"your age {age} year old")

if job_status:
    print("you have a job")
else:
    print("you dont have a job")

#arithmetic & math stuf

friends = 0
friends +=6
friends -=1
friends *=3
friends /=5
friends = int(friends)
friends **=3 # this is exponent expression this means (friends)^3 # its a power expression
friends = friends % 2   #modulas operator used for remainder
#you have odd number of friends
print(friends)
print(3**3)     #another exponent expression  3 power 3 (3^3)

x = 3.14
y = -4.21
z = 5

result = round(x)       #round will round the decimal number to closest integer number
result = round(x,3)     #round the decimal number upto 3 digits
result = abs(y)         #abs is the absolute value of a number decimal or integer
result = pow(x,z)       #pow is the power same as x ** z or x^z
result = max(x,y,z)     #max help find max value among few values
result = min(x,y,z)     #min help find min value among few values

print(result)

"""
import os
import random
from platform import processor, system

from PyQt5.QtCore import Qt
from PyQt5.uic.Compiler.qtproxies import QtGui

"""
import math     #importing math module so we can access math functions

x = 9
y = 23.543

#print(math.pi)           #PI constant 22/7 = 3.141592653589793
#print(math.e)            #exponential constant e = 2.718281828459045
#print(math.sqrt(x))      #square root of x
#print(math.pow(x,2)      #power of x raised 2
#print(math.ceil(y))      #round the decimal number to the upper number
#print(math.floor(y))     #round the decimal number to the lower number
"""
"""
#make a circumference of the circle calculator
import math

PI = math.pi
print("***** Calculate Circumference of the Circle *****")
radious = float(input("Enter radious of the circle: "))

result = 2 * PI * radious

print(f"Circumference of the circle is: {round(result,2)}cm")
"""
"""
#Calculate the area of the circle
import math

radious = float(input("Enter the radious of the circle: "))
result = math.pi*pow(radious,2)

print(f"area of the circle: {round(result,2)}cm²")
"""
"""
#find the hypotenious of the right angle triangle
import math

p = float(input("Enter the prependicular of the triangle: "))
b = float(input("Enter the base of the triangle: "))

h = math.sqrt(pow(p,2)+pow(b,2))
print(f"hypotenious of the right angle triangle: {round(h,2)}cm")
"""
"""
#if else and elif must be on same line vertically and executables must be indent atleast 1 block
#i have no idea what i am doing
import math

age = int(input("Enter your age: "))

if age <=0:
    print("you cant sign up")
elif age < 18:
    print("you are too young to sign up")
elif age > 100:
    print("you are too old to sign up")
else :
    print("you are ready to sign up")
"""
"""
#making a fully functional calculator
i = 0
print("***** Calculator in Python *****")

num1 = float(input("Enter num1: "))
op = input("Enter op (+,-,*,/): ")
num2 = float(input("Enter num2: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else :
    print("invalid input!")
    exit(1)

print(f"result: {round(result,2)}")

exit(0)
"""
"""
response = input("Would you like some food (Y/N): ")

if response == "n":
    print("no food for you!")
elif response == "y":
    print("have some food")
else:
    print("invalid input!")
"""
"""
name = input("Enter your name: ")
if name == "":
    print("you did not enter your name!")
else:
    print(f"your name is: {name}")
"""
"""
online = True
if online:
    print("the user is online")
else:
    print("the user is offline")
"""
"""
#Python Calculator

num1 = float(input("Enter num1: "))
op = input("Enter op(+,-,*,/): ")
num2 = float(input("Enter num2: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("invalid input!")
    exit(1)

print(f"result: {round(result,2)}")
"""
"""
#Python Weight Convertor

print("***** Pound to Kilogram Weight Convertor *****")

weight = float(input("Enter your weight: "))
unit = input("Convert it to kilogram or pound (K or L): ")

if unit == "K":
    weight = weight / 2.2046
    unit = "kg"
    print(f"your weight is: {round(weight, 2)} {unit}")
elif unit == "k":
        weight = weight / 2.2046
        unit = "kg"
        print(f"your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight * 2.2046
    unit = "lbs"
    print(f"your weight is: {round(weight, 2)} {unit}")
elif unit == "l":
    weight = weight * 2.2046
    unit = "lbs"
    print(f"your weight is: {round(weight, 2)} {unit}")
else:
    print("invalid input!")
"""
"""         #to type ° in windows type alt + 0176
print("***** Celsius or Fahrenheit temperature convertor *****")

temp = float(input("Enter the temperature: "))
#temp = round(temp,1)
convert_unit = input("convert it to Celsius or Fahrenheit (C/F): ")

if convert_unit == "f":

convert_temp = round((temp * (9/5))+32,1)
print(f"{temp}°C : {convert_temp}°F")

elif convert_unit == "c":

convert_temp = round((temp - 32)*(5/9),1)
print(f"{temp}°F : {convert_temp}°C")

else:
print(f"{convert_unit} is an invalid unit of measurement")
"""
"""
#logical operator (and, or , not)

name = input("Enter your name: ")
age = input("Enter your age: ")
if age:
    age = int(age)
    age+=1
#here is the use of (and , or , not) #it works just like ( && , || , ! ) just in words
if name == "" or not age:
    print("you must enter your name and age!")
elif name and age:
    print(f"your name is: {name}")
    print(f"your age is: {age}")
"""
"""
#termary operators in Python 

#it works just like any other language it performs and it returns
#but syntex is in english and it performs if first then check if condition
#this is the standard way to do if else using ternary operator in Python
x = -5
y = True if x>0 else False   #perfoem something or return something if condition is True
print(y)                     #else perform or return something else 
print(type(y))
"""
"""
x = 5455      #  print(f"{x} is neither positive not negative") if x == 0
print(f"{x} is negative") if x<0 else print(f"{x} is positive")
result = "EVEN" if x % 2 == 0 else "ODD"
print(result)
"""
"""
x = 23
y = 12
max = x if x>y else y
min = x if x<y else y
print(min)
"""
""" 
#this is a nested if else ternary operator
x = 100
status = "adult" if 18 <= x < 60 else ("old" if 60 <= x < 100 else ("child" if 0 <= x < 18 else "you should't even be alive'"))

print(status)
"""
"""
name = "sahil kumar"
#name = "234"

result = len(name)
result = name.find("a")  #it return -1 if cant find
result = name.rfind("a")
result = name.capitalize()  #it will only make first letter of a string capital space does shaperate the string
result = name.upper()       #make the entire string capital regardless of space shaperating string
result = name.lower()       #make the entire string lower case regardless of space shaperating string
result = name.isdigit()     #return True if string only contain number and no letter
result = name.isalpha()     #return True if string only contain alphabet letter with no spaces
result = name.isupper()     #return True if entire string is capital regardless of space
result = name.islower()     #return True if entire string is in lower case space gets ignored
result = name.count("a")    #count every occurance of the the character
result = name.replace("a", "-")     #replace every occurance of the character with a character

print(result)
"""
"""
number = input("Enter your number with Country code: ")
first_dash = number.find("-")    #find index position of first occurance of the character

number = list(number)            #convert string into list (array of char) using list()
number[first_dash] = " "         #replace specific char using their index with specific char
number = "".join(number)         #convert it back to string using join() since we converted it to list
                                 #we need to add string (it can be an empty string) in order to join the string

#number = number.replace("-"," ",1)     #this replace will only replace 1st occurance of the character not all
number = number.replace("-","")     #this replace will replace all occurance of the character
                                                     #replace first ocurance of "+91 " char with space only once
number = number.replace("+91 ","",1)    #since number is string it can replace

number = int(number)    #now converting the number string into int(integer or number)
#number += 8        #since now its int(integer) you can perform arthemetic operations like these

print(number)
"""
"""
# validate user input
# 1.username is no more than 12 character long
# 2.username must not contain spaces
# 3.username must not contain any digits
import time     #importing time just for testing
username = input("Enter a username: ")

if len(username) > 12:
    print("username must be 12 character long")
elif username.find(" ") != -1:  #you can also use ! symbol for not when checking condition with = : !=
    print("username must not contain any spaces")
elif not username.isalpha():
    print("username must not contain numbers")
time.sleep(2)       #added this just for testing and value is in secound
print(f"welcome {username}")
"""
"""
#indexing with String

#number = input("Enter number with country code: ")
number = "1234-5678-9012-3456"
first_das_index = number.find("-")
#number[3:3:1] = " "

#print(number[first_das_index])
#print(number)              #print entire string
#print(number[0])           #print char(string) at index position
#print(number[::3])         #print every third(3rd) element(char/string) its called steps
#print(number[::])          #print every element since we did't give any value python assumes we want all elements
#print(number[:4])          #print first 4 char from the string double dot is shaperating the passing value
#print(number[2:4])         #print char from index 2 to index 4 from the string
#print(number[2:4:2])       #print char from index 2 to index 4 at every 2nd step or at every 2nd element
#print(number[-2])          #print char at index 2 from reverse (reverse index is in negative "-")
#print(number[3:-2])        #print every 1st +ve char from 3 to -2
#print(number[-2:-9])       #cant print char from index -2 to -9 thats because index is in -ve
                            #its reading the string in reverse it trying to print char from index 2 to 9 from reverse
                            #but not specifieng steps so Python assumes at every 1st +ve steps
                            #so to print string using reverse index(-ve index) steps must be in -ve
                            #so it will jump from backward instade of jumping from front
#print(number[-2:-9:-2])    #print every 2nd char from reverse from 2 to 9 from reverse
#print(number[::-1])        #print string in reverse order
                            #print char from first to last at every 1st char from reverse
#print last 4 digit from number
last_number = number[-4:]
print(f"XXXX-XXXX-XXXX-{last_number}")
#reverse all the char in the string
reversed_number = number[::-1]
print(f"reversed string: {reversed_number}")
"""
"""
#format specifiers = {value:flags}

price1 = 3000000.14159
price2 = 56.2555
price3 = -54.2542

print(f"price1: ${price1:<+10,.3f}")    
print(f"price2: ${price2:<+10,.3f}")
print(f"price3: ${price3:<+10,.3f}")
"""
"""
#while loop
name = input("Enter your name: ")

while name == "":
    print("you did not enter your name")
    name = input("Enter your name: ")
print(f"hello {name}")
"""
"""
#compound interest calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter principal amount: "))
    if principal <= 0:
        print("principal can't be less than or equal to 0")
while rate <= 0:
    rate = float(input("Enter interest rate: "))
    if rate <= 0:
        print("rate can't be less than or equal to 0")
while time <= 0:
    time = int(input("Enter the time in year: "))
    if time <= 0:
        print("time can't be less than or equal to 0")

interest = principal *(pow(1+(rate/100),time))

print(f"Balance after {time} is: ${interest: ,.2f}")
"""
"""
#for loop
name = "sahil kumar"
name_len = len(name)
"""
"""
for x in reversed(range(1,11)):
    print(x)
"""
"""
for x in range(0,name_len):
    #print(name[x])
    print(f"{name[x]}")
"""
"""
for x in name:
    print(x)
"""
"""
#loop upto 20 and skip 13 and 17 break on 19

for x in range(0,20):
    if x == 13 or x == 17:
        continue
    elif x == 19:
        break
    else:
        print(x)

exit(0)
"""
"""
#make a countdown timer must takes input in second
import time

second = int(input("Enter the time in seconds: "))

for second in range(second,0,-1):
    time.sleep(1)
    hour = int(second / 3600)
    minute = int(second / 60)%60
    second = second % 60

    print(f"{hour:02}:{minute:02}:{second:02}")
print("TIMER's UP!")
"""
"""
#make countdown timer clock that loop forever
import time

app_started = True
while app_started:
    print("***** Countdown Timer Clock *****")
    hour = int(input("Enter hour (0 to 99): "))
    while not hour <= 99:
        print("hour must be less than or equal to 99")
        hour = int(input("Enter hour (0 to 99): "))

    minute = int(input("Enter minutes (0 to 59): "))
    second = int(input("Enter second (0 to 59): "))

    hour = hour * 3600
    minute = minute * 60
    second = second + minute + hour

    for second in range(second,0,-1):
        hour = int(second / 3600)
        minute = int(second / 60) % 60
        second = second % 60
        time.sleep(1)

        print(f"{hour:02}:{minute:02}:{second:02}")

    print("TIME'S UP!\n")
"""
#nested loop

"""
for x in range(3):
    for y in range(1,10):
        print(y,end = "")
    print()
"""
"""
#draw a rectangle using nested loop
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))

print(rows)
print(columns)

for row in range(rows):
    for column in range(columns):

        print("*",end = "")
        #print(f"{row}:{column}")
    print()
"""
"""
#draw a triangle using nested loop
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))

print(rows)
print(columns)

for row in range(rows):
    for columns in range(columns):

        print("*",end = "")
        #print(f"{row}:{columns}")
    print()
"""
#collection = single "veriable" used to store multiple values
# List = [] ordered changeable. duplicates ok
# Set = {}  unordered and unchangeble, but add/remove ok. no duplicates
#Tuple = () ordered(input order) and unchangeable(can't add or remove or arrange).duplicates ok.faster

#dictionary {keys : values} this one is also a collection studying this later on
"""
#List []
animals = ["cat","dog","rat","pig","tiger"]

#print(animals[1])
#for animal in animals:
#    print(animal, end = " ")
#print(len(animals))    #len function can also be used for collection like List to find the length(no of elements) of the colelction

#print(help(animals))   #print all the method available for this list collection print all the details
#print(dir(animals))    #print all the method available for this list collection print only name of methods
#animals[0] = "big cat" #modefy any element in List[] using their index number
#print(animals)
#print("big cat" in animals)    #return True if string found in animals List[]

#mathods of List []
animals.insert(1,"big cat")     #insert string at specific index in the List
animals.append("lion")      #append the string in the Container(List) #insert string at the end of List in Container
animals.append("cat")
#animals.remove("pig")
#animals.clear()
#x = animals.count("cat")
#x = animals.index("cat")    #return first index position of the string from the List[]
#animals.reverse()   #reverse the position of all the elements in the List(no order) reverse accordingly
#animals.sort()     #arrange the elements in alphabetical order
"""
"""
#to arrange in reversed alphabetical order
animals.sort()
animals.reverse()

print(animals)
"""
#Set {}
"""
    #its not arranged.each elements will be arranged differently every time you run
    #duplicates are not allowed. only 1 dog will print
animals = {"cat", "dog", "rat", "dog", "tiger"}
#animals[0] = "big cat"     #cannot modify the element not possible in set
animals.add("big cat")
animals.remove("big cat")

#animals.sort()     #not possible to arrange #Set{} is UnChangeble

animals.pop()   #this will pop(remove) the first element each (since it's not arranged it could be anyone)
#print(len(animals))     #len() method return total no element
#print("big cat" in animals)     #return True or False if string is present in the Set{} or not
#print(animals)
#print(help(animals))    #print all the details of all the available methods for the Set{}
#print(dir(animals))     #print name of all the available methods for the Set{} 
"""
#Tuple ()
"""
animals = ("cat", "dog", "rat", "dog", "tiger")

#print(dir(animals))    #print name of all the available methods for Tuple ()
#print(help(animals))   #print all the detailed description of all the available methods for Tuple ()
#print(len(animals))    #print no of elements of the Tuple ()
#print("big cat" in animals)     #return True if String found in the Tuple ()
#animals.add("big cat")     #not possible in Tuple ()
#animals.sort()            #not possible to short the Tuple()
    #only these 2 methods are available for Tuple ()
#print(animals.index("tiger"))  #return index of the string if it found in th Tuple ()
#print(animals.count("dog"))    #return no of time String present in the Tuple ()
    #NOTE:- its loopable so you can loop on it using for loop
for animal in animals:
    print(animal,end=" ")
"""
"""
#Shopping cart program create user cart.show all the products and total price.makesure user don't leave it empty
import itertools    #importing itertools (iteration tools) its generate infinite number from 0
                    #it can be user in loop like for loops
foods = []      #decalring the foods list but not assigning them
prices = []     #decalring the prices list but not assigning them
total = 0       #declare int veriable with value 0

print("***** Grocery shopping for foods *****")
print(" ------- CREATING YOUR CART -------")
print()
for x in itertools.count():     #count method counts the number that itertools will generate from 0
#    print(x)
    food = input("Enter the food to buy (Q to quit): ")
    while not food:
        food = input("Enter the food to buy (Q to quit): ")
    if food.upper() == "Q":
        break
    elif food and food != "q" or food != "Q" and food != foods[x]:
        price = input(f"Enter the price of the {food}: $")
        while not price:
            price = input(f"Enter the price of the {food}: $")
        price = float(price)
        foods.append(food)
        prices.append(price)
        total += price
print()
print("----- YOUR CART -----")

for i in range(len(foods)):
    print(f"{foods[i]:10}  {prices[i]:8}$")

print("---------------------")
print(f"Total:      {total:8}$")
print("---------------------")
"""
"""
#make a calculator for operations with 2 numbers with (+,-,*,/,%) operators

num1 = input("Enter num1: ")
while num1 =="":
    num1 = input("Enter num1: ")

op = input("Enter op(+,-,*,/,): ")
while op =="":
    op = input("Enter op(+,-,*,/,%): ")

num2 = input("Enter num2: ")
while num2 =="":
    num2 = input("Enter num2: ")

num1 = float(num1)
num2 = float(num2)

if op == "+":
    result = num1 + num2
    print(f"result: {result}")
elif op == "-":
    result = num1 - num2
    print(f"result: {result}")
elif op == "*":
    result = num1 * num2
    print(f"result: {result}")
elif op == "/":
    result = num1 / num2
    print(f"result: {result:.2f}")
elif op == "%":
    result = num1 % num2
    print(f"result: {result:.2f}")
else:
    print("Invalid Operator!")
    print("please use one of these op(+,-,*,/,)")
"""
#2D Collection

#2D List []     ordered, changeble(can add or remove), arrangeble, duplicates ok
#2D Set {}      unOrdered, unchangeble(can't arrange but can add or remove), duplicates ok
#2D Tuple ()    ordered, unchangeble(can't arrange or add or remove), duplicates ok

#animals = [["rat","bat","vempire"],["cat","lion","tiger"],["dog","sephard","pitbul","retriver"]]

"""
cat = ["tiger","lion","panther","cheeta"]
dog = ["shephard","pitbul","retriver"]
snake = ["viper","cobra","ratel"]
number = (0,1,2,3,4,5,6,7,8,9)

animals = [cat,dog,snake,number]

birds = ("falcon", "boldEagle", "hawk", "kiwi")
animals.insert(3,birds)

# print(animals)
# animals[2][1] = "King Cobra"
# print(animals[2][1])
# print(animals[3][0])
# print(animals[3][5])
# print(animals[3][9])

for count in animals:
    for subCount in count:
        print(subCount,end=" ")
    print()
"""
"""
#make a numPad using 2D Collection #basically make a collection of numPad and print it on screen

upto3 = (1,2,3)
from4to6 = (4,5,6)
from7to9 = (7,8,9)
rest = ("*",0,"#")
numPad = (upto3,from4to6,from7to9,rest)

for numPadElement in numPad:
    for numPadSubElement in numPadElement:
        print(numPadSubElement,end=" ")
    print()
"""
#quiz game in Python
"""
questions = ("1. What does AI stand for?",
             "2. Which library in Python is most commonly used for Machine Learning?",
             "3. In Java, what is the default value of a boolean variable?",
             "4. What is the extension of a compiled Java file?",
             "5. In C, which of the following is used to print formatted output?",
             "6. Which Python keyword is used to define a function?",
             "7. What is the output of the following Python code? print(2 ** 3)",
             "8. Which data structure is used to implement recursion?",
             "9. In Java, what is the purpose of the final keyword when applied to a variable?",
             "10. Which of the following is NOT a valid Python data type?")

options = (("a) Artificial Instruction",
            "b) Automated Intelligence",
            "c) Artificial Intelligence",
            "d) Autonomous Integration"),
           ("a) NumPy",
            "b) Pandas",
            "c) Scikit-learn",
            "d) Flask"),
           ("a) true",
            "b) false",
            "c) null",
            "d) 0"),
           ("a) .java",
            "b) .class",
            "c) .jar",
            "d) .exe"),
           ("a) printf()",
            "b) count",
            "c) print()",
            "d) format()"),
           ("a) function",
            "b) def",
            "c) func",
            "d) define"),
           ("a) 6",
            "b) 8",
            "c) 9",
            "d) Error"),
           ("a) Queue",
            "b) Stack",
            "c) Linked List",
            "d) Tree"),
           ("a) To declare a constant",
            "b) To allow inheritance",
            "c) To indicate a global variable",
            "d) To enable multithreading"),
           ("a) tuple",
            "b) array",
            "c) dictionary",
            "d) set"))

counter = 0
correctCount = 0
answers = ("C","C","B","B","A","B","B","B","A","B")
guesses = []

print("********** Quiz Game in Python **********")
for question in questions:
    print("-----------------------------------------------------------------------------------")
    print(question)
    for option in options[counter]:
        print(option)

    print()
    guess = input("Enter ( A, B, C, D): ").upper()
    guesses.append(guess)

    if guesses[counter] == answers[counter]:
        print("Correct!")
        correctCount += 1
    else:
        print("Wrong!")
        print(f"{answers[counter]} is the correct answer")

    counter +=1

print("-----------------------------------------------------------------------------------")
print("          RESULT          ")
print("-----------------------------------------------------------------------------------")

marks = (correctCount / counter) * 100
marks = int(marks)

print(f"Total correctly answered: {correctCount}")
print(f"SCORE: {correctCount}/{counter}     MARKS: {marks:3}%")
print("-----------------------------------------------------------------------------------")
"""
# dictionary {keys : values}

#dictionary is a collection of {key : value} pairs ordered ,changeable. No duplicates
#this is the samething as HashTable from Java
#dictionary is one of the four collections that we learn earlier and used in 2D Collection
"""
animalSpecies = {"Golden Retriever" : "Dog","German Shephard" : "Dog","Pit Bull" : "Dog","Huskey" : "Dog"}

# for animal in animalSpecies.keys():
#     if animal == "Golden Retriever":
#         print(f"\n{animal} is cute and friendly dog breeds.\n{animal} are very gentle and affectionate by nature.\n{animal} fer color is striking golden")
#     elif animal == "German Shephard":
#         print(f"\n{animal} is one of the smartest dog breed and they are very loyal pets and they are good guardian dog")
#     elif animal == "Pit Bull":
#         print(f"\n{animal} are one of the most dangerous dog breeds.\n{animal} are violent in nature and their higher muscle density makes them look threatening and dangerous")
#     elif animal == "Huskey":
#         print(f"\n{animal} is the most friendly and gentle dog breeds and they are very affectionate.this species of dog originally came from woolf so they do resemble wolf.\n{animal}'s very playful and energetic and they screem over every little thing they are drama queens.\nthey are like little kids")

    #just a reminder that if you forget the methods then you can always do this
#print(dir(animalSpecies))   #print name of all the methods available for dictionary
#print(help(animalSpecies))  #print details of all the methods available for dictionary

# animalSpecies.clear()       #this will clear all the {"keys" : "values"} pairs from the dictionary
# print(animalSpecies)        #it will print empty dictionary

#print(animalSpecies.get("Huskey")) #this(.get()) returns the values depending on the keys you enter as perimeter
# if animalSpecies.get("Huskey"): #well y can also use them in conditions like these
#     print("Huskey {keys} pair exist in the dictionary")
# else:
#     print("Huskey {keys} pair does't exist in the dictionary")

# print(animalSpecies)    #print the entire dictionary
# print(len(animalSpecies))

animalSpecies.popitem()     #remove the latest key:value pair from the dictionary
# print(animalSpecies)
animalSpecies.pop("Pit Bull")   #remove any key:value pair from the dictionary
# print(animalSpecies)
animalSpecies.clear()   #clear all the elements{keys:values} in the dictionary
# print(animalSpecies)
animalSpecies.update({"Lion":"Cat"})    #add new element {key :value} pair in the dictionary
animalSpecies.update({"Huskey":"Wolf"})     #add new {key : value} pair in the dictionary
# print(animalSpecies)
animalSpecies.update({"Lion":"Big Cat"})    #modefy the existing element{key : value} pair
animalSpecies.update({"Huskey":"Wild Wolf"})    #modefy the existing element{key : value} pair
# print(animalSpecies)

# print(animalSpecies.values())   #this(.values()) will returns all the values in the dictionary.its useful for condition in loop and if else
# print(animalSpecies.keys())     #this(.keys()) will returns all the keys in the dictionary.its useful for condition in loop and if else

# item = animalSpecies.items()    #(.items()) returns dictionary object of key value pairs which resemble 2D List[] of Tuple()
# print(item)     #item = [(),()] #these are iterable so they can be used in for loop

for key,value in animalSpecies.items():
    print(key,":",value)
"""
#make a menu program that display the menu and also display your order with total price
"""
menu = {"pizza": 3.0,"nacho":4.5,"popcorn":6,"fries":2.5,"chips":1,"pretzel":3.5,"soda":3,"lemonade":4.25}
selectedItems = []
selectedItemPrice = []

print("******** MENU LIST ********")
#print("-------- MENU LIST --------")
for key,value in menu.items():
    print(f" {key:15} :   ${value:.2f}")
#print("---------------------------")
print("***************************")
while True:
    selectItem = input("Select an item (q to quit): ")
    if selectItem.lower() == "q":
        break
    elif menu.get(selectItem) is not None:
        selectedItems.append(selectItem)
        selectedItemPrice.append(menu.get(selectItem))

total = 0

#print("****************************")
#print("----------------------------")

#print(f"******** YOUR ORDER ********")
print(f"-------- YOUR ORDER --------")
for i in range(len(selectedItems)):
    print(f" {selectedItems[i]:20} ${selectedItemPrice[i]:.2f}")
    total +=selectedItemPrice[i]

#print("****************************")
print("----------------------------")
print(f" Total Price:\t\t ${total:.2f}")
print("----------------------------")
#print("****************************")
"""
#Generate random number
"""
import random

#print(help(random))
#print(dir(random))

options = ["rock","paper","seasor"]

# min = 12
# max = 49
#number = random.randint(5,8)       #generates a random number between 5 and 8.5 and 8 both numbers are included
#number = random.randint(min,max)
#number = random.random()           #this will generate floating point number between 0 to 1 (1 is not included)
                                    #since it generates floating point number generating 1 will exceed the limit
                                    #so number will get very close to 1 but would not generate 1

# options2D = (["rock", "paper", "seaser"],(1,2,3),["one","two","three"])

# number = random.choice(options2D)    #generates a random choice from given choice (can't use dictionary{:} and set{}) but 2D lists can also be used
# number = random.choice(number)

# print(number)

# cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","Q"]

# random.shuffle(cards)     #(shuffle the list(cards))randomly arranging the cards(list)

# print(cards)
"""
#number guessing game
"""
import random

min = 1
max = 99
totalGuess = 10
guessCount = 0
wordGuessCount = "Zero"
numberFound = False

secretnumber = random.randint(min,max)
# secretnumber = 25

print("***** Number Guessing Game in Python *****")
print("------------------------------------------")
print(f"Select a number between {min} and {max}")
print(f"you can guess total {totalGuess} times")
print("------------------------------------------")

while guessCount < totalGuess:
    guessCount += 1

    if guessCount == 1:
        wordGuessCount = "1st"
    elif guessCount == 2:
        wordGuessCount = "2nd"
    elif guessCount == 3:
        wordGuessCount = "3rd"
    elif guessCount == 4:
        wordGuessCount = "4th"
    elif guessCount == 5:
        wordGuessCount = "5th"
    elif guessCount == 6:
        wordGuessCount = "6th"
    elif guessCount == 7:
        wordGuessCount = "7th"
    elif guessCount == 8:
        wordGuessCount = "8th"
    elif guessCount == 9:
        wordGuessCount = "9th"
    elif guessCount == 10:
        wordGuessCount = "10th"

    guess = input("Guess the Secret Number: ")

    if guess.isdigit():
        guess = int(guess)
        if guess == secretnumber:
            numberFound = True
            print()
            print("------------------------------------------")
            print("You Win!")
            print(f"Secret Number is: {secretnumber}")
            print(f"You Guessed the Secret Number in {wordGuessCount} guess")
            print("------------------------------------------")
            break
        elif guess > secretnumber and guessCount < totalGuess:
            print("Too High! Try again!")
        elif guess < secretnumber and guessCount < totalGuess:
            print("Too Low! Try again!")
    else:
        print("invalid input!")
        print(f"Please select a number between {min} and {max}")
        # print()

if not numberFound:
    print()
    print("------------------------------------------")
    print("You Lose!")
    print(f"Secret Number is: {secretnumber}")
    print("You Filed to guess the Secret Number")
    print("------------------------------------------")

"""
"""
#game of rock,paper,scissors
import random,time

options = ("Rock", "Paper", "Scissors")
playAgain = True

print("***** Rock,Paper,scissors in Python *****")

while playAgain:

    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Please Enter a choice (Rock,Paper,Scissors): ")
        player = player.capitalize()

    print(f"Computer: {computer}")
    print(f"Player: {player}")
    print()

    if player.capitalize() == computer.capitalize():
        print("its a draw!")
    elif player.capitalize() == "Rock" and computer.capitalize() == "Scissors":
        print("You Win!")
    elif player.capitalize() == "Rock" and computer.capitalize() == "Paper":
        print("You Lose!")
    elif player.capitalize() == "Paper" and computer.capitalize() == "Scissors":
        print("You Lose!")
    elif player.capitalize() == "Paper" and computer.capitalize() == "Rock":
        print("You Win!")
    elif player.capitalize() == "Scissors" and computer.capitalize() == "Rock":
        print("You Lose!")
    elif player.capitalize() == "Scissors" and computer.capitalize() == "Paper":
        print("You Win!")

    if not input("Play again (y/n): ").lower() == "y":
        playAgain = False

print("Thanks for playing!")
"""
"""
#make a dice roller program it should roll no of dice user enters number should be limited (1 to 6)
import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

dice = {1:("┌───────────┐",
           "│           │",
           "│     ●     │",
           "│           │",
           "└───────────┘"),
        2:("┌───────────┐",
           "│  ●        │",
           "│           │",
           "│        ●  │",
           "└───────────┘"),
        3:("┌───────────┐",
           "│     ●     │",
           "│           │",
           "│  ●     ●  │",
           "└───────────┘"),
        4:("┌───────────┐",
           "│  ●     ●  │",
           "│           │",
           "│  ●     ●  │",
           "└───────────┘"),
        5:("┌───────────┐",
           "│  ●     ●  │",
           "│     ●     │",
           "│  ●     ●  │",
           "└───────────┘"),
        6:("┌───────────┐",
           "│  ●     ●  │",
           "│  ●     ●  │",
           "│  ●     ●  │",
           "└───────────┘")}
#dice is the dictionary
rolled_dice = []
total = 0

no_of_dice = int(input("How many dice (1 to 6)?: "))

for l in range(no_of_dice):
    rolled_dice.append(random.randint(1,6))

for i in range(len(dice.get(1))):
    for j in range(no_of_dice):
        print(dice.get(rolled_dice[j])[i],end="")
    print()
for t in rolled_dice:
    total += t
print(f"Total: {total}")
"""
#functions
# are same as c maybe little better so
#function is a reusable block of code use "def" to define a function
"""
def happyNewYear(name):
    print(f"happy new year to you {name}")

happyNewYear("sahil")
happyNewYear("Pravin")
happyNewYear("mom")
happyNewYear("dad")

def add(num1 ,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1 , num2):
    return num1/num2

num1 = 545
num2 = 21

print(add(num1,num2))
print(subtract(num1,num2))
print(multiply(num1,num2))
print(f"{divide(num1,num2):.2f}")
"""
#make username generator based on name and date of birth and mobile number
"""
import random
import time

# these must update with previous files when app starts including counter
counter = 0
generated_username = []
generated_username_number = []
mobile_numbers = []
admin_privilege = []
generate_username_and_counter = {}
userdata_with_key_username = {}


#must not be modified
atoz = {0:"",1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

#username generator function in sign up screen function
def create_username(use_first_name,use_last_name,date_of_birth,mobile_number):
    username = ""
    global counter

    use_first_name = use_first_name.lower()
    use_last_name = use_last_name.lower()

    username = use_first_name[2] + use_first_name[0]  + date_of_birth[1] + atoz.get(random.randint(1,26)) + use_last_name[1] + atoz.get(random.randint(1,26)) + date_of_birth[-1] + use_first_name[-1] + use_last_name[-2] + mobile_number[2] + mobile_number[7] + atoz.get(random.randint(1,26))

    if username not in generated_username:
        # print("generated username not found in the list")
        mobile_numbers.append(mobile_number)
        generated_username.append(username)
        generated_username_number.append(counter)
        #adding the username with counter as the key
        generate_username_and_counter.update({counter : username})

        #here should be modefyed according to need later on !!!
        #adding the user data with username as the key
        userdata_with_key_username.update({username : {"first_name": use_first_name,"last_name": use_last_name,"date_of_birth":date_of_birth,"mobile_number":mobile_number}})
        # userdata_with_key_username[counter] = { username : { "first_name": use_first_name, "last_name": use_last_name,"date_of_birth": date_of_birth, "mobile_number": mobile_number } }

        counter +=1
    else :
        # print("generated username found in the list.generating new username")
        create_username(use_first_name,use_last_name,date_of_birth,mobile_number)

    return username

#login screen function
def login_screen():
    print()
    print("***** User Login *****")
    print("1. login with username")
    print("2. login with number")
    print("3. sign up")
    login_input = input("Enter your choice: ")
    while login_input != "1" and login_input != "2" and login_input != "3":
        login_input = input("Enter your choice: ")

    if login_input == "1":

        print("***** login with username *****")
        entered_username_count = 0
        entered_username = ""
        while not entered_username and entered_username_count < 3:
            entered_username = input("Enter your username: ")
            if entered_username in generated_username:
                entered_password = ""
                while not entered_password:
                    entered_password = input("Enter your Password: ")
                    if entered_password in mobile_numbers:
                        print("correct password")
                        home_page_screen(entered_username,entered_password)
                    else:
                        print("Incorrect Password!")
                        print("Try Again!")
                        entered_password = ""
            else:
                print("Incorrect username!")
                print("Try Again!") if entered_username_count < 2 else print()
                entered_username = ""

                entered_username_count +=1
        find_username = input("Enter Registered mobile no to find your username: ")
        if find_username:
            if find_username not in mobile_numbers:
                print("this mobile number is not registered")
                register = input("would you like to register (y/n)?: ")
                while register != "y" and register != "n":
                    register = input("would you like to register?: ")
                if register == "y":
                    sign_up()
                else:
                    login_screen()
            elif find_username in mobile_numbers:
                print(f"you username is: {generate_username_and_counter.get(mobile_numbers.index(find_username))}")
                print("register mobile number is the password")
                login_screen()
        else:
            login_screen()
    elif login_input == "2":
        print("***** login with number *****")
        enter_number = ""
        while not enter_number or not enter_number.isdigit() or len(enter_number) != 10:
            enter_number = input("Enter your registered mobile number: ")
        if enter_number in mobile_numbers:
            if verify_user(enter_number):
                home_page_screen(generate_username_and_counter.get(mobile_numbers.index(enter_number)),enter_number)
            else:
                login_screen()
        #elif enter_number not in mobile_numbers:
        else:
            print("this mobile number is not registered")
            register_number = input("would you like to register (y/n)?: ")
            while register_number != "y" and register_number != "n":
                register_number = input("would you like to register (y/n)?: ")
            if register_number == "y":
                sign_up()
            else:
                login_screen()
    else:
        sign_up()

#verify the user mobile number
def verify_user(verify_number):
    generated_otp = random.randint(1000,9999)
    print(f"message received on mobile number {verify_number}")
    print(f"you have received otp: {generated_otp} for user verification of mobile number {verify_number}")
    enter_otp = input("Enter 4 digit otp send on registered number: ")
    while not enter_otp.isdigit() or len(enter_otp) !=4:
        enter_otp = input("Enter 4 digit otp send on registered number: ")
    enter_otp = int(enter_otp)
    if enter_otp != generated_otp:
        print("invalid OTP")
        print("verification failed!")
        resend_otp = input("resend Otp (y/n): ")
        while resend_otp != "y" and resend_otp != "n":
            resend_otp = input("resend Otp (y/n): ")
        if resend_otp == "y":
            verify_user(verify_number)
        else:
            return False
    else:
        print("number verification successful!")
        return True

#see all your details screen
def your_details(your_username,your_password):
    print()
    print("***** User Details *****")
    print(f"Username: {your_username}      Password: {your_password}")
    print(f"first name: {userdata_with_key_username.get(your_username).get("first_name")}")
    print(f"last name: {userdata_with_key_username.get(your_username).get("last_name")}")
    print(f"date of birth: {userdata_with_key_username.get(your_username).get("date_of_birth")}")
    print(f"mobile number: {userdata_with_key_username.get(your_username).get("mobile_number")}")
    print()
    go_back = input("press (Q) to go back: ")
    while go_back.lower() != "q":
        go_back = input("press (Q) to go back: ")
    home_page_screen(your_username,your_password)

def modify_user_details(user_username,user_number):
    print("***** Modify User Data *****")
    print("1. Change First Name")
    print("2. Change Last Name")
    print("3. Change Date of Birth")
    print("4. Go Back")
    modify_user_data = input("Enter your choice: ")
    while modify_user_data != "1" and modify_user_data != "2" and modify_user_data != "3" and modify_user_data != "4":
        modify_user_data = input("Enter your choice: ")
    modify_user_data = int(modify_user_data)
    if modify_user_data == 1:
        print("***** change first name *****")
        print(f"current first name: {userdata_with_key_username.get(user_username).get("first_name")}")
        new_first_name = input("Enter new first name: ")
        while not new_first_name:
            new_first_name = input("Enter new first name: ")
        userdata_with_key_username.update({user_username: {"first_name": new_first_name,"last_name": userdata_with_key_username.get(user_username).get("last_name"),"date_of_birth": userdata_with_key_username.get(user_username).get("date_of_birth"),"mobile_number": userdata_with_key_username.get(user_username).get("mobile_number")}})
        modify_user_details(user_username,user_number)

    elif modify_user_data == 2:
        print("***** change last name *****")
        print(f"current last name: {userdata_with_key_username.get(user_username).get("last_name")}")
        new_last_name = input("Enter new last name: ")
        while not new_last_name:
            new_last_name = input("Enter new last name: ")

        userdata_with_key_username.update({user_username: {"first_name": userdata_with_key_username.get(user_username).get("first_name"),"last_name": new_last_name,"date_of_birth": userdata_with_key_username.get(user_username).get("date_of_birth"),"mobile_number": userdata_with_key_username.get(user_username).get("mobile_number")}})
        modify_user_details(user_username, user_number)

    elif modify_user_data == 3:
        print("***** Change Your Date of Birth *****")
        print(f"current date of birth: {userdata_with_key_username.get(user_username).get("date_of_birth")}")
        new_date_of_birth = input("Enter new Date of Birth: ")
        while not new_date_of_birth:
            new_date_of_birth = input("Enter new Date of Birth: ")
        userdata_with_key_username.update({user_username: {"first_name": userdata_with_key_username.get(user_username).get("first_name"), "last_name": userdata_with_key_username.get(user_username).get("last_name"),"date_of_birth": new_date_of_birth,"mobile_number": userdata_with_key_username.get(user_username).get("mobile_number")}})
        modify_user_details(user_username, user_number)

    else:
        home_page_screen(user_username,user_number)

def add_new_user():
    sign_up()

def ask_for_admin_homepage_screen(ask_admin_homepage_username,ask_admin_homepage_password):
    if ask_admin_homepage_username not in admin_privilege:
        print("you can't access this you are not the admin")
        home_page_screen(ask_admin_homepage_username,ask_admin_homepage_password)
    else:
        admin_homepage_screen(ask_admin_homepage_username,ask_admin_homepage_password)

def ask_for_admin_privilege(ask_for_username,ask_for_password):
    print()
    print("***** Ask for Admin Privilege *****")
    if ask_for_username not in admin_privilege:
        print("1. send request")    #request accepted or rejected
        print("2. Go Back")
        ask_for_choice = input("Enter your choice: ")
        while ask_for_choice != "1" and  ask_for_choice != "2":
            ask_for_choice = input("Enter your choice: ")
        ask_for_choice = int(ask_for_choice)
        if ask_for_choice == 1:
            luck = random.randint(0,1)
            if luck == 0:
                print("request accepted!")
                admin_privilege.append(ask_for_username)
                print(f"username {ask_for_username} set to admin.")
                home_page_screen(ask_for_username,ask_for_password)
            else:
                print("request rejected!")
                send_request = input("send request again (y/n)?: ")
                while send_request != "y" and send_request != "n":
                    send_request = input("send request again (y/n)?: ")
                if send_request == "y":
                    ask_for_admin_privilege(ask_for_username,ask_for_password)
                else:
                    home_page_screen(ask_for_username,ask_for_password)
        else:
            home_page_screen(ask_for_username,ask_for_password)
    else:
        print("you are already a admin")
        home_page_screen(ask_for_username,ask_for_password)

def logout_current_account():
    login_screen()

def print_counter(cou_username,cou_number):
    print()
    print(counter)
    print()
    admin_homepage_screen(cou_username,cou_number)

def print_generated_username(gen_user_username,gen_user_number):
    print()
    print(generated_username)
    print()
    admin_homepage_screen(gen_user_username,gen_user_number)

def print_generated_username_number(gen_user_num_username,gen_user_num_number):
    print()
    print(generated_username_number)
    print()
    admin_homepage_screen(gen_user_num_username,gen_user_num_number)

def print_mobile_numbers(mob_num_username,mob_num_number):
    print()
    print(mobile_numbers)
    print()
    admin_homepage_screen(mob_num_username,mob_num_number)

def print_admin_privilege(admin_pri_username,admin_pri_number):
    print()
    print(admin_privilege)
    print()
    admin_homepage_screen(admin_pri_username,admin_pri_number)

def print_generate_username_and_counter(gen_user_and_count_username,gen_user_and_count_number):
    
    print()
    for counter_key,username_value in generate_username_and_counter.items():
        print(f"{{{counter_key}: '{username_value}'}}")
    print()
    admin_homepage_screen(gen_user_and_count_username,gen_user_and_count_number)

def print_userdata_with_key_username(user_key_username,user_key_number):

    print()
    for username_key,userdata_value in userdata_with_key_username.items():
        print(f"{{'{username_key}': {userdata_value}}}")
    print()
    admin_homepage_screen(user_key_username,user_key_number)

def admin_homepage_screen(admin_homepage_username,admin_homepage_number):
    print()
    print("***** Admin Homepage Screen *****")
    print(f"username: {admin_homepage_username}      number: {admin_homepage_number}")
    print("1. counter")
    print("2. generated_username")
    print("3. generated_username_number")
    print("4. mobile_numbers")
    print("5. admin_privilege")
    print("6. generate_username_and_counter")
    print("7. userdata_with_key_username")
    print("8. Go Back to user homepage screen")
    admin_homepage_input = input("Enter your choice: ")
    while admin_homepage_input != "1" and admin_homepage_input != "2" and admin_homepage_input != "3" and admin_homepage_input != "4" and admin_homepage_input != "5" and admin_homepage_input != "6" and admin_homepage_input != "7" and admin_homepage_input != "8":
        admin_homepage_input = input("Enter your choice: ")
    admin_homepage_input = int(admin_homepage_input)

    if admin_homepage_input == 1:
        print_counter(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 2:
        print_generated_username(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 3:
        print_generated_username_number(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 4:
        print_mobile_numbers(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 5:
        print_admin_privilege(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 6:
        print_generate_username_and_counter(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 7:
        print_userdata_with_key_username(admin_homepage_username,admin_homepage_number)

    elif admin_homepage_input == 8:
        home_page_screen(admin_homepage_username,admin_homepage_number)

    else:
        print("Something went Wrong!")


#home screen function
def home_page_screen(home_page_username,home_page_number):
    print()
    print("***** User Homepage Screen *****")
    print(f"username: {home_page_username}      number: {home_page_number}")
    if home_page_username in admin_privilege:
        print("you are now the admin")
    print("1. see all your details")
    print("2. modify your details")
    print("3. add new user")
    print("4. go to admin homepage screen")
    print("5. ask for admin privilege")
    print("6. logout current account")
    home_page_input = input("Enter your choice: ")
    while home_page_input != "1" and home_page_input != "2" and home_page_input != "3" and home_page_input != "4" and home_page_input != "5" and home_page_input != "6":
        home_page_input = input("Enter your choice: ")
    home_page_input = int(home_page_input)

    if home_page_input == 1:
        your_details(home_page_username, home_page_number)

    elif home_page_input == 2:
        modify_user_details(home_page_username, home_page_number)

    elif home_page_input == 3:
        add_new_user()

    elif home_page_input == 4:
        ask_for_admin_homepage_screen(home_page_username,home_page_number)

    elif home_page_input == 5:
        ask_for_admin_privilege(home_page_username, home_page_number)

    elif home_page_input == 6:
        logout_current_account()

    else:
        print("Something went Wrong!")

#sign up screen function
def sign_up():
    first_name = ""
    last_name = ""
    dob = ""
    number = ""
    noUser = False

    print()
    print("***** New User Sign Up *****")
    print("Generate your unique username.")
    while not first_name:
        first_name = input("Enter your first name: ")
    while not last_name:
        last_name = input("Enter your last name: ")
    while not dob:
        dob = input("Enter you date of birth (dd-mm-yyyy): ")
    while not number:
        number = input("Enter your mobile number: ")
        number = number.replace(" ", "")
        number = number.replace("-", "")
        if number in mobile_numbers:
            print("this number is already registered please use another number or login")
            print("1. login")
            print("2. continue signing up")
            numberFound = input("Enter your choice: ")
            while numberFound != "1" and numberFound != "2":
                numberFound = input("Enter your choice: ")
            if numberFound == "1":
                print("login")
                login_screen()
                first_name = ""
                last_name = ""
                dob = ""
                number = ""
                noUser = True
                break
            else:
                number = ""

        #removing das and spaces from the strings
    first_name = first_name.replace(" ","")
    last_name = last_name.replace(" ","")
    original_dob = dob          #dob is cleaned no das or space original_dob is keeping the original user typed dob
    # dob = dob.replace(" ","")
    # dob = dob.replace("-","")

    make_username = ""

    if not noUser:
        make_username = create_username(first_name,last_name,dob,number)

    print("Your Entered Details are Shown.")
    print(f"your name is: {first_name.capitalize()} {last_name.capitalize()}")
    print(f"your date of birth is: {original_dob}")
    print(f"your mobile number is: {number}")
    print("Generating your Username...")
    time.sleep(1)
    print("Your Username is Generated Successfully.")
    # print("Your Account has been Created Successfully.")
    print("You are Successfully Signed Up.")
    print(f"Your Generated Username is: {make_username}")
    print(f"Your mobile number is the password: {number}")
    print("You will be automatically redirected to the Homepage.")
    home_page_screen(make_username,number)

    print()
    print("***** generated username list *****")
    print(mobile_numbers)
    print(generated_username)
    print(generated_username_number)
    print(generate_username_and_counter)
    for i in range(len(generated_username_number)):
        print(i)
        print(userdata_with_key_username.get(generate_username_and_counter.get(i)))
    # for j in range(len(generated_username_number)):
    #     print(j)
    #     print(f"{userdata_with_key_username.get(j).get(generate_username_and_counter.get(j)).get("first_name")} {userdata_with_key_username.get(j).get(generate_username_and_counter.get(j)).get("last_name")}")
    #     print(f"{userdata_with_key_username.get(j).get(generate_username_and_counter.get(j)).get("date_of_birth")}")
    #     print(f"{userdata_with_key_username.get(j).get(generate_username_and_counter.get(j)).get("mobile_number")}")

def load_all_userdata():
    create_username("sahil","kumar","20-10-2004","9801560832")
    create_username("nitish", "chaudhari", "02-03-2001", "6545645654")
    create_username("golu", "yadev", "12-05-2008", "6542879135")
    create_username("monu", "pasban", "21-08-2007", "6854768546")


#first screen login or sign up function
print("loading all the userdata.")
load_all_userdata()
print("All the userdata loaded successfully.")
print("***** You need to login first before entering *****")
print("if you dont have an account then sign up first")
print("1. Sign Up")
print("2. Login")
sign_or_login = input("Enter you choice: ")

while sign_or_login != "1" and sign_or_login != "2":
    sign_or_login = input("Enter you choice: ")
if sign_or_login == "1":
    #print("You will automatically redirected to the Sign Up page.")
    time.sleep(1)
    sign_up()
elif sign_or_login == "2":
    login_screen()

else:
    print("something went wrong!")

"""
#positional arguments and default arguments

#these are the arguments that you pass when calling a function
#positional arguments are the arguments that you pass every time as a value
"""
def sum(num1,num2):     #here num1 and num2 are positional arguments because these arguments must accept a value or a arguments each time
    return num1 + num2
print(sum(12,34))
"""
#default arguments
"""                             #order does matter so just make sure positional arguments comes first and then comes default arguments like num2 and num1
def turn_odd(num2,num1=0):      #here num2 is the positional argument and  num1 is the default argument meaning it already contain a default value
    for x in range(num1,num2):  #so if you dont pass any value then it gona use its default value and if you passed the value then 
        result = (2*x)+1        #its gona use the value that you passes rather than default value.default value only gets used when no value has been passed
        print(result)
turn_odd(20)
"""
"""
#keyword arguments
def turn_even(num1,num2):       #these are normal arguments of a function
    for x in range(num1,num2):
        result = (2*x)
        print(result)           #order of the arguments does not matter but positional arguments must be in the first and any other comes after positional argumets
turn_even(num2 = 15,num1 = 1)   #this is keyword arguments so just precede the value with the name of arguments you are pass that for and set that equal too
"""
#ARBITRARY arguments
# *args = allow you to pass non-key arguments
# **kwargs = allow you to pass multiple keyword arguments
#         * = unpacking operator (basically reference operator from C)
"""
def sum(*args):     #here args can be renamed as whatever but * this must be there because this is a  unpacking operator
    x = 0
    for i in args:
        x += i
    return x
print(sum(8,2,5,5,44))    # *args can accept as many arguments as needed and packs it as double meaning you can loop over it
"""
"""
def print_username(*args):
    for x in args:
        print(x,end=" ")

print_username("mr.","sahil","kumar","mobile no","+91","9801560832")
"""
# **kwargs = this allows you to pass multiple keyword arguments
"""
def print_address(**kwargs):        #this packs it into a dictionary with keyword as the key and passed arguments with the keyword as the value
    for x,y in kwargs.items():
        print(f"{x}: {y}")
print_address(street="ekangar sarai road",city="patna",state="bihar",zip="801301")  # *kwargs allows to pass multiple keyword arguments
"""
#using both *args and **kwargs
"""
def shipping_lavel(*args,**kwargs):
    for x in args:
        print(x,end=" ")
    print()
    for y in kwargs.values():
        print(y,end=" ")
#this works just fine but make sure order matter between these 2
shipping_lavel("mr.","pravin","kumar","9801560832","dhurgaon",street="123 fake street",city="patna",state="bihar",zip=165243,apr=651)
"""
"""
email = "sahil1123@gmail.com"

if "@gmail.com" in email and "." in email:
    print("its a valid email")
else:
    print("its not a valid email")
"""
#list comprehension
#its a consize way of writting for loop     #returnSomething/doWithSomething for something in something(list,tople,set,dixnuary) if condition is right and surrounded by []
"""
names = "sahil kumar"
num_int = 0
numes_in_number = [ord(name) for name in names]

# print(numes_in_number)

num = [chr(num) for num in numes_in_number]

[print(numb, end="") for numb in num if numb.isalnum()]     #this is an example of list comprehension and also you can only use these in a list or ("[]") must be used like this
"""
"""
def isprime(num):
    if num == 1:
        print(f"{num} is not a prime number")
        return False
    elif num < 4 and not num % 2 == 0 and not num % 3 == 0:
        print(f"{num} is a prime number")
        return True
    elif num % 2 == 0 and num % 3 == 0:
        print(f"{num} is not a prime number")
        return False

    x = 5
    for i in range(num):
        if num == x:
            continue
        elif num % x == 0:
            print(f"{num} is not a prime number")
            return False
        elif num % x+2 == 0:
            print(f"{num} is not a prime number")
            return False
        x +=6

numbers = [1,2,-5,-4,2,-54,1,0,2,4,-8,-9,-17,-11,-29]
positive_num = [num for num in numbers if num>0]
negative_num = [num for num in numbers if num < 0]
zeros = [num for num in numbers if num == 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
prime_numbers = [num for num in numbers if isprime(num)]

print(prime_numbers)
"""
"""
#type conversion string to int
word = "Z"
#ord() this allows us to convert char to a int based on their ASCII values but one char at a time
int_word = ord(word)

print(int_word)
"""
#match statement/function its same as switch in other languages
"""
def which_day(day):
    match(day):
        case 0:
            print("its sunday!")
        case 1 :
            print("its monday!")
        case 2:
            print("its tuesday!")
        case 3:
            print("its wednusday!")
        case 4:
            print("its thrusday!")
        case 5:
            print("its friday!")
        case 6:
            print("its saturday!")
        case _:
            print("invalid input!")
which_day(-7)
"""
"""
def is_weekend(day):
    match(day):
        case "monday" | "tuesday"| "wednusday"|"thrusday"|"friday":
            return False
        case "sunday"| "saturday":
            return True

print(is_weekend("monday"))
"""
#logical operators ( & , | , !) = (and,or,not)
"""
x = 2
if 0 < x & x < 5:
    print(x)
if x == 2 | x == 3:
    print("its a prime number")
if x != 2:
    print("x is not equal to 2")
else:
    print("number is out of range")
"""
#more match cases its very similat to switch in java and C
"""
def is_holiday(day):
    match(day):
        case "monday" | "tuesday" | "wednusday" | "thrusday" | "friday":
            print("its a work day")
        case "saturday" | "sunday":
            print("its a holiday")
        case _:
            print("invalid input!")
is_holiday("_")
"""
"""
#modules    #madules are files containing code that you want to import like here import math module its a build-in module 
# import math   #you can import either build in module or your own. you can create your own modules
# import math as m  #to create just make another .py file amd import it and thats it
from math import e

# print(math.e)
# print(m.e)
print(e)    #this will print value of e imported from math module which is exponential constant
e = 6       #this will override the e that was imported from math and change the value of e from exponential constant to 6
print(e)    #this will print 6
"""
#importing myOwn created module that i just created
"""
import sahilModule as sm    #that's all i created

# print(sm.pi)
result = sm.hypotenious(5,5)
result = sm.cube(5)
result = sm.square(5)
result = sm.circumferenceCircle(5)
result = sm.areaCircle(5)
result = sm.areaTriangle(5,3.5)
result = sm.areaRect(5,5)

print(result)
"""
#if __name__ == "__main__":
"""
def main():
    print(__name__)     #here printing the veriable it just normal veriabla just in-build one that stores name of the file if the file not executed directly
    print("this file has been executed directly")       #if the file executed directly then the veriable __name__ will be set to the string "__main__"

if __name__ == "__main__":  #if this file will execute directly then veriable __name__ will set to string "__main__"
    main()      #if the file has been executed indirectly as a module then veriable __name__ will set to the name of the file
"""
#making a simple banking program in python
"""
def deposit():
    print("**********************************")
    deposit_amount = float(input("Enter Deposit Amount: "))
    print("**********************************")

    if deposit_amount < 0:
        print("**********************************")
        print("Not a Valid Amount!")
        print("**********************************")
    else:
        return deposit_amount

    return deposit_amount

def show_balance(current_amount):
    print("**********************************")
    print(f"Your Current Amount is: ${current_amount:,.2f}")
    print("**********************************")
    return 0

def withdraw(current_amount):
    print("**********************************")
    withdraw_amount = float(input("Enter Withdraw Amount: "))
    print("**********************************")
    if withdraw_amount < 0:
        print("**********************************")
        print("Not a Valid Amount!")
        print("**********************************")
        return 0
    elif withdraw_amount > current_amount:
        print("**********************************")
        print("Entered Amount is higher than your back balance")
        print("**********************************")
        return 0
    else:
        return withdraw_amount

def main():
    current_amount = 0
    is_running = True

    while is_running:
        print("*********************************")
        print("     Simple Banking Program     ")
        print("*********************************")
        print("1. Check Balance.")
        print("2. Deposit.")
        print("3. Withdraw.")
        print("4. Exit.")

        print("**********************************")
        inpt = input("Enter Your Choice: ")
        print("**********************************")

        if inpt == "1":
            show_balance(current_amount)
        elif inpt == "2":
            current_amount += deposit()
        elif inpt == "3":
            current_amount -= withdraw(current_amount)
        elif inpt == "4":
            is_running = False
        else:
            print("invalid input!")

    print("Thanks for Using the Bank App.")
    print("Closing the Program...")

if __name__ == "__main__":
    main()
else:
    print("this module file has been executed indirectly")
"""
#slot matching in python   #🍇🍉🍒🍎🥑
"""
def spin():
    symbols = ["🍇","🍎","🍉","🍒","🥑"]
    rows = [random.choice(symbols) for _ in range(3)]
    return rows
def print_spin_rows(rows):
    print("*************")
    print(" | ".join(rows))
    print("*************")

def win_payment(rows,bet):
    if rows[0] == rows[1] == rows[2]:
        if rows[0] == "🍇":
            return bet * 2
        if rows[0] == "🍎":
            return bet * 3
        if rows[0] == "🍉":
            return bet * 5
        if rows[0] == "🍒":
            return bet * 10
        if rows[0] == "🥑":
            return bet * 20
    return 0

def main():
    current_balance = 100
    print("***********************")
    print("slot matching in python")
    print("symbols: 🍇🍉🍒🍎🥑")
    print("***********************")

    while current_balance > 0:
        print("*******************************")
        print(f"your current balance is: ${current_balance}")
        bet = input("Enter your bet amount: ")
        print("*******************************")
        while not bet.isnumeric():
            print("Invalid Amount!")
            bet = input("Enter your bet amount: ")
            print("*******************************")

        bet = int(bet)

        if bet <= 0:
            print("bet amount can't be less than or equal to 0.")
            continue
        elif bet > current_balance:
            print("Insufficient funds!")
            continue
        else:
            current_balance -= bet
            print("Spinning...\n")
            rows = spin()
            print_spin_rows(rows)
            reward = win_payment(rows,bet)

            if reward < 0:
                print("********************")
                print("you lost this round.")
                print("********************")
            else:
                print("********************")
                print(f"you won: ${reward}")
                print("********************")
            current_balance += reward
        play_again = input("would you like to play again(y/n): ").lower()
        if play_again != "y":
            break

    print("****************************************")
    print(f"Game Over! your current balance is: {current_balance}")
    print("****************************************")
    print("Closing the Program...")

if __name__ == "__main__":
    main()
"""
#message encryption program in python
"""
import string,random

char = " "+string.punctuation+string.digits+string.ascii_letters    #getting all the char and num for encryption from string module its in-build frature
char = list(char)       #converting all the char into list
key = char.copy()       #making the copy of the list for key to encrypt
random.shuffle(key)
encrypted = ""
decrypted = ""
plain_text = input("Enter a text to encrypt: ")
for i in plain_text:
    index_of_text  = char.index(i)
    encrypted += key[index_of_text]
print(f"Encrypted message is: {encrypted}")
encrypted_text = input("Enter a text to decrypt: ")
for i in encrypted_text:
    index_of_text  = key.index(i)
    decrypted += char[index_of_text]
print(f"Decrypted message is: {decrypted}")
"""
#hangman game in python
"""
import random
from sahilModule import words


hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\",
                  "   "),
               5:(" o ",
                  "/|\\",
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\")}

def  display_hangman(wrong_guess):
    print("**********")
    for i in hangman_art[wrong_guess]:
        print(i)
    print("**********")
def display_guesses(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True
    while is_running:
        display_hangman(wrong_guesses)
        display_guesses(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalnum():
            print("invalid input!")
            continue
        if guess in guessed_letter:
            print(f"you is already guessed the letter: {guess}")
            guessed_letter.add(guess)
            continue
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("You Win!")
            is_running = False
        elif wrong_guesses >= len(hangman_art)-1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("You Lose!")
            is_running = False

if __name__ == "__main__":
    main()
"""
#OOP (object oriented programing) in python
#this is same as java create a class than make instance of that class and give that object a name it can be either in the same file or imported as a module
"""
# class Car:        #this is the way to create object in same file by creating class in same file
#     def __init__(self,model,year,color,for_sale):
#         self.for_sale = for_sale
#         self.year = year
#         self.model = model
#         self.color = color
#     def move(self):
#         print(f"{self.model} is moving.")
#     def stop(self):
#         print(f"{self.model} is stoped.")
#     def description(self):
#         print(f"{self.year} {self.color} {self.model} {self.for_sale}")

from sahilModule import Car    #or this is the another way of creating obj by creating class in shaperate file and importing them like this

car1 = Car("bugati",2024,"yellow",True)
car2 = Car("farrari",2025,"red",False)

car1.move()
car1.stop()
car1.description()
print()
car2.move()
car2.stop()
car2.description()
"""
#class veriables    #they allow you to share data among all object created from that class
"""
class students:
    year = 2025     #class veriable this will shared with all instance of this class
    no_of_students = 0      #they are outside of the constructor but inside of the object class
    def __init__(self,name,age):    #this is the constructor of the class its called initialize and self is this
        self.name = name
        self.age = age
        students.no_of_students += 1    #here i am incrementing the class  veriable by accessing it by class name instade of self means this constroctor

student1 = students("sahil",18)
student2 = students("pravin",19)
student3 = students("Nitish",19)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(students.year)
print(students.no_of_students)
"""
#inheratance in python
"""
class animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class cat(animal):          #this cat class is inherating the animal class to inherate any class you pass the parent class in the perimeter
    def speak(self):            #this cat class have access to all the functionalityes of the parent class animal
        print("MEOWW!")
class dog(animal):              #this dog class also inherating the animal class ans has access to all the functionality of the parent class animal
    def speak(self):            #and these chield class cal also have their own unique function or veriable these functions called methods
        print("BHOO!")

orange_cat = cat("orange_cat")
black_cat = cat("black_cat")

pit_bull = dog("pit Bull")
huskey = dog("huskey")

print(orange_cat.name)
print(orange_cat.is_alive)
orange_cat.eat()
orange_cat.sleep()
orange_cat.speak()
print()
print(black_cat.name)
print(black_cat.is_alive)
black_cat.eat()
black_cat.sleep()
black_cat.speak()
print()
print()
print(pit_bull.name)
print(pit_bull.is_alive)
pit_bull.eat()
pit_bull.sleep()
pit_bull.speak()
print()
print(huskey.name)
print(huskey.is_alive)
huskey.eat()
huskey.sleep()
huskey.speak()
"""
#multiple inheritance
"""
class living_being:     #this is called multilayer inheritance so basically when parent class also has parent class and that parent class can also have parent class
    def __init__(self,name):
        self.name = name
    def is_alive(self):
        print(f"{self.name} is a living being and its alive")
class animals(living_being):    #this is a parent class and this is also a child class to its parent class (living_being) class
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class preditor(animals):        #this parent class inheriting animal class
    def hunt(self):
        print(f"{self.name} is hunting")
class pray(animals):            #this parent class also inheriting animal class
    def run(self):
        print(f"{self.name} is fleeing")
class rabit(pray):
    pass
class halk(preditor):
    pass
class fish(pray,preditor):      #this is called multiple inheritance so when chield class have more than 1 parent class its called multiple inheritance
    pass

rabit = rabit("rabit")
halk = halk("halk")
fish = fish("fish")

rabit.eat()
rabit.sleep()
rabit.run()
rabit.is_alive()
"""
#super
#this key word used to access the methods of super class (parent class)
"""
import math

class shapes:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def description(self):
        print(f"it is {self.color} and {"not filled" if not self.is_filled else "filled":}")

class circle(shapes):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def description(self):
        print(f"its a circle with area: {2*math.pi*self.radius**2:.2f}cm^2")
        super().description()       #here in the description method i am accessing parent class description also from description method

class triangle(shapes):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

    def description(self):
        print(f"its a triangle with area: {(1/2)*self.width*self.height:.2f}cm^2")
        super().description()

class square(shapes):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width

    def description(self):
        print(f"its a square with area: {self.width**2:.2f}cm^2")
        super().description()

square1 = square("red",False,5)
circle1 = circle("blue",True, 12)
triangle1 = triangle("green",False,12,25)

square1.description()
circle1.description()
triangle1.description()
"""
#polymorfism    #its a concept  #polymorfism is a greek work which means many form or shapes
"""
from abc import ABC,abstractmethod  #inheritance is a way to achieve polymorfism and another is duck typing

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class circle(shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2
class rectangle(shape):

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height
class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return (1/2)*self.base*self.height
class pizza(circle):
    def __init__(self,name,radius):
        self.name = name
        super().__init__(radius)

shapes = [circle(5),rectangle(3,8),triangle(8,6),pizza("vanila_flawor_pizza",5)]

for i in shapes:
    print(i.area())
"""
#duck typing
#as long as the object have the minimum necessary methods/attributs than it can be trited as another object
#if it looks like a dick and quacks like a duck, it must be a duck
"""
class animal:
    is_alive = True

class dog(animal):
    def speaks(self):
        print("BHOO!")

class cat(animal):
    def speaks(self):
        print("MEOW!")

class car:      #notice that car object is not a sub-class of the animal class 
    is_alive = False    #it just have the min neccessary methods so ful-fills min requirements to be a animal object

    def speaks(self):
        print("broom!")

animals = [dog(),cat(),car()]

for i in animals:
    i.speaks()
    print(i.is_alive)
"""
#static method
#this belongs to the class rather than any instance of that class
"""
class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"{self.name} : {self.position}"

    @staticmethod   #this is something you add when defining a static method
    def validL_position(position):      # this is a static method you access this from class rather than any instance of that class
        valid_positions = ["manager","cook","janitor","casher"]
        for valid_position in valid_positions:
            return True if position == valid_position else False

employee1 = Employee("sahil","manager")     #creating an object out of the class

print(employee1.get_info())     # printing the method by accessing it through the class

print(Employee.validL_position("manager"))  #printing the valid_position method by accessing it through Employee class directly without creating any objects because its a static method
"""
#class method
#this let you access the class data its best for class level data required access to the class itself
"""
class student:
    count = 0
    total_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa
    def get_info(self):
        return f"{self.name} {self.gpa}"
    @classmethod
    def get_count(cls):     #these are class method they allow you to access class data directly instade of any instance of that class 
        return f"total student count: {student.count}"
    @classmethod                #this is something you add when creating a class method
    def get_average_gpa(cls):       #these classmethods take (cls) as perimiter insted of (self)
        return f"total average gpa: {student.total_gpa / student.count:.2f}"

student1 = student("sahil",9.6)
student2 = student("pravin",8.2)
student3 = student("golu",8.25)

print(student.get_average_gpa())        #printing class method here by accessing directly through class rather than any instance of that class
print(student.get_count())      #creating an object of that class is unnecessory for a class method
"""
#magic methods in python
"""
class book:
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):      #modefying the beehiver of 'print(book1)' because it print memory address of where book1 is stored
        return f" '{self.title}' by {self.author}"

    def __eq__(self,other):     #modefying the behavior of print(book1 == book2) because it dont work well by default it not supppose to work
        return self.title == other.title and self.author == other.author

    def __lt__(self,other):     #modefying the behavior of print(book1 > book2) because it dont work
        return self.num_pages > other.num_pages

    def __gt__(self,other):     #modefying for greater than print(book1 < book2)
        return self.num_pages < other.num_pages

    def __add__(self,other):    #modefying for adding book1 and book2 so it will add their pages i am customizing it
        return f"{self.num_pages + other.num_pages} Pages"

    def __contains__(self,keyword):     #modefy to check if keyword exist in the title or in the author so return True or False
        return keyword in self.title or keyword in self.author

    def __getitem__(self,key):      #return the value if the key is title or author else return not found
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        else:
            return f"key '{key}' is not found"

book1 = book("programing in c","danis ritchi",214)
book2 = book("math","r.d.sharma",376)

# print(book1)
# print(book1 == book2)
# print(book1 > book2)
# print(book1 < book2)
# print(book1+book2)
# print("sharma" in book2)
print(book1["title"])
print(book1["audio"])
"""
# @property decorator
# we can define a method as a property of a class benefits is that we can add additional logic when read, write, or delete attributes
# it gives us getter, setter, and deleter method
"""
class Rectangle:
    def __init__(self,width,height):
        self._width = width         #here making width private by adding underscore at first so it can only be used in this class
        self._height = height       #technically we can access the private width as well by adding underscore in front of it

    def area(self):
        return f"{self._width * self._height} cm^2"

    @property       #this is a getter method
    def width(self):
        return f"{self._width} cm"  #returning the private width using '_' underscore

    @property       #this is also a getter method
    def height(self):
        return f"{self._height} cm"

    @width.setter   #this is a setter method
    def width(self,new_width):
        self._width = new_width
        print("new width has been updated successfully...")

    @height.setter  #this is also a setter method
    def height(self,new_height):
        self._height = new_height
        print("new height has been updated successfully...")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted successfully...")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted successfully...")

rectangle = Rectangle(3,4)
# rectangle.width = 12
rectangle.width = 6
rectangle.height = 8

del rectangle.width
del rectangle.height

# print(rectangle._width)
# print(rectangle._height)

# print(rectangle.width)      #printing the width using getter method of the object decorator is @property
# print(rectangle.height)
# print(f"area = {rectangle.area()}")
"""
#decorator
# it's a function that extends the behavior of another function without modifying it
#you can apply multiple decorator to a base function  #pass the base function as an arguments to a function
    # this is how to create a decorator so you can add it in your function to extends it behavior
"""
def add_sprinkle(function):     #this is the function that i making a decorator out of and name of the function is optional you can have whatever
    def wrapper(*args,**kwargs):              #wrapper function is important because without it function will get called when ever decorator is added
        print("*you add sprinkles 🎊*")
        function(*args,**kwargs)              #calling the function that i acception as a perimeter name of the function can be whatever
    return wrapper              #here returning wrapper function

def add_chocolate(function):
    def wrapper(*args,**kwargs):      #wrapper class should not accept the function it should only accept *args multiple arguments
        print("*you add chocolate 🍫*")
        function(*args,**kwargs)
    return wrapper

@add_chocolate
@add_sprinkle
def get_ice_cream(flavor):
    print(f"here is your '{flavor}' ice cream 🍨")

get_ice_cream("vanilla")    #when the function accepting perimeter then wrapper class must accept *args
"""
#exception handling (try,except,finally)
#exception are an event that interrupts normal flow of a program (ZeroDivisionError,TypeError,ValueError,and many more)
"""
try:        #we gona try any dangerous code in this try block
    user_input = int(input("Enter a number to divide 10: "))
    result = 10 / user_input
    print(result)
except ZeroDivisionError:       #and if catch any exceptions then perform something from this except block
    print("you cant divide any number with zero IDIOT!!!")
except ValueError:              #samething if catch exception match then perform something from this except block
    print("please enter a number!")
except Exception:        #here catching(except) all exceptions using this 'Exception' for all exceptions
    print("Something Went Wrong!")
finally:        #this finally block will always execute regardless of whether an exception occur or not!
    print("do some clean up here because it will always execute regardless of whether an exception occur or not")
    print("finally block is useful when opening any file closing any file in the end after it has been opened")
"""
#file handling
#file detection
"""
import os

path = "simple_file/text.txt"

if os.path.exists(path):
    print(f"the location '{path}' exist")
    if os.path.isfile(path):
        print("the location is a file")
    elif os.path.isdir(path):
        print("the location is a directory")
else:
    print("the location does not exist")
"""
#file writing (.txt) file
"""
# write_data = "i am not a robot"
employees = ["manager","guard","cook","cashier","owner"]

file_path = "simple_file/text.txt"

try:
    with open(file_path,"w") as write_file:
        # write_file.write(write_data,"w")
        for employee in employees:
            write_file.write(employee+"\n")
        print(f"file {file_path} sucessfully created")
except FileExistsError:
    print("File already exist!")
"""
#file writing (.json) file
"""
import json

employee1 = {"name": "patric","age": 23,"number": "9854628725"}
employee2 = {"name": "peter parker","age": 28,"number":"1234567859"}
employee3 = {"name": "jack","age": 25,"number": "6842397152"}
employee4 = {"name": "mikel","age": 29,"number":"6547891253"}

employees = {"manager":employee1,"cook":employee2,"casher":employee3,"owner":employee4}

file_path = "simple_file/text.json"

try:
    with open(file_path,"w") as file_for_json:
        json.dump(employees,file_for_json,indent=4)
except FileExistsError:
    print("file already exists!")
"""
#file writing (.csv) file
"""
import csv

employees = [["name","age","gender","number","job"],
             ["sahil kumar",18,"male","9801560832","unemployed"],
             ["pravin kumar",19,"male","6203557851","unemployed"],
             ["raj kumar",32,"male","1245786532","government job"],
             ["lalita mangasker",59,"femail","9875632145","singer"]]

file_path = "simple_file/text.csv"
    #with automatically closes the file
with open(file_path,"w",newline="") as file_csv:    #create file in write mode name file_csv 
    writer = csv.writer(file_csv)   #create a writer object and access the asv file writer feature
    for row in employees:       #loop over each rows and write them in the file using writer object
        writer.writerow(row)
"""
#file reading (.txt)
"""
file_path = "simple_file/text.txt"

with open(file_path,"r") as file_txt:
    content = file_txt.read()
    print(content)
"""
#file reading (.json)
"""
import json

file_path = "simple_file/text.json"

with open(file_path,"r") as file_json:
    file_dictinuary_content = json.load(file_json)  #loading data from json file directly all of it in its exact form dict

    print(file_dictinuary_content)
"""
#file reading (.csv)
"""
import csv

file_path = "simple_file/text.csv"

with open(file_path,"r") as file_csv:
    content = csv.reader(file_csv)      #store all the content in the veriable class is _csv.reader
    for rows in content:    #needs to print this line by line since its a collection
        print(rows)     #print csv file line by line because its a collection with rows and columns

    # print(content)    #this return memory address of the collection where its stored
"""
#date and time
"""
import datetime

date = datetime.date(2024,1,16)
today = datetime.date.today()

time = datetime.time(18,13,45)
now = datetime.datetime.now()

now_str = now.strftime("%H:%M:%S %d-%m-%Y")

print(now_str)
print(now)
"""
#timer clock
"""
import datetime
import time
import pygame

music_file = "simple_file/DJ RASANYA AKU SEDANG MELAYANG.mp3"

def set_timer(alerm_time):
    print(f"alerm time is set to: {alerm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print(current_time)

        if current_time == alerm_time:
            print("Times Up!")

            pygame.mixer.init()
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break

        time.sleep(1)

if __name__ == "__main__":
    alerm_time = input("Enter alerm time (HH:MM:SS): ")
    set_timer(alerm_time)
"""
#multi-threading
"""
import threading,time
    #these functions are the task that i need to do
def walk_dog():
    time.sleep(8)
    print("1.you walk the dog")
def take_out_trash():
    time.sleep(2)
    print("2.you take out trash")
def send_mail():
    time.sleep(4)
    print("3.you send a mail")

#these are the thread that doing something shaperately with main thread
thread1 = threading.Thread(target=walk_dog)         #target is the task that thread is doing
thread2 = threading.Thread(target=take_out_trash)   #thread1,2,3 these are thread veriables
thread3 = threading.Thread(target=send_mail)

print(type(thread1))        #its prints out as a  threading.Thread  class type

thread1.start()     # here starting the each individual threads
thread2.start()     # same thing as you can see
thread3.start()     # you have eyes right

thread1.join()      # here joining the threads so it will wait until it terminates
thread2.join()      # same thing
thread3.join()      # same
print("*****************************************")
walk_dog()          #calling the function directly so i can see the difference of time
take_out_trash()
send_mail()
"""
#feching data from website using api
"""
import requests     #this module is not included in the default package, need to install it manually
import json         #to install any python package use  "pip install <package_name> "

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}"  #complete the url here
#store the returned data into response veriable
    response = requests.get(url)    #send request to this url using build-in api in request module
#ckecking the html response code if its 200 then everything is OK if its not then not OK
    if response.status_code == 200:    #200 means OK  #404 means failed   #403 means forbidden
        return response.json()      #turn store data into json formate (key: value) and return it
    else:
        print("failed to retrieve data.")

if __name__ == "__main__":
    while True:
        input_name = input("Enter Pokemon Name: ")
        # pokemon_name = "pikachu"
        # pokemon_name = "typhlosion"
        
        pokemon_name = input_name

        #returned data is a dictinuary
        pokemon_data = get_pokemon_info(pokemon_name)

        if pokemon_data:

            # print(pokemon_data)    #print entire the data on the screen
            print(f"name: {pokemon_data["name"]}")    #printing the data (value) by key since its a dictionary
            print(f"id: {pokemon_data["id"]}")
            print(f"height: {pokemon_data["height"]}")
            print(f"weight: {pokemon_data["weight"]}\n")

            #here i am just storing it in a json file
            file_path = "pokemon_data_file/pokemon.json"
            #here i am creating the file and storing the data
            with open(file_path,"w") as json_file:
                json.dump(pokemon_data,json_file,indent=4)

        else:
            print("something went wrong!")
"""
#PyQt5 GUI interface
#PyQt5 is not build in library you need to install it manually using pip
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow       #just importing important stuf
from PyQt5.QtGui import QIcon   #importing this for icon

class MainWindow(QMainWindow):      #this class extends QMainWindow
   def __init__(self):              #this is the constructor
       super().__init__()           #constructor from super class
       image_path = "simple_file/moai-emoji.png"
       self.setWindowTitle("my first cool GUI")     #well this is how to set title in gui app
       self.setGeometry(700,300,500,500)    #set the dimension and location of the gui app
       self.setWindowIcon(QIcon(image_path))    #set the icon of the app

def main():
    app = QApplication(sys.argv)    #make app object of QApplication which accept sys.argv as perimeter
    window = MainWindow()           #make window object of MainWindow class which extends QMainWindow
    window.show()                   #make the window object visible by showing it using window.show()
    sys.exit(app.exec_())           #system.exit and application.exec_() this will wait for interaction

if __name__ == "__main__":
    main()
"""
#adding QLabel in PyQt5
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        image_path = "simple_file/moai-emoji.png"
        self.setWindowIcon(QIcon(image_path))
        self.setWindowTitle("my cool GUI app")
        self.setGeometry(600,300,850,600)

        label_text = "sahil kumar"

        label = QLabel(label_text,self)
        label.setFont(QFont("calibre",50))
        label.setGeometry(0,0,800,400)
        label.setStyleSheet("color: #00ff00;"
                            "background-color: black;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline")
        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignVCenter)   #V center
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter)   #H center
        # label.setAlignment(Qt.AlignLeft)
        # label.setAlignment(Qt.AlignCenter)    #center & center

        # label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)    #V bottom and H center "|" allows to mix flags

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
#adding image in the label using QPixmap from PyQt5.QtGui
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QIcon  # QPixmap allow to add image in the label

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        image_path = "simple_file/moai-emoji.png"
        sample_text = "sahil kumar"
        self.setWindowTitle("my cool Gui App")
        self.setWindowIcon(QIcon(image_path))
        self.setGeometry(450,200,950,700)

        label = QLabel(self)
        label.setGeometry(0,0,250,250)
        label.setStyleSheet("background-color: Green")

        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        #top-left corner
        label.setGeometry(0,0,label.width(),label.height())
        #top-right corner
        label.setGeometry((self.width()-label.width()),0,label.width(),label.height())
        #down-right corner
        label.setGeometry((self.width() - label.width()), (self.height() - label.height()), label.width(),label.height())
        #down-left corner
        label.setGeometry(0,(self.height()-label.height()),label.width(),label.height())
        #left-vertical-center
        label.setGeometry(0,(self.height()-label.height())//2,label.width(),label.height())
        #right-vertical-center
        label.setGeometry((self.width()-label.width()),(self.height()-label.height())//2,label.width(),label.height())
        #top-horizontal-center
        label.setGeometry((self.width()-label.width())//2,0,label.width(),label.height())
        #bottom-horizontal-center
        label.setGeometry((self.width()-label.width())//2,(self.height()-label.height()),label.width(),label.height())
        #center-center (horizontal & vertical center)
        label.setGeometry((self.width()-label.width())//2,(self.height()-label.height())//2,label.width(),label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
#PyQt5 layout
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QWidget,QGridLayout,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        image_path = "simple_file/moai-emoji.png"
        app_title = "my cool GUI App"
        simple_text = "sahil kumar"
        self.setWindowIcon(QIcon(image_path))
        self.setWindowTitle(app_title)
        self.setGeometry(600,200,800,800)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1",self)
        label2 = QLabel("#2",self)
        label3 = QLabel("#3",self)
        label4 = QLabel("#4",self)
        label5 = QLabel("#5",self)

        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: blue")
        label3.setStyleSheet("background-color: green")
        label4.setStyleSheet("background-color: yellow")
        label5.setStyleSheet("background-color: purple")

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        grid = QGridLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,1,0)
        grid.addWidget(label4,1,1)
        grid.addWidget(label5,2,2)

        # central_widget.setLayout(vbox)
        # central_widget.setLayout(hbox)
        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
#PyQt5 buttons
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton
from PyQt5.QtGui import QIcon,QFont
from PyQt5.Qt import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        image_file = "simple_file/moai-emoji.png"
        app_title = "my cool GUI App"
        self.setWindowIcon(QIcon(image_file))
        self.setWindowTitle(app_title)
        self.setGeometry(600,150,800,800)
        self.button = QPushButton("click me",self)
        self.label = QLabel("Hello Sahil",self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150,150,500,150)
        self.button.setFont(QFont("ink free",65))
        # self.button.setStyleSheet("font-family: ink free;"
        #                           "font-size: 45px;")
        self.button.setStyleSheet("font-style: italic;"
                                  "font-weight: bold")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(150,300,500,300)
        self.label.setStyleSheet("font-size: 55px;"
                                 "font-weight: bold")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def on_click(self):
        print("button clicked")
        self.button.setText("clicked!")
        self.label.setText("goodbuy sahil")
        self.button.setDisabled(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
#PyQt5 checkbox
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        image_path = "simple_file/moai-emoji.png"
        app_title = "my cool GUI App"
        self.setWindowIcon(QIcon(image_path))
        self.setWindowTitle(app_title)
        self.setGeometry(600,150,800,800)
        self.checkbox = QCheckBox("do you like pizza!",self)
        self.setStyleSheet("background-color: #636363;"
                           "color: #19ff19")
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,600,300)
        self.checkbox.setStyleSheet("font-size: 40px")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self,state):   #by the way state also have value of 0 or 2 unchecked and checked

            #1.this the first method
        # if state == 2:
        #     print("you like pizza!")
        # else:
        #     print("you do not like pizza!")

            #2.this is the second method    #all these three method are doing the exact same thing
        if state == Qt.Checked:
            print("you like pizza!")
        else:
            print("you do not like pizza!")

            #3.this is the third method
        # if self.checkbox.isChecked():
        #     print("you like pizza!")
        # else:
        #     print("you do not like pizza!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
#PyQt5 redio buttons
"""
import sys
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QRadioButton,QButtonGroup
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        image_file = "simple_file/moai-emoji.png"
        app_title = "my cool Gui App"
        self.setWindowIcon(QIcon(image_file))
        self.setWindowTitle(app_title)
        self.setGeometry(600,150,800,800)

        self.radio_button1 = QRadioButton("UPI",self)
        self.radio_button2 = QRadioButton("visa",self)
        self.radio_button3 = QRadioButton("MasterCard",self)
        self.radio_button4 = QRadioButton("Pay Cash",self)
        self.radio_button5 = QRadioButton("Pay Online",self)
        self.initUI()

    def initUI(self):
        self.radio_button1.setGeometry(0,0,300,50)
        self.radio_button2.setGeometry(0,50,300,50)
        self.radio_button3.setGeometry(0, 100, 300, 50)
        self.radio_button4.setGeometry(0, 150, 300, 50)
        self.radio_button5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{font-size: 30px;"
                           "padding: 10px;"
                           "color: #077ed9;}")
        self.button_group1 = QButtonGroup()
        self.button_group2 = QButtonGroup()

        self.button_group1.addButton(self.radio_button1)
        self.button_group1.addButton(self.radio_button2)
        self.button_group1.addButton(self.radio_button3)

        self.button_group2.addButton(self.radio_button4)
        self.button_group2.addButton(self.radio_button5)

        self.radio_button1.toggled.connect(self.radio_button_changed)
        self.radio_button2.toggled.connect(self.radio_button_changed)
        self.radio_button3.toggled.connect(self.radio_button_changed)
        self.radio_button4.toggled.connect(self.radio_button_changed)
        self.radio_button5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
#PyQt5 QLineEdit
"""
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QLineEdit,QPushButton,QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        image_file = "simple_file/moai-emoji.png"
        app_title = "my cool GUI App"
        self.setWindowIcon(QIcon(image_file))
        self.setWindowTitle(app_title)
        self.setGeometry(600,150,800,800)
        self.label = QLabel(self)
        self.line_edit = QLineEdit(self)
        self.submit_button = QPushButton("submit",self)
        self.reset_button = QPushButton("reset",self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(100,100,600,50)
        self.line_edit.setStyleSheet("font-size: 30px;")
        self.setStyleSheet("QPushButton{font-size: 30px}")
        self.line_edit.setPlaceholderText("Enter you name")

        self.reset_button.setGeometry(120,250,250,50)
        self.reset_button.clicked.connect(self.reset_button_do_something)
        self.submit_button.setGeometry(430,250,250,50)
        self.submit_button.clicked.connect(self.submit_button_do_something)

        self.label.setGeometry(130,400,550,300)
        self.label.setStyleSheet("color: #56fc14;"
                                 "font-size: 60px")
        self.label.setAlignment(Qt.AlignCenter)

    def reset_button_do_something(self):
        self.line_edit.setText("")

    def submit_button_do_something(self):
        text = self.line_edit.text()
        self.line_edit.setText("")
        self.label.setText(f"hello {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
#PyQt5 css stylesheet  .setStyleSheet()
"""
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton,QWidget,QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        image_path = "simple_file/moai-emoji.png"
        app_title = "my cool Gui App"
        self.setWindowIcon(QIcon(image_path))
        self.setWindowTitle(app_title)
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
"""
        # self.setStyleSheet("""
            # QPushButton{
            # font-size: 45px;
            # font-weight: bold;
            # font-style: italic;
            # font-family: areal;
            # padding: 30px 90px;
            # margin: 10px;
            # border: 5px solid;
            # border-radius: 25px;}
            #
            # QPushButton#button1{
            # background-color: #ff1b17;
            # }
            # QPushButton#button2{
            # background-color: rgb(37, 255, 8)
            # }
            # QPushButton#button3{
            # background-color: hsl(240, 100%, 54%)
            # }
            #
            # QPushButton#button1:hover{
            # background-color: #ff6361;
            # }
            # QPushButton#button2:hover{
            # background-color: rgb(131, 255, 115)
            # }
            # QPushButton#button3:hover{
            # background-color: hsl(240, 100%, 68%)
            # }
            # """)
"""
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
#
# if __name__ == "__main__":
#     main()
"""
#digital clock using PyQt5 library
"""
import sys
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        image_file = "simple_file/moai-emoji.png"
        app_title = "Digital Clock"
        self.setGeometry(600,300,300,100)
        self.setWindowIcon(QIcon(image_file))
        self.setWindowTitle(app_title)
        self.setStyleSheet("background-color: black")
        self.time_label = QLabel(self)
        self.timer = QTimer()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        #adding custom font here
        font_id = QFontDatabase.addApplicationFont("simple_file/DS-DIGIB.TTF")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_families)

        #setting my_font here in the time_label
        self.time_label.setFont(my_font)

        self.time_label.setStyleSheet("color: #00ff11;font-size: 60px")

        #calling the update time first
        self.update_time()

        #adding timer to update timer every second(1 frame / second)
        self.timer.timeout.connect(self.update_time)

        # updating time every second
        self.timer.start(1000)      #its in millisecond so 1000 mill sec = 1 sec

    #updating time
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

#making sure all these line of code only execute when called directly from same file
if __name__ == "__main__":
    main()
"""
#making a Stopwatch program using PyQt5 library in python
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt,QTimer,QTime
from PyQt5.QtGui import QIcon

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        image_file = "simple_file/img.png"
        self.setWindowIcon(QIcon(image_file))
        self.setWindowTitle("Cool Gui Stopwatch")
        self.time_label = QLabel("00:00:00.00",self)
        self.timer = QTimer(self)
        self.time = QTime(0,0,0,0)
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        #these are just StyleSheets that i just pasted it tool me 15 min to find right color and size
        self.setStyleSheet("background-color: #303030;")
        self.time_label.setStyleSheet("color: #00ff04;font-size: 60px;font-family: calibre;")
        self.start_button.setStyleSheet("color: #00f2ff;background-color: #454545;font-family: Areal;font-size: 20px;font-weight: bold;padding: 7px 35px;")
        self.stop_button.setStyleSheet("color: #00f2ff;background-color: #454545;font-family: Areal;font-size: 20px;font-weight: bold;padding: 7px 35px;")
        self.reset_button.setStyleSheet("color: #00f2ff;background-color: #454545;font-family: Areal;font-size: 20px;font-weight: bold;padding: 7px 35px;")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.formet_time(self.time))

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.formet_time(self.time))

    def formet_time(self,times):
        hours = times.hour()
        minut = times.minute()
        secoun = times.second()     #single slash for division
        millsec = times.msec()//10  #double slash used for integer division

        return f"{hours:02}:{minut:02}:{secoun:02}.{millsec:02}"

def main():
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
"""
#make an api weather app to fetch weather data from weather api server

# Api key:  ec15677f8c84d2cc544220593168cf9d
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# import requests
# import json
#
# Api_key = "ec15677f8c84d2cc544220593168cf9d"
#
# # city_name = input("Enter a city name: ").capitalize()
# city_name = "miami".capitalize()
#
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Api_key}"
# data_file = "city_weather_data_files/city_weather_data.json"
#
# for i in range(60):
#     responde = requests.get(url)
#
# data = responde.json()
#
# with open(data_file,"w") as city_file:
#     json.dump(data,city_file,indent=4)
#
# print(responde.status_code)
#
# city_name = data["name"]
# temp = data["main"]["temp"]
# city_weather_description = data["weather"][0]["description"]
#
# print(city_name)
# print(f"{temp-273.15:.2f}°C")
# print(city_weather_description)

########################################################################################################################
#load file and store list

# import json,csv
#
# name_list = ["sahil","pravin","nitish","golu","gaurav",]
# name_list_read = ["kumar","kumar","gupta","yadav","Mukhya","narayan"]
#
# file_path_json = "store_data_files/name_list.json"
#
# with open(file_path_json,"w") as json_file_read:
#     json.dump((name_list,name_list_read),json_file_read)
#
# with open(file_path_json,"r") as json_file_read:
#     reaspond = json.load(json_file_read)
#
# print(reaspond[1])
# print(name_list)
# print(name_list_read)

# store dictionary in the file and load it back
# import json,csv
#
# num_dict = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5"}
#
# generate_username_and_counter = {0: "hs0lue4la08o",1: "tn2vhw1hr46k",2: "lg2ram8ue41r",3: "nm1vad7ua55b"}
#
# userdata_with_key_username = {"hs0lue4la08o": {"first_name": "sahil", "last_name": "kumar", "date_of_birth": "20-10-2004", "mobile_number": "9801560832"},
#                               "tn2vhw1hr46k": {"first_name": "nitish", "last_name": "chaudhari", "date_of_birth": "02-03-2001", "mobile_number": "6545645654"},
#                               "lg2ram8ue41r": {"first_name": "golu", "last_name": "yadev", "date_of_birth": "12-05-2008", "mobile_number": "6542879135"},
#                               "nm1vad7ua55b": {"first_name": "monu", "last_name": "pasban", "date_of_birth": "21-08-2007", "mobile_number": "6854768546"} }
#
# file_path_json = "pokemon_data_file/name_list.json"
#
# with open(file_path_json,"w") as json_dict:
#     json.dump(False,json_dict)
#     # json.dump(num_dict,json_dict)
#
# # print(num_dict)
#
# with open(file_path_json,"r") as json_dict_read:
#     reasponse = json.load(json_dict_read)
#
# print(reasponse)
# print(type(reasponse))
#
# # print(userdata_with_key_username)
# #
# # print(True) if userdata_with_key_username == reasponse else print(False)

#make an api weather app to fetch weather data from weather api server
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import requests,json

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.placeholder_label = QLabel("Enter City Name:",self)
        self.line_edit = QLineEdit(self)
        self.search_button = QPushButton("Get Weather",self)
        self.temp_label = QLabel(self)   #type alt + 0176 = °
        self.emoji_label = QLabel(self)    #type win + . = emoji tab
        self.weather_desc = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cool Gui Weather App")
        self.setWindowIcon(QIcon("simple_file/moai-emoji.png"))

        vbox = QVBoxLayout()
        vbox.addWidget(self.placeholder_label)
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.search_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.weather_desc)

        self.setLayout(vbox)

        self.placeholder_label.setAlignment(Qt.AlignCenter)
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.weather_desc.setAlignment(Qt.AlignCenter)

        self.placeholder_label.setObjectName("placeholder_label")
        self.search_button.setObjectName("search_button")
        self.line_edit.setObjectName("line_edit")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.weather_desc.setObjectName("weather_desc")

        # self.setStyleSheet("""
"""
            # QLabel#placeholder_label{
            #     font-size: 50px;
            #     font-style: italic;
            # }
            # QLineEdit#line_edit{
            #     font-size: 40px;
            # }
            # QPushButton#search_button{
            #     font-size: 30px;
            #     font-weight: bold;
            # }
            # QLabel#temp_label{
            #     font-size: 75px;
            # }
            # QLabel#emoji_label{
            #     font-size: 100px;
            #     font-family: segoe UI emoji;
            # }
            # QLabel#weather_desc{
            #     font-size: 55px;
            # } """
          # """)
"""
        
        self.search_button.clicked.connect(self.get_weather)

    def get_weather(self):

        Api_key = "ec15677f8c84d2cc544220593168cf9d"  #please use your own

        city_name = self.line_edit.text()

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Api_key}"

        try:
            respond = requests.get(url)
            respond.raise_for_status()
            respond = respond.json()

            if respond["cod"] == 200:
                self.display_weather(respond)

        except requests.exceptions.HTTPError as http_error:
            match(respond.status_code):
                case 400:
                    self.display_errors("Bad requests\nPlease check your input")
                case 401:
                    self.display_errors("Unauthorized\nInvalid API key")
                case 403:
                    self.display_errors("Forbidden\nAccess is Denied")
                case 404:
                    self.display_errors("Not found\nCity not found")
                case 500:
                    self.display_errors("Internal Server Error\nPlease try again later")
                case 502:
                    self.display_errors("Bad Gateway\nInvalid response from the server")
                case 503:
                    self.display_errors("Service Unavailable\nServer is down")
                case 504:
                    self.display_errors("Gateway timeout\nno response from the server")
                case _:
                    self.display_errors(f"http error occurred: \n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_errors("Connection Error\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_errors("Timeout Error\nthe requests timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_errors("TooMany Redirects\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_errors(f"Request Error\n{req_error}")

    def display_weather(self,respond):
        temp = respond["main"]["temp"]
        emoji_id = respond["weather"][0]["id"]
        description = respond["weather"][0]["description"]
        temp_c = temp - 273.15

        self.temp_label.setStyleSheet("font-size: 75px")
        self.temp_label.setText(f"{temp_c:.2f}°C")
        self.emoji_label.setText(self.weather_emoji(emoji_id))
        self.weather_desc.setText(f"{description}")


    @staticmethod       #static method should not have self
    def weather_emoji(emoji_id):
        if 200 <= emoji_id <= 232:
            return "⛈️"
        elif 300 <= emoji_id <= 321:
            return "🌨️"
        elif 500 <= emoji_id <= 531:
            return "🌧️"
        elif 600 <= emoji_id <= 622:
            return "❄️"
        elif 701 <= emoji_id <= 781:
            return "🌫️"
        elif emoji_id == 800:
            return "☀️"
        elif 801 <= emoji_id <= 804:
            return "🌥️"

    def display_errors(self,error_message):
        self.temp_label.setStyleSheet("font-size: 40px")
        self.temp_label.setText(f"{error_message}")
        self.emoji_label.clear()
        self.weather_desc.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
"""
