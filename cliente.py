import os

from metodos import (
    validar_cpf,
    continuar
)

from dataclasses import dataclass

lista_clientes = []

@dataclass
class Cliente:
    cpf: str
    nome: str
    endereco: str
    
    @staticmethod
    def cadastrar_cliente():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            try:
                cpf = input('''
____________________________________\n
 Digite o CPF do cliente: ''')
                
                validar_cpf(cpf)

                # Verifica se o cliente já foi cadastrado
                if any(cliente.cpf == cpf for cliente in lista_clientes):
                    print('''
____________________________________\n
 Esse cliente já foi cadastrado.
____________________________________''')

                else:
                    nome = input('''
____________________________________\n
 Digite o nome do cliente: ''')
                    
                    endereco = input('''
____________________________________\n
 Digite o endereço do cliente: ''')

                    lista_clientes.append(Cliente(cpf=cpf, nome=nome, endereco=endereco))
                    print(f'''
____________________________________\n
      Novo cliente cadastrado!
____________________________________\n
    CPF: {lista_clientes[-1].cpf}
    Nome: {lista_clientes[-1].nome}
    Endereço: {lista_clientes[-1].endereco}
____________________________________\n''')

            except ValueError:
                print('\n          CPF inválido!')
            
            finally:
                if not continuar():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break