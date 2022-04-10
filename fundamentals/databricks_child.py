# Databricks notebook source
dbutils.widgets.text("input", "", "Enter Parameter here")

# COMMAND ----------

input_params = dbutils.widgets.get("input")

# COMMAND ----------

print(input_params)

# COMMAND ----------

dbutils.notebook.exit(100)

# COMMAND ----------


