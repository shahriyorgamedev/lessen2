from random import choice

print('Hello and wellcome to Rock Paper Scissor Game!!!\nTry to find the correct answer "Rock, Paper or Scissors"')
choices = ("Rock","Paper","Scissors")


running = True
while running:
    AI_input = choice(choices)
    user_input = input('Choose option (Rock, Paper or Scissors): ')
    if user_input == 'Rock' and AI_input == "Paper":
        print("AI won! you choose Rock AI choose Paper")
    if user_input == 'Paper' and AI_input == "Scissors":
        print("AI won! you choose Paper AI choose Scissors")
    if user_input == 'Scissors' and AI_input == "Rock":
        print("AI won! you choose Scissors AI choose Rock")
    if AI_input == 'Rock' and user_input == "Paper":
        print("You won! AI choose Rock you choose Paper")
    if AI_input == 'Paper' and user_input == "Scissors":
        print("You won! AI choose Paper you choose Scissors")
    if AI_input == 'Scissors' and user_input == "Rock":
        print("You won! AI choose Scissors you choose Rock")
    if AI_input == user_input:
        print("Try again your choice are same")
    if user_input not in choices:
        print("Choose from these (Rock, Paper or Scissors) Do'nt write another words")