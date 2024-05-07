from tkinter import YES


name = input("Enter your name: ")
sport = input(" What sport do you wish to participate in: ")
age = int(input("Enter you age: "))
if age >= 12:
    print("You are eligible for soccer")
elif age >= 10:
    print("You are eligibe for basketball, swimming, and track.")
else:
    print("You are eligible for track.")
equipment = input("Do you have proper equipment for your chosen sport ")
if equipment == YES:
    print("Go to practice, you have all the equiment you need, you got this!")
else:
    print("You need equipment to participate in this sport, have a nice day.")