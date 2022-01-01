data = {}
    

def no_data():
    print("DAFTAR NILAI")
    print("------------")
    print(72*"=")
    print("| {0:^10} | {1:^10} | {2:^6} | {3:^6} | {4:^6} |   {5:^12}  |".format("NIM", "NAMA", "TUGAS", "UTS", "UAS", "NILAI AKHIR"))
    print(72*"=")
    print("|                             TIDAK ADA DATA                           |")
    print(72*"=")
    print()
            

def lihat():
    if len(data) <= 0:
        no_data()
    else:
        print("DAFTAR NILAI")
        print("------------")
        print(72*"=")
        print("| {0:^10} | {1:^10} | {2:^6} | {3:^6} | {4:^6} |   {5:^12}  |".format("NIM", "NAMA", "TUGAS", "UTS", "UAS", "NILAI AKHIR"))
        print(72*"=")
        for z in data.items():
            print(f"| {z[1][0]:>10} | {z[0]:>10} | {z[1][1]:>6} | {z[1][2]:>6} | {z[1][3]:>6} |   {z[1][4]:>12}  |") 
            print(72*"=")
        print()
            
            
def tambah():
    print("TAMBAH DATA")
    print("------------")
    try :
        nama = input("Nama Mahasiswa\t: ")
        nim = int(input("NIM Mahasiswa\t: "))
        tugas = int(input("Nilai Tugas\t: "))
        uts = int(input("Nilai UTS\t: "))
        uas = int(input("Nilai UAS\t: "))
        akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100)
        data[nama] = [nim, tugas, uts, uas, akhir]
        print()

    except ValueError :
        print("Data yang dimasukkan salah! Ulangi lagi!")
        print()


def ubah():
    if len(data) <= 0:
        no_data()
    else :
        print("UBAH DATA")
        print("-----------")
        try :
            nama = input("Nama Anda\t: ")
            if nama in data.keys():
                nim = int(input("NIM Mahasiswa\t: "))
                tugas = int(input("Nilai Tugas\t: "))
                uts = int(input("Nilai UTS\t: "))
                uas = int(input("Nilai UAS\t: "))
                akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100)
                data[nama] = [nim, tugas, uts, uas, akhir]
                print()
                
        except ValueError :
            print("Data harus berupa angka!")
            print()


def hapus():
    if len(data) <=0:
        no_data()
    else:
        print("HAPUS DATA")
        print("-----------")
        nama = input("Nama Anda\t: ")
        if nama in data.keys():
            del data[nama]
            print()


loop = True
while loop :
    print("PILIH MENU")
    print("----------")
    print("\n1.Lihat \n2.Tambah \n3.Ubah \n4.Hapus \n5.Keluar")
    print()
    try:
        tanya = int(input("Pilih : "))
        print()

        if tanya==1:
            lihat()
        
        elif tanya==2: 
            tambah()
        
        elif tanya==3: 
            ubah()
        
        elif tanya==4: 
            hapus()
        
        elif tanya==5:
            print("Program Selesai")
            print()
            loop = False
            
    except ValueError:
        print()
        print("Tidak ada menu! Ulangi lagi!")
        print()