import art
import game_data
import random

# Initialisation
play_game = True
score = 0
againstB = ""

# Function for play a game
def play(compare1, compare2):
    choose = ""
    win = ""

    difChoose = {
        "a": compare1['follower_count'],
        "b": compare2['follower_count']
    }
    
    # Print the Versu
    print(f"compare A: {compare1['name']}, a {compare1['description']}, from {compare1['country']}")
    print(art.vs)
    print(f"compare B: {compare2['name']}, a {compare2['description']}, from {compare2['country']}")
    
    while choose != "a" and choose != "b":
        choose = (input("Who has more followers? Type 'A' or 'B'  ")).lower()
    
    for inChoose in difChoose:
        if inChoose != choose:
            if difChoose[choose] >= difChoose[inChoose]:
                win = True
                againstB = compare1
            else:
                win = False
    
    return win
    
# Functioin for print a score 
def printScore(score):
    if score >= 1:
        print(f"You're right! Current score: {score}")

while play_game:
    print(art.logo)
    printScore(score)
    
    # Choose the random think while compare
    compare1 = random.choice(game_data.data)
    compare2 = random.choice(game_data.data)
    
    if againstB == "":
        result = play(compare1, compare2)
    else:
        result = play(againstB, compare2)
        
    if result:
        score = score + 1
        againstB = compare2
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        play_game = False