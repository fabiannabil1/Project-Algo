import os

def clear_console():
    os.system('cls')

def login_user(username,password):
    with open('login.csv','r') as file:
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
    with open('login.csv','r') as file:
        data_user = file.read()
        data_user = data_user.split(',')
        if check[0] == data_user[0] and check[1] == data_user[1]:
            akun_baru = [input('Masukkan Username baru :'),
                         input('Masukkan Password baru :')]
            with open('login.csv','w') as user_baru:
                simpan_baru = f'{akun_baru[0]},{akun_baru[1]}'
                user_baru.write(simpan_baru)
        else:
            print('Username atau Password yang anda masukkan salah')
            print('1. Kembali ke login')
            print('2. Ulangi mengubah akun')
            pilihan_ubah = int(input('Pilihan anda :'))
            match pilihan_ubah:
                case 1:
                    exit
                case 2:
                    ganti_userpass()
                case _ :
                    exit

while True:
    clear_console()
    with open('Tampilan Login.txt','r') as gui:
        first_gui = gui.read()
        
        print(first_gui)

    pilihan_awal = int(input('Ketikkan Pilihan Anda\t:'))
    match pilihan_awal:
        case 1 :
            username_login = [input('Masukkan Username\t:'),
                              input('Password \t\t:')]
            login_user(username_login[0],username_login[1])
        case 2 :
            ganti_userpass()
        case 3 :
            clear_console()
            break