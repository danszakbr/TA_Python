import module_tugas

print("pilih bangun ruang yang akan dihitung")
print("1. lingkaran")
print("2. segitiga")

opsi = int(input("\nKetik Pilih:"))
if opsi == 1:
    print("hitung Lingkaran")
    lingkaran = module_tugas.lingkaran()
elif opsi == 2:
    alas = int(input("Masukkan nilai alas: "))
    tinggi = int(input("Masukkan nilai tinggi: "))
    sisi = int(input("Masukkan sisi: "))
    module_tugas.segitiga(alas,tinggi,sisi)
    