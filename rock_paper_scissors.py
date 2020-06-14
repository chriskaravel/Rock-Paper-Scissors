import random
import time

rock = 1
paper = 2 
scissors = 3

names={ rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules={rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

def scores():
    global player_score,computer_score
    print("High Scores")
    print("\nPlayer ", +player_score)
    print("\nComputer ", +computer_score)

def start():
    print("Let's play a game of  Rock, Paper, Scissors.")
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1,3)
    result(player, computer)
    return play_again()

def move():
    while True:
        player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Oops! I didn't understand that. Please enter 1, 2 or 3")

def result(player,computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(0.5)
    print("Computer threw {0}!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Its a tie")
    elif rules[player] == computer:
        print(rules[player])
        print(computer)
        print("Victory!")
        player_score += 1
    else:
        print("Defeat")
        print(rules[player])
        print(computer)
        computer_score += 1


def play_again():
    answer = input ("Would u like to play again? y/n: ")
    if answer.upper() in ("Y","YES"):
        return answer
    else:
        print("Thank you for playing.See you next time!")


if __name__ == '__main__':
    start()




