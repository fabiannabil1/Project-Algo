import pandas as pd


def Baca_Saldo():
    def Total_Debit():
        df_Debit = pd.read_csv('Data Debit.csv')
        panjang_index = len(df_Debit.index)
        total_debit = df_Debit.iloc[0:panjang_index,2]
        total_debit = total_debit.sum()
    def Total_Kredit():
        df_Debit = pd.read_csv('Data Kredit.csv')
        panjang_index = len(df_Debit.index)
        total_kredit = df_Debit.iloc[0:panjang_index,2]
        total_kredit = total_kredit.sum()
    def Total_Utang():
        df_Debit = pd.read_csv('Data Debit.csv')
        panjang_index = len(df_Debit.index)
        total_utang = df_Debit.iloc[0:panjang_index,2]
        total_utang = total_utang.sum()

Baca_Saldo()