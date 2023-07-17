#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome, idade, curso, matricula):
    db.cur.execute("""
                   INSERT into public.tbAluno (nome, idade, curso, matricula)
                   VALUES ('%s','%s','%s','%s')
                   """ % (nome, idade, curso, matricula))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM tbAluno
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para excluir registro no banco de dados
def excluir(nome):
    db.cur.execute("""
                    DELETE FROM into public.tbAluno WHERE ('%s')
                   """ % (nome))
    
    db.con.commit()
                   