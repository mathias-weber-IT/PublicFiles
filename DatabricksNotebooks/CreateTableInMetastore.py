from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType, IntegerType 
spark = SparkSession.builder.appName('SparkSession').getOrCreate()

df_bigmac = spark.read.option("header",True) \
     .csv("/mnt/csvfiles/supersize_big-mac-adjusted-index.csv")

df_bigmac.write.mode("overwrite").saveAsTable("bigmacdata")
