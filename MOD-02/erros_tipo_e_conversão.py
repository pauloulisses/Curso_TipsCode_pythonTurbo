#print(len(123)) aqui irá da erro pois a função len ler strigs e não int, float e douba


num_char = len(input('Qual seu nome? '))

# conversão dinámica
new_num_char = str(num_char)

print('Seu nome tem ' + new_num_char + 'caracteres ')


# TIPO INT
numeber = 123
print(type(numeber))



# TIPO STR
number2 =  str(321)
print(type(number2))


# TIPO FLOAT

number3 = float(456)
print(type(number3))


# SOMA 
# irá somar 70 + 100.5 = 170.5 número float
print(70 + float('100.5'))