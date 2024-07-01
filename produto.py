# Importando bibliotecas
import os
from dataclasses import dataclass

# Importando métodos
from metodos import continuar

lista_produtos = []

@dataclass
class Produto:
    nome: str
    valor: float
    qntd: int

    # Função para inserir um novo produto
    @staticmethod
    def novo_produto(nome):
        
        try:
            valor = float(input('''
______________________________________________________\n
            Insira o valor do produto: R$'''))
            qntd = int(input('''
______________________________________________________\n
            Insira a quantidade do produto: '''))
            lista_produtos.append(Produto(nome=nome, valor=valor, qntd=qntd))
            print(f'''
______________________________________________________\n
                Novo produto registrado
______________________________________________________\n
                    Produto: {lista_produtos[-1].nome}
                    Valor: R${lista_produtos[-1].valor}
                    Estoque: {lista_produtos[-1].qntd}
______________________________________________________\n''')
                        
        except:
            print('\n Por favor, insira valores válidos.\n')

        if not continuar():
            os.system('cls' if os.name == 'nt' else 'clear')

        else:
            Produto.fluxo_produto()


    # Função para adicionar produtos ao estoque
    @staticmethod
    def adicionar_estoque(nome):
        for produto in lista_produtos:
            if produto.nome == nome:
                try:
                    qntd = int(input('''
______________________________________________________\n
            Insira a quantidade do produto: '''))
                    produto.qntd += qntd

                    print(f'''
______________________________________________________\n
                  Estoque alimentado
______________________________________________________\n
                   Produto: {produto.nome}
                   Valor: R${produto.valor}
                   Estoque: {produto.qntd}
______________________________________________________\n''')
                    break

                except ValueError:
                    print(' Por favor, insira um valor inteiro.')

        if not continuar():
            os.system('cls' if os.name == 'nt' else 'clear')
                
        else:
            Produto.fluxo_produto()


    # Função para controlar o fluxo de novos produtos ou quantidade do estoque
    @staticmethod
    def fluxo_produto():
        os.system('cls' if os.name == 'nt' else 'clear')

        nome = input('''
______________________________________________________\n
            Insira o nome do produto: ''').lower().strip()
        if any(produto.nome == nome for produto in lista_produtos):
            Produto.adicionar_estoque(nome)
        else:
            Produto.novo_produto(nome)