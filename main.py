#rock,paper,scissors game
import random

print("Welcome to Rock Paper Scissors!")

cpuScore = 0
playerScore = 0
tieScore = 0

choices = ['rock', 'paper', 'scissors']

def checkForWinner(players_pick, cpu_pick):
    if(players_pick == cpu_pick):
        print("It's a tie, play again!")
        return "TIE" 

    elif(players_pick == "rock" and cpu_pick == "paper"):
        print("You lost!")
        return "CPU"

    elif(players_pick == "rock" and cpu_pick == "scissors"):
        print("You won!")
        return "PLAYER"

    elif(players_pick == "paper" and cpu_pick == "rock"):
        print("You won!")
        return "PLAYER"

    elif(players_pick == "paper" and cpu_pick == "scissors"):
        print("You lost!")
        return "CPU"

    elif(players_pick == "scissors" and cpu_pick == "rock"):
        print("You lost!")
        return "CPU"

    elif(players_pick == "scissors" and cpu_pick == "paper"):
        print("You won!")
        return "PLAYER"
    
    
while (playerScore != 3 and cpuScore != 3):
    while True:
        players_pick = input('R/P/S?: ').lower()
        if(players_pick == "rock" or players_pick == "paper" or players_pick == "scissors"):
            break
        else:
            print('Error!')
    

    cpu_pick = random.choice(choices)
    print("player: ", players_pick)
    print("cpu: ", cpu_pick)
    result = checkForWinner(players_pick, cpu_pick)
    if (result == 'PLAYER'):
        playerScore += 1
    elif (result == 'CPU'):
        cpuScore += 1
    elif (result == "TIE"):
        tieScore += 1
    print("Your score: ", playerScore, "CPU score: ", cpuScore, "TIES: ",tieScore)
print("Game over...")
