daftar = (str(input("Masukkan daftar siswa :")))
print ("Daftar siswa :", daftar.title().split(","))
tambah = (str(input("Masukan siswa yang ingin ditambahkan :")))
kapital1 = daftar.title()
kapital2 = tambah.title()


if kapital2 not in kapital1 :
    print ("Hasil penambahan pada daftar siswa :", [daftar.title(), tambah.upper()])
else :
    print("Siswa atas nama", (tambah.upper()), "sudah berada dalam daftar siswa")
