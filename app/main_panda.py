import uuid

from sqlalchemy import create_engine
import codecs
import pandas as pd
try:
    mydb = create_engine('mysql+mysqlconnector://root:password@127.0.0.1:3306/nome_banco', echo=True)

    print(uuid.uuid4())

    #mydb = connection.connect(host="localhost", database = 'nome_banco',user="root", passwd="password",use_pure=True)
    query = "Select * from pessoa;"
    result_dataFrame = pd.read_sql(query,mydb)
    df = pd.DataFrame(result_dataFrame)

    print(df)

    df["uuid_convertido"] = list(map(lambda x: uuid.UUID(int=int.from_bytes(x)), df["id_binary"]))
    print(df)

    #mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))