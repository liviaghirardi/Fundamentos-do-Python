"""
Crie um programa que solicite ao usuário o valor do raio de uma esfera e calcule o seu volume.
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""
import math
math.pi

#Entrada: Solicitar os valores
raio = float(input("Digite o raio da esfera: "))

#Processamento: V = 4/3 π r³, onde V é o volume e r é o raio
volume = float(4/3 * math.pi * raio**3)

print (f"O valor do volume da esfera é: {volume:.5}")