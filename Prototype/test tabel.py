import csv
import pandas as pd


def tulis(data):
    with open('Data Pilihan.csv','a') as file:
        writer =csv.writer(file)
        writer.writerow(data)

def menu():
    print('Ini Menuuuu')
    print('Ini Menuuuu')
    print('Ini Menuuuu')
    print('Ini Menuuuu')
    print('Ini Menuuuu')
    input()

def Pilihan(data):
    if data == 'Padi':
        print('menuuuuu')
        input()
    elif data == 'Jagung':
        print('menuuuuu')
        input()
    elif data == '':
        print('menuuuuu')
        input()


while True:   
    print('1.Padi\n2.Jagung\n3.Kedelai')
    pilihan = input('Masukkan Pilihan: ')
    match pilihan:
        case '1' :
            tulis(['Padi'])
            menu()
        case '2' :
            tulis(['Jagung'])
            menu()
        case '3' :
            tulis(['Kedelai'])
            menu()
        case '4':
            break
        case '5':
            a = pd.read_csv('Data Pilihan.csv')
            print(a)
            input()
        case _ :
            pass

for angka in range(1,11):
    if angka % 2 == 0:
        continue
    else:
        print(angka)

angka = int(input('Masukkan Angka : '))
while angka > 0:
    if angka == 50:
        print("saldo limit, nabung lah ntar miskin!!")
        break
    else:
        print('Habiskan Uanggnyaa sekarang jugaa!')
        print('sisa saldo =', angka)
        angka -= 10


buah = ['mangga','mangga','ayam']
hapus = 'mangga'
while hapus in buah:
    buah.remove(hapus)
print(buah)

print(len('[]================================================================[]'))
