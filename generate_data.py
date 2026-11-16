# import random
# import sqlite3
# import pandas as pd
# from faker import Faker

# fake = Faker("id_ID")
# random.seed(42)

# # 1. table lagu
# songs = pd.DataFrame({
#     "song_id":range(1,201),
#     "title":[fake.sentence(nb_words=3).rstrip(".") for _ in range(200)],
#     "writer":[fake.name() for _ in range(200)],
#     "genre":[random.choice(["Pop","Rock","Dangdut","Jazz","Indie"]) for _ in range(200)],
# })

# # 2. table royalti: 200 lagu x 12 bulan x 3 jenis pendapatan
# rows = []
# for song_id in ["song_id"]:
#     for month in pd.date_range("2025-01-01", periods=12, freq="MS"):
#         for source in ["Streaming","Radio","Live Performance"]:
#             rows.append({
#                 "song_id": song_id,
#                 "period" : month.strftime("%Y-%m"),
#                 "source" : source,
#                 "amount" : round(random.uniform(10_000,5_000_000),2),
#             })
# royalties = pd.DataFrame(rows)

# # simpan ke sqlite
# conn = sqlite3.connect("royalty.db")
# songs.to_sql("songs", conn, if_exists="replace", index=False)
# royalties.to_sql("royalties", conn,if_exists="replace", index=False)            
# conn.close()

# print(f"Selesai: {len(songs)} lagu, {len(royalties)} royalti disimpan ke royalty.db")
import random
import sqlite3
import pandas as pd
from faker import Faker

fake = Faker("id_ID")
random.seed(42) # untuk membuat data acak yang sama setiap kadli dijalankan

# create table lagu
songs = pd.DataFrame({
    "song_id": range(1,201),
    "title": [fake.sentence(nb_words=3).rstrip(".") for _ in range(200)],
    "writer": [fake.name() for _ in range(200)],
    "genre" : [random.choice(["pop","Rock","Dangdut","Jazz","Indie"]) for _ in range(200)],
})

# tabel royalti: 200 lagu x 12 bulan x 3 jenis pendapatan
rows = []
for song_id in songs["song_id"]:
    for month in pd.date_range("2026-01-01", periods = 12, freq="MS"):
        for source in ["Streaming","Radio","Live Performance"]:
            rows.append({
                "song_id" : song_id,
                "period" : month.strftime("%Y-%m"),
                "source" : source,
                "amount" : round(random.uniform(10_000, 5_000_000), 2),
            })
royalties = pd.DataFrame(rows) # ambil dari rows = []

# simpan ke sqlite
conn = sqlite3.connect("royalty.db")
songs.to_sql("songs", conn, if_exists="replace", index = False) # to_sql disini untuk memnidahkan data frame pandas menjadi table di sqlite
royalties.to_sql("royalties", conn, if_exists="replace", index = False)
conn.close()

print (f"Done: {len(songs)} songs, {len(royalties)} baris royalty")           