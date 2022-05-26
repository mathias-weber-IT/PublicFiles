# Databricks notebook source
# DBTITLE 1,Read XML file as string
xml_file = open('/dbfs/mnt/xmlfiles/NestedXML.xml').read()
print(xml_file)

# COMMAND ----------

# DBTITLE 1,Put XML file string into pandas dataframe
import pandas as pd

data = {'Index': [i for i in range(1)],
	'XML': [xml_file for i in range(1)]}

df_string = pd.DataFrame(data)

# COMMAND ----------

# DBTITLE 1,Convert XML file string to binary format, zip the binary and put the result into a pandas dataframe
import gzip

b_xml_file = xml_file.encode('utf-8')
compressed_xml_file = gzip.compress(b_xml_file)

data = {'Index': [i for i in range(1)],
	'XML': [compressed_xml_file for i in range(1)]}

df_compressed = pd.DataFrame(data)

# COMMAND ----------

print(xml_file)

# COMMAND ----------

print(b_xml_file)

# COMMAND ----------

print(compressed_xml_file)

# COMMAND ----------

# DBTITLE 1,Put binary into pandas dataframe
data = {'Index': [i for i in range(1)],
	'XML': [b_content for i in range(1)]}

df_binary = pd.DataFrame(data)

# COMMAND ----------

# DBTITLE 1,Convert pandas dataframes to pyspark dataframes
sparkDF_compressed = spark.createDataFrame(df_compressed)
sparkDF_binary = spark.createDataFrame(df_binary)
sparkDF_string = spark.createDataFrame(df_string)

# COMMAND ----------

# DBTITLE 1,Create SQL tables for pyspark dataframes
sparkDF_compressed.write.mode("overwrite").saveAsTable("CompressedFiles")
sparkDF_binary.write.mode("overwrite").saveAsTable("BinaryFiles")
sparkDF_string.write.mode("overwrite").saveAsTable("StringFiles")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM StringFiles

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM BinaryFiles

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM CompressedFiles
