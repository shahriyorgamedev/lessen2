from random import randint

print('Hello and wellcome to number guess game!!!\nTry to find the number I guess between 1 and 100')
Generated_number = randint(1,100)
attempts = 0

running = True
while running:
    attempts += 1
    user_input = int(input('Guess the number: '))
    if user_input > Generated_number:
        print("Your guess is bigger than the number number i guess")
    if user_input < Generated_number:
        print("Your guess is lower than the number i guess")
    if user_input == Generated_number:
        print(f"You Find it!!!\nYour attempts: {attempts}")
