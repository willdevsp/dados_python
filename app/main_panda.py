import datetime
import uuid

import dateutil.utils
import pyarrow as pa
import pyarrow.parquet as pq

from sqlalchemy import create_engine
import codecs
import pandas as pd

try:
    mydb = create_engine('mysql+mysqlconnector://root:password@127.0.0.1:3306/nome_banco', echo=True)

    print(uuid.uuid4())

    #mydb = connection.connect(host="localhost", database = 'nome_banco',user="root", passwd="password",use_pure=True)
    query = "Select * from pessoa;"
    result_dataFrame = pd.read_sql(query, mydb)
    df = pd.DataFrame(result_dataFrame)

    print(df)

    df["id_binary"] = list(map(lambda x: str(uuid.UUID(int=int.from_bytes(x))), df["id_binary"]))
    df["ano"] = dateutil.utils.today().strftime("%y")
    df["mes"] = dateutil.utils.today().strftime("%m")
    df["dia"] = dateutil.utils.today().strftime("%d")
    print(df)

    df.to_parquet('df.parquet', partition_cols=["ano", "mes", "dia"],
                  compression='gzip')

    df_parquet = pd.read_parquet('df.parquet')

    print(df_parquet)

    #mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))
