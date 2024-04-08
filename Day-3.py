ascii_art = """          ,-.-,-,
         _/ / / /       /)
       ,'        `.   ,'')
     _/(@) `.      `./ ,')
    (____,`  \\:`-.   \\ ,')
     (_      /::::}  / `.)
      \\    ,' :,-' ,)\\ `.)
       `.        ,')  `..)
         \\-....-'\\      \\)"""
print(ascii_art)
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
a = input("You're at cross road. Where do you want to go? Type 'left' or 'right'")
if a == 'left':
    b = input(
        "You've come to a lake. There is an island in the middle of the lake.Type 'wait' to wait for a boat. Type "
        "'swim' to swim across.")
    if b == 'wait':
        c = input(
            "You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. "
            "Which colour do you choose?")
        if c == 'red':
            print("Game Over,You Lost")
        elif c == 'blue':
            print("Game Over,You Lost")
        elif c == 'yellow':
            print("You won!!")
    elif b == 'swim':
        print("Game Over,You Lost")
elif a == 'right':
    print("Game Over,You Lost")
