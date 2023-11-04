import os

def clear_console():
    os.system('cls')

def Register():
    regist =[input('Masukan Nama Anda\t:'),
             input('Masukkan Pekerjaan Anda\t:'),
             input('Masukkan Username\t:'),
             input('Masukkan Password\t:')]
    with open('login.csv','w', encoding='utf-8') as register:
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
    with open('login.csv','r', encoding='utf-8') as file:
        data = file.read()
        data = data.split(',')
        if username == data[0] and password == data[1]:
            print('Login Berhasil')
        else:
            print('Login Gagal')
        input('enter untuk melanjutkan..')

def ganti_userpass():
    clear_console()
    check =[input('Masukkan Username Lama :'),
            input('Masukkan Password Lama :')]
    with open('login.csv','r', encoding='utf-8') as file:
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
            with open('Tampilan Register.txt','r', encoding='utf-8') as registers:
                register_gui = registers.read()
                print(register_gui)
            Register()
        else:
            clear_console()
            with open('Tampilan Login.txt','r', encoding='utf-8') as gui:
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
