suhu = float(input("Masukkan suhu tubuh anda :"))


if suhu > 50:
    print("Anda bukan manusia :)")
elif suhu < 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
elif (suhu > 37.5) and (suhu <= 50):
    print("Anda demam! Jangan berpergian ke tempat Umum.")
elif (suhu >= 32.5) and (suhu <= 37.5):
    print("Suhu anda normal!")