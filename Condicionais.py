""" 
Faça um programa que calcule a média de 4 notas com duas casas decimais
e imprima caso: 
    média maior igual 6 "aluno aprovado"
    média menor que 6 e maior que 5 "aluno em Prova Final"
    média igual a 5 ou menor "aluno reprovado"

"""


from statistics import median
from tokenize import Double


evaluation1 = float(input('Digite a primeira Nota:'))
evaluation2 = float(input('Digite a segunda Nota:'))
evaluation3 = float(input('Digite a terceira Nota:'))
evaluation4 = float(input('Digite a quarta Nota:'))

media = float(evaluation1 + evaluation2 + evaluation3 + evaluation4) / 4

if media >= 6:
    print('Aluno Aprovado!', media)
elif media < 6 and media  >= 5:
    print('Aluno encaminhado para Prova Final!')
else:
    print('Aluno Reprovado!')
