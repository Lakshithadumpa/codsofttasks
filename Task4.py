#ROCK PAPER SCISSORS
import random
def computer():
    x = ['rock', 'paper', 'scissors']
    return random.choice(x)
def user():
    while True:
        print("If you want to stop the game, enter 'stop'.")
        usch = input("Enter your choice: ").strip().lower()
        comch = computer()                  
        if usch == "stop":
            print("Game Over!")
            break
        if usch not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        print(f"Computer choice: {comch}, Your choice: {usch}")
        if usch == comch:
            print("It's a Tie!")
        elif (usch == 'rock' and comch == 'scissors') or \
             (usch == 'scissors' and comch == 'paper') or \
             (usch == 'paper' and comch == 'rock'):
            print("You won!")
        else:
            print("You lost!")
user()
