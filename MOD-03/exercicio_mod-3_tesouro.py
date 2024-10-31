# Mensagem de Boas Vindas
print('Bem-vindo à ilha do Tesouro. \nSua missão é encontrar o tesouro.')


# Solicitando ao usuário que escolha o lado a seguir 
lado = input('Digite qual lado você quer seguir: Direita [D] ou Esquerda [E]: ')

# Solicitando ao usuário que escolha se quer nadar ou andar
nadar_andar = input('Digite se você quer Nadar [N] ou Andar [A]: ')

# Solicitando ao usuário qual porta ele deve abrir
porta = input('Digite qual porta você quer abrir: Vermelha [V], Azul [A] ou Amarela [Am]: ')

# Verificando o lado escolhido
if lado == 'D' or lado == 'd':
    print('Game Over')
elif lado == 'E' or lado == 'e':
    print('Siga em frente')
else:
    print('Lado escolhido inválido')

# Escolha se você quer Nadar ou Andar
if nadar_andar == 'N' or nadar_andar == 'n':
    print('Game Over')
elif nadar_andar == 'A' or nadar_andar == 'a':
    print('Continue andando no jogo')
else:
    print('Opção inválida! Você não escolheu nem Andar nem Nadar.')

# Escolhendo a cor da porta
if porta == 'V' or porta == 'v':  # Alterado para 'V'
    print('Game Over')
elif porta == 'A' or porta == 'a':  # Alterado para 'A'
    print('Game Over')
elif porta == 'Am' or porta == 'am':  # Alterado para 'Am'
    print('Vitória!')
else:
    print('Porta inválida!')
