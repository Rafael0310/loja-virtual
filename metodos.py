def validar_cpf(cpf):
    if len(cpf) != 11:
        raise ValueError
    
    else:
        try:
            int(cpf)
        except:
            raise ValueError

def continuar():
    while True:
        try:
            opcao = int(input('''
                  Deseja continuar?\n
                      1 - Sim
                      2 - Não
______________________________________________________
 '''))
            
            match opcao:
                case 1:
                    return True
                case 2:
                    return False
                case _:
                    print(' Opção inválida! Tente novamente.')

        except ValueError:
            print(' Por favor, insira um valor inteiro.')