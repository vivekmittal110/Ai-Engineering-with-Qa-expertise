'''
1-snake
2-water
3-gun
'''
import random
choice = int(input("Enter your choice (1 for snake, 2 for water, 3 for gun): "))

if choice == 1:
    print("you chose snake")
elif choice == 2:
    print("you chose water")
elif choice == 3:
    print("you chose gun")
else:
    print("Invalid choice")

choices = [1,2,3]
c_choice = random.choice(choices)

