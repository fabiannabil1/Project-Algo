import csv
import pandas as pd

b = input()
a = pd.read_csv('Data Debit.csv')
# print(a)
if b == (a.loc[2,'Kategori']):
    print('benar')
else:
    print('salah')