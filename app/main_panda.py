import datetime
import uuid
import logging
import dateutil.utils
import pyarrow as pa
import pyarrow.parquet as pq
import datetime as dt

from sqlalchemy import create_engine
import codecs
import pandas as pd

try:
    mydb = create_engine('mysql+mysqlconnector://root:password@127.0.0.1:3306/nome_banco', echo=True)

    query = "Select * from pessoa;"
    result_dataFrame = pd.read_sql(query, mydb)
    df = pd.DataFrame(result_dataFrame)

    print(df)



    df["id_binary"] = list(map(lambda x: str(uuid.UUID(int=int.from_bytes(x, 'big'))), df["id_binary"]))
    today = dateutil.utils.today()
    delta = dt.timedelta(days=1)
    umdiaantes = today - delta
    print(today)
    print(umdiaantes)

    anomesdia = umdiaantes.strftime("%y%m%d")
    print(anomesdia)
    df["anomesdia"] = anomesdia


    df.to_parquet('df.parquet', partition_cols=["anomesdia"])

    df_parquet = pd.read_parquet('df.parquet')

    print(df_parquet)

    #mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))
