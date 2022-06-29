#   __  __   _____ ____  ____          _        ______ _____  
#  |  \/  | |_   _/ __ \|  _ \   /\   | |      |  ____|  __ \ 
#  | \  / |   | || |  | | |_) | /  \  | |      | |__  | |__) |
#  | |\/| |   | || |  | |  _ < / /\ \ | |      |  __| |  _  / 
#  | |  | |  _| || |__| | |_) / ____ \| |____  | |    | | \ \ 
#  |_|  |_| |_____\___\_\____/_/    \_\______| |_|    |_|  \_\
#             ___  __  ___    __ __  ___  _  _   
#            |__ \/_ |/ _ \  / //_ |/ _ \| || |  
#               ) || | | | |/ /_ | | (_) | || |_ 
#              / / | | | | | '_ \| |> _ <|__   _|
#             / /_ | | |_| | (_) | | (_) |  | |  
#            |____||_|\___/ \___/|_|\___/   |_|  

#  Tugas Besar - Dasar-Dasar Pemrograman
#  Muhammad Iqbal Fathur Rohman - 2106184
#  Teknik Informatika - E

menu_makanan = ["Egg Roll","Shrimp Roll","Spicy Chicken","Chicken Katsu","Yakitori","Yakisoba","Onigiri"]
harga_makanan = [5000,10000,15000,15000,20000,20000,5000]
menu_minuman = ["Aqua botol","Coca Cola","Sprite","Boba Series","Kopi hitam"]
harga_minuman = [3000,5000,5000,10000,3000]
tax = 0.1
diskon_member = 0.1
diskon_pembelanjaan1 = 0.01
diskon_pembelanjaan2 = 0.02
diskon_pembelanjaan3 = 0.03
total_menu = len(menu_makanan)+len(menu_minuman)
total_menu_makanan = len(menu_makanan)
total_menu_minuman = len(menu_minuman)
pesanan = []
jumlah_pesanan = []
harga = []

import os
os.system ("cls")
import datetime

def baelz():
    print("            ____             _     _____           _         ")
    print("           |  _ \           | |   |  __ \         | |        ")
    print("           | |_) | __ _  ___| |___| |__) |___  ___| |_ ___   ")
    print("           |  _ < / _` |/ _ \ |_  /  _  // _ \/ __| __/ _ \  ")
    print("           | |_) | (_| |  __/ |/ /| | \ \  __/\__ \ || (_) | ")
    print("           |____/ \__,_|\___|_/___|_|  \_\___||___/\__\___/  ")

def daftarmenu():
    print("\n+=======================================================================+")
    print(f"|                          DAFTAR MENU ({total_menu})                             |")
    print("+=======================================================================+")
    print(f"|  No.\t| Makanan ({total_menu_makanan})\t\t\t\t\t| Harga\t\t|")
    print("+-------+-----------------------------------------------+---------------+")
    for i in range(total_menu_makanan):
        print(f"| {i+1}.\t| {menu_makanan[i]}\t\t\t\t\t| Rp {harga_makanan[i]}\t|")
    print("+-------+-----------------------------------------------+---------------+")
    print(f"|  No.\t| Minuman ({total_menu_minuman})\t\t\t\t\t| Harga\t\t|")
    print("+-------+-----------------------------------------------+---------------+")
    for i in range(total_menu_minuman):
        print(f"| {i+1+total_menu_makanan}.\t| {menu_minuman[i]}\t\t\t\t\t| Rp {harga_minuman[i]}\t|")
    print("+-------+-----------------------------------------------+---------------+")
    pilihan_lainlain()
    memesan()
    
def pilihan_lainlain():
    print("\n|  77. | Selesai        |  88. | Edit Pesanan      |  99. | Bersihkan\t|")
    print("|  66. | Tampilkan Menu |  55. | Tampilkan Pesanan |  44. | Keluar\t|")

def jumlah_total(x):
    z=0;
    for i in range(len(x)):
        y = x[i]
        z+=y 
    return z

def list_pesanan():
    print("\n+=======================================================================+")
    print(f"|                           LIST PESANAN                                |")
    print("+=======================================================================+")
    print("|  No.  | Pesanan                     (Jumlah dipesan)  | Harga         |")
    print("+-------+-----------------------------------------------+---------------+")
    for i in range(len(pesanan)):
        print(f"| {i+1}.\t| {pesanan[i]}\t\t\t\t({jumlah_pesanan[i]})\t| Rp {harga[i]}\t|")
    print("+-------+-----------------------------------------------+---------------+")
    print(f"|\t  Jumlah \t\t\t\t({jumlah_total(jumlah_pesanan)})\t| Rp {jumlah_total(harga)}\t|")
    print("+-----------------------------------------------------------------------+")

def memesan():
    try:
        pemilihan_jawaban(int(input("\nSilahkan input pilihan yang Anda inginkan : ")))
    except ValueError:
        print("\n[!] Masukan inputan yang benar !")
        memesan()

def edit_pesanan():
    print("\n|  90. | Hapus Pesanan  |  80. | Reset Pesanan  |  70. | Selesai Edit\t|")
    try:
        edit = int(input("\nSilahkan input pilihan yang Anda inginkan : "))
    except ValueError:
        print("\n[!] Masukan inputan yang benar!")
        edit_pesanan()
    
    if (edit == 90):
        try:
            hapus_pesanan = int(input("\nHapus pesanan No berapa? "))
        except ValueError:
            print("\n[!] Masukan sesuai No pada List Pesanan !")
            edit_pesanan()
        if (hapus_pesanan <= len(pesanan)):
            pesanan_yang_mau_dihapus = pesanan[hapus_pesanan-1]
            yakin_hapus = input(f"Menghapus {pesanan_yang_mau_dihapus} dari pesanan? (y/t) : ")
            if (yakin_hapus == 'y'):
                del pesanan[hapus_pesanan-1]
                del harga[hapus_pesanan-1]
                del jumlah_pesanan[hapus_pesanan-1]
                print(f"\n[V] Menghapus {pesanan_yang_mau_dihapus} dari pesanan berasil.")
            else:
                print(f"\n[X] Menghapus {pesanan_yang_mau_dihapus} dari pesanan gagal.")
            edit_pesanan()
        else:
            print("\n[!] Masukan sesuai No pada List Pesanan !")
            edit_pesanan()
    elif (edit == 80):
        yakin_hapus = input(f"Reset semua pesanan? (y/t) : ")
        pesanan_yang_mau_direset = len(pesanan)
        if (yakin_hapus == 'y'):
            for i in range(len(pesanan)):
                del pesanan[0]
                del harga[0]
                del jumlah_pesanan[0]
            print(f"\n[V] Reset {pesanan_yang_mau_direset} pesanan berasil.")
        else:
            print(f"\n[X] Reset {len(pesanan)} pesanan gagal.")
        edit_pesanan()
    elif (edit == 70):
        print("\n[V] Selesai mengedit pesanan.")
        pilihan_lainlain()
        memesan()
    else:
        print("\n[!] Masukan inputan yang benar !")
        edit_pesanan()

def pesanan_selesai():
    pelayan = input("\nMasukan Nama pelayan : ")
    pemesan = input("Masukan Nama pemesan : ")
    meja = input("Meja berapa? ")
    member = input("Apakah pembeli merupakan member dari BaelzResto? (y/t) : ")

    os.system ("cls")
    baelz()
    print("          .=[ Perum Bumi Abdi Negara 1 No 197 RT/RW 03/13 ]=.")
    print("                        Karangpawitan, Garut")
    print(datetime.datetime.now().strftime("\n\tDate Time\t: %x %X"))
    print(f"\tPemesan / meja\t: {pemesan} / {meja}")
    print(f"\tService\t\t: {pelayan}")
    list_pesanan()
    print(f"|\t  TAX \t\t\t\t\t({int(tax*100)}%)\t| Rp {int(jumlah_total(harga)*tax)}\t|")
    if (jumlah_total(harga) >= 100000):
        print(f"|\t  Diskon Pembelanjaan 3\t\t\t({int(diskon_pembelanjaan3*100)}%)\t| -Rp {int(jumlah_total(harga)*diskon_pembelanjaan3)}\t|")
        diskonan = int(jumlah_total(harga)*diskon_pembelanjaan3)
    elif (jumlah_total(harga) >= 75000):
        print(f"|\t  Diskon Pembelanjaan 2\t\t\t({int(diskon_pembelanjaan2*100)}%)\t| -Rp {int(jumlah_total(harga)*diskon_pembelanjaan2)}\t|")
        diskonan = int(jumlah_total(harga)*diskon_pembelanjaan2)
    elif (jumlah_total(harga) >= 50000):
        print(f"|\t  Diskon Pembelanjaan 1\t\t\t({int(diskon_pembelanjaan1*100)}%)\t| -Rp {int(jumlah_total(harga)*diskon_pembelanjaan1)}\t|")
        diskonan = int(jumlah_total(harga)*diskon_pembelanjaan2)
    else:
        diskonan = 0
    if (member == 'y'):
        print(f"|\t  Diskon Member\t\t\t\t({int(diskon_member*100)}%)\t| -Rp {int(jumlah_total(harga)*diskon_member)}\t|")
        print("+=======================================================================+")
        total_pembayaran = jumlah_total(harga)+int(jumlah_total(harga)*tax)-int(jumlah_total(harga)*diskon_member)-diskonan
    else:
        print("+=======================================================================+")
        total_pembayaran = jumlah_total(harga)+int(jumlah_total(harga)*tax)-diskonan
    print(f"|\t  TOTAL \t\t\t\t\t| Rp {total_pembayaran}\t|")
    print("+=======================================================================+")
    pembayaran_tunai = int(input("\n\tPembayaran Tunai \t\t: "))
    pembayaran_nontunai = int(input("\tPembayaran Non Tunai \t\t: "))
    kembalian = (pembayaran_tunai+pembayaran_nontunai)-total_pembayaran
    print(f"\tKembalian\t\t\t: {kembalian}\n")
    sampai_jumpa()
    input()

def pemilihan_jawaban(jawaban):
    if (jawaban <= total_menu):
        if (jawaban > total_menu_makanan):
            jumlah = int(input(f"Memesan {menu_minuman[jawaban-1-total_menu_makanan]} dengan jumlah : "))
            if (jumlah > 0):
                pesanan.append(menu_minuman[jawaban-1-total_menu_makanan])
                jumlah_pesanan.append(jumlah)
                harga.append(harga_minuman[jawaban-1-total_menu_makanan]*jumlah)
                print(f"\n[V] Berhasil memasukan {menu_minuman[jawaban-1-total_menu_makanan]} dengan jumlah {jumlah} kedalam pesanan.")
                pilihan_lainlain()
                memesan()
            else:
                print(f"\n[X] Gagal memasukan {menu_minuman[jawaban-1-total_menu_makanan]} kedalam pesanan.")
                pilihan_lainlain()
                memesan()
        else:
            jumlah = int(input(f"Memesan {menu_makanan[jawaban-1]} dengan jumlah : "))
            if (jumlah > 0):
                pesanan.append(menu_makanan[jawaban-1])
                jumlah_pesanan.append(jumlah)
                harga.append(harga_makanan[jawaban-1]*jumlah)
                print(f"\n[V] Berhasil memasukan {menu_makanan[jawaban-1]} dengan jumlah {jumlah} kedalam pesanan.")
                pilihan_lainlain()
                memesan()
            else:
                print(f"\n[X] Gagal memasukan {menu_makanan[jawaban-1]} kedalam pesanan.")
                pilihan_lainlain()
                memesan()
    else:
        if (jawaban == 66):
            daftarmenu()
            memesan()
        elif (jawaban == 55):
            list_pesanan()
            pilihan_lainlain()
            memesan()
        elif (jawaban == 44):
            os.system ("cls")
            baelz()
            sampai_jumpa()
        elif (jawaban == 99):
            os.system ("cls")
            baelz()
            selamat_datang()
            daftarmenu()
            pilihan_lainlain()
            memesan()
        elif (jawaban == 88):
            list_pesanan()
            edit_pesanan()
        elif (jawaban == 77):
            pesanan_selesai()
        else:
            print("\n[!] Masukan inputan yang benar !")
            pilihan_lainlain()
            memesan()

def selamat_datang():
    print("               .=[ Selamat Datang di Baelz Restoran ]=.")
    print("               Silahkan pilih menu yang akan Anda pesan")
def sampai_jumpa():
    print("            .=[ Sampai jumpa kembali di Baelz Restoran ]=.")
    print("                          Terimakasih banyak\n\n")

baelz()
selamat_datang()
daftarmenu()