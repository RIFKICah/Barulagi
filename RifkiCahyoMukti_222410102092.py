import random
halo = random.randint(0, 100)

print(halo)

print("Tebak lah angka yang benar")
print("angka berada di antara 0-100")
#quis = input("masukan angka = ")
quis = halo
while True :
    x = int(input("masukan angka = "))
    x += 1

    if x > halo :
        print("Tidak Tepat, Angka terlalu besar")
    elif x < halo :
        print("Tidak Tepat, Angka terlalu kecil")
    elif x == halo :
        print("benar")
        break
    pass



#    elif x == 7:
#        print("anda kurang beruntung")
#        break
# mohon maaf pak saya belum paham cara menginput sebuah pembatas
# saya baru mulai belajar 1 minggu ini dikarenakan baru mendapat laptopnya








#for x in quis:
#    if x == halo:
#        print("Angka yang kamu masukan benar")
#    elif x > halo:
#        print("Angka yang kamu masukan terlalu besar")
#    elif x < halo:
#        print("Angka yang kamu masukan terlalu kecil")
#    break
