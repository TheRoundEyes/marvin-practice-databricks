# Databricks notebook source
import pandas as pd
test = "Hello World"

# COMMAND ----------

print(test)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "HELLO"

# COMMAND ----------

# MAGIC %scala
# MAGIC val msg = "hello"

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

# MAGIC %fs
# MAGIC ls dbfs:/databricks-datasets/COVID/USAFacts/

# COMMAND ----------

# MAGIC %fs
# MAGIC head dbfs:/databricks-datasets/COVID/USAFacts/covid_deaths_usafacts.csv

# COMMAND ----------

# MAGIC %sh
# MAGIC ps

# COMMAND ----------


