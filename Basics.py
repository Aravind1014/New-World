# a=int(input("Enter the number: "))
# if a>0:
#     print("Positive")
# elif a<0:
#     print("Negative")
# elif a==0:
#     print("Zero")
# else:
#     print("null")

#######Implement a grading system that assigns letter grades based on numerical scores##

# x=int(input("Enter the Score: "))
# # if x>=90:
# #     print("A")
# # elif x>=80:
# #     print("B")
# # else:
# #     print("F")

####Design a program that determines if a year is a leap year or not.##

# a=int(input("Enter the year: "))
# if a%4==0 and a%100!=0 or a%400==0:
#     print("Its Leap Year")
# else:
#     print("Its not leap Year")

####Create a BMI calculator that provides weight status categories##
#
# height = float(input("Get Height: "))
# weight = float(input("Get Weight: "))
# BMI = weight/(height**2)
# if BMI<=18.5:
#     print(f"Ur BMI {BMI:.2f}: Underweight")
# elif BMI>18.5 and BMI<=24.5:
#     print("Normal")
# elif BMI>25.0 and BMI<39.9:
#     print("Overweight")
# else:
#     print("Obese")


#########Write a program that checks if a triangle is equilateral, isosceles, or scalene#
# x=int(input("X: "))
# y=int(input("Y: "))
# z=int(input("Z: "))
# if x==y==z:
#     print("Equilateral")
# elif x==y or y==z or z==x:
#     print("Isosceles")
# else:
#     print("scalene")

#####Create a simple calculator that performs different operations based on user input.
# a=int(input("value1: "))
# b=int(input("value2: "))
# c=str(input("Addition,subtraction,Multiplication,Division: "))
# if c=="Addition":
#     print("value of Addition: ",a+b)
# elif c=="subtraction":
#     print("Value of subtraction: ",a-b)
# elif c=="Multiplication":
#     print("Value of Multiplication: ",a*b)
# elif c=="Division":
#     if a==0:
#         print("Not Divisible")
#     else:
#         print("Value of Division: ",a/b)
# else:
#     print("Null")

##########Create a program that determines the largest of three numbers
# a=int(input("Enter the First number: "))
# b=int(input("Enter the Second number: "))
# c=int(input("Enter the Third number: "))
# if a>=b and a>=c:
#     print(f"Value {a=} is largest number")
# elif b>=a and b>=c:
#     print(f"Value {b=} is largest number ")
# elif c>=a and c>=b:
#     print(f"Value {c=} is largest number")
# else:
#     print ("null")

# #####Design a simple login system that checks username and password
# user1=input("Enter username: ")
# user2=input("Enter password: ")
# if user1=="password" and user2=="wer":
#     print("successfull login")
# else:
#     print("invalid username")

##Implement a tax calculator that applies different rates based on income brackets
# income=float(input("Enter the amount: "))
# if income>300000 and income<=700000:
#     a=income*5/100
#     b=income/12
#     print(f"tax slab: {a: .2f}")
#     print(f"monthly income: {b: .2f}")
# elif income>700000 and income<=1000000:
#     a =income*10/100
#     b = income/12
#     print(f"tax slab: {a: .2f}")
#     print(f"monthly income: {b: .2f}")
# elif income>1000000 and income<=1500000:
#     a=income*15/100
#     b = income/12
#     print(f"tax slab: {a: .2f}")
#     print(f"monthly income: {b: .2f}")
# elif income>1500000:
#     a =income*20/100
#     b = income/12
#     print(f"tax slab: {a: .2f}")
#     print(f"monthly income: {b: .2f}")
# else:
#     if income <= 300000:
#         b = income/12
#         print(f"monthly income: {b: .2f}")
#         print("Nil")

# ##Write a program that calculates shipping cost based on package weight and destination
# shipping_cost=int(input("Values of shippingcost in Rs: "))
# package_weight=int(input("value of packageweight in Kg: "))
# destination=int(input("value of destination in KM: "))
# cost=2
# weight=1
# distance=10
# formula=(cost)+(weight*package_weight)+(distance*destination)
# if package_weight<1 and destination<5:
#     print ("shipping free")
# else:
#     print ("shipping cost: ",formula)
# ####Implement a basic traffic light simulator that changes colors based on time.
# import time
# traffic_light=str(input("Enter the light color: "))
# if traffic_light=="red":
#     print("STOP")
#     time.sleep(65)
# elif traffic_light=="yellow":
#     print("Ready")
#     time.sleep(30)
# elif traffic_light=="Green":
#     print("Go")
#     time.sleep(45)
# else:
#     print("failure in signal")

###Write a program that determines if a number is prime or composite.
# a=int(input("Enter the number: "))
# # for i in range(2,a):
# #   if a%i==0:
# #       print("value is composite number")
# #       break
# # else:
##     print("value is prime number")

##Create a program that converts temperatures between Celsius and Fahrenheit based on user choice
# temp=float(input("Enter degree:"))
# formula_CF=5/9*(temp-32)
# if True:
#     print(f"The fahrenheit to celcius degree is:{temp: .2f},{formula_CF: .2f}")
# temp = float(input("Enter degree:"))
# formula_F=9/5*(temp+32)
# if True:
#     print(f"The celcius to fahrenheit degree is:{temp: .2f},{formula_F: .2f}")

##Design a simple quiz game that checks answers and keeps score.
# print("welcome to Quiz game!")
# a=input("do u wish to play the game: ")
# score=0
# if a=="yes":
#     print("how many color does rainbow have? ")
#     print("a.7 color\nb.2 color\nc.5 color")
#     x=input("enter the option: ")
#     if x=="a":
#         print("yes")
#         score += 1
#         print(f"{score}")
#     # elif x=="b":
#     #     print("no")
#     # elif x=="c":
#     #     print("no")
#     else:
#         print("wrong answer")
#         print(f"{score}")

# print("which planet human being can live: ?")
# print("a.Mars/nb.jupiter/nc.earth")
# score=0
# y=input("Enter the option: ")
# if y=="a":
#     print("no")
# elif y=="b":
#     print("no")
# elif y=="c":
#     print("yes")
#     score=+1
#     print(f"{score: }")
# else:
#     print("Invalid Entry")

###Implement a basic age verification system for a website.
# x=int(input("Enter age: "))
# if x>=18:
#     print("Adult")
# else:
#     print("child")

##Implement a simple rock-paper-scissors game.
# player1=input("Enter Rock,paper,scissors: ")
# player2=input("Enter Rock,paper,scissors: ")
# if player1==player2:
#     print("Tie")
# elif player1=="Rock" and player2=="scissors":
#     print("player1=win,player2=smashes")
# elif player1=="paper" and player2=="scissors":
#     print("player1=smashes,player2=win")
# elif player1=="Rock" and player2=="paper":
#     print("player1=smashes,player2=win")
# else:
#     print("out of game")

##Create a program that checks if a string is a palindrome.
# x=input("Enter String: ")
# rev=x[:: -1]
# if x==rev:
#     print (rev + " is palindrome")
# else:
#     print (rev + " is not palindrome")

##Write a program that determines the day of the week based on a given date.
# import datetime
# day=int(input("enter the day: "))
# month=int(input("enter the month: "))
# year=int(input("enter the year: "))
# date = datetime.date(year, month, day)
# x=date.strftime("%A")
# print(x,date)

##Design a simple ATM simulator with options for withdrawal, deposit, and balance check

# print("a.withdraw\nb.deposit\nc.balance_check")
# y=input("enter the option: ")
# balance=500
# if y=="a":
#     withdraw=float(input("enter the withdraw_amount: "))
#     if withdraw>balance:
#         print("insufficient balance")
#     if withdraw<balance:
#         balance=balance-withdraw
#         print(f"amount withdraw {balance}: ")
# if y=="b":
#     deposit=float(input("enter the deposit_amount: "))
#     balance=balance+deposit
#     print (f"amount deposit {balance}: ")
# if y=="c":
#     print (f"balance_check {balance} ")

# ##Create a program that simulates a vending machine, allowing item selection and handling payment
# print("1.pepsi\n2.waterbottle\n3.coke\n4.maaza")
# x = input("Enter the item (1-4): ")
# pepsi = 20
# waterbottle = 10
# coke = 25
# maaza = 15
# balance = 50
# if x== "1":
#     print(f"rate of pepsi {pepsi}")
#     y=(input("payment method card or cash: "))
#     if y=="card":
#         if balance>20:
#            balance -= 20
#            print(f"show the balance {balance}")
#     if y=="cash":
#         print("insert 20rs")
# elif x=="2":
#     print (f"rate of waterbottle {waterbottle}")
#     y=(input("payment method card or cash: "))
#     if y=="card":
#         if balance>10:
#             balance-=10
#             print(f"show the balance {balance}")
#     if y=="cash":
#             print("insert 50rs")
# elif x=="3":f
#     print (f"rate of coke {coke}")
# elif x=="4":
#     print(f"rate of maaza {maaza}")
# else:
#     print ("thank you")
##Calculate the average of elements in a list
# a=[1,3,9,6]
# sum=0
# count=0
# for i in a:
#     sum=sum+i
#     count=count+1
#     average=sum/count
# print(average)

##Find the largest element in a list.
# x=[10,25,45,100,85,200,90]
# largest=x[0]
# for i in x:
#     if i>largest:
#         largest=i
# print(f"largest element {largest} ")

##
# def add():
#     a=int(input("enter the value: "))
#     b=int(input("enter the value: "))
#     print(a+b)
#
# def sub():
#     a=int(input("enter the value: "))
#     b=int(input("enter the value: "))
#     print(a-b)
#
# def multiply():
#     a=int(input("enter the value: "))
#     b=int(input("enter the value: "))
#     print(a*b)
#
# def Div():
#     a=int(input("enter the value: "))
#     b=int(input("enter the value: "))
#     print(a/b)
# add()
# sub()
# multiply()
# Div()
#######
# def findevenorodd(y):
#     if y%2==0:
#         print("Even")
#     else:
#         print("Odd")
# x=int(input("enter the number: "))
# findevenorodd(x)

###
# def findpassorfail(x):
#     if x>35:
#         print("pass")
#     else:
#         print("fail")
# y=int(input("enter the score: "))
# findpassorfail(y)

####
# def printrange(R1,R2):
#     for i in range(R1,R2):
#         print(i)
# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# printrange(a,b)

####
# s_username="EMC"
# s_password="123"
# uname=str(input("enter the username: "))
# password=str(input("enter the password: "))
# def validate():
#     if (s_username==uname and s_password==password):
#         return True
#     else:
#         return False
# a=validate()
# print(a)

##
# def add():
#     print(a+b)
# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# c=int(input("enter the number: "))
#
# add=a+b
# print(add*c)





































