"""
tabela de pizza
pizza pequena - R$15,00 Reais
pizza Média - R$20,00 Reais
pizza Grande - R$25,00 Reais


Adiciona pepperoni na pizza pequena - + R$ 2,00 Reais
Adiciona pepperoni na pizza média e grande - + R$ 3,00 Reais
Queijo extra em todos os tamnhos (sim ou não) + R$ 1,00 Reais

"""

print('Bem vindo à Pizzaria Ulisses')

tamanho_pizza = input('Digite o tamanho da sua pizza: pequena (p), média (m), grande (g) ')
pepperoni = input('Adicionar pepperoni a pizza: sim(s) ou não(n)')
Queijo_extra = input('Adicionar queijo extra: sim (s) ou não(n)')
if tamanho_pizza == 'p':
    print('Pizza escolhida foi a pequena')
elif tamanho_pizza == 'm':
    print('Pizza escolhida foi a média')
elif tamanho_pizza == 'g':
    print('Pizza escolhida foi a grande')

   