def lingkaran():
    r = int(input("masukkan nilai r: "))
    luas = 3.14*r**2
    keliling = 2*3.14*r
    print("Luas: ", luas)
    print("Keliling: ", keliling)
    return luas, keliling

def segitiga(a,t,sisi):
    luas = 0.5*a*t
    keliling = sisi*3
    print("luas: ", luas)
    print("Keliling: ", keliling)
    return luas, keliling