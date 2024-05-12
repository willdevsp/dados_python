from sqlalchemy import create_engine
from sqlalchemy.sql import text

def getSchemas():
    tabelas = []
    try:
        mydb = create_engine('mysql+mysqlconnector://root:password@127.0.0.1:3306/nome_banco', echo=True)

        query = "show tables;"


        with mydb.connect() as conn:
            result = conn.execute(text(query))
            for row in result:
                tabelas.append({"nome": row[0]})

            for tabela in tabelas:
                sql = f'desc {tabela["nome"]}'
                resultCampos = conn.execute(text(sql))

                campos = []
                for campo in resultCampos:
                    j = {
                        "Field": campo[0],
                        "Type": campo[1],
                        "Null": campo[2],
                        "Key": campo[3],
                        "Default": str(campo[4]),
                        "Extra": campo[5]
                    }
                    print(j)
                    campos.append(j)

                tabela["campos"] = campos
    except Exception as e:
        conn.close()
        print('ERRO',str(e))

    return tabelas


getSchemas()