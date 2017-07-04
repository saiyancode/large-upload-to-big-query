import pandas as pd
from pandas.io.gbq import read_gbq, to_gbq
import sqlite3
import time
import glob
import os

projectid = PROJECT_ID
dataset_table = DATASET.TABLE

# Load all to memory and insert into Big Query

df = pd.read_csv('filename.csv', encoding='utf-8')

to_gbq(df, dataset_table, projectid ,chunksize=10000, if_exists='append')

# Read CSV in chunks (500k rows) and upload 10k at a time

for chunk in pd.read_sql_query("SELECT * FROM TABLE_NAME", con=con, chunksize=500000):
    df = chunk
    to_gbq(df, dataset_table, projectid, chunksize=10000, if_exists='append')



