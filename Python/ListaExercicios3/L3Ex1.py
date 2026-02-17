"""
Escreva um programa que calcule o delta de uma equação de segundo grau.
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""

#Entrada: Solicitar os valores
a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

#Processamento
delta = float(b**2 - 4 * a * c)

#Saída
print ("O valor de delta é: ",delta)