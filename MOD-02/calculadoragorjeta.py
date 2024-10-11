#calculadora de gorjeta
# como fazer a porcentagem
# 10 * 150 / 100  aqui está dizendo 10 % de 150 / 100
# outra forma de calcular 150 * 0.10 que sera de 10%


print('Seja bem-vindo(a) ao APP gorjeta')

conta = float(input('Informe o valor da conta R$: '))

porcentagem = int(input('Que porcentagem de gorjeta você gostaria de dar? R$10%, R$12%, OU R$15%? '))

pessoas = int(input('Quantas pessoas irá pagar? '))

contaComGorjeat = porcentagem / 100 * conta + conta

valor_total = contaComGorjeat / pessoas

print(valor_total)
