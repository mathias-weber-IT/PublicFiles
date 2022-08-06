import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType, IntegerType
from pyspark.sql.functions import monotonically_increasing_id 
from pyspark.sql.functions import col
spark = SparkSession.builder.appName('SparkSession').getOrCreate()

df = spark.read.option("header",True).csv("/mnt/csvfiles/supersize_big-mac-adjusted-index.csv")
df = df.withColumn("id", monotonically_increasing_id())
df = df.withColumn("id_batch", col("id") % 5000)

df.createOrReplaceTempView("bigmacdata")
