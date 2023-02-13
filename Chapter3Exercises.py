# 1. Day of the Week.
userNumber = int(input('Enter a number between 1 through 7: '))

if userNumber == 1:
    print("The day is Monday")
if userNumber == 2:
    print('The day is Tuesday')
if userNumber == 3:
    print('The day is Wednesday')
if userNumber == 4:
    print('The day is Thursday')
if userNumber == 5:
    print('The day is Friday')
if userNumber == 6:
    print('The day is Saturday')
if userNumber == 7:
    print('The day is Sunday')
else:
    print('That number is outside 1-7. ')

# 2. Areas of Rectangles.

firstLength = int(input('Enter the first rectangles length: '))
firstWidth = int(input('Enter the first rectangles width: '))
secondLength = int(input('Enter the second rectangles length: '))
secondWidth = int(input('Enter the second rectangles width: '))

area1 = firstWidth * firstLength
area2 = secondLength * secondWidth

if area1 > area2:
    print('The first rectangle had a greater area than the second.\n')
    print('Rectangle #1: ', area1, '\n')
    print('Rectangle #2: ', area2, '\n')
if area1 < area2:
    print('The second rectangle had a greater area than the first.\n')
    print('Rectangle #1: ', area1, '\n')
    print('Rectangle #2: ', area2, '\n')
if area1 == area2:
    print('The rectangles had an equal area. \n')
    print('Rectangle #1: ', area1, '\n')
    print('Rectangle #2: ', area2, '\n')


#3. Age Classifier.


age = int(input('Enter your age: '))

if age < 1:
    print('You are an infant. ')
if age >= 1 and age <= 13:
    print('You are a child. ')
if age >= 13 and age <= 20:
    print('You are a teenager. ')
if age >= 20:
    print('You are an adult. ')

#4. Roman Numerals

number = int(input('Enter a number:'))

if number == 1:
    print('The Roman Numeral for', number, ' is I')
if number == 2:
    print('The Roman Numeral for', number, ' is II')
if number == 3:
    print('The Roman Numeral for', number, ' is III')
if number == 4:
    print('The Roman Numeral for', number, ' is IV')
if number == 5:
    print('The Roman Numeral for', number, ' is V')
if number == 6:
    print('The Roman Numeral for', number, ' is VI')
if number == 7:
    print('The Roman Numeral for', number, ' is VII')
if number == 8:
    print('The Roman Numeral for', number, ' is VIII')
if number == 9:
    print('The Roman Numeral for', number, ' is IX')
if number == 10:
    print('The Roman Numeral for', number, ' is X')
if number < 1 and number > 10:
    print('That number is outside 1-10. ')

#5. Mass and Weight.

mass = float(input('Enter the objects mass in kg: '))

weight = mass * 9.8

print(f'The weight of the object is {weight:.2f}')

if weight > 500:
    print('The object is too heavy')
if weight < 100:
    print('The object is too light')

#6. Magic Date

year = int(input('Enter a two digit year: '))
day = int(input('Enter a day in numerical form: '))
month = int(input('Enter a month in numerical form: '))

if month * day == year:
    print(month, '/', day, '/', year, ' is a magic date.')
if month * day != year:
    print(month, '/', day, '/', year, ' is not a magic date.')


#7. Color Mixer.


color1 = input('Enter a color: ')
color2 = input('Enter another color: ')

if color1 == 'yellow' and color2 == 'red':
    print('Red and yellow create orange')
if color1 == 'red' and color2 == 'yellow':
    print('Red and yellow create orange')
if color1 == 'yellow' and color2 == 'blue':
    print('Blue and yellow create green')
if color1 == 'blue' and color2 == 'yellow':
    print('Blue and yellow create green')
if color1 == 'blue' and color2 == 'red':
    print('Red and blue create purple')
if color1 == 'red' and color2 == 'blue':
    print('Red and blue create purple')
else:
    print('That is not a primary color')

#8. Hot Dog Cookout Calculator

population = int(input('Enter how many people will attend the cookout: '))
hotdogsPerPerson = int(input('Enter how many hotdogs each person will eat: '))
hotdogsEaten = hotdogsPerPerson * population

totalPackages = hotdogsEaten / 10
totalBuns = hotdogsEaten / 8
print(hotdogsEaten % 8)
print('The minimum amount of hot dog packages needed will be: ', totalPackages)
print('The minimum amount of hot dog buns needed will be: ', totalBuns)
print('The number of hotdogs left over will be:', hotdogsEaten % 8)
print('The number of hotdog buns left over will be:', hotdogsEaten % 10)


#9. Roullette Wheel Colors


pocketNumber = int(input('Enter a pocket number: '))

if pocketNumber == 0:
    print('The pocket color is green.')
elif pocketNumber > 36 or pocketNumber < 0:
    print('This number is outside the 0-36 value range.')

if pocketNumber >= 1 and pocketNumber <= 10:
    if pocketNumber % 2 == 0:
        print('The pocket color is black')
    elif pocketNumber % 2 != 0:
        print('The pocket color is red')

if pocketNumber >= 11 and pocketNumber <= 18:
    if pocketNumber % 2 == 0:
        print('The pocket color is red')
    elif pocketNumber % 2 != 0:
        print('The pocket color is black')

if pocketNumber >= 19 and pocketNumber <= 28:
    if pocketNumber % 2 == 0:
        print('The pocket color is black')
    elif pocketNumber % 2 != 0:
        print('The pocket color is red')

if pocketNumber >= 29 and pocketNumber <= 36:
    if pocketNumber % 2 == 0:
        print('The pocket color is red')
    elif pocketNumber % 2 != 0:
        print('The pocket color is black')


#10. Money Counting Game

pennies = 1
nickels = 5
dimes = 10
quarters = 25

userPennies = int(input('Enter the amount of pennies: '))
userNickels = int(input('Enter the amount of Nickels: '))
userDimes = int(input('Enter the amount of dimes: '))
userQuarters = int(input('Enter the amount of quarters: '))
total = (userPennies * pennies) + (userQuarters * quarters) + (userDimes * dimes) + (userNickels * nickels)

if total == 100:
    print('Congrats! the amount you entered is equal to one dollar')
elif total > 100:
    print('The amount you entered was more than one dollar')
elif total < 100:
    print('The amount you entered was less than one dollar')


#11. Book Club Points

booksPurchased = int(input('Enter the amount of books purchased this month: '))

if booksPurchased == 0:
    print('You earned 0 points this month')
elif booksPurchased == 2:
    print('You earned 5 points this month')
elif booksPurchased == 4:
    print('You earned 15 points this month')
elif booksPurchased == 6:
    print('You earned 30 points this month')
elif booksPurchased >= 8:
    print('You earned 60 points this month')

#12. Software Sales

softwarePurchased = int(input('Enter the number of pakckages purchased: '))

if softwarePurchased >= 10 and softwarePurchased <= 19:
    print('You have a 10% discount, your total is: $', (softwarePurchased -(softwarePurchased * .10)))
elif softwarePurchased >= 20 and softwarePurchased <= 49:
    print('You have a 20% discount, your total is: $', (softwarePurchased -(softwarePurchased * .20)))
elif softwarePurchased >= 50 and softwarePurchased <= 99:
    print('You have a 30% discount, your total is: $', (softwarePurchased -(softwarePurchased * .30)))
elif softwarePurchased >= 100:
    print('You have a 40% discount, your total is: $', (softwarePurchased -(softwarePurchased * .40)))


#13. Shipping Charges

packageWeight = float(input('Enter the weight of the package in pounds: '))

if packageWeight <= 2:
    print('Your total shipping charges are: $', (packageWeight * 1.50))
elif packageWeight > 2 and packageWeight <= 6:
    print('Your total shipping charges are: $', (packageWeight * 3))
elif packageWeight > 6 and packageWeight <= 10:
    print('Your total shipping charges are: $', (packageWeight * 4))
elif packageWeight > 10:
    print('Your total shipping charges are: $', (packageWeight * 4.75))


#14. Body Mass Index
weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

BMI = weight * (703 / (height * height))
print(f'Your BMI is: {BMI:.2f}')

if BMI < 18.5:
    print('You are underweight')
elif BMI > 25:
    print('You are overweight')


#15. Time Calculator

userNumber = int(input('Enter a number of seconds: '))

if userNumber >= 60:
    minutes = userNumber / 60
elif userNumber >= 3600:
    hours = userNumber / 3600
    minutes = hours / 60
    seconds = minutes * 60
elif userNumber >= 86400:
    days = userNumber / 86400
    hours = days / 24
    minutes = hours / 60
    seconds = minutes * 60

#16. February Days

year = int(input('Enter the year: '))

if year % 100 == 0 and year % 400 == 0:
    print(f'In {year} February has 29 days')
if year % 100 != 0 and year % 4 == 0:
    print(f'In {year} February has 29 days')
else:
    print(f'In {year} February has 28 days')

#17. WiFi diagnostic tree

answer = input('Is there something wrong with your wifi? ')

if answer == 'yes':
    print('Reboot the computer and try to connect.')
    answer = input('Did that fix the problem?')
    if answer == 'yes':
        pass
    elif answer == 'no':
        print('Reboot the router and try to connect.')
        answer = input('Did that fix the problem?')
        if answer == 'yes':
            pass
        elif answer == 'no':
            print('Make sure the cables between the router and modem are plugged in firmly.')
            answer = input('Did that fix the problem?')
            if answer == 'yes':
                pass
            elif answer == 'no':
                print('Move the router to a new location and try again.')
                answer = input('Did that fix the problem?')
                if answer == 'yes':
                    pass
                elif answer == 'no':
                    print('Get a new router.')
                    pass





































































































