# treasure island project
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# 1 - prompt user left or right, left continues, right ends game
decision1 = input("Left or Right: ")
if decision1.lower() == "left":
    decision2 = input("Swim or Wait: ")
    if decision2.lower() == "wait":
        decision3 = input("Which door? Red, Blue, or Yellow: ")
        if decision3.lower() == "yellow":
            print("You Win!")
        elif decision3.lower() == "red":
            print("Burned by fire. Game over.")
        elif decision3.lower() == "blue":
            print("Eaten by beasts. Game over.")
        else: print("Game over.")
    else : print("Attacked by trout. Game over.")
else: print("Fall into a hole. Game over.")