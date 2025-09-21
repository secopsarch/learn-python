from random import choices


print('''
            ___,
       _.-'` __|__
     .'  ,-:` \;',`'-,
    /  .'-;_,;  ':-;_,'.
   /  /;   '/    ,  _`.-\.
  |  | '`. (`     /` ` \`|
  |  |:.  `\`-.   \_   / |
  |  |     (   `,  .`\ ;'|
   \  \     | .'     `-'/
    \  `.   ;/        .'
     '._ `'-._____.-'`
        `-.____|
          _____|_____
    abw  |___________|
''')
print("Welcome to the treasure Island")
print("Your mission is to find the treasure")
print("you're at a cross road. Where do you want to go?")
side = (input('\t Type "left" or "right" \n')).lower()

if side == "left":
    print("You've come to a lake.")
    action = (input('Type "wait" for the boat. Type "swim" to swim across\n')).lower()
    if action == "wait":
        print("There are three doors.")
        color = (input(" One red, one yellow and one blue. Which color do you choose?\n")).lower()
        if color == "blue":
            print("Game Over, you choose blue!!")
        elif color == "red":
            print("Game Over, you choose red!!")
        elif color == "yellow":
            print("You Win...you choose yellow")
        else:
            print("not a valid color")
    else:
        print("you die")
else:
    print("You have fall into the hole, Game Over!.")


        



    


