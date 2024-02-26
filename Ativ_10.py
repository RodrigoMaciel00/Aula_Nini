import random

print('=' * 30)
print('Jogo: Pedra, Papel e Tesoura')
print('=' * 30)

opcoes = ['pedra', 'papel', 'tesoura']

escolha_usuario = input('Escolha: pedra, papel ou tesoura: ').lower()

escolha_computador = random.choice(opcoes)

print(f'O computador escolheu: {escolha_computador}')

if escolha_usuario == escolha_computador:
    print('Empate!')
elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
     (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
     (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
    print('Você venceu!')
else:
    print('Você perdeu!')
