"""
Faça um programa que leia as notas de duas provas, calcule a média aritmética simples, e
informe se o aluno foi aprovado (média maior ou igual a 6) ou reprovado (média menor que 6).
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""
from pickle import encode_long

p1 = float(input("Digite a nota: "))
p2 = float(input("Digite a nota: "))
media=(p1+p2) / 2
if  media >= 6:
    print("O aluno foi aprovado")

elif media < 6:
    print("O aluno foi reprovado")