import trabjogospy.bd as bd
import trabjogospy.menu as men
relatorioUsuario = './trabjogospy/relatorios/NomeDeUsuario.txt'
relatorioData = './trabjogospy/relatorios/DataCriacao.txt'
relatorioFinalizado = './trabjogospy/relatorios/Finalizado.txt'


def addJogo(user):
    condition = True
    while condition:
        while True:
            try:
                while True:
                    nome = str(input('Insira o nome do jogo: ')).strip()
                    if not nome:
                        print('[#ERRO#] O nome do jogo não pode estar vazio!')
                    else:                        
                        break            
            except (ValueError, TypeError):
                print('[#ERRO#] Valor inválido! Por favor, digite um caracter não numerico!')
            else:
                break
        
        while True:
            try:
                horajogo = float(input('Insira quantas horas foram jogadas no jogo: '))
            except (ValueError, TypeError):
                print('[#ERRO#] Valor inválido! Por favor, digite um numero Real!')
            else:
                break
        
        while True:
            try:
                conquistas = int(input('Insira quantas conquistas você adquiriu no jogo: '))
            except (ValueError, TypeError):
                print('[#ERRO#] Valor inválido! Por favor, digite um numero Inteiro!')
            else:
                break
        
        fim = int(0)
        while True:
            acabou = str(input('Ja terminou o jogo?: ')).lower()
            if(acabou == 's' or acabou == 'sim'):
                fim = int(1)
                break
            elif(acabou == 'n' or acabou == 'nao' or acabou == 'não'):
                fim = int(0)
                break
            else:
                print('[#ERRO#] Opção inválida! Por favor digite uma opção válida! Opções válidas: [S/N]')
        from datetime import datetime
        data = datetime.now().strftime('%d/%m/%Y')
        bd.inserirJogo(user,nome,horajogo,conquistas,fim,data)
        while True:
            resposta = str(input('Gostaria de inserir mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('[#ERRO#] Opção inválida! Por favor digite uma opção válida! Opções válidas: [S/N]')

def verJogoLogin(user):
    for dado in bd.exibeJogo():
        final = int(dado[5])
        if(final == 1):
            fim = 'Sim'
        elif(final == 0):
            fim = 'Não'
        compararusuario = str(dado[1])
        if(user == compararusuario):
            print('Adicionado por: {}\nNome: {}\nTempo Jogado: {}\nConquistas: {}\nFinalizado?: {}\n'.format(dado[1],dado[2],dado[3],dado[4],fim))

def verJogoUsuarioRelatorio(usuariorelatorio):
    for dado in bd.exibeJogo():
        final = int(dado[5])
        if(final == 1):
            fim = 'Sim'
        elif(final == 0):
            fim = 'Não'
        compararusuario = str(dado[1])
        if(usuariorelatorio == compararusuario):
            print('Adicionado por: {}\nNome: {}\nTempo Jogado: {}\nConquistas: {}\nFinalizado?: {}\n'.format(dado[1],dado[2],dado[3],dado[4],fim))
            relatorio  = open(relatorioUsuario, 'a', encoding= 'UTF-8')
            relatorio.writelines('Adicionado por: {}\nNome: {}\nTempo Jogado: {}\nConquistas: {}\nFinalizado?: {}\n'.format(dado[1],dado[2],dado[3],dado[4],fim))
            relatorio.write("\n")
            relatorio.close()

def verJogoSemParametro():
    for dado in bd.exibeJogo():
        final = int(dado[5])
        if(final == 1):
            fim = 'Sim'
        elif(final == 0):
            fim = 'Não'        
        print('ID: {}\nAdicionado por: {}\nNome: {}\nTempo Jogado: {}\nConquistas: {}\nFinalizado?: {}\n'.format(dado[0],dado[1],dado[2],dado[3],dado[4],fim))

def verJogoFinalizado(fim):
    for dado in bd.exibeJogo():
        final = int(dado[5])
        if(final == 1):
            fim = 'Sim'
        elif(final == 0):
            fim = 'Não'
        compararfinalizado = str(fim)
        if(fim == compararfinalizado):
            print('Finalizado?: {}\nNome: {}\nTempo Jogado: {}\nConquistas: {}\n'.format(fim,dado[2],dado[3],dado[4]))
            relatorio = open(relatorioFinalizado, 'a' ,encoding= 'UTF-8')
            relatorio.writelines('Finalizado?: {}\nNome: {}\nTempo Jogado: {}\nConquistas: {}\n'.format(fim,dado[2],dado[3],dado[4]))
            relatorio.write("\n")
            relatorio.close()

def verJogoData(date):
    for dado in bd.exibeJogo():
        final = int(dado[5])
        if(final == 1):
            fim = 'Sim'
        elif(final == 0):
            fim = 'Não'
        comparardata = str(dado[6])
        if(date == comparardata):
            print('Adicionado em: {}\nNome: {}\nTempo Jogado: {}\nConquistas: {}\nFinalizado?: {}\n'.format(dado[6],dado[2],dado[3],dado[4],fim))
            relatorio = open(relatorioData, 'a', encoding= 'UTF-8')
            relatorio.writelines('Adicionado em: {}\nNome: {}\nTempo Jogado: {}\nConquistas: {}\nFinalizado?: {}\n'.format(dado[6],dado[2],dado[3],dado[4],fim))
            relatorio.write("\n")
            relatorio.close()

def trocarNomeJogo():
    verJogoSemParametro()
    condition = True
    while condition:
        while True:
            try:
                id_jogo = int(input('Insira o ID do jogo que deseja alterar o nome: '))
            except (ValueError, TypeError):
                print('[#ERRO#] Valor inválido! Por favor, digite um numero Inteiro!')
            else:
                break
        
        while True:            
            nome = str(input('Digite o novo nome: ')).strip()
            if not nome:
                print('[#ERRO#] O nome do jogo não pode estar vazio!')
            else:
                break
        bd.attNomeJogo(nome, id_jogo)
        while True:
            resposta = str(
                input('Gostaria de alterar o nome de mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('[#ERRO#] Opção inválida! Por favor digite uma opção válida! Opções válidas: [S/N]')

def trocarTempojogadoJogo():
    verJogoSemParametro()
    condition = True
    while condition:
        while True:
            try:
                id_jogo = int(input('Insira o ID do jogo que deseja alterar por quanto tempo jogou: '))
            except(ValueError, TypeError):
                print('[#ERRO#] Valor inválido! Por favor, digite um numero Inteiro!')
            else:
                break
        
        while True:
            try:
                horajogo = float(input('Por quanto tempo Jogou ?: '))
            except(ValueError, TypeError):
                print('[#ERRO#] Valor inválido! Por favor, digite um numero Real!')            
            else:
                break
        bd.attHoraJogo(horajogo, id_jogo)
        while True:
            resposta = str(input('Gostaria de alterar por quanto tempo jogou em mais algum jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('[#ERRO#] Opção inválida! Por favor digite uma opção válida! Opções válidas: [S/N]')

def trocarConquistasJogo():
    verJogoSemParametro()
    condition = True
    while condition:
        while True:
            try:
                id_jogo = int(input('Insira o ID do jogo que deseja alterar as conquistas: '))
            except(ValueError, TypeError):
                print('[#ERRO#] Valor inválido! Por favor, digite um numero Inteiro!')
            else:
                break
        while True:
            try:
                conquistas = int(input('Digite o novo Tempo Jogado: '))
            except(ValueError, TypeError):
                print('[#ERRO#] Valor inválido! Por favor, digite um numero Inteiro!')
            else:
                break
        bd.attConquistaJogo(conquistas, id_jogo)
        while True:
            resposta = str(input('Gostaria de alterar as conquistas de mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('[#ERRO#] Opção inválida! Por favor digite uma opção válida! Opções válidas: [S/N]')

def trocarFinalizadoJogo():
    verJogoSemParametro()
    condition = True
    while condition:
        while True:
            try:
                id_jogo = int(input('Insira o ID do jogo que deseja alterar a marcação de finalizado: '))
            except(ValueError, TypeError):
                print('[#ERRO#] Valor inválido! Por favor, digite um numero Inteiro!')
            else:
                break
        
        while True:
            fim = int(0)
            acabou = str(input('O Jogo foi Finalizado ?: ')).lower()
            if(acabou == 's' or acabou == 'sim'):
                fim = 1
                break
            elif(acabou == 'n' or acabou == 'nao' or acabou == 'não'):
                fim = 0
                break
            else:
                print('Opção inválida! Por favor digite uma opção válida! Opções válidas: [S/N]')
        bd.attFinalizadoJogo(fim, id_jogo)
        while True:
            resposta = str(input('Gostaria de alterar o status de finalizado de mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('[#ERRO#] Opção inválida! Por favor digite uma opção válida! Opções válidas: [S/N]')

def excluirJogo():
    verJogoSemParametro()
    condition = True
    while condition:
        while True:
            try:
                id_jogo = int(input('Insira o ID do jogo que deseja excluir: '))
            except(ValueError, TypeError):
                print('[#ERRO#] Valor inválido! Por favor, digite um numero Inteiro!')
            else:
                break
        bd.delJogo(id_jogo)
        while True:
            resposta = str(input('Gostaria de excluir mais um jogo?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('[#ERRO#] Opção inválida! Por favor digite uma opção válida! Opções válidas: [S/N]')

def cadastrarUsuario():    
    condition = True
    while condition:
        existe = int(0)
        validar = True
        while validar:
            while True:
                user = str(input('Digite seu nome de usuario: ')).strip()
                if not user:
                    print('[#ERRO#] O nome de usuario não pode estar vazio!')
                else:
                    break
            for dado in bd.exibeJogador():
                usuariocomparar = str(dado[1])
                if(usuariocomparar == user):
                    print('Este nome de usuario já está em uso! \nPor favor, digite um novo nome de usuario!')
                    existe = 1
                    validar = True
                    break
                else:
                    existe = 0
                    validar = False
            if(existe == 0):
                validar = False
            elif(existe == 1):
                validar = True
        redigitar = True
        while redigitar:
            while True:
                senha = str(input('Digite uma senha de 8 a 12 caracteres: '))
                if not senha:
                    print('ERRO! O nome do jogo não pode estar vazio!')
                elif(len(senha) > 12):
                    print('A senha pode ter no maximo 12 caracteres!')
                elif(len(senha) < 8):
                    print('A senha tem que ter no mínimo 8 caracteres!')
                else:
                    break
            senhacomparar = senha
            t = 3
            for i in range(3):
                t = t-1
                reescrever = str(input('Digite novamente sua senha: '))
                if(senhacomparar == reescrever):
                    redigitar = False
                    bd.inserirUser(user, senha)
                    break
                else:
                    if(t > 0):
                        print(f'As senhas não correspondem.\n Mais {t} tentativas!')
                        redigitar = True
                    elif(t == 0):
                        print('Você tentou validar sua senha muitas vezes!\n Digite uma nova.\n')
                        resgistrar = True
        while True:
            resposta = str(input('Gostaria de adicionar mais um usuario?: ')).lower()
            if(resposta == 's' or resposta == 'sim'):
                condition = True
                break
            elif(resposta == 'n' or resposta == 'nao' or resposta == 'não'):
                condition = False
                break
            else:
                print('[#ERRO#] Opção inválida! Por favor digite uma opção válida! Opções válidas: [S/N]')

def validarUsuario():
    condition = True
    while condition:
        incorreto = int(0)
        validar = True
        while validar:
            if(incorreto == 1):
                print('[#ERRO#] Usuario ou senha incorreto(s)! Por favor, digite novamente!')
            elif(incorreto == 0):
                print('Entre com seu usuario e com sua senha!\n')
            while True:
                user = str(input('Digite seu nome de usuario: '))
                if not user:
                    print('ERRO! O nome de usuario não pode estar vazio!')
                else:
                    break
            while True:
                senha = str(input('Digite sua senha: '))
                if not senha:
                    print('ERRO! O campo de senha não pode estar vazio!')
                else:
                    break
            for dado in bd.exibeJogador():
                usuariocomparar = str(dado[1])
                senhacomparar = str(dado[2])
                if(usuariocomparar == user and senhacomparar == senha):
                    validar = False
                    print('Você se logou!')
                    id_usuario = int(dado[0])                    
                    break
                else:
                    incorreto = int(1)
                    validar = True        
        men.menu(user, id_usuario, senha)
        condition = False        

def excluirUsuario(id_jogador):
    bd.excluirJogador(id_jogador)