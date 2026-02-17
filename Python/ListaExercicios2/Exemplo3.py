"""
Cálculo da área do círculo
Criado por: Lívia Ghirardi do Amaral
Professora: Luciana
"""
import math

#ENTRADA - Solicite o valor de raio do círculo
raio = float(input("Digite o valor do raio: "))

#PROCESSAMENTO - Cálculo da área do círculo
area = math.pow(raio,2.0) * math.pi
#area = raio**2 *math.pi

#SAÍDA - Exibe o resultado
print(f"A área do circulo é {area:.4}")