print('=' * 30)
print('Contador de números pares')
print('=' * 30)

num = int(input('Digite um valor: '))

x = 0

while x <= num:
    if x % 2 == 0:
        print('->', end='')
        print(x, end=' ')
    x = x + 1
