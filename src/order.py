import data_makanan
import data_minuman

def ordernow():
    harga = 0
    print("\nContoh pengisian: AP,AS,AD")
    input_user_makanan = list((input("Masukan kode makanan (jika tidak ada silahkan ketik 1): ")).split(','))
    input_user_minuman = list((input("Masukan kode minuman (jika tidak ada silahkan ketik 1): ")).split(','))

    print("\nMakanan yang anda pesan:")
    dumi = 1
    for i in input_user_makanan:
        KEY_I = i in data_makanan.makanan
        if KEY_I:
            print(f"{dumi}. {data_makanan.makanan.get(i,'Kode tidak ditemukan')}")
            harga_i = int(data_makanan.harga_makanan.get(data_makanan.makanan[i]))
            harga += harga_i
            dumi += 1
        elif i == '1':
            print("tidak ada")
        else:
            print(f"{dumi}. kode yang anda masukan salah / tersedia")
            dumi += 1

    print("\nMinuman yang anda pesan: ")
    dumj = 1    
    for j in input_user_minuman:
        KEY_J = j in data_minuman.minuman
        if KEY_J:
            print(f"{dumj}. {data_minuman.minuman.get(j,'Kode tidak ditemukan')}")
            harga_j = int(data_minuman.harga_minuman.get(data_minuman.minuman[j]))
            harga += harga_j
            dumj += 1
        elif j == '1':
            print("Tidak ada")
            continue
        else:
            print(f"{dumj}. kode yang anda masukan salah / tersedia")
            dumj += 1
    return harga


