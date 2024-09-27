import os
import sqlite3
from sqlite3 import *


def ConexaoBanco():
    caminho = "C:\\Users\\user\\Desktop\\João\\Projetos\\Python\\Agenda de Contatos\\Banco\\agenda"
    con=None
    try:
        con = sqlite3.connect(caminho)
    except Error as error:
        print(error)
    return con


vcon = ConexaoBanco()


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as error:
        print(error)
    finally:
        print("Operação Realizada com Sucesso")


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado
    

def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registros")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")


def menuInserir():
    os.system("cls")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    vsql = "INSERT INTO contatos (NOMECONTATO, TELEFONECONTATO, EMAILCONTATO) VALUES('"+nome+"', '"+telefone+"', '"+email+"')"
    query(vcon, vsql)


def menuDeletar():
    os.system("cls")
    id = input("Digite o nome do id do contato a ser deletado: ")
    vsql = "DELETE FROM contatos WHERE IDCONTATO ="+id
    query(vcon, vsql)


def menuAtualizar():
    os.system("cls")
    id = input("Digite o ID do contato a ser alterado: ")
    r = consultar(vcon,"SELECT * FROM contatos WHERE IDCONTATO ="+id)
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    if(len(nome) == 0):
        nome = rnome

    if(len(telefone) == 0):
        telefone = rtelefone

    if(len(email) == 0):
        email = remail
    vsql = "UPDATE contatos SET NOMECONTATO = '"+nome+"', TELEFONECONTATO = '"+telefone+"', EMAILCONTATO = '"+email+"' WHERE IDCONTATO ="+id
    query(vcon, vsql)


def menuConsultar():
    vsql = "SELECT * FROM contatos"
    res = consultar(vcon, vsql)
    limite = 10
    cont = 0
    for r in res:
        print("ID:{0:_<3} Nome:{1} Telefone:{2} Email:{3}".format(r[0], r[1], r[2], r[3]))
        cont += 1
        if(cont >= limite):
            cont = 0
            os.system("pause")
            os.system("cls")
    print("Fim da lista")
    os.system("pause")


def menuConsultarNome():
    nome = input("Digite o nome: ")
    vsql = "SELECT * FROM contatos WHERE NOMECONTATO LIKE '%"+nome+"%'"
    res = consultar(vcon, vsql)
    limite = 10
    cont = 0
    for r in res:
        print("ID:{0:_<3} Nome:{1} Telefone:{2} Email:{3}".format(r[0], r[1], r[2], r[3]))
        cont += 1
        if(cont >= limite):
            cont = 0
            os.system("pause")
            os.system("cls")
    print("Fim da lista")
    os.system("pause")


opcao = 0
while opcao != 6:
    menuPrincipal()
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        menuInserir()
    elif opcao == 2:
        menuDeletar()
    elif opcao == 3:
        menuAtualizar()
    elif opcao == 4:
        menuConsultar()
    elif opcao == 5:
        menuConsultarNome()
    elif opcao == 6:
        os.system("cls")
        print("Programa Finalizado")
    else:
        os.system("cls")
        print("Opção Inválida")
        os.system("pause")


vcon.close()
os.system("pause")

