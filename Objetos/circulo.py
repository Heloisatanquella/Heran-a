from Objetos.formas import Forma
from menu.menu import submenu
from Objetos.utils import request_parametros
import math

class Circulo(Forma):

    def __init__(self, raio):
        # Chama a função init da classe Pai e popula as variáveis
        super().__init__('Círculo', 0, 0, 0, raio)

    @staticmethod
    def parametros():
        print(f'\n Digite o parâmetro do Círculo')

        raio = request_parametros('raio')
        return [raio]
    
    def cal_area(self):
        valor = (self.raio * self.raio) * math.pi
        self.str_area(valor)
        return valor

    def cal_perimetro(self):
        valor = (math.pi * 2) * self.raio
        self.str_perimitro(valor)
        return valor

def opc_circulo():
    parametros = Circulo.parametros()
    raio = parametros[0]
    circulo = Circulo(raio)

    while True:
        opc_sub = submenu()

        if opc_sub == 1:
            circulo.cal_area()
        elif opc_sub == 2:
            circulo.cal_perimetro()
        elif opc_sub == 3:
            break


