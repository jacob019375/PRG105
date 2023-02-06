
income = int(input('Enter the amount you make per month: '))
housing = int(input('Enter the monthly expense on housing: '))
food = float(input('Enter the monthly expense on food: '))
transportation = float(input('Enter the monthly expense on transportation: '))
phone = float(input('Enter the monthly expense on phone: '))
utilities = float(input('Enter the monthly expense on utilities: '))
clothing = float(input('Enter the monthly expense on clothing: '))

housing_percentage = housing / income
food_percentage = food / income
transportation_percentage = transportation / income
phone_percentage = phone / income
utilities_percentage = utilities / income
clothing_percentage = clothing / income

total_expenses = housing + food + clothing + utilities + phone + transportation

print(f'You spent {housing_percentage:.2%} of your income on housing')
print(f'You spent {food_percentage:.2%} of your income on food')
print(f'You spent {transportation_percentage:.2%} of your income on transportation')
print(f'You spent {phone_percentage:.2%} of your income on phone')
print(f'You spent {utilities_percentage:.2%} of your income on utilities')
print(f'You spent {clothing_percentage:.2%} of your income on clothing')

final_balance = income - total_expenses
print(f'You have ${final_balance:.2f} left after monthly expenses. ')