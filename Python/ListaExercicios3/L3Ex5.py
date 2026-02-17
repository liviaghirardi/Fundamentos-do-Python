"""
Escreva um programa que calcule a média geométrica entre três números informados pelo
usuário. Utilize o tipo de dados double.
Fórmula da média geométrica: equivalente a (num1 × num2 × num3) **1/3
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""

import math

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float (input("Digite o terceiro número: "))

media = pow(n1 * n2 *n3, 1/3)

print("A média geométrica é: ",media)