import uuid

from sqlalchemy import create_engine
import codecs
import pandas as pd
try:
    mydb = create_engine('mysql+mysqlconnector://root:password@127.0.0.1:3306/nome_banco', echo=True)

    #mydb = connection.connect(host="localhost", database = 'nome_banco',user="root", passwd="password",use_pure=True)
    query = "Select * from pessoa;"
    result_dataFrame = pd.read_sql(query,mydb)
    df = pd.DataFrame(result_dataFrame)
    endereco = ["Rua Joaquim leal", "Rua impata", "rua Guarulhos"]
    df["endereco"] = endereco
    df["mais_velho"] = df["idade"] * 5
    UUID = uuid.uuid4()
    df["new_id"] = UUID
    df["byte"] = UUID.bytes
    df["binary_to_uuid"] = list(map(lambda x: uuid.UUID(int=int.from_bytes(x)), df["byte"]))

    print(df["new_id"], df["binary_to_uuid"])
    #mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))