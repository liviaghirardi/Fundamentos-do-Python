"""
DESVIO CONDICIONAL SIMPLÊS
Apresenta mensagens se o número inteiro digitado for maior que 1000
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""
#ENTRADA
num = int(input("Digite um número inteiro: "))

#Se o número for maior que 1000 faça
if num > 1000:
    print("o número digitado é maior que 1000")
    print("Fim...")

#Apresenta a mensagem independente do if,porque está no mesmo nível da if
print("Fim...")

'''
SINTAXE DA FUNÇÃO IF SIMPLES

if teste_lógico:
    linha_instituição_se_verdeiro
'''