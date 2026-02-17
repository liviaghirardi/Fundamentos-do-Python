"""
Faça um programa que pergunte a idade do usuário e informe se ele pode ou não se aposentar.
Obs. Uma pessoa só pode se aposentar quando atingir 60 anos (idade mínima).
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""

num = int(input("Digite a idade: "))
if num >= 60:
    print("Você pode se aposentar")
elif num < 60:
    print("Infelizmente você não pode se aposeentar")