print('=' * 30)
print('Média de números pares')
print('=' * 30)

numeros = []
soma_pares = 0
cont_pares = 0

qtd_numeros = int(input('Digite a quantidade de números na lista: '))

for i in range(qtd_numeros):
    numero = int(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        soma_pares += numero
        cont_pares += 1

if cont_pares == 0:
    print('Não há números pares na lista.')
else:
    media_pares = soma_pares / cont_pares
    print(f'A média dos números pares é: {media_pares}')
