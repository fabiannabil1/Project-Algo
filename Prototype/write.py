import pandas as pd 


def Edit_data():
    def edit_debit():
        data_debit = pd.read_csv('Data Debit.csv')
        print(f"{'-=-=-=-=-=Data Debit Anda=-=-=-=-=-':^68}")
        print(data_debit)
        print('Pilih pengeditan yang akan dilakukan :')
        print(f"{'1. Hapus Baris'}\n{'2. Kembali'}")
        pilihan_edit = input('Masukkan Pilihan (Nomor) : ')
        if pilihan_edit == '1' or pilihan_edit == '2':
            if pilihan_edit == '1':
                print('Mode Hapus Baris')
                pilihan_baris = int(input('Nomor baris yang akan dihapus : '))
                if pilihan_baris > (len(data_debit.index)-1):
                    print('Pilihan melebihi banyak baris....')
                    input('Enter untuk mengulang..')
                    edit_debit()
                else:
                    data_debit = data_debit.drop(pilihan_baris)
                    data_debit.index = range(0,len(data_debit))
                    data_debit.to_csv('Data Debit.csv',index= False)
                    print('Data Terupdate')
                    print(data_debit)
                    edit_debit()
            else:
                Edit_data()
        else:
            edit_debit()

    def edit_kredit():
        data_kredit = pd.read_csv('Data Kredit.csv')
        print(f"{'-=-=-=-=-=Data Kredit Anda=-=-=-=-=-':^68}")
        print(data_kredit)
        print('Pilih pengeditan yang akan dilakukan :')
        print(f"{'1. Hapus Baris'}\n{'2. Kembali'}")
        pilihan_edit = input('Masukkan Pilihan (Nomor) : ')
        if pilihan_edit == '1' or pilihan_edit == '2':
            if pilihan_edit == '1':
                print('Mode Hapus Baris')
                pilihan_baris = int(input('Nomor baris yang akan dihapus : '))
                if pilihan_baris > (len(data_kredit.index)-1):
                    print('Pilihan melebihi banyak baris....')
                    input('Enter untuk mengulang..')
                    edit_kredit()
                else:
                    data_kredit = data_kredit.drop(pilihan_baris)
                    data_kredit.index = range(0,len(data_kredit))
                    data_kredit.to_csv('Data Kredit.csv',index= False)
                    print('Data Terupdate')
                    print(data_kredit)
                    edit_kredit()
            else:
                Edit_data()
        else:
            edit_kredit()

    def edit_utang():
        data_utang = pd.read_csv('Data Utang.csv')
        print(f"{'-=-=-=-=-=Data Utang Anda=-=-=-=-=-':^68}")
        print(data_utang)
        print('Pilih pengeditan yang akan dilakukan :')
        print(f"{'1. Hapus Baris'}\n{'2. Kembali'}")
        pilihan_edit = input('Masukkan Pilihan (Nomor) : ')
        if pilihan_edit == '1' or pilihan_edit == '2' :
            if pilihan_edit == '1':
                print('Mode Hapus Baris')
                pilihan_baris = int(input('Nomor baris yang akan dihapus : '))
                if pilihan_baris > (len(data_utang.index)-1):
                    print('Pilihan melebihi banyak baris....')
                    input('Enter untuk mengulang..')
                    edit_utang()
                else:
                    data_utang = data_utang.drop(pilihan_baris)
                    data_utang.index = range(0,len(data_utang))
                    data_utang.to_csv('Data Utang.csv',index= False)
                    print('Data Terupdate')
                    print(data_utang)
                    edit_utang()
            else:
                Edit_data()
        else:
            edit_utang()
    
    print(f"{'Pilih pengeditan yang akan dilakukan'}\n{'1. Debit'}\n{'2. Kredit'}\n{'3. Utang'}\n{'4. Kembali'}")
    pilihan_edit_data = input('Ketikkan pilihan (Nomor) :')
    if pilihan_edit_data == '1' or pilihan_edit_data == '2' or pilihan_edit_data == '3' or pilihan_edit_data ==  '4':
        if pilihan_edit_data == '1':
            edit_debit()
        elif pilihan_edit_data == '2':
            edit_kredit()
        elif pilihan_edit_data == '3':
            edit_utang()
        else:
            #menu fitur
            pass
    else:
        Edit_data()

Edit_data()