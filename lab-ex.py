import random

from hamcrest import less_than

rock = r'''
 _______  _______  _______  _       
(  ____ )(  ___  )(  ____ \| \    /\
| (    )|| (   ) || (    \/|  \  / /
| (____)|| |   | || |      |  (_/ / 
|     __)| |   | || |      |   _ (  
| (\ (   | |   | || |      |  ( \ \ 
| ) \ \__| (___) || (____/\|  /  \ \
|/   \__/(_______)(_______/|_/    \/

'''
# print(rock)

papers = r'''
 _______  _______  _______  _______  _______  _______ 
(  ____ )(  ___  )(  ____ )(  ____ \(  ____ )(  ____ |
| (    )|| (   ) || (    )|| (    \/| (    )|| (    \/
| (____)|| (___) || (____)|| (__    | (____)|| (_____ 
|  _____)|  ___  ||  _____)|  __)   |     __)(_____  )
| (      | (   ) || (      | (      | (\ (         ) |
| )      | )   ( || )      | (____/\| ) \ \__/\____) |
|/       |/     \||/       (_______/|/   \__/\_______)

'''
#print(papers)

scissors = r'''
 _______  _______ _________ _______  _______  _______  _______  _______ 
(  ____ \(  ____ \ __   __/(  ____ \(  ____ \(  ___  )(  ____ )(  ____ \
| (    \/| (    \/   ) (   | (    \/| (    \/| (   ) || (    )|| (    \/
| (_____ | |         | |   | (_____ | (_____ | |   | || (____)|| (_____ 
(_____  )| |         | |   (_____  )(_____  )| |   | ||     __)(_____  )
      ) || |         | |         ) |      ) || |   | || (\ (         ) |
/\____) || (____/\___) (___/\____) |/\____) || (___) || ) \ \__/\____) |
\_______)(_______/\_______/\_______)\_______)(_______)|/   \__/\_______)

'''
#print(scissors)

# choice = [rock, papers, scissors]
# computer = ()

# input = int(input('what do you choose? Type "0" for Rock, "1" for Paper, "2" for Scissors. '))
# if input == 0:
#     print(f"you choose: {choice[0]}")
#     computer = print(f"computer choose: {random.choice(choice)}")
#     if computer == choice[2]:
#         print("You win")
#     elif computer == choice[1]:
#         print("you lose")
#     else:
#         print("try again")
# elif input == 1:
#     print(f"you choose: {choice[1]}")
#     computer = print(f"computer choose: {random.choice(choice)}")
#     if computer == choice[0]:
#         print("you win")
#     elif computer == choice[2]:
#         print("you lose")
#     else:
#         print("try again")
# elif input == 2:
#     print(f"you choose: {choice[2]}")
#     computer = print(f"computer choose: {random.choice(choice)}")
#     if computer == choice[1]:
#         print("you win")
#     elif computer == choice[0]:
#         print("you lose")
#     else:
#         print("try again")
# else:
#     print("please specify the right input")


# # print(random.choice(choice))
images = [rock, papers, scissors]

user_choice = int(input('what do you choose? Type "0" for Rock, "1" for Paper, "2" for Scissors. \n '))
if user_choice >=0 and user_choice <=2:
    print(images[user_choice])
computer_choice = random.randint(0, 2)
print(f"computer chose: ")
print(images[computer_choice])

if user_choice >=3 or user_choice <0:
    print("you typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice ==2:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice > user_choice:
    print("you lose!")
elif computer_choice == user_choice:
    print("its a draw!")


