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

def Register():
    def password():
       pilihan_password = input('Ketikkan Password anda:')
       if verifikasi_password(pilihan_password):
          regist[3] = pilihan_password
       else:
          print('Password diluar kriteria!')
          print('Minimal 8 karakte, memiliki huruf kecil,kapital ,dan simbol')
          password()

    regist =[input('Masukan Nama Anda\t:'),
            input('Masukkan Pekerjaan Anda\t:'),
            input('Buat Username\t\t:'),'password']
    password()
            
    yakin_tidak = input('Apakah anda yakin? (y/t):')
    print(regist)
    # if yakin_tidak == 'y':
    #     with open('login.csv','w') as register:
    #     user_data = f"{regist[0]},{regist[1]},{regist[2]},{regist[3]}"
    #     register.write(user_data)
    #     print('Username dan Password tersimpan')
    #     input('enter untuk melanjutkan')
    #     # Login_pengguna()
    # else:
    #     Register()
          
          
Register()









  
#  def Register():
#         clear_console()
#         with open('Tampilan Register.txt','r',encoding='utf-8') as registers:
#                 register_gui = registers.read()
#                 print(register_gui)
#                 registers.close()
#         regist =[input('Masukan Nama Anda\t:'),
#                 input('Masukkan Pekerjaan Anda\t:'),
#                 input('Buat Username\t\t:'),
#                 input('Buat Password\t\t:')]
#         yakin_tidak = input('Apakah anda yakin? (y/t):')
#         if yakin_tidak == 'y':
#             with open('login.csv','w') as register:
#                 user_data = f"{regist[0]},{regist[1]},{regist[2]},{regist[3]}"
#                 register.write(user_data)
#             print('Username dan Password tersimpan')
#             input('enter untuk melanjutkan')
#             Login_pengguna()
#         else:
#             Register()