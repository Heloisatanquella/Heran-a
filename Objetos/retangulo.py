from Objetos.formas import Forma
from menu.menu import submenu
from Objetos.utils import request_parametros

class Retangulo(Forma):

    def __init__(self, largura, altura):
        # Chama a função init da classe Pai e popula as variáveis
        super().__init__('Retângulo', altura, largura, 0, 0)

    @staticmethod
    def parametros():
        print(f'\n Digite os parâmetros do Retangulo')

        largura = request_parametros('largura')
        altura = request_parametros('altura')
        return [largura, altura]

def opc_retangulo():
    parametros = Retangulo.parametros()
    largura = parametros[0]
    altura = parametros[1]
    retangulo = Retangulo(largura, altura)

    while True:
        opc_sub = submenu()

        if opc_sub == 1:
            retangulo.cal_area()
        elif opc_sub == 2:
            retangulo.cal_perimetro()
        elif opc_sub == 3:
            break


