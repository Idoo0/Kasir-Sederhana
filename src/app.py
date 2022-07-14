import display
import data_makanan
import data_minuman
import order

while True:
    display.display_header()

    print("\n"+"Makanan".center(48))
    display.display_data(data_makanan.makanan,data_makanan.harga_makanan)

    print("\n"+"Minuman".center(48))
    display.display_data(data_minuman.minuman,data_minuman.harga_minuman)

    while True :
        harga = order.ordernow()
        while True:
            confrim = input("\nApakah pesanan anda sudah benar? (y/n) : ")
            if confrim == 'n' or confrim == 'N':
                break
            elif confrim == 'y' or confrim == 'Y':
                break
            else :
                print("Masukan yang benar! (y/n)")
        if confrim == 'y' or confrim == 'Y':
            break
    if confrim == 'y' or confrim == 'Y':
        break

print(f"\nTotal harga yang harus dibayarkan Rp.{harga:,}")

print("\nTerimakasih, silahkan lakukan pembayaran!\n")
