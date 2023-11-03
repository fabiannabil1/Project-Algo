import pandas as pd
import os

def clear_console():
     os.system('cls')

def Kategori_transaksi():
    with open('Data kategori.csv','r') as kategori_transaksi:
         kategori = kategori_transaksi.read()
         kategori = kategori.split(',')
    data_kategori = { "Kategori" : kategori}
    data_kategori = pd.DataFrame(data_kategori)
    print(data_kategori)

def Catat_Debit():
        Debit = [
                input('Masukkan Nama Transaksi :'),
                Kategori_transaksi(),
                input('Masukkan Tipe Transaksi :'),
                input('Masukkan Nominal Transaksi :')]  
        tambah_debit = f"{Debit[0]},{Debit[2]},{Debit[3]}\n"

        with open('Data Debit.csv','a') as debit:
            debit.write(tambah_debit)
        debit.close()
        print('Berhasil disimpan!')
        input('enter untuk melanjutkan...')

def Catat_Kredit():
        Kredit = [
                input('Masukkan Nama Transaksi :'),
                Kategori_transaksi(),
                input('Masukkan Tipe Transaksi :'),
                input('Masukkan Nominal Transaksi :')]  
        tambah_kredit = f"{Kredit[0]},{Kredit[2]},{Kredit[3]}\n"

        with open('Data Kredit.csv','a') as kredit:
            kredit.write(tambah_kredit)
        kredit.close()
        print('Berhasil disimpan!')
        input('enter untuk melanjutkan...')

def Catat_Utang():
        utang = [
                input('Masukkan Nama Transaksi :'),
                Kategori_transaksi(),
                input('Masukkan Tipe Transaksi :'),
                input('Masukkan Nominal Transaksi :')]  
        tambah_utang = f"{utang[0]},{utang[2]},{utang[3]}\n"

        with open('Data Utang.csv','a') as utang:
            utang.write(tambah_utang)
        utang.close()
        print('Berhasil disimpan!')
        input('enter untuk melanjutkan...')

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