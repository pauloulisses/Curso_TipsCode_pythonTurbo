# LISTAS

frutas = ['Maça', 'Mnaga', 'Banana', 'Pera']
print(frutas)


# Array Listas dos estados Brasileiros

brazilian_states = [
    "Acre", "Alagoas", "Amapá", "Aamazonas", "Bahia", "Ceará", "Distrito Federal", 
    "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", 
    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", 
    "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", 
    "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
]

# Acessandos todos os indices da variável
print(brazilian_states)

# corringindo o erro contido no indice Amazonas pois o mesmo teve um erro de digitação e esta 2 aa
brazilian_states[3] = 'Amazonas'
print(brazilian_states)

# Atribuindo um novo elemento a lista append adiciona ao ultimo indice da lista
brazilian_states.append('EXU')
print(brazilian_states)

# Atribuindo varios elementos a lista .extend lembrar dos colchetes [] para informar ao python que é uma lista
brazilian_states.extend(['BODOCÓ', 'OURICURI', 'SANTA CRUZ'])
print(brazilian_states)

# [0] acessa o indice da lista que será Acre por ser o primeiro índice zero
print(brazilian_states[0])

# [-1] acessa o indice da lista de trás para frente que será Tocantins
print(brazilian_states[-1])
