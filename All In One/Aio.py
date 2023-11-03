import os
import pandas as pd

def clear_console():
        os.system('cls')

def Login_pengguna():
    def Register():
        regist =[input('Masukan Nama Anda\t:'),
                input('Masukkan Pekerjaan Anda\t:'),
                input('Masukkan Username\t:'),
                input('Masukkan Password\t:')]
        with open('login.csv','w') as register:
            user_data = f"{regist[0]},{regist[1]},{regist[2]},{regist[3]}"
            register.write(user_data)
        register.close()
        yakin_tidak = input('Apakah anda yakin? (y/t):')
        if yakin_tidak == 'y':
            print('Username dan Password tersimpan')
            input('enter untuk melanjutkan')
        else:
            Register()

    def login_user(username,password):
        with open('login.csv','r') as file:
            data = file.read()
            data = data.split(',')
            if username == data[2] and password == data[3]:
                print('Login Berhasil')
            else:
                print('Login Gagal')
            input('enter untuk melanjutkan..')
            Fitur_Fitur()

    def ganti_userpass():
        clear_console()
        check =[input('Masukkan Username Lama :'),
                input('Masukkan Password Lama :')]
        with open('login.csv','r') as file:
            data_user = file.read()
            data_user = data_user.split(',')
            if check[0] == data_user[2] and check[1] == data_user[3]:
                akun_baru = [input('Masukkan Username baru :'),
                            input('Masukkan Password baru :')]
                with open('login.csv','w') as user_baru:
                    simpan_baru = f'{data_user[0]},{data_user[1]},{akun_baru[0]},{akun_baru[1]}'
                    user_baru.write(simpan_baru)
            else:
                print('Username atau Password yang anda masukkan salah')
                print('1. Kembali ke login')
                print('2. Ulangi mengubah akun')
                pilihan_ubah = int(input('Ketikkan pilihan anda :'))
                match pilihan_ubah:
                    case 1:
                        exit
                    case 2:
                        ganti_userpass()
                    case _ :
                        exit

    while True:
        with open('login.csv','r') as lihat:
            a = len(lihat.readlines())
            if a == 0:
                with open('Tampilan Register.txt','r') as registers:
                    register_gui = registers.read()
                    print(register_gui)
                Register()
            else:
                clear_console()
                with open('Tampilan Login.txt','r') as gui:
                    first_gui = gui.read()
                    print(first_gui)
                with open('login.csv','r') as welcomings:
                    welcoming = welcomings.read()
                    Profil_Pengguna = welcoming.split(',')
                    welcome = f"{'Selamat Datang'} {Profil_Pengguna[0]}"
                    print(f"{welcome:^68}")
                pilihan_awal = (input('Ketikkan Pilihan Anda\t:'))
                match pilihan_awal:
                    case '1' :
                        username_login = [input('Masukkan Username\t:'),
                                        input('Password \t\t:')]
                        login_user(username_login[0],username_login[1])
                    case '2' :
                        ganti_userpass()
                    case '3' :
                        clear_console()
                        break
                    case _ :
                        pass

def Fitur_Fitur():
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


while True:
    # Login_pengguna()
    Fitur_Fitur()