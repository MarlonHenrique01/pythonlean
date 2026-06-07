
#                               ********REVERSE GAME******** 



print('----------Reverse Game-----------')

palavra = input("Digite uma palavra e veremos se ela e igual de traz para frente: 'q para sair'  ")

reverse = palavra[::-1]

if reverse == palavra:
        print('{} e sim igual a {} lida de traz para frente, parabens!!!'.format(reverse.upper(), palavra.upper()))
else:
        print('Essa palavra não e a mesma de traz para frente tente novamente haha!!!!')
