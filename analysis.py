# import sqlite3
# import pandas as pd

# conn = sqlite3.connect("royalty.db")
# df = pd.read_sql("SELECT * FROM royalties", conn)

# print (df.groupby("source") ["amount"].sum())
# print (df.groupby("period")["amount"].sum().head())

import sqlite3
import pandas as pd

# connect ke database
# kita mau melakuakn query dari tabel royalties dan songs, dimana kita mau hitung genre ada berapa lagu, lagu total dan rata ratanya

conn = sqlite3.connect("royalty.db")
df = pd.read_sql("""
                select s.genre, 
                count(distinct s.song_id) as jumlah_lagu,
                round(sum(r.amount)) as total,
                round(sum(r.amount)) / count(distinct s.song_id) as rata_per_lagu
                from royalties r
                join songs s on s.song_id = r.song_id
                group by s.genre
                order by rata_per_lagu Desc;
                 """,conn)

# print(df.groupby("genre")["jumlah_lagu"].sum())
print (df)