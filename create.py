from conectar import cursor, conexao

def inserir_numeros(conc, n1, n2, n3, n4, n5, n6):
    try:
        inserir_numeros = f"""INSERT INTO jogos(concurso, n1, n2, n3, n4, n5, n6)
        values
        ('{conc}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}', '{n6}');"""
        cursor.execute(inserir_numeros)
        conexao.commit()
    except:
        print('Error! Não foi possivel adiconar o(s) número(s). Tente novamente.')