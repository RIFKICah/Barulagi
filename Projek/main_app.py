# READ
# ADD data
# UPDATE data
# DELETE data
import os
import NOTE as NOTE


if __name__ == "__main__":  # supaya running program menjadi lebih rapi
    sistem_op = os.name     # untuk mendeteksi sistem operasinya apa
                            # supaya saat program dijalankan sistem_op ini bisa clear tampilan dari terminal

    match sistem_op :                   
        case "posix": os.system("clear")    
        case "nt" : os.system("cls")
    
    print(3*"-", "AgriTool", 3*"-",end="\n")
    print(6*"=", "$" ,6*"=")
    print("Menyediakan Alat Pertanian \nDalam Kondisi Baru Maupun Kondisi Bekas")
    print(40*"=")

    #check database ada atau tidak
    NOTE.init_console()



    while (True) :
        match sistem_op :                   # artinya = cek sistem_op apakah posix atau nt
            case "posix": os.system("clear")    # Untuk Linux   (clear)
            case "nt" : os.system("cls")        # Untuk Windows (cls)
                # nanti setelah tampilan terminal di clear maka akan di print yang dibawah ini
        
        # yang pertama muncul di terminal
        print(3*"-", "AgriTool", 3*"-",end="\n")
        print(6*"=", "$" ,6*"=")
        print("Menyediakan Alat Pertanian \nDalam Kondisi Baru Maupun Kondisi Bekas")
        print(40*"=")

        # ini yang kedua
        print("PILIHLAH SALAH SATU!") # ini adalah user Optionnya atau yang bisa dipilih oleh user
        print(f"1. Membeli")
        print(f"2. Menjual")
        print(f"3. Memesan\n")
        
        # lalu bagian user inputan.
        user_pilih = input("1/2/3 \n=")
        

        match user_pilih:           # kembali mengecek inputan user itu yang mana
            case "1" : NOTE.read_console() # berisi daftar dari barang atau produk yang dijual
            case "2" : NOTE.create_console() # di bagian menjual ini terdapat 3 yaitu create delete dan update
                # jual "utamakan selesai"
                # merubah harga     !second ide
                # batal jual        !third ide
            case "3" : print("Memesan") #
                # create (menginput data saja) "utamakan selesai"
                # delete (menghapus pesanan)    !second ide
        

        #
        sudahkah = input("apakah selesai (y/n)?")   # bagian ini berguna untuk jika user masih belum selesai
        if sudahkah == "y" or sudahkah == "Y":      # -menggunakan program (n) program akan dimulai ulang
                                               # sedangkan jika user sudah selesai (y) maka program berakhir
            break

        
    print(40*"=")
    print("Program Berakhir","="," Terima Kasih ")
    print(40*"=")
            




    






























