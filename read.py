from conectar import cursor
from prettytable import PrettyTable


def listar_numeros():
    sql = 'Select * from jogos'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    tabela = PrettyTable()
    tabela.field_names = ['ID', 'Concurso', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6']

    for linha in linhas:
        tabela.add_row(linha)
    print(tabela)


def listar_numeros_no():
    sql = 'Select * from jogos'
    cursor.execute(sql)