import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node MySQL
MySQL_node1714590979873 = glueContext.create_dynamic_frame.from_options(
    connection_type = "mysql",
    connection_options = {
        "useConnectionProperties": "true",
        "dbtable": "pessoa",
        "connectionName": "conexao com rds",
    },
    transformation_ctx = "MySQL_node1714590979873"
)

# Script generated for node SQL Query
SqlQuery0 = '''
select uuid_to_bin("id_binary") from myDataSource
'''
SQLQuery_node1714592733880 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"myDataSource":MySQL_node1714590979873}, transformation_ctx = "SQLQuery_node1714592733880")

# Script generated for node Amazon S3
AmazonS3_node1714592906786 = glueContext.write_dynamic_frame.from_options(frame=SQLQuery_node1714592733880, connection_type="s3", format="glueparquet", connection_options={"path": "s3://willbucketwlm/parquet/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1714592906786")

job.commit()