import pandas as pd

tipe = 0 
df_kategori = pd.read_csv('Data kategori.csv')
tipe_transaksi = df_kategori.iloc[tipe,0]
print(tipe_transaksi)

list = [tipe_transaksi,'Makan']
print(list)