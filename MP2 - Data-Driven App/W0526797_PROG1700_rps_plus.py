import random
import math

# ANSI color codes for move text coloring
RED = '\033[0;31m'
BLUE = '\033[0;34m'
WHITE = '\033[0m'
GREEN = '\033[92m'
YELLOW = '\033[1;33m'

color_map = {
    "rock": f"{BLUE}rock{WHITE}",
    "paper": f"{GREEN}paper{WHITE}",
    "scissors": f"{RED}scissors{WHITE}"
}

valid_moves = ["rock", "paper", "scissors"]
valid_set = {"rock", "paper", "scissors"}
score = {"player": 0, "cpu": 0, "ties": 0}
history = []

get_player_move = (valid_set)
get_cpu_move = (valid_moves)
print_scoreboard = (score)
print_history = (history)

wins_over = {("rock","scissors"), ("scissors","paper"), ("paper","rock")}

# Function
def coloredprint(message, color=WHITE):
    print(f"{color}{message}{WHITE}")

def get_player_move(valid_moves):
    prompt = f"Enter your move ({color_map['rock']}, {color_map['paper']}, {color_map['scissors']}): "
    move = input(prompt).strip().lower()
    while move not in valid_moves:
        print("Invalid move. Try again.")
        move = input(prompt).strip().lower()
    return move

def get_cpu_move(valid_moves):
    return random.choice(valid_moves)

def print_scoreboard(score):
    print(f"Scoreboard - Player: {score['player']}, CPU: {score['cpu']}, Ties: {score['ties']}")

def print_history(history):
    print("Game History:")
    for round_num, (player_move, cpu_move, result) in enumerate(history, start=1):
        print(f"Round {round_num}: Player = {player_move}, CPU = {cpu_move} - Result: {result}")


best_of = input("Enter the number of rounds to play (best of 3, 5, 7): ")
if int(best_of) % 2 == 0:
    print("Invalid input. Please enter odd numbers only.")
else:
    pass

while True:
    player_move = get_player_move(valid_set)
    cpu_move = get_cpu_move(valid_moves)
    

    if player_move == cpu_move:
        result = "tie"
        score["ties"] += 1
    elif (player_move, cpu_move) in wins_over:
        result = "player"
        score["player"] += 1
    else:
        result = "cpu"
        score["cpu"] += 1
    
    history.append((player_move, cpu_move, result))
    
    print(f"You chose {player_move}, CPU chose {cpu_move}. Result: {result}")
    print_scoreboard(score)

    if score["player"] > math.ceil(int(best_of)//2):
        print("You win the game!")
        break

    elif score["cpu"] > math.ceil(int(best_of)//2):
        print("CPU wins the game!")
        break

print_history(history)