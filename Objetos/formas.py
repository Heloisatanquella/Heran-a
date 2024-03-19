class Forma:

    def __init__(self, forma, altura, largura, base, raio):
        self.forma = forma
        self.altura = altura
        self.largura = largura
        self.base = base
        self.raio = raio

    def __str__(self) -> str:
        return self.forma
    
    def str_area(self, valor):
        print(f'\n A área do {self.forma} é igual a {round(valor, 3)}m²')
    
    def str_perimitro(self, valor):
        print(f'\n O perímetro do {self.forma} é igual a {round(valor, 3)}m')

    def cal_area(self):
        valor = self.altura * self.largura
        self.str_area(valor)
        return valor

    def cal_perimetro(self):
        valor = (self.largura + self.altura) * 2 
        self.str_perimitro(valor)
        return valor