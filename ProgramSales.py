
count = 0
total = 0

for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
    sales = float(input(f'Enter the total amount of sales on {day}: '))
    total += sales
    count += 1

print(f'The total amount of sales was ${total} and the average amount of sales was ${(total / count):.2f}')