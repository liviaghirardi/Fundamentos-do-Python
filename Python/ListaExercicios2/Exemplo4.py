"""
Crie um programa em python que calcule a area de um triângulo retângulo
Data 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professor: Luciana
"""

#Entrada: Solicitar o valor da base e da altura

base = float(input("Digite a base do triângulo retângulo: "))
altura = float(input("Digite a altura do triângulo retângulo: "))

# Processamento: area = (base * altura)/2
area = (base * altura)/2.0

#Saída: Exibe o resultado
print(f"A area do triângulo retângulo é: {area:4}")