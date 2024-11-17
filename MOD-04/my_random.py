# Importação da lib random
import random

# importação do meu modulo criando no outro arquivo 
import meu_modulo

# importação do meu modulo 2
import meu_modulo2

# Random criarar números aleátorios inteiros
random_int =  random.randint(1, 10)

# print do random
print(random_int)

# print da minha variável criado no outro arquivo, meu_modulo
print(meu_modulo.name)

# print da minha variável criada no outro arquivo, meu_modulo2
print(meu_modulo2.salmo)



# Random aleátorios de número de ponto flotoante

# Irá variar o número específico entre 0 e 10 pois ele não irá incluir o 10
# pois 0 multiplicado por 10 é 0
number_0_to_1 = random.random() * 10
print(number_0_to_1)
