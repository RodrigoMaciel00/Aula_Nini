print('=' * 30)
print('Par ou Ímpar')
print('=' * 30)

num = int(input('Digite qualquer número e revelarei se é par ou ímpar: '))

if (num % 2) == 0:
    print(f'É par: {num}')
else:
    print(f'É ímpar: {num}')
