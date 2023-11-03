import os
import pandas as pd

def clear_console():
    os.system('cls')

def Catat_Debit():
    Debit = [input('Masukkan Nama Transaksi :'),
             input('Masukkan Tipe Transaksi :'),
             input('Masukkan Nominal Transaksi :')]  
    tambah_debit = f"{Debit[0]},{Debit[1]},{Debit[2]}"
    with open('Data Debit.csv','a',newline='\n') as debit:
        debit.write(tambah_debit)
    debit.close()

def Catat_Kredit():
    Kredit = [input('Masukkan Nama Transaksi :'),
             input('Masukkan Tipe Transaksi :'),
             input('Masukkan Nominal Transaksi :')]
    tambah_kredit = f"{Kredit[0]},{Kredit[1]},{Kredit[2]}"
    with open('Data Kredit.csv','a',newline='\n') as kredit:
        kredit.write(tambah_kredit)
    kredit.close()

def Catat_Utang():
    Utang = [input('Masukkan Nama Transaksi :'),
             input('Masukkan Tipe Transaksi :'),
             input('Masukkan Nominal Transaksi :')]
    tambah_utang = f"{Utang[0]},{Utang[1]},{Utang[2]}"
    with open('Data Utang.csv','a',newline='\n') as utang:
        utang.write(tambah_utang)
    utang.close()

while True:
    clear_console()
    with open('GUI Catat.txt','r') as pilihan_catat:
        pilih_fitur = pilihan_catat.read()
        print(pilih_fitur)
    pilihan_fitur = int(input('Masukkan Pilihan Anda :'))
    match pilihan_fitur:
        case 1 :
            Catat_Debit()
        case 2 :
            Catat_Kredit()
        case 3 :
            Catat_Utang()
        case 4 :
            print('salah input')
