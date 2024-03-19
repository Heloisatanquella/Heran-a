from Objetos.formas import Forma
from menu.menu import submenu
from Objetos.utils import request_parametros

class Triangulo(Forma):

    def __init__(self, base, altura):
        # Chama a função init da classe Pai e popula as variáveis
        super().__init__('Triângulo', altura, 0, base, 0)

    @staticmethod
    def parametros():
        print(f'\n Digite os parâmetros do Triângulo')

        base = request_parametros('base')
        altura = request_parametros('altura')
        return [base, altura]
    
    def cal_area(self):
        valor = (self.base * self.altura) / 2
        self.str_area(valor)
        return valor

    def cal_perimetro(self):
        valor = (self.altura * 2) + self.base
        self.str_perimitro(valor)
        return valor

def opc_triangulo():
    parametros = Triangulo.parametros()
    base = parametros[0]
    altura = parametros[1]
    triangulo = Triangulo(base, altura)

    while True:
        opc_sub = submenu()

        if opc_sub == 1:
            triangulo.cal_area()
        elif opc_sub == 2:
            triangulo.cal_perimetro()
        elif opc_sub == 3:
            break


