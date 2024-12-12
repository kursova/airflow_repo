import pandas as pd

file_path = "dirty_store_transactions.csv"
df = pd.read_csv(file_path)

df["STORE_LOCATION"] = df["STORE_LOCATION"].str.strip()  
df["STORE_LOCATION"] = df["STORE_LOCATION"].str.replace(r"[^\w\s]", "", regex=True)  

df["PRODUCT_ID"] = df["PRODUCT_ID"].str.replace(r"[^\w\s]", "", regex=True)  

df.fillna({
    "MRP": df["MRP"].mean(), 
    "SP": df["SP"].mean(),   
}, inplace=True)

df.drop_duplicates(inplace=True)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")  
df.dropna(subset=["Date"], inplace=True)  

clean_file_path = "clean_store_transactions.csv"
df.to_csv(clean_file_path, index=False)

print(f"Temizlenmiş veri {clean_file_path} dosyasına kaydedildi.")