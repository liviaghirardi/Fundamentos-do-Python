"""
Escreva um programa que calcule o perímetro e a área de um retângulo.
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""

#Entrada: Solicitar os valores
largura = float(input("Digite a largura do retângulo: "))
comprimento = float(input("Digite o comprimento do retângulo: "))

#Processamento: Calcular
area =  float(comprimento * largura)
perimetro = float( largura * 2 + comprimento * 2 )

print ("A área do retângulo é ", area)
print ("O perimetro do retângulo é: ",perimetro)