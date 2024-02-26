print('=' * 30)
print('Números pares na lista')
print('=' * 30)

listanum = []
Maior = 0
Menor = 0

for c in range(0, 5):
    listanum.append(int(input(f'digite um valor na lista {c}: ')))
    if c == 0:
        Maior = listanum[c]
        Menor = listanum[c]
    else:
        if listanum[c] > Maior:
            Maior = listanum[c]
        if listanum[c] < Menor:
            Menor = listanum[c]

print(f'Vc digitou os valores {listanum}')
print(f'Esse é o maior valor: {Maior}')
print(f'E esse é o menor: {Menor}')
