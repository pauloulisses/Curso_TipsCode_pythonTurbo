# Escreva um programa em python onde o cliente vai digitar um número
# qualquer e retorne se esse número digitado é PAR ou ÍMPAR


print('Descobrindo de o número digitado é par ou ímpar! ')

numero_digitado = int(input('Digite o número desejado: '))
if numero_digitado % 2 == 0:
    print('Numero digitado é par! ')

else:
    print('Número digitado é ímpar')    
