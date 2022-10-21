#Sistema de login com Python

from time import sleep


def banco():
    print('-'*16)
    print('Banco do Alfredo')
    print('-'*16)

    print('Tem uma conta [T] ou criar uma [C]\n')
    contas = input('Digite aqui: ').upper()
    print()

    #Parte de criar conta

    if(contas == 'C'):
        print('==-Create-== \n')
        nome = input('Nome de usuário: ')
        years = input('Informe a idade: ')

        passaword = input('Senha do usuário: ')
        passawordConfirm = input('Confirmar senha: ')

        #Caso ele acerte a senha

        if(passaword == passawordConfirm):
            print('Carregando...')
            sleep(1)
            print('Conta criada! \n')
            sleep(1)
            escolhaLogin = input('Deseja logar? [S] || [N]: ').upper()
            
            #Se a escolha for Não

            if(escolhaLogin == 'N'):
                print('Carregando...')
                sleep(2)
                print('Programa encerrado!')
                exit()

            #Se ele escolher Sim            
            if(escolhaLogin == 'S'):
                login = input('Nome: ')
                senha = input('Senha: ')
                idade = input('Idade: ')
                if(login != nome):
                    while(login != nome):
                        erroLogin = input('Nome de usuário incorreto, informe aqui: ')
                        if(erroLogin == nome):
                            None
                        if(senha != passaword):
                            while(passaword != senha ):
                                erroSenha = input('Senha incorreta! Informe a senha novamente!: ')
                                if(erroSenha == passaword):
                                    None
                                if(idade != years):
                                    while(idade != years):
                                        erroIdade = input('Idade incorreta! Informe a idade!: ')
                                        if(years == idade):
                                            print('Você entrou na conta!')
                                            exit()
                                    exit()
                            exit()
                    exit()


       #Se ele errar a senha

        if(passawordConfirm != passaword):
            while(passawordConfirm != passaword):
                erro = input('[ERROR 404] Senha incorreta! Tente novamente!: ')
                if(erro == passaword):
                    print('Conta criada! \n')
                    sleep(1)
                    escolhaLogin = input('Deseja logar? [S] || [N]: ').upper()

                    #Se for não
                    if(escolhaLogin == 'N'):
                        print('Carregando...')
                        sleep(2)
                        print('Programa encerrado!')
                        exit()

                    #Se for Não
                    if(escolhaLogin == 'S'):
                        login = input('Nome: ')
                        senha = input('Senha: ')
                        idade = input('Idade: ')
                        if(login != nome):
                            while(login != nome):
                                erroLogin = input('Nome de usuário incorreto, informe aqui: ')
                                if(erroLogin == nome):
                                    None
                                if(senha != passaword):
                                    while(senha != passaword):
                                        erroSenha = input('Senha incorreta! Informe a senha novamente!: ')
                                        if(erroSenha == passaword):
                                            None
                                if(idade != years):
                                    while(idade != years):
                                        erroIdade = input('Idade incorreta! Informe a idade!: ')
                                        if(years ==  idade):
                                            print('Você entrou na conta!')
                                            exit()
                                    exit()
                            exit()
                    exit()
banco()
