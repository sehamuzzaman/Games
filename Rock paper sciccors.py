import random
options= ("rock","paper","scissors")
running= True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player= input("Enter a choice(rock,paper,scissors): ")
    print(f"Player: {player}")
    print(f"computer: {computer}")

    if player==computer:
        print("It's a Tie!!")
    elif player=="rock" and computer=="scissors":
        print("YOU WIN!")
    elif player=="paper" and computer=="rock":
        print("YOU WIN!")
    elif player == "scissor" and computer == "paper":
        print("YOU WIN!")
    else:
        print("You Lose!")
    if not input("Play again (y/n): ").lower()=="y":
       running=False
print("Thanks for playing!")
