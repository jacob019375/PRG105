

creditScore = int(input('Enter your credit score: '))


if 300 <= creditScore <= 629:
    print(f'Your {creditScore} credit score is bad.')
elif 630 <= creditScore <= 689:
    print(f'Your {creditScore} credit score is fair.')
elif 690 <= creditScore <= 719:
    print(f'Your {creditScore} credit score is good.')
elif 720 <= creditScore <= 850:
    print(f'Your {creditScore} credit score is excellent.')
