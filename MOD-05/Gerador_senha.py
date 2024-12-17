# import random
#
# # Listas
# letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
#            'm','n','o','p','q','r','s','t','u','v','x','y','z']
#
# numbers = ['0','1','2','3','4','5','6','7','8','9']
#
# symbols = ['!','#','$','%','&','(', ')','*','+']
#
# # Entradas do usuário
# nr_letters = int(input('Quantas letras você deseja em sua senha?: \n'))
# nr_symbols = int(input('Quantos símbolos você deseja?: \n'))
# nr_numbers = int(input('Quantos números você deseja?: \n'))
#
# # Fácil: senha sem mistura
# password = ''
#
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#     print(password)


# dificil

import random

# Listas
letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
           'm','n','o','p','q','r','s','t','u','v','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(', ')','*','+']

# Entradas do usuário
nr_letters = int(input('Quantas letras você deseja em sua senha?: \n'))
nr_symbols = int(input('Quantos símbolos você deseja?: \n'))
nr_numbers = int(input('Quantos números você deseja?: \n'))

# Lista para armazenar os caracteres da senha
password_list = []
# Adiciona letras aleatórias
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Adiciona símbolos aleatórios
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Adiciona números aleatórios
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Embaralha os caracteres da lista
random.shuffle(password_list)

# Junta a lista em uma string
password = ''.join(password_list)

# Exibe a senha gerada
print(f'Sua nova senha é: {password}')
