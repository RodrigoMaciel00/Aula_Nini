print('=' * 30)
print('Sequência de Fibonacci')
print('=' * 30)

limite = int(input('Digite um valor limite para a sequência de Fibonacci: '))

s1 = 0
s2 = 1

print(s1, end=', ')
while s2 <= limite:
    print(s2, end=', ')
    s1, s2 = s2, s1 + s2

print('Fim')
