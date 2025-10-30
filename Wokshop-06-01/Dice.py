import random
player1_score = 0
player2_score = 0

while player1_score < 3 and player2_score < 3:
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    print(f"Player1:{roll1} | Player2:{roll2}")
    if roll1 > roll2:
        player1_score += 1
    elif roll2 > roll1:
        player2_score += 1
print("Winner:", "Player 1" if player1_score > player2_score else "Player 2")