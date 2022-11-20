
from . import Operasi

def create_console():
    print("\n\n"+"="*100)
    print("silahkan masukan data!\n")
    nama_barang = input("nama barang\t: ")
    Kondisi = input("kondisi barang\t: ")
    while True :    
        try:
            harga_jual = int(input("Harga barang\t: "))
            if len(str(harga_jual)) >= 4:
                break
            else :
                print("harga harus angka, silahkan masukan harga lagi")
            
        except:
            print("harga harus angka, silahkan masukan harga lagi (harga >= 1000)")
    
    Operasi.create(nama_barang,harga_jual,Kondisi)
    print("\nberikut adalah data anda")
    read_console()


            


    

def read_console():
    data_file = Operasi.read()

    index = "No"
    Nama_barang = "Nama barang"
    Harga = "Harga barang"
    kondisi = "kondisi barang"
    
    # header
    print("\n"+"="*100)
    print(f"{index:4} | {Nama_barang:40} | {Harga:12} | {kondisi:8}")
    print("-"*100)
    
    # data

    for index,data in enumerate(data_file):
        data_break = data.split(",") 
        pk = data_break[0]
        nama_barang = data_break[1]
        harga_jual = data_break[2]
        Kondisi = data_break[3]
        print(f"{index+1:4} | {nama_barang:.40} | {harga_jual:.12} | {Kondisi:.8}")

    # footer
    
    print("="*100+"\n")