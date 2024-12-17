
'''

total = 0

1.Inicializa uma variável chamada total com o valor 0.
Essa variável será usada para armazenar a soma acumulada dos números durante o loop.

2. for number in range(1, 101):

range(1, 101) gera uma sequência de números de 1 a 100 (o limite superior 101 não é incluído).

3. O loop for percorre essa sequência número por número.
A cada iteração, a variável number assume o valor do número atual da sequência.


4.total += number
Isso é o mesmo que total = total + number.
O valor atual de number é somado ao valor existente em total e o resultado é armazenado novamente em total.
print(total)

Depois que o loop termina (após somar todos os números de 1 a 100), o valor total da soma é exibido no console.

'''
total = 0
for number in range (1, 101):
    total += number
print(total)