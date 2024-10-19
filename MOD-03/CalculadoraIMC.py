print('Calculadora de IMC')

peso = float(input('Informe seu peso atual (kg): '))
altura = float(input('Informe sua altura (m): '))

imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Classificação: Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Classificação: Peso normal')
elif 25 <= imc < 30:
    print('Classificação: Sobrepeso')
else:
    print('Classificação: Obesidade')
    
