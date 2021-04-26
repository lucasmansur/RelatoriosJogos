import trabjogospy.bd as bd
import trabjogospy.Desk as desk


def traco():
    linha = '-'
    print(linha*70)


def titulo():
    title = '|MENU PRINCIPAL|'
    print(title.center(70))


def opcoes():
    print('[1] - Cadastrar Jogos\n[2] - Ver Jogos\n[3] - Alterar Jogos\n[4] - Deletar Jogos\n[5] - Opções de Usuario\n[6] - Gerar Relatório\n[7] - Sair do Programa')

def menu(user, id_usuario, senha):
    traco()
    titulo()
    traco()
    print(f'|Usuario Ativo|.....................................|{user}|')
    traco()
    opcoes()
    traco()
    id_jogador = int(id_usuario)
    senhacomparar = senha
    user = user
    id_usuario = id_usuario
    senha = senha
    escolha(id_jogador,senhacomparar,user,id_usuario,senha)


def escolha(id_jogador, senhacomparar, user, id_usuario, senha):
    escolhe = str(input('[R]: ')).lower().strip()
    if(escolhe == '1' or escolhe == 'cadastrar' or escolhe == 'cadastrarjogo' or escolhe =='cadastrarjogos'):
        desk.addJogo(user)
        menu(user,id_usuario,senha)
    elif(escolhe == '2' or escolhe == 'ver' or escolhe == 'verjogo' or escolhe == 'verjogos'):
        desk.verJogoLogin(user)
        menu(user, id_usuario, senha)
    elif(escolhe == '3' or escolhe == 'alterar' or escolhe == 'alterarjogo' or escolhe == 'alterarjogos'):
        traco()
        print('[1] - Nome\n[2] - Tempo Jogado\n[3] - Conquistas\n[4] - Finalizado')
        traco()
        while True:
            alterar = str(input('O que gostaria de alterar em Jogo?: ')).lower().strip()
            if(alterar == '1' or alterar == 'nome'):
                desk.trocarNomeJogo()
                menu(user, id_usuario, senha)
                break
            elif(alterar == '2' or alterar == 'tempo' or alterar == 'tempojogado'):
                desk.trocarTempojogadoJogo()
                menu(user, id_usuario, senha)
                break
            elif(alterar == '3' or alterar == 'conquistas' or alterar == 'conquista'):
                desk.trocarConquistasJogo()
                menu(user, id_usuario, senha)
                break
            elif(alterar == '4' or alterar == 'finalizado'):
                desk.trocarFinalizadoJogo()
                menu(user, id_usuario, senha)
                break
            else:
                print('[#ERRO#] Opção inválida! Por favor, escolha uma opção válida!\n[1] - Nome\n[2] - Tempo Jogado\n[3] - Conquistas\n[4] - Finalizado')
    elif(escolhe == '4' or escolhe == 'excluir' or escolhe == 'excluirjogo'):
        desk.excluirJogo()
        menu(user, id_usuario, senha)
    elif(escolhe == '5' or escolhe == 'opcoes' or escolhe == 'opcoesdeusuario' or escolhe == 'opcoesusuario' or escolhe == 'opções' or escolhe == 'opçõesdeusuario' or escolhe == 'opçõesusuario' or escolhe == 'opcoesusuário' or escolhe == 'opcoesdeusuário' or escolhe == 'opçõesdeusuário' or escolhe == 'opçõesusuário'):
        traco()
        print('[1] - Alterar nome do usuario\n[2] - Alterar senha\n[3] - EXCLUIR USUARIO')
        traco()
        opcao = str(input('[R]: ')).lower().strip()
        if(opcao == '1' or opcao == 'alterarnome'):
            validar = True
            while validar:
                while True:
                    novousuario = str(input('Digite seu nome de usuario: ')).strip()
                    if not novousuario:
                        print('[#ERRO#] O nome de usuario não pode estar vazio!')
                    else:
                        break
                for dado in bd.exibeJogador():                
                    usercompar = str(dado[1])
                    if(usercompar == novousuario):
                        print('[#ERRO#] Este nome de usuario já está em uso! Por favor, Escolha outro!')                    
                        validar = True
                        break
                    else:                    
                        validar = False
            t = 3
            for i in range(3):
                t = t-1
                senha = str(input('Digite sua senha para continuar a operação: '))
                if(senha == senhacomparar):
                    bd.attNomeJogador(novousuario, id_jogador)
                    break
                else:                    
                    if(t > 0):
                        print(f'[#ERRO#] Senha incorreta! Mais {t} Tentativas!')
                    elif(t == 0):
                        print('Numero de tentativas excedido! Cancelando operação...')
                        exit()
        elif(opcao == '2' or opcao == 'alterarsenha'):
            while True:
                novasenha = str(input('Digite sua nova senha de 8 a 12 caracteres: ')).strip()
                if(len(novasenha) > 12):
                    print('[#ERRO#] Sua senha pode ter no máximo 12 caracteres!')
                elif(len(novasenha) < 8):
                    print('[#ERRO#] Sua senha deve ter no mínimo 8 caracteres!')
                elif not novasenha:
                    print('[#ERRO#] Sua senha não pode estar em branco!')
                else:
                    break
            t = 3
            for i in range(3):
                t = t-1
                senha = str(input('Digite sua senha para confirmar a operação: '))
                if(senha == senhacomparar):
                    bd.attSenhaJogador(novasenha, id_jogador)
                    break
                else:
                    if(t > 0):
                        print(f'[#ERRO#] Senha incorreta! Mais {t} Tentativas!')
                    elif(t == 0):
                        print('Numero de tentativas excedido! Cancelando operação...')
                        exit()
        elif(opcao == '3' or opcao == 'excluir' or opcao == 'excluirusuario'):
            print('\n!!!----ATENÇÃO----!!!\n')
            print('ESTA OPÇÃO DELETARÁ SEU USUARIO PARA SEMPRE! ISSO NÃO PODERÁ SER DESFEITO!')
            confirma = str(input('Digite "CONFIRMA" para prosseguir: ')).strip()
            if(confirma == 'CONFIRMA'):
                t = 3
                for i in range(3):
                    t = t-1
                    senha = str(input('Digite sua senha para confirmar a operação: '))
                    if(senha == senhacomparar):
                        bd.delJogador(id_jogador)
                        break
                    else:
                        if(t > 0):
                            print(f'[#ERRO#] Senha incorreta! Mais {t} Tentativas!')
                        elif(t == 0):
                            print('Numero de tentativas foi excedido! A Operação está sendo Cancelanda ...')
                            exit()
            else:
                print('Cancelando operação...')
                exit()
    elif(escolhe == '6' or escolhe == 'gerar' or escolhe == 'gerarrelatorio' or escolhe == 'relatorio'):        
        while True:
            relatorio = str(input('Escolha qual relatório deseja gerar:\n[1] - Data de criação\n[2] - Nome de Usuario\n[3] - Jogos finalizados\n[R]: ')).lower().strip()
            if(relatorio == '1' or relatorio == 'data' or relatorio == 'datacriacao'):
                validar = True
                msg = int(0)
                while validar:
                    if(msg == 1):
                        print('[#ERRO#] Nenhum jogo adicionado nessa data. Por favor, digite outra!')
                    dia = str(input('[DIA]: '))
                    mes = str(input('[MÊS]: '))
                    ano = str(input('[ANO]: '))
                    date = str(dia+'/'+mes+'/'+ano)
                    for dado in bd.exibeJogo():
                        comparardata = str(dado[6])
                        if(comparardata == date):
                            validar = False
                            msg = 0
                            break
                        else:
                            msg = 1
                            validar = True
                print('Gerando Relatorio...\n')
                desk.verJogoData(date)
                break
            elif(relatorio == '2' or relatorio == 'nome' or relatorio == 'nomeusuario' or relatorio == 'nomedeusuario'):
                validar = True
                msg = int(0)
                while validar:
                    if(msg == 1):
                        print('[#ERRO#] Este Usuario ainda não adicionou nenhum jogo!\n Por favor, digite outro usuario.')
                    usuariorelatorio = str(input('Digite o nome de usuario para filtrar!: '))
                    for dado in bd.exibeJogo():
                        compararusuario = str(dado[1])
                        if(compararusuario == usuariorelatorio):
                            validar = False
                            msg = 0
                            break
                        else:
                            msg = 1
                            validar = True
                print('Gerando Relatório...\n')            
                desk.verJogoUsuarioRelatorio(usuariorelatorio)
                break
            elif(relatorio == '3' or relatorio == 'jogofinalizado' or relatorio == 'finalizado'):            
                while True:
                    final = str(input('Gostaria de filtrar por jogos finalizados?: ')).lower().strip()
                    if(final == 'finalizado' or final == 'finalizados'):
                        fim = str('Sim')
                        break
                    elif(final == 'naofinalizado' or final == 'naofinalizados' or final == 'nãofinalizado' or final == 'nãofinalizados'):
                        fim = str('Não')
                        break
                    else:
                        print('[#ERRO#] Opção inválida! Por favor digite uma opção válida! Opções válidas: [S/N]')
                print('Gerando Relatório...\n')
                desk.verJogoFinalizado(fim)
                break
            else:
                print('[#ERRO#] Opção inválida! Por favor, digite uma opção válida!\n[1] - Data de criação\n[2] - Nome de Usuario\n[3] - Jogo finalizado ou não\n')            
    elif(escolhe == '7' or escolhe == 'sair' or escolhe == 'sairprograma' or escolhe == 'sairdoprograma'):
        print('Saindo...')
        exit()
    else:
        print('[#ERRO#] Opção inválida! Por favor, digite uma opção válida!\n[1] - Cadastrar Jogo\n[2] - Ver Jogos\n[3] - Alterar Jogo\n[4] - Deletar Jogo\n[5] - Opções de Usuario\n[6] - Gerar Relatorios\n[7] - Sair do Programa')