# Array Listas dos estados Brasileiros

brazilian_states = [
    "Acre", "Alagoas", "Amapá", "Aamazonas", "Bahia", "Ceará", "Distrito Federal", 
    "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", 
    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", 
    "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", 
    "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
]


# Função len me da a quantidade de elementos dentro desse array "lista"
print(len(brazilian_states))

# Irá da um erro: lista index está fora do intervalo
#print(brazilian_states[27])

# Resolvendo os casos do erro de lista index está fora do intervalo4

# cria uma variável e atribui a lista a ela com a função len = 'tamanho'
num_of_states = len (brazilian_states)
# printa a variável da lista entre colchetes coloca a variável que se atribui o tamnho da variável lista
print(brazilian_states[num_of_states -1])