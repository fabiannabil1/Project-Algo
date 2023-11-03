import pandas as pd

def Menu_Hapus_Tambah():
    #clear_console()
    #Header()
    print(f"{'Tambah / Hapus Kategori':^68}")
    with open('Hapus Kategori.txt','r') as gui_cat:
        gui_cat = gui_cat.read()
        print(gui_cat)
    pilhan_add_del = input('Pilihan Anda :')
    match pilhan_add_del:
        case '1' :
            Tambah_Kategori()
        case '2' :
            hapus_kategori
        case _ :
            Menu_Hapus_Tambah()

    def Tambah_Kategori():
        #clear_console()
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
            Menu_Hapus_Tambah()

def hapus_kategori():
        #clear_console()
        frame_cat = pd.read_csv('Data kategori.csv')
        print(frame_cat)
        panjang_index = len(frame_cat)
        print("Ketikkan Nomor Urut Kategori Untuk Menghapus ")
        print("Apabila Batal Ketik 't' untuk Batal ")
        hapus_cat = input('Kategori yg akan dihapus :')
        hapus_cat_str = str(hapus_cat)
        if hapus_cat_str == 't':
            #Menu sebelum ini
            Menu_Hapus_Tambah()
        else:
            if hapus_cat <= (panjang_index-1):
                frame_cat = frame_cat.drop(hapus_cat)
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
                    Menu_Hapus_Tambah()
                case _ :
                    Menu_Hapus_Tambah()
hapus_kategori()