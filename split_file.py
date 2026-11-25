# retype again split_file.py
import sqlite3
from pathlib import Path
import pandas as pd

conn = sqlite3.connect("royalty.db")
df = pd.read_sql("SELECT * FROM royalties", conn)
conn.close()

folder = Path("output_1")
folder.mkdir(exist_ok = True)

for sumber, bagian in df.groupby("source"):
    nama = sumber.replace(" ","_")
    path_file = folder / f"royalti_{nama}.xlsx"
    bagian.to_excel(path_file, index=False)
    print(f"{path_file}:{len(bagian)} baris")


# import sqlite3
# from pathlib import Path
# import pandas as pd

# conn = sqlite3.connect("royalty.db")
# df = pd.read_sql("SELECT * FROM royalties",conn)
# conn.close()

# folder = Path("output")
# folder.mkdir(exist_ok=True)

# # disini gropyu by source
# for sumber, bagian in df.groupby("source"):
#     nama = sumber.replace(" ","_")
#     path_file = folder / f"royalti_{nama}.xlsx"
#     bagian.to_excel(path_file, index=False)
#     print(f"{path_file}: {len(bagian)} baris")
    
# #check 
# total_baris = 0
# total_uang = 0
# for file in folder.glob("*.xlsx"):
#     d = pd.read_excel(file)
#     total_baris += len(d)
#     total_uang += d["amount"].sum()
    
# print (total_baris, round(total_uang, 2))    
    