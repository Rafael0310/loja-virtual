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
        opcao = int(input('O que deseja fazer?'))

        match opcao:
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                print('Encerrando...')
                quit()

            case _:
                print('Opção inválida! Tente novamente.')
                
    except ValueError:
        print('Por favor, insira um valor inteiro.')
    except:
        print('Erro inesperado, tente novamente.')