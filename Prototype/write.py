import pandas as pd

a =input('Nama :')
b =input('Kategori :')
c =input('Nominal :')
simpan = {'Nama' : [a], 'Kategori' : [b], 'Nominal' : [c]}
simpan = pd.DataFrame(simpan)
files = 'Data Debit.csv'
with open(files,'a') as file:
    file.write(simpan)