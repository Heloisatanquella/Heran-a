def request_parametros(nome):
    while True:
                parametro = input(f'\n Digite a(o) {nome} em metros: ')
                if parametro.isdigit():
                    return float(parametro)
                
                print(f'\n Digite um valor númerico')