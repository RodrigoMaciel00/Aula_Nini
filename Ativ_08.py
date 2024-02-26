print('=' * 30)
print('Verificação de Número Primo')
print('=' * 30)

num = int(input("Digite um número para verificar se é primo: "))

if num <= 1:
    print("Não é primo")
else:
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print("É primo")
    else:
        print("Não é primo")
