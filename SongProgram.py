
for i in range(0, 3):
    bottles = 3
    print(f'{bottles - i} bottles of beer on the wall,')
    print(f'{bottles - i} bottles of beer')
    print(f'Take one down, pass it around')
    if bottles == 0:
        print(f'No more bottles of beer on the wall\n')
    else:
        print(f'{bottles - 1} of beer on the wall\n')