from . import Database
from . Util import random_string

def create(nama_barang,harga_jual,Kondisi):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["harga_jual"] = str(harga_jual) + Database.TEMPLATE["harga_jual"][len(str(harga_jual)):] 
    data["nama_barang"] = nama_barang + Database.TEMPLATE["nama_barang"][len(nama_barang):]
    data["kondisi"] = Kondisi + Database.TEMPLATE["kondisi"][len(Kondisi):]

    data_str = f'{data["pk"]},{data["nama_barang"]}, {data["harga_jual"]}, {data["kondisi"]} \n'
    print(data_str)

    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("salah pak")


def create_first_data():

    
    nama_barang = input("nama barang: ")
    while True :    
        try:
            harga_jual = int(input("Harga barang\t: "))
            if len(str(harga_jual)) >= 4:
                break
            else :
                print("harga harus angka, silahkan masukan harga lagi")
            
        except:
            print("harga harus angka, silahkan masukan harga lagi (harga >= 1000)")

    Kondisi     = input("Kondisi barang: ")
    
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["harga_jual"] = str(harga_jual)
    data["nama_barang"] = nama_barang + Database.TEMPLATE["nama_barang"][len(nama_barang):]
    data["kondisi"] = Kondisi + Database.TEMPLATE["kondisi"][len(Kondisi):]

    data_str = f'{data["pk"]},{data["nama_barang"]}, {data["harga_jual"]}, {data["kondisi"]} \n'
    print(data_str)

    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("salah pak")
        
def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            isi = file.readlines()
            return isi
    except:
        print("membaca database ERROR")
        return False


    