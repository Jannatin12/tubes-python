# membuat fungsi untuk membaca file teks yang saya buat
def baca_data(filename):
    file = open(filename, "r") #memanggil fungsi open untuk membuka file teks
    
    teks = file.readline() #membaca perbaris
    while teks != "":
        list_data = teks.split("/") #mengubah string ke dalam list
        teks = file.readline()
        print (list_data)
    file.close() #menutup file
    return list_data

# list posisi
posisi = [] #membuat list posisi kosong
nama_file = "file_text2.txt"
posisi = baca_data(nama_file) #menampilkan list posisi yg berisi file teks

#membuat dictionary skor pemain hitam dengan huruf kecil dan putih dengan huruf besar
skor = {
	"k": 200, "K": 200,
	"q": 9, "Q": 9,
	"r": 5, "R": 5,
	"b": 3, "B": 3,
	"n": 3, "N": 3,
	"p": 1, "P": 1
}

pemain = [0, 0]
#membuat fungsi nilai_buah dengan parameter s sebagai skor dan p sebagai pemain
def nilai_buah(s, p):
    baca_kolom = []
    for i in range(len(s)): 
        baca_kolom = list(s[i]) #memasukkan perbaris list s ke dalam baca_kolom
        print(baca_kolom)
        for j in range(len(baca_kolom)): #iterasi list(s[i])
            if baca_kolom [j].isalpha(): #mengecek apakah elemen di dalam list itu huruf atau bukan
                if baca_kolom [j].isupper(): #jika dia huruf, dia tuh kapital atau bukan
                    p[0] = skor[baca_kolom[j]] + p[0] #jika iya, maka akan dimasukkan ke skor pemain putih
                else:
                    p[1] = skor[baca_kolom[j]] + p[1] #jika tidak, maka akan dimasukkan ke skor pemain hitam
    return p #mereturn skor dari pemain putih dan hitam

# membuat fungsi jumlah_petak_kosong
def jumlah_petak_kosong(n):
    jumlah = 0
    for i in n: #iterasi elemen dari list
        for k in i: #iterasi elemen dari elemen i
            if k.isalpha() == False: #jika k bukan huruf
                jumlah += int(k) #maka jumlahnya ditambah dengan k
    return jumlah #mereturn jumlah

#memanggil fungsi dan output program
hasil_akhir = nilai_buah(posisi, pemain)
print("Skor pemain putih = ", hasil_akhir[0])
print("Skor pemain hitam = ", hasil_akhir[1])
print("Jumlah petak kosong yang tersisa", jumlah_petak_kosong(posisi))