from pathlib import Path
import pandas as pd

folder = Path("output")

bagian = []
for file in sorted(folder.glob("royalty_*.xlsx")):
    bagian.append(pd.read_excel(file))
    
df = pd.concat(bagian, ignore_index=True)
print(len(df), round(df["amount"].sum(), 2))    