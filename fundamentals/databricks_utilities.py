# Databricks notebook source
# MAGIC %fs
# MAGIC ls

# COMMAND ----------

dbutils.fs.ls('/')


# COMMAND ----------

for folder in dbutils.fs.ls('/'):
    print(folder)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.help('mount')

# COMMAND ----------

dbutils.notebook.run("./databricks_child",10, {"input":"Called from main notebook"})

# COMMAND ----------

# MAGIC %pip install pandas

# COMMAND ----------


