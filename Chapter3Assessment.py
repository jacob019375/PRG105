

userIdentity = int(input('Please enter what suits you: 1. student, 2. veteran, 3. show sponsor, 4. retiree, 5. general public. '))
tickets = int(input("How many tickets are you buying? "))

if userIdentity == 1:
    total = tickets * 5
    if 4 <= tickets <= 8:
        FinalTotal = total - (total * .10)
    elif 9 <= tickets <= 15:
        FinalTotal = total - (total * .15)
    elif tickets > 15:
        FinalToTal = total - (total * .20)

if userIdentity == 2:
    total = tickets * 7
    if 4 <= tickets <= 8:
        FinalTotal = total - (total * .10)
    elif 9 <= tickets <= 15:
        FinalTotal = total - (total * .15)
    elif tickets > 15:
        FinalTotal = total - (total * .20)

if userIdentity == 3:
    total = tickets * 7
    if 4 <= tickets <= 8:
        FinalTotal = total - (total * .10)
    elif 9 <= tickets <= 15:
        FinalTotal = total - (total * .15)
    elif tickets > 15:
        FinalTotal = total - (total * .20)

if userIdentity == 4:
    total = tickets * 6
    if 4 <= tickets <= 8:
        FinalTotal = total - (total * .10)
    elif 9 <= tickets <= 15:
        FinalTotal = total - (total * .15)
    elif tickets > 15:
        FinalTotal = total - (total * .20)

if userIdentity == 5:
    total = tickets * 10
    if 4 <= tickets <= 8:
        FinalTotal = total - (total * .10)
    elif 9 <= tickets <= 15:
        FinalTotal = total - (total * .15)
    elif tickets > 15:
        FinalTotal = total - (total * .20)


print(f'The final total is ${FinalTotal} after discounts')
