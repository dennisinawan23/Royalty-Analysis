# import sqlite3
# import pandas as pd

# conn = sqlite3.connect("royalty.db")
# df = pd.read_sql("SELECT * FROM royalties", conn)

# print (df.groupby("source") ["amount"].sum())
# print (df.groupby("period")["amount"].sum().head())

import sqlite3
import pandas as pd

# <<<<<<< HEAD
conn = sqlite3.connect("royalty.db")
royalties = pd.read_sql("SELECT * FROM royalties", conn)
songs = pd.read_sql("SELECT * FROM songs", conn)
conn.close()

print (royalties.shape)

# latihan 2 : total per sumber
print (royalties.groupby("source")["amount"].sum())
# group by ("source")["amount"].sum() --> artinya kita mau mengelompokan baris per sumber, ambil column amount dan jumlahkan per kelompoknya

# latihan 4 : tren bulanan
print (royalties.groupby("period")["amount"].sum())

# latihan 5 : total per genre
gabung = royalties.merge(songs, on="song_id", how="left") # merge(songs, on = :"song_id", how="inner") artinya on menentukan kolom penghubung. Inner hanya menyimpan baris yang cocok di kedua table
print(len(gabung))
print(gabung.groupby("genre")["amount"].sum().sort_values(ascending=False))

# check inner dan left pada on
songs_sebagian = songs[songs["song_id"] <=100]

inner = royalties.merge(songs_sebagian, on="song_id", how="inner")
left = royalties.merge(songs_sebagian, on="song_id", how="left") 

print(len(inner))
print(len(left))
print(left["genre"].isna().sum()) 

# Inner : data yang tidak ada akan dihilangkan
# left : data yang tidak ada akan tetap ada, tapi kolom yang tidak ada akan diisi dengan NaN
                     
                       
                       
                       
                       
# =======
# # connect ke database
# # kita mau melakuakn query dari tabel royalties dan songs, dimana kita mau hitung genre ada berapa lagu, lagu total dan rata ratanya

# conn = sqlite3.connect("royalty.db")
# df = pd.read_sql("""
#                 select s.genre, 
#                 count(distinct s.song_id) as jumlah_lagu,
#                 round(sum(r.amount)) as total,
#                 round(sum(r.amount)) / count(distinct s.song_id) as rata_per_lagu
#                 from royalties r
#                 join songs s on s.song_id = r.song_id
#                 group by s.genre
#                 order by rata_per_lagu Desc;
#                  """,conn)

# # print(df.groupby("genre")["jumlah_lagu"].sum())
# print (df)
# >>>>>>> d9b954de795b0a4d53036809220a746f3c37eca5
