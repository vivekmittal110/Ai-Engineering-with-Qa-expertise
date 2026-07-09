'''
1-snake
2-water
3-gun
'''
import random
def game(choice):
    choices = [1,2,3]
    c_choice = random.choice(choices)
    print(c_choice)    
    if choice == c_choice:
        print("draw")
    elif choice == 1:
        if c_choice == 2:
            print("you win, snake drinks the water")
        else:
            print("you loose, gun shoots snake")
    elif choice == 2:
        if c_choice == 1:
            print("you loose, snake drinks the water")
        else:
            print("you win, gun sinks in water")        
    else:
        if c_choice == 2:
            print("you loose, gun sinks in water")
        else:
            print("you win, gun shoots snake")

play = 1
while play == 1 :
    choice = int(input("Enter your choice (1 for snake, 2 for water, 3 for gun): "))
    game(choice)
    play = int(input("if want to play again press 1, for exit press 0 : "))
    



