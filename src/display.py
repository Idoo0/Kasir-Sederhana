import os

def display_header():
    os.system("cls")
    print("="*50)
    print("Warung Dadang".center(50))
    print("Makanan dan Minuman".center(50))
    print("="*50)

def display_data(data,harga):
    datadum = data.copy()
    hargadum = harga.copy()
    keys = datadum.keys()

    print(f"{'='*40}".center(50))
    print(f"|{'Kode'.center(6)}|{'Nama'.center(20)}|{'Harga'.center(10)}|".center(50))
    print(f"{'='*40}".center(50))
 
    dumi = 1
    for i in keys:
        dumk = 1
        dumj = 1
        for j in datadum:
            if dumj == dumi:
                for k in hargadum:
                    if dumk == dumi:
                        print(f"|{i:^6}|{datadum[j]:^20}|{hargadum[k]:^10}|".center(50))
                    else:
                        dumk += 1
                        continue
                    if True:
                        break
            else:
                dumj += 1
                continue            
            if True:
                break
        dumi += 1

    print(f"{'='*40}".center(50))