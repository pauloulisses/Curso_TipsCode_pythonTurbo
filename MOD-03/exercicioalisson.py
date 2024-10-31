"""
A função lower() em Python converte todas as letras de uma string para minúsculas. Ela é útil para normalizar entradas de texto, 
especialmente quando você quer comparar strings, sem se preocupar com letras maiúsculas ou minúsculas.

No seu código, lower() é usada para garantir que, independentemente de o usuário digitar "Esquerda", "ESQUERDA" ou "esquerda", a entrada seja transformada para "esquerda". 
Isso facilita a comparação e evita erros devido a variações de caixa.

"""




print('Bem-Vindo(a) a ilha do tesouro perdido!')
print('Sua missão é encontrar o tesouro!')

print(''' 
  /'=----=           ______
            ((    ||          "--.__."
             "  @>||_____________//
          _______ /^\"""""""""""//\========)
         _--"""--/-. "\        // _\-:::-/_-.
       ." .-"""-/ "_\  "\  == // ;::\:::/::".\
      ; /     _/ "  \\   "\-+//--..._\_/:::::\\
      . ;    o    . ||   ( ()/)======(o)::::::.
      . \         ; .|    -|.;____...."b:::::;
       . -._  _ -  ;       ==    :::::::::::;
        "-..____.'     ls         ":::::::'

''')

choice1 = input('Você está em uma encruzilhada, para onde você deseja ir? Digite "esquerda" ou "direita": ').lower()

if choice1 == 'esquerda':
    choice2 = input('Você deseja "nadar" ou "esperar"? ').lower() # converte todas as letras da str para minúscula 
    if choice2 == 'esperar':
        choice3 = input('Qual porta deseja abrir: Vermelha, Amarela, Azul? ').lower()
        if choice3 == 'vermelha':
            print('Game Over')
        elif choice3 == 'amarela':
            print('Parabéns, você achou o tesouro!')
        elif choice3 == 'azul': 
            print('Comido por feras')
        else:
            print('Você escolheu uma alternativa que não existe')
    else:
        print('Game Over')
else:
    print('Game Over')




