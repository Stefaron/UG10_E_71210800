print("""====Kalkulator Akar dan Pangkat====
Pilihan menu :
1. Pangkat 2 (Kuadrat)
2. Pangkat 3 (Kubik)
3. Akar Kuadrat
""")

#input
menu = int(input("Masukkan menu yang anda pilih :"))
print("")

#proses
if (menu >=1) and (menu <= 3) :
    bilangan = int(input("Masukkan bilangan yang ingin dipangkatkan :"))
    if menu == 1:
        rumus = (bilangan**2)
        print("Hasil dari pemangkatan bilangan", (bilangan), "dengan 2 (Kuadrat) adalah", rumus)
    elif menu == 2:
        rumus = (bilangan**3)
        print("Hasil dari pemangkatan bilangan", (bilangan), "dengan 3 (Kubik) adalah", rumus)
    elif menu == 3:
        rumus = (bilangan**0.5)
        print("Hasil akar kuadrat dari bilangan", (bilangan), "adalah", rumus)
else :
    print("Pilihan menu yang dimasukkan tidak sesuai!")