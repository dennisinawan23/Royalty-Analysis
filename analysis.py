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
# pd,option.display.float_format = "{:,.2f}".format                  
single_data = left[left["genre"].isna()] 
print(single_data.head())
print(single_data["song_id"].unique())

# kita check total samas setelah merge
print(royalties["amount"].sum())
print(left["amount"].sum())

# indicator = true utu kita bisa menandai baris yang tidak ada di table songs, tapi ada di table royalties
check = royalties.merge(songs_sebagian, on="song_id", how="left", indicator=True)
print(check["_merge"].value_counts())

                       
                       
                       
 