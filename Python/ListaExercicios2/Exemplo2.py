"""
Calcular perímetro do círculo
Data: 15/02/2025
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""
#importando blibioteca matemática
import math

# ENTRADA - Solicita ao usuário o valor do diâmetro do círculo
diametro = float(input("Digite o valor do diâmetro: "))

#PROCESSAMENTO - Cálculo do Perímetro = PI * diâmetro
perimetro =  math.pi * diametro
#perimetro = 3.4 * diametro

#SAÍDA - Exibe o resultado do perímetro
print(f"O perímetro do círculo é {perimetro:.4}")