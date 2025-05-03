# # Conditional Statements, Logical Operators, Code Blocks, and Scope,

# print("Welcome to the roller coaster")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("what is your age? "))
#     if age <= 7:
#         print("please pay 5$ ")
#     elif age <= 12:
#         print("please pay 12$ ")
#     elif age > 12:
#         print("please pay 20$ ")
# else:
#     print("Sorry you cannot ride, you need to grow up!")


# input_number = int(input("please enter a number:" ))

# if input_number % 2 == 0:
#     print("this is a EVEN number")
# else:
#     print("this is a ODD number")


# print("Welcome to online pizza delivery")
# size = input("What size pizza do you want? S, M or L: ")
# topings = input("Do you want panner on your pizza? Y or N: ")
# add_on = input("Do you want Extra cheese? Y or N: ")
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25
# extra_cheese = 1
# sbill = 0
# mbill = 0
# lbill = 0

# if size == small_pizza:
#     if topings == Y:
#         sbill = int(small_pizza + 2)
#     elif add_on == Y:
#         sbill = int(small_pizza + 2 + extra_cheese)
#     else:
#         print(f"Your final bill is: ${round(sbill, 2)}")
# if size == medium_pizza:
#     if topings == Y:
#         mbill = medium_pizza + 3
#     elif add_on == Y:
#         mbill = medium_pizza + 3 + extra_cheese
#     else:
#         print(f"Your final bill is: ${round(mbill, 2)}")
# if size == large_pizza:
#     if topings == Y:
#         lbill = large_pizza + 3
#     elif add_on == Y:
#         lbill = large_pizza + 3 + extra_cheese
#     else:
#         print(f"Your final bill is: ${round(lbill, 2)}")
# else:
#     print("Thank you for choosing us!")
    
# print("Welcome to online pizza delivery")
# size = input("What size pizza do you want? S, M or L: ")
# topings = input("Do you want panner on your pizza? Y or N: ")
# add_on = input("Do you want Extra cheese? Y or N: ")
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("please select from the available option")

#     if topings == "Y":
#         if size == "S":
#             bill += 2
#         else:
#             bill += 3
#     if add_on == "Y":
#         bill += 1

# print(f"your final bill is: ${bill}.")

print("Welcome to the roller coaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age <= 7:
        print("please pay 5$ ")
    elif age <= 12:
        print("please pay 12$ ")
    elif age > 12 and age < 45 or age > 55:
        print("please pay 20$ ")
    elif age >= 45 or age <= 55:
        print("no ticket for you, the admission is free!!!")
else:
    print("Sorry you cannot ride, you need to grow up!")
