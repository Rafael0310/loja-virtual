# Importando bibliotecas
import os
from dataclasses import dataclass

# Importando métodos
from metodos import (
    validar_cpf,
    continuar
)

from produto import lista_produtos
from cliente import lista_clientes

itens_pedido = {}

@dataclass
class Pedido:
    itens_pedido: []
    quantidade: int

    def checar_listas():
        os.system('cls' if os.name == 'nt' else 'clear')

        if lista_produtos and lista_clientes:
            Pedido.fazer_pedido()

        else:
            print('\n Por favor, cadastre pelo menos um produto e um cliente antes de registrar uma venda.')

    # Função para verificar se o cliente encontra-se registrado
    @staticmethod
    def procurar_cliente(cpf):
        if any(cliente.cpf == cpf for cliente in lista_clientes):
            return True
        else:
            print(' Cliente não localizado.')
            return False

    # Função para verificar se o produto encontra-se registrado
    @staticmethod
    def procurar_produto(nome):
        if any(produto.nome == nome for produto in lista_produtos):
            return True
        else:
            print(' Produto não localizado.')
            return False

    # Função para verificar se o estoque é capaz de suprir a compra
    @staticmethod
    def verificar_estoque(item, qntd):
        for produto in lista_produtos:
            if produto.nome == item:
                if produto.qntd - qntd < 0:
                    return True
                else:
                    return False

    def fazer_pedido():
        valor_total = 0.0
        qntd = 0

        while True:
            try:
                cpf = input(' Digite o CPF do cliente: ')
                validar_cpf(cpf)

                if Pedido.procurar_cliente(cpf):
                    while True:
                        # Imprime os itens registrados e solicita o interessado pelo cliente
                        for produto in lista_produtos:
                            print(f'''______________________________________________________\n
    Produto: {produto.nome} - Preço: R${produto.valor} - Estoque: {produto.qntd}''')

                        item = input('______________________________________________________\n\n Digite o nome do produto que deseja comprar\n 0 - Fechar a compra\n ')
            
                        # se item for diferente de 0, significa que o usuário ainda não deseja finalizar a compra
                        if not item == '0':
                            # Verifica se o produto foi localizado
                            if Pedido.procurar_produto(item):

                                while True:
                                    try:
                                        # Usuário insere a quantidade do produto
                                        qntd = int(input(' Qual a quantidade desejada?\n'))

                                        if not Pedido.verificar_estoque(item, qntd):
                                            itens_pedido[item] = qntd
                                            print(f' Foi/foram adicionado/s {qntd} {item}/s ao pedido.')
                                            break

                                        else:
                                            print(' Estoque insuficiente para a compra.')

                                    except:
                                        print(' Por favor, insira um valor inteiro.')
                        else:
                            print('''
______________________________________________________\n
                      Nota Fiscal
______________________________________________________\n''')
                            for item in itens_pedido:
                                for produto in lista_produtos:
                                    if produto.nome == item:
                                        valor_total += produto.valor * qntd
                                        produto.qntd -= qntd
                                        print(f' Produto: {produto.nome} - Valor: {produto.valor} - Quantidade: {qntd}')
                                        print('______________________________________________________')
                                        
                            print(f'\n              Valor total: {valor_total}')
                            break

            except:
                print('______________________________________________________\n                 CPF inválido!')

            finally:
                if not continuar():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

            