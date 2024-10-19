print('Seja bem-vindo(a) ao TipsCode') 

altura = (int(input('Qual é a sua altura? '))) 
if altura >= 120: 
    print('Vendo o ingresso! ') 
    idade = int(input('Qual é a sua idade? ')) 
    if idade <= 12: 
     print('O ingresso vai custar R$5 Reais')
    elif idade <= 18: 
       print('O ingresso vai custar R$12')
    else:
      print('O ingresso vai custa R$24 Reais ')   

else:
   print('Lamento você não vai! ')      