from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import SparkSession

# Inicializa o Spark Session
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Conecta ao banco de dados
jdbc_url = "jdbc:postgresql://your-database-url:5432/your-database"
username = "your-username"
password = "your-password"
db_table = "your-table"
partition_column = "date"


# Cria um DynamicFrame a partir dos dados do banco de dados
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="postgresql",
    connection_options={"url": jdbc_url, "user": username, "password": password, "dbtable": db_table}
)

# Converte o DynamicFrame para um DataFrame
data_frame = dynamic_frame.toDF()

# Salva o DataFrame no Amazon S3
data_frame.write.mode("overwrite").partitionBy(partition_column).parquet("s3://your-bucket/your-output-path/")

