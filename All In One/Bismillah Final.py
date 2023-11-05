import os
import pandas as pd

def clear_console():
        os.system('cls')

def Header():
    with open('Header.txt','r') as header:
        header = header.read()
        print(header)
        
def verifikasi_password(password):

  if len(password) < 8:
    return False
  
  ada_kapital = False
  ada_huruf_kecil = False
  ada_simbol = False
  simbol = "[_@#$%^&*()-]"

  for char in password:
    if char.isalpha():
      if char.islower():
        ada_huruf_kecil = True
      else:
        ada_kapital = True
    elif char in simbol:
      ada_simbol = True

  return ada_huruf_kecil and ada_kapital and ada_simbol

def Login_pengguna():
    def Register():
        def password():
            pilihan_password = input('Buat Password\t\t:')
            if verifikasi_password(pilihan_password):
                regist[3] = pilihan_password
            else:
                print('Password diluar kriteria!')
                print('Minimal 8 karakter, memiliki huruf kecil,kapital ,dan simbol')
                password()

        clear_console()

        with open('Tampilan Register.txt','r',encoding='utf-8') as registers:
                register_gui = registers.read()
                print(register_gui)
                registers.close()
        regist =[input('Masukan Nama Anda\t:'),
                input('Masukkan Pekerjaan Anda\t:'),
                input('Buat Username\t\t:'),'password']
        password()
        yakin_tidak = input('Apakah anda yakin? (y/t):')
        if yakin_tidak == 'y':
            with open('login.csv','w') as register:
                user_data = f"{regist[0]},{regist[1]},{regist[2]},{regist[3]}"
                register.write(user_data)
            print('Username dan Password tersimpan')
            input('enter untuk melanjutkan')
            Login_pengguna()
        else:
            Register()

    def login_user(username,password):
        with open('login.csv','r') as file:
            data = file.read()
            data = data.split(',')
            if username == data[2] and password == data[3]:
                print('Login Berhasil')
                input('enter untuk melanjutkan..')
                Menu_Awal()
            else:
                print('Login Gagal')
                input('Enter untuk login ulang')
                Login_pengguna()

    def ganti_userpass():
        def password():
            pilihan_password = input('Masukkan Password baru :')
            if verifikasi_password(pilihan_password):
                akun_baru[1] = pilihan_password
            else:
                print('Password diluar kriteria!')
                print('Minimal 8 karakter, memiliki huruf kecil,kapital ,dan simbol')
                password()

        clear_console()
        Header()
        check =[input('Masukkan Username Lama :'),
                input('Masukkan Password Lama :')]
        with open('login.csv','r') as file:
            data_user = file.read()
            data_user = data_user.split(',')
            if check[0] == data_user[2] and check[1] == data_user[3]:
                akun_baru = [input('Masukkan Username baru :'),'password']
                password()
                with open('login.csv','w') as user_baru:
                    simpan_baru = f'{data_user[0]},{data_user[1]},{akun_baru[0]},{akun_baru[1]}'
                    user_baru.write(simpan_baru)
                input('Username dan Password telah diubah, enter untuk melanjutkan...')
                Login_pengguna()
            else:
                print('Username atau Password yang anda masukkan salah')
                print('1. Kembali ke login')
                print('2. Ulangi mengubah akun')
                pilihan_ubah = input('Ketikkan pilihan anda :')
                match pilihan_ubah:
                    case '1':
                        Login_pengguna()
                    case '2':
                        ganti_userpass()
                    case _ :
                        Login_pengguna()
    
    with open('login.csv','r') as lihat:
        keadaan_dbs_login = len(lihat.readlines())
        if keadaan_dbs_login == 0:
            Register()
        else:
            clear_console()
            with open('Tampilan Login.txt','r',encoding='utf-8') as gui:
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
                    username_login = [input('Masukkan Username\t:'),input('Password \t\t:')]
                    login_user(username_login[0],username_login[1])
                case '2' :
                    ganti_userpass()
                case '3' :
                    clear_console()
                    exit
                case _ :
                    Login_pengguna()


def Menu_Awal():
    clear_console()
    with open('Menu Awal.txt','r') as gui_menu:
        gui_menu = gui_menu.read()
        print(gui_menu)
        pilihan_menu = input('Ketikkan Pilihan Anda :')
        match pilihan_menu:
            case '1' :
                Fitur_Pencatatan()
            case '2' :
                Baca_Saldo()
            case '3' :
                Edit_data()
                pass
            case '4' :
                profil_pengguna()
            case '5' :
                Login_pengguna()
            case _ :
                Menu_Awal()

def profil_pengguna():
    clear_console()
    Header()
    with open('login.csv','r') as profil:
        profil = profil.read()
        profil = profil.split(',')
        Nama = f"Nama : {profil[0]}"
        Pekerjaan = f"Pekerjaan : {profil[1]}"
        print(f"{'=-=-=-=-=-=Profil=-=-=-=-=-=':^68}")
        print(f"{Nama:^68}")
        print(f"{Pekerjaan:^68}")
    pilihan_edit_profil = input('update profil? (y/t)\t:')
    if pilihan_edit_profil == 'y':
        Nama_baru = input('Masukkan Nama\t\t:')
        Pekerjaan_baru = input('Masukkan Pekerjaan\t:')
        with open('login.csv','r') as baca_profil:
            baca_profil = baca_profil.read()
            baca_profil = baca_profil.split(',')
            baca_profil = f"{Nama_baru},{Pekerjaan_baru},{profil[2]},{profil[3]}"
            with open('login.csv','w') as profil_baru:
                profil_baru.write(baca_profil)
                input('Profil Terupdate, enter untuk melanjutkan...')
        profil_pengguna()
    else:
        Menu_Awal()

def Fitur_Pencatatan():
    clear_console()
    def Kategori_transaksi():
        kategori_kategori = pd.read_csv('Data kategori.csv' )
        print(kategori_kategori)
    def Catat_Debit():
            clear_console()
            Header()
            print(f"{'CATAT DEBIT':^68}")
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
            tambah_lagi = input('Tambah lagi? y/t:')
            if tambah_lagi == 'y':
                Catat_Debit()
            else:
                Fitur_Pencatatan()

    def Catat_Kredit():
            clear_console()
            Header()
            print(f"{'CATAT KREDIT':^68}")
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
            tambah_lagi = input('Tambah lagi? y/t:')
            if tambah_lagi == 'y':
                Catat_Kredit()
            else:
                Fitur_Pencatatan()
    def Catat_Utang():
            clear_console()
            Header()
            print(f"{'CATAT UTANG':^68}")
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
            tambah_lagi = input('Tambah lagi? y/t:')
            if tambah_lagi == 'y':
                Catat_Utang()
            else:
                Fitur_Pencatatan()

    clear_console()
    with open('GUI Catat.txt','r') as pilihan_catat:
        pilih_fitur = pilihan_catat.read()
        print(pilih_fitur)
    pilihan_fitur = input('Masukkan Pilihan Anda :')
    match pilihan_fitur:
        case '1' :
            Catat_Debit()
        case '2' :
            Catat_Kredit()
        case '3' :
            Catat_Utang()
        case '4' :
            Menu_Hapus_Tambah_Kategori()
        case '5' :
            Menu_Awal()
        case _ :
            Fitur_Pencatatan()

def Menu_Hapus_Tambah_Kategori():
    def Menu_Kelola():
        clear_console()
        with open('Hapus Kategori.txt','r') as gui_cat:
            gui_cat = gui_cat.read()
            print(gui_cat)
        pilhan_add_del = input('Pilihan Anda :')
        match pilhan_add_del:
            case '1' :
                Tambah_Kategori()
            case '2' :
                hapus_kategori()
            case '3' :
                Fitur_Pencatatan()
            case _ :
                Menu_Hapus_Tambah_Kategori()

    def Tambah_Kategori():
        clear_console()
        Header()
        frame_cat = pd.read_csv('Data kategori.csv')
        print(frame_cat)
        tambah_kategori = input('Ketikkan Kategori Baru :')
        tambah_kategori = {'Kategori' : tambah_kategori}
        panjang_index = len(frame_cat)
        frame_cat.loc[panjang_index] =  tambah_kategori
        frame_cat.to_csv('Data kategori.csv', index= False)
        print(frame_cat)
        pilihan_cat = input('kategori telah ditambah.. buat kategori baru lagi? y/t :')
        if pilihan_cat == 'y':
            Tambah_Kategori()
        else:
            Menu_Hapus_Tambah_Kategori()

    def hapus_kategori():
        clear_console()
        Header()
        frame_cat = pd.read_csv('Data kategori.csv')
        print(frame_cat)
        panjang_index = len(frame_cat)
        print("Ketikkan Nomor Urut Kategori Untuk Menghapus ")
        print("Apabila Batal Ketik 't' untuk Batal ")
        hapus_cat = input('Kategori yg akan dihapus :')
        hapus_cat_str = str(hapus_cat)
        match hapus_cat_str:
            case 't':
                Menu_Hapus_Tambah_Kategori()
            case _ :
                if int(hapus_cat) <= panjang_index-1:
                    frame_cat = frame_cat.drop(int(hapus_cat))
                    frame_cat.index = range(0,len(frame_cat))
                else:
                    print('Pilihan diluar jangkauan..')
                    input('enter untuk mengulang')
                    hapus_kategori()
                print(frame_cat)
                print('Hapus Lagi? y/t')
                hapus_cat_lagi = input('Pilihan Anda :')
                match hapus_cat_lagi:
                    case 'y':
                        hapus_kategori()
                    case 't':
                        Menu_Hapus_Tambah_Kategori()
                    case _ :
                        Menu_Hapus_Tambah_Kategori()
    
    Menu_Kelola()

def Baca_Saldo():
    # def Total_Debit():
    df_Debit = pd.read_csv('Data Debit.csv')
    panjang_index = len(df_Debit.index)
    total_debit = df_Debit.iloc[0:panjang_index,2]
    total_debit = total_debit.sum()
        # print(total_debit)
    # def Total_Kredit():
    df_Kredit = pd.read_csv('Data Kredit.csv')
    panjang_index = len(df_Kredit.index)
    total_kredit = df_Kredit.iloc[0:panjang_index,2]
    total_kredit = total_kredit.sum()
        # print(total_kredit)
    # def Total_Utang():
    df_Utang = pd.read_csv('Data Utang.csv')
    panjang_index = len(df_Utang.index)
    total_utang = df_Utang.iloc[0:panjang_index,2]
    total_utang = total_utang.sum()
        # print(total_utang)
    
    clear_console()
    Header()
    print(f"{'Laporan Keuangan Anda'}")
    print('Total Pemasukan\t\t\t: Rp.',total_debit)
    print('Total Pengeluaran\t\t: Rp.',total_kredit)
    print('Total Utang\t\t\t: Rp.',total_utang)
    print('Saldo Total\t\t\t: Rp.',total_debit-total_kredit)
    print('Saldo Jika Utang Terbayar\t: Rp.',total_debit-(total_utang+total_kredit))
    input('Enter untuk kembali ke menu')
    Menu_Awal()

def Edit_data():
    def edit_debit():
        clear_console()
        Header()
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
        clear_console()
        Header()
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
        clear_console()
        Header()
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
    
    clear_console()
    Header()
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
            Menu_Awal()
    else:
        Edit_data()

Login_pengguna()
# profil_pengguna()
# Fitur_Pencatatan()