def menu():
    print(f'\n Escolha uma forma geométrica:')

    while True:
        print(f'\n Opção 1: Quadrado')
        print(f'\n Opção 2: Retângulo')
        print(f'\n Opção 3: Triângulo')
        print(f'\n Opção 4: Círculo')
        print(f'\n Opção 5: Sair')
        opc = input('\n')

        if opc.isdigit():
            opc = int(opc)
            if opc > 0 and opc < 6:
                return opc
            
        print(f'\n Digite um valor válido')

def submenu():
        print(f'\n Escolha um calculo de sua preferencia: ')
        
        while True:
            print(f'\n Opção 1: Área')
            print(f' Opção 2: Perímetro')
            print(f' Opção 3: Voltar')

            opc = input('\n')

            if opc.isdigit():
                opc = int(opc)
                if opc > 0 and opc < 4:
                    return opc
                
            print(f'\n Digite um valor válido')