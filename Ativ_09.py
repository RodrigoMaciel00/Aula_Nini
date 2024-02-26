print('=' * 30)
print('Filtragem de Nomes')
print('=' * 30)

lista_nomes = ['Andy', 'Matheus', 'Lucas', 'Ayesha', 'Gabriel']

lista_valida = []

for nome in lista_nomes:
    if nome.startswith('A'):
        lista_valida.append(nome)

print("Nomes que começam com 'A':", lista_valida)
