from . import Operasi


DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"xxxxxx",
    "nama_barang":255*" ",
    "harga_jual":"               ", # 15 digit harga
    "kondisi":255*"  " 
}



def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("database tersedia, init done!")
    
    except:
        print("database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()

            







