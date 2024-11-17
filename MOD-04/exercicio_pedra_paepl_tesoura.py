
# importação da lib
import random

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


'''


tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


'''


pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___


'''
user_choice = int(input('Qual é a opção que você deseja? (0) Pedra, (1) Papel, (2) Tesoura! \n'))

computer_choice = random.randint(0, 2)

print(f'Computador: {computer_choice}')

if user_choice == 0 and computer_choice == 2:
    print('Você ganhou')
elif computer_choice > user_choice:
    print('Você perdeu')

else:
    print('Você digitou uma opção inválida')