import sqlite3

conn = sqlite3.connect('trabjogospy/Databd.bd')
cursor = conn.cursor()

def criaTabelaJogo():
    conn.execute("""CREATE TABLE IF NOT EXISTS jogo(
                    id_jogo INTEGER PRIMARY KEY AUTOINCREMENT,
                    user txt NOT NULL,         
                    nome TEXT NOT NULL,
                    horajogo FLOAT NOT NULL,
                    conquistas INT,
                    fim INT,
                    data txt NOT NULL)""")
    
def inserirJogo(user,nome,horajogo,conquistas,fim,data):
    conn.execute('INSERT INTO jogo (user,nome,horajogo,conquistas,fim,data) values(?,?,?,?,?,?)',(user,nome,horajogo,conquistas,fim,data))
    conn.commit()  
    
def exibeJogo():
    return conn.execute('SELECT * FROM jogo')

def attNomeJogo(nome,id_jogo):
    conn.execute('UPDATE jogo SET nome = ? where id_jogo = ? ' ,(nome,id_jogo))
    conn.commit()
    
def attHoraJogo(horajogo,id_jogo):
    conn.execute('UPDATE jogo SET horajogo = ? where id_jogo = ? ',(horajogo,id_jogo))
    conn.commit()
    
def attConquistaJogo(conquistas,id_jogo):
    conn.execute('UPDATE jogo SET conquistas = ? where id_jogo = ? ' ,(conquistas,id_jogo))
    conn.commit()
    
def attFinalizadoJogo(fim,id_jogo):
    conn.execute('UPDATE jogo SET fim = ? where id_jogo = ? ' ,(fim,id_jogo))
    conn.commit()
    
def delJogo(id_jogo):
    conn.execute('DELETE FROM jogo WHERE id_jogo = ? ',(id_jogo, ))  
    conn.commit()
    
def criarTabelaJogador():
    conn.execute("""CREATE TABLE IF NOT EXISTS jogador(
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,         
                    user TEXT NOT NULL,
                    senha VARCHAR(12) NOT NULL)""")   

def inserirUser(user,senha):
    conn.execute('INSERT INTO jogador (user, senha) values(?,?)',(user,senha))
    conn.commit()

def exibeJogador():
    return conn.execute('SELECT * FROM jogador')

def attNomeJogador(user,id_usuario):
    conn.execute('UPDATE jogador SET user = ? where id_usuario = ? ' ,(user,id_usuario))
    conn.commit()

def attSenhaJogador(senha,id_usuario):
    conn.execute('UPDATE jogador SET senha = ? where id_usuario = ? ' ,(senha,id_usuario))
    conn.commit()

def delJogador(id_usuario):
    conn.execute('DELETE FROM jogador WHERE id_usuario = ? ',(id_usuario, ))  
    conn.commit()
