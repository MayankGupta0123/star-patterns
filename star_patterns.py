# Right-angled Triangle
n = int(input('Enter n: '))

for i in range(1, n+1):
    print('*' * (i))

# Pyramid
n = int(input('Enter n: '))

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))

# Hollow Square
n = int(input('Enter n: '))

for i in range(1, n+1):
    if(i == 1 or i == n):
        print('*' * n)
    else:
        print('*' + ' ' * (n-2) + '*')
