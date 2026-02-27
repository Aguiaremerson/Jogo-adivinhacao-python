numero =int(input ("Digite um numero inteiro de  0 a 6: "))

import random
nome1 =0
nome2 = 1
nome3 = 2
nome4 =3
nome5 = 4
nome6 = 5
lista = [nome1, nome2, nome3, nome4,nome5, nome6]
escolhido = random.choice(lista)

if numero == escolhido:
    print('Voçê  Ganhou' )
else:
    print ("Você perdeu o computador escolheu {}".format(escolhido))

                   # o codigo do gustavo gauanabara
#form random import randint
#computador =randint (0,5)
#print (" Vou pensar em um numero entre 0 e 5 tente adivinha,,)
#jogador = int (input ('Em que numero eu pensei ?))
#if jogador == comutador :
   #print ("Parabens vc conseguiu me vencer ")
#else:
   #print ("eu ganhui voce perdeu")