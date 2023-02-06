
eggs = 3
milk = 3
butter = 1

servings = int(input('Please enter the number of servings of eggs: '))
print(f'For {servings} servings of eggs, you will need: \n')

adjusted_eggs = eggs * servings
adjusted_milk = milk * servings
adjusted_butter = butter * servings

print(f"{adjusted_eggs:.2f}", 'eggs\n')
print(f"{adjusted_milk:.2f}", 'tablespoons of milk\n')
print(f"{adjusted_butter:.2f}", 'tablespoons of butter')