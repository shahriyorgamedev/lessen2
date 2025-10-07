# Cafe menu
meals = ['Manti','Osh',"Shorva"]
prices_of_meals = [30,35,25]

drinks = ['Coke','Water','Tea']
prices_of_drinks = [15,5,10]

salads = ['Salad','Olivia','Vekter']
prices_of_salads = [20,30,35]

print(f'\n\n{'-' * 50}\n')



print(f'{" " * 10}Menu:')
print(f'{" " * 3}Meals:\n')
print(f'1) {meals[0]} -- {prices_of_meals[0]},000 sum')
print(f'2) {meals[1]} -- {prices_of_meals[1]},000 sum')
print(f'3) {meals[2]} -- {prices_of_meals[2]},000 sum\n')
print(f'{" " * 3}Drinks:\n')
print(f'1) {drinks[0]} -- {prices_of_drinks[0]},000 sum')
print(f'2) {drinks[1]} -- {prices_of_drinks[1]},000 sum')
print(f'3) {drinks[2]} -- {prices_of_drinks[2]},000 sum\n')
print(f'{" " * 3}Salads:\n')
print(f'1) {salads[0]} -- {prices_of_salads[0]},000 sum')
print(f'2) {salads[1]} -- {prices_of_salads[1]},000 sum')
print(f'3) {salads[2]} -- {prices_of_salads[2]},000 sum\n')


print(f'\n{'-' * 50}\n')

data = []


def choice():
    user_choice = int(input('Choose option 1-3:\n1 - to choose meals\n2 - to choose drinks\n3 - to choose salad\n'))
    return user_choice

def meal():
    meal_choice = int(input(f'Choose option 1-3 to choose meals:\n1 - {meals[0]} -- {prices_of_meals[0]},000 sum\n2 - {meals[1]} -- {prices_of_meals[1]},000 sum\n3 - {meals[2]} -- {prices_of_meals[2]},000 sum\n'))
    data.append(meal_choice)
    return meal_choice

def drink():
    drink_choice = int(input(f'Choose option 1-3 to choose drinks:\n1 - {drinks[0]} -- {prices_of_drinks[0]},000 sum\n2 - {drinks[1]} -- {prices_of_drinks[1]},000 sum\n3 - {drinks[2]} -- {prices_of_drinks[2]},000 sum\n'))
    data.append(drink_choice)
    return drink_choice

def salad():
    salad_choice = int(input(f'Choose option 1-3 to choose salad:\n1 - {salads[0]} -- {prices_of_salads[0]},000 sum\n2 - {salads[1]} -- {prices_of_salads[1]},000 sum\n3 - {salads[2]} -- {prices_of_salads[2]},000 sum\n'))
    data.append(salad_choice)
    return salad_choice


meal()
drink()
salad()


print(f'\n\n{'-' * 50}\n')


print(f"You ordered:\n{meals[data[0]]} -- {prices_of_meals[data[0]]}000 sum\n{drinks[data[1]]} -- {prices_of_drinks[data[1]]}000 sum\n{salads[data[2]]} -- {prices_of_salads[data[2]]}000 sum")
print(f"Overall price: {prices_of_meals[data[0]] + prices_of_drinks[data[1]] + prices_of_salads[data[2]]}000 sums")
  
print(f'\n\n{'-' * 50}\n')


# user_choice = int(input('Choose option 1-3:\n1 - to choose meals\n2 - to choose drinks\n3 - to choose salad\n'))
# if user_choice == 1:
#     meal_choice = int(input(f'Choose option 1-3 to choose meals:\n1 - {meals[0]} -- {prices_of_meals[0]},000 sum\n2 - {meals[1]} -- {prices_of_meals[1]},000 sum\n3 - {meals[2]} -- {prices_of_meals[2]},000 sum\n'))
#     if meal_choice == 1:
#         data.append(0)
#     if meal_choice == 2:
#         data.append(1)
#     if meal_choice == 3:
#         data.append(2)
#     if meal_choice not in (1,2,3):
#         print('Please choose valid option!')
# print(data)
# print(f'\n{'-' * 50}\n')
# running = True
# while running:
#     user_choice = int(input('Choose option 1-3:\n1 - to choose meals\n2 - to choose drinks\n3 - to choose salad\n'))
#     if user_choice == 1:
#         meal_choice = int(input(f'Choose option 1-3 to choose meals:\n1 - {meals[0]} -- {prices_of_meals[0]},000 sum\n2 - {meals[1]} -- {prices_of_meals[1]},000 sum\n3 - {meals[2]} -- {prices_of_meals[2]},000 sum\n'))
#         if meal_choice == 1:
#             data.append(0)
#         if meal_choice == 2:
#             data.append(1)
#         if meal_choice == 3:
#             data.append(2)
#         if meal_choice not in (1,2,3):
#             print('Please choose valid option!')
#     if user_choice == 2:
#         drink_choice = int(input(f'Choose option 1-3 to choose drinks:\n1 - {drinks[0]} -- {prices_of_drinks[0]},000 sum\n2 - {drinks[1]} -- {prices_of_drinks[1]},000 sum\n3 - {drinks[2]} -- {prices_of_drinks[2]},000 sum\n'))
#     if user_choice == 3:
#         salad_choice = int(input(f'Choose option 1-3 to choose salad:\n1 - {salads[0]} -- {prices_of_salads[0]},000 sum\n2 - {salads[1]} -- {prices_of_salads[1]},000 sum\n3 - {salads[2]} -- {prices_of_salads[2]},000 sum\n'))
#     else:
#         print('Please choose valid option!')

# print(data)

