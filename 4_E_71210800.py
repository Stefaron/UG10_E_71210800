a = int(input("Masukkan bilangan 1 :"))
b = int(input("Masukkan bilangan 2 :"))
c = int(input("Masukkan bilangan 3 :"))

if a<b and a<c:
        if b<c:
            print("Urutan bilangan dari yang terkecil adalah", a, b, c)
        else:
            print("Urutan bilangan dari yang terkecil adalah", a, c, b)
elif b<a and b<c:
        if a<c:
            print("Urutan bilangan dari yang terkecil adalah", b, a, c)
        else:
            print("Urutan bilangan dari yang terkecil adalah", b, c, a)
else:
        if a<b:
            print("Urutan bilangan dari yang terkecil adalah", c, a, b)
        else:
            print("Urutan bilangan dari yang terkecil adalah", c, b, a)