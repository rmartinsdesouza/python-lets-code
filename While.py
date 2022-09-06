""" 
Faça um programa que solicite um numero inteiro
e quando o numero digitado for igual o numero 
secreto imprima você acertou o número correto,
caso não seja igual peça outro numero até estar certo.

 """


numSecreto = 10

while (exit != 's'):

    valorDigitado = int(input('Digite um numero de 0 a 10 e tente adinhar qual o numero correto:'))

    if numSecreto == valorDigitado:
        print('Você acertou Parabéns!')
        exit = 's'    
    else:
        print('Ha você errou, tente novamente')
