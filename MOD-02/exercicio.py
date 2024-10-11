"""
Neste exercício, o objetivo é escrever um programa
que some um número de dois dígitos.

Terá um input onde você vai extrair os dois números
do mesmo input
"""
# Solicita que o usuário insira um valor com dois dígitos.
entrada = input('Digite um valor com 2 digitos: ')
# Extrai o primeiro dígito da entrada como uma string e converte para inteiro.
num1 = int(entrada[0])
#Extrai o segundo dígito da entrada como uma string e converte para inteiro.
num2 = int(entrada[1])
# Exibe o valor de num1.
print(num1)
#Exibe o valor de num2.
print(num2)
#Soma os dois números extraídos.
newNumber = num1 + num2
#Exibe o resultado da soma.
print(newNumber)

