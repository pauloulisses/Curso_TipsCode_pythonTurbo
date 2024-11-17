import random

# aqui está dizendo se deu 0 é cara
# se deu 1 é coroa
cara_ou_coroa = random.randint(0, 1)

if cara_ou_coroa == 0:
    print('Cara')
else:
    print('Coroa')