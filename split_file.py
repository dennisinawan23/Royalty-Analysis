import sqlite3
from pathlib import Path
import pandas as pd

conn = sqlite3.connect("royalty.db")
df = pd.read_sql("SELECT * FROM royalties",conn)
conn.close()

