# def game(new_score):
#     num = new_score
#     return num

# s = int(input("Enter your new score : "))
# num = game(s)

# with open("highscore.txt") as f:
#     score = f.read()
#     if int(score) < num:
#         print(f"old high score was {score}")
#         score = num
#         print(f"your score is {num}")
#         print(f"new high score is {score}")
#     else:
#         print(f"Your score is {num}")
#         print(f"current high score is {score}")
# with open("highscore.txt","w") as w:
#     w.write(str(score))

def game():
    score = int(input("Enter your new score :  "))
    with open("highscore.txt") as f:
        highscore = f.read()
        if highscore == "":
            highscore = 0
        if int(highscore) < score:
            print(f"old high score was {highscore}")
            highscore = score
            print(f"your score is {score}")
            print(f"new high score is {highscore}")
        else:
            print(f"Your score is {score}")
            print(f"current high score is {highscore}")
    with open("highscore.txt","w") as w:
        w.write(str(highscore))
game()