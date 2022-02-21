# Databricks notebook source
from pyspark import SparkConf, SparkContext

# COMMAND ----------

conf = SparkConf().setAppName("Read File")

# COMMAND ----------

sc = SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

text = sc.textFile("/FileStore/tables/sample.txt")

# COMMAND ----------

print(text)
#O/P - /FileStore/tables/sample.txt MapPartitionsRDD[1] at textFile at NativeMethodAccessorImpl.java:0

# COMMAND ----------

print(text.collect())
#O/P - ['1 2 3 4', '11 22 33 44', '111 22']

# COMMAND ----------


