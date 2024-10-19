#IF e ELSE Aninhados

altura = int(input('Qual é a sua altura? '))

if altura >= 102:
    print('Vende o ingresso! ')
    idade = int(input('Qual é a sua idade? '))
    if idade >= 18:
        print('Igresso vai custar R$ 24 Reais')
    else:
        print('O ingresso vai custar R$ 12 Reais')

else:
    print('Lamento você não vai! ')    