print('Bem vindo à Pizzaria Ulisses')
# Solicitando ao usuário o tamanho da pizza
tamanho_pizza = input('Digite o tamanho da sua pizza: pequena (p), média (m), grande (g): ')
# Solicita ao usuário se deseja adicionar pepperoni
pepperoni = input('Adicionar pepperoni a pizza: sim (s) ou não (n): ')
# Solicita ao usuário se deseja adicionar queijo extra
queijo_extra = input('Adicionar queijo extra: sim (s) ou não (n): ')

# Inicializa o preço da pizza com base no tamanho escolhido
if tamanho_pizza == 'p':
    preco_pizza = 15.00
    print('Pizza escolhida foi a pequena.')
elif tamanho_pizza == 'm':
    preco_pizza = 20.00
    print('Pizza escolhida foi a média.')
elif tamanho_pizza == 'g':
    preco_pizza = 25.00
    print('Pizza escolhida foi a grande.')
else:
    print('Tamanho inválido! Selecione uma opção válida.')
    preco_pizza = 0

# Adiciona o custo do pepperoni, se selecionado
if pepperoni == 's':
    if tamanho_pizza == 'p':
        preco_pizza += 2.00  # Adiciona R$2,00 para pizza pequena
    else:
        preco_pizza += 3.00  # Adiciona R$3,00 para pizza média ou grande

# Adiciona o custo do queijo extra, se selecionado
if queijo_extra == 's':
    preco_pizza += 1.00

# Exibe o preço final se o tamanho for válido
if preco_pizza > 0:
    print(f'O preço final da sua pizza é: R$ {preco_pizza:.2f} Reais')


   