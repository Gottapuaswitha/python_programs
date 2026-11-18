##n=int(input("enter a number:"))
##if n==10:
##    print("equal")
##if n>=10:
##    print("greater")
##if n<=100:
##    print("possible")
##print("done")
##
##age=int(input("Enter a number:"))
##if age>=18:
##    print("Eligible For Voting")
##    
##
##a = 10
##if a>5:
##    print("A is greater than 5")
##    
##a = 20
##if a > 0:
##    print("positive number")
##
##age = 20
##if age>=18:
##    print("Eligible For Voting")
##a = 10
##b = 10
##if a == b:
##    print("Both are equal")
##num = 10
##if num %2 == 0:
##    print("Even Number")
##    
##marks = 100
##if marks>=35:
##    print("pass")
##    
##a=int(input("enter a number:"))
##if a % 2 == 0:
##    print("even number")
##
##a = 10
##b = 20
##if a<b:
##    print("A is smaller")
##
##
##age = int(input("enter your age:"))
##if age >= 60:
##    print("Senior-Citizen")
##    
##num = int(input("enter a number:"))
##if num < 100 :
##    print("Less than 100")
##
##product = int(input("Enter Your Price:"))
##if product > 5000:
##    print("Expensive Product")
##
##student = int(input("enter your percentage:"))
##if student >= 90:
##    print("Excellent performance")
##    
##salary = int(input("Enter your salary:"))
##if salary < 30000:
##    print("Low salary")
##
##num = int(input("enter number:"))
##if num % 5 == 0:
##    print("Divisible by 5")
##
##num = int(input("enter a number:"))
##if num > 10:
##    if num < 50:
##        print("Number is between 10 and 50")
##    
##age = int(input("enter your age:"))
##if age >= 18 and age <=25:
##marks = int(input("enter your marks:"))
##income = int(input("enter your income:"))
##if marks >= 90 or income < 200000:
##    print("Eligible for scholorship")
##
##num = int(input("enter a number:"))
##if num != 10:
##    print("Number is Not 10")
##
##num = int(input("enter a number:"))
##if num < 10 or num > 50:
##    print("valid number")
##
##age = int(input("enter your age:"))
##if age>=18 and age < 60:
##    print("Eligible for job")
##
##marks = int(input("enter your marks:"))
##if marks >= 95:
##    print("outstanding")
##if marks >= 50:
##    print("Good")
##
##num = int(input("enter number:"))
##if num < 100:
##    print("small")
##if num == 100:
##    print("exact")
##if num > 100:
##    print("big")
##
##num = int(input("enter number:"))
##if num %2 == 0:
##    print("even")
##if num > 10:
##    print("Greater than 10")
##
##marks = int(input("enter marks:"))
##if marks >= 90:
##    print("excellent")
##if marks >= 35:
##    print("pass")
##if marks < 35:
##    print("Fail")
##
##marks = int(input("enter marks:"))
##if marks >= 35:
##    print("check agin")
##if marks >= 90:
##    print("excellent")
##if marks <35:
##    print("fail")
##
##num = int(input("enter number:"))
##if num > 0:
##    if num > 100:
##        print("Big number")
##    else:
##        print("small")
##
##
##age = int(input("enter your age:"))
##if age>=18:
##    if age>=60:
##        print("senior-citizen")
##    else:
##        print("Adult")
##else:
##    print("minor")
##
##marks = int(input("enter your marks:"))
##if marks>=35:
##    print("pass")
##
##    if marks>=75:
##        print("First class")
##    else:
##        print("second class")
##else:
##    print("fail")
##
##age = int(input("enter your age:"))
##if age >= 18:
##    print("Eligible")
##    if age >= 21:
##        print("Can Apply For All Jobs")
##    else:
##        print("Limited Eligibility")
##else:
##    print("Not Eligible")
##
##bill = int(input("enter your bill:"))
##if bill <= 100:
##    print("Low usage")
##else:
##    print("high usage")
##    if bill >= 300:
##        print("very high usage")
##    else:
##        print("Moderate usage")
##    
##
##password =input("entyer your password:")
##if password == "pyhton123":
##    print("correct password")
##    if len(password)>=8:
##        print("strong password")
##    else:
##        print("Weak password")
##else:
##    print("wrong password")
##
##
##num = int(input("enter your number:"))
##if num >= 0:
##    print("positive")
##    if num % 2 == 0:
##        print("even")
##    else:
##        print("odd")
##else:
##    print("not positive")
##
##'''
##n=int(input("enter number:"))
##if n>10:
##    print("greater than 10")
##if n>20:
##    print("greater than 20")
##if n >= 50 and n <= 60:
##    print("half")
##'''
##'''
##password = input("Enter password: ")
##
##if password.isalpha():
##    print("valid")
##else:
##    print("not valid")
##
##'''
##'''
##s = input("Enter a value: ")
##
##if s.isalpha() or s.isdigit():
##    print("Valid")
##else:
##    print("Not Valid")
##'''
##'''
##password=input()
##if password.isalpha() and password.isnumeric():
##    print("valid")
##
##else:
##    print("invalid")
##'''
##value = input("Enter your input:")
##
##if all(char in string.punctuation for char in value):
##    print("Valid")
##else:
##    print("Invalid")
##
'''
s = input("Enter symbols:")

if s in ["@", "#", "$", "%", "*", "&", "!"]:
    print("valid")
else:
    print("invalid")


password=input()

if not(password.isalnum()):
    print("valid")
else:
    print("invalid")


num = int(input("enter number:"))
if num % 2 == 0:
    print("even")
else:
    ptint("odd")
'''
'''
l = ["pardhu", "john", "balayya", "sampu"]

name = input("Enter your name:")

if name not in l:
    print("Valid")
else:
    print("Invalid")
'''
'''
a = ["pardhu", "john", "balayya", "sampu"]
name = input("Enter your name:")
if name not in a:
    print("Valid")
    a.append(name)
    print(a)
    print("Success")
else:
    print("Invalid")
'''
'''
num=int(input("enter number:"))
if num%5 == 0:
    print("bus")
if num%3==0:
    print("fizz")
else:
    print("wrong")
'''
'''
num = int(input("Enter a number: "))
if num %5==0 and num%3==0:
    print("fizzbuzz")
elif num%5==0:
    print("buzz")
elif num%3==0:
    print("fizz")
else:
    print("wrong")
'''
#age?
#age 6-12 child
#age 13-18 teenage
#age 19-26 youth
#age greate than 27 uncle

age=int(input("Enter your age: "))
if age>=6 and age<=12:
    print("child")
elif age>=13 and age<=18:
    print("teenage")
elif age>=19 and age<=26:
    print("youth")
elif age > 27:
    print("uncle")
else:
    print("no category")
    
