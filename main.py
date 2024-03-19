# Exercício de Herança e Sobrescrita de métodos
# Crie um programa para calcular a área e perímetro das seguintes figuras geométricas: retângulo, quadrado, triângulo e círculo.
# O programa deve conter um menu que solicite ao usuário qual figura ele deseja realizar os cálculos e solicitar os parâmetros para o cálculo.
# O resultado dos cálculos exibidos para o usuário devem conter 3 casas decimais.
from menu.menu import menu
from Objetos.quadrado import opc_quadrado
from Objetos.retangulo import opc_retangulo
from Objetos.triangulo import opc_triangulo
from Objetos.circulo import opc_circulo

def main():
    while True:
        opc = menu()
        if opc == 1:
            opc_quadrado()

        if opc == 2: 
            opc_retangulo()

        if opc == 3:
            opc_triangulo()

        if opc == 4:
            opc_circulo()

        if opc == 5:
            break

main()

# Formulas:
#    Quadrado:
#       params: Lados
#    Retangulo:
#       params: Largura e Altura
#        area = lar x alt
#        per = ( lar x 2 ) + ( alt x 2 )
#
#    Triangulo:
#       params: Base e Altura
#        area = ( base x alt ) / 2
#        per = ( alt x 2 ) + base
#
#    Circulo:
#       params: Raio
#        area = pi x ( raio x raio )
#        per = 2 x pi x raio
