import os

from cliente import Cliente
from produto import Produto
from pedido import Pedido

while True:
    print('''
____________________________________\n
            Loja Virtual
____________________________________\n
        1 - Cadastrar cliente
        2 - Cadastrar produto
        3 - Fazer um pedido
        4 - Sair
____________________________________\n
''')
    try:
        opcao = int(input('O que deseja fazer? '))

        match opcao:
            case 1:
                Cliente.cadastrar_cliente()

            case 2:
                Produto.fluxo_produto()

            case 3:
                pass

            case 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Encerrando...')
                quit()

            case _:
                print('Opção inválida! Tente novamente.')
                
    except ValueError:
        print('Por favor, insira um valor inteiro.')
