"""
Faça um programa que leia dois números e informe qual é o maior.
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o primeiro número: "))
# Se o número 1, for maior que o 2, aparecerá "O primeiro número é maior que o segundo"
if  n1 > n2:
    print("O primeiro número é maior que o segundo")
# Se o segundo número, for maior que o 2,aparecerá "O primeiro número é maior que o segundo"
elif n2 > n1:
    print("O segundo número é maior que o primeiro")
# Se os dois números forem iguais, aparecerá "Os dois números são iguais"
else:
    print("Os dois números são iguais")