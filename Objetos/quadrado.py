from Objetos.formas import Forma
from menu.menu import submenu
from Objetos.utils import request_parametros

class Quadrado(Forma):

    def __init__(self, lado):
        # Chama a função init da classe Pai e popula as variáveis
        super().__init__('Quadrado', lado, lado, 0, 0)

    @staticmethod
    def parametros():
        print(f'\n Digite os parâmetros do Quadrado')

        lado = request_parametros('lado')
        return [lado]

def opc_quadrado():
    parametros = Quadrado.parametros()
    lado = parametros[0]
    quadrado = Quadrado(lado)

    while True:
        opc_sub = submenu()

        if opc_sub == 1:
            quadrado.cal_area()
        elif opc_sub == 2:
            quadrado.cal_perimetro()
        elif opc_sub == 3:
            break


