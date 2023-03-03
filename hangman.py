import random
import json

# Connection to the Json File
with open("/Users/samue/Documents/hangman/hangman_game/data.json", "r") as f:
    data = json.load(f)

# Select a random word from the "words" dictionary in the json file
word_ran = data["words"][random.randrange(0,726)]

# Variables used for the game logic
key = list(word_ran.lower())
wrongAnswers = 0
rightAnswers = len(key)

# Takes the answer key and turns it into blanks to start the game
legend = []
for x in key:
    legend.append("_")

print(legend)
print(key)

# Game logic - takes letter input from user and compares it to the answer key. If the letter is in the answer key it will replace the dash in the legend at the same index, and increment the rightAnswers down by 1. If it is not in the key it will increase the wrongAnswers variable by 1. After each check, whether right or wrong, it will propt the user to put in another letter. If the rightAnswers variable reaches zero, print out the statement "You Win!". If the wrongAnswers variable reaches 6, print out "You lose."
while wrongAnswers < 6 and rightAnswers != 0:
    playerInput = input("Please enter a letter and press enter. ")
    playerInput.lower()
    if playerInput in key:
        for i, string in enumerate(key):
            if string == playerInput:
                legend[i] = key[i]
                print(legend)
                rightAnswers -= 1
            else:
                pass
    else:
        wrongAnswers += 1
        print("That letter is not in the word")
        print(legend)

# When the while loop breaks one of these resolution messages with print to tell the user if they won or lost. 
if wrongAnswers == 6:
    print("You lose.")
elif rightAnswers == 0:
    print("You Win!")
else:
    pass