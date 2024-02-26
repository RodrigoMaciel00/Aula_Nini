from math import factorial

print('=' * 30)
print('Cálculo do Fatorial')
print('=' * 30)

n = int(input('Digite um número inteiro positivo para calcular o seu fatorial: '))

if n < 0:
    print('O número deve ser inteiro positivo.')
else:
    fatorial_de_n = factorial(n)
    print(f'O fatorial de {n} é: {fatorial_de_n}')
