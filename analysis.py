import sqlite3
import pandas as pd

conn = sqlite3.connect("royalty.db")
df = pd.read_sql("SELECT * FROM royalties", conn)

print (df.groupby("source") ["amount"].sum())
print (df.groupby("period")["amount"].sum().head())
