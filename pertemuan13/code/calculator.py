print("Calculator Python")
print("----------------")

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("----------------")

def penjumlahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def perkalian(x, y):
    return x * y

def pembagian(x, y):
    if y == 0:
        return "Error: Tidak bisa dibagi dengan nol"
    return x / y

tipe = input("Silakan masukkan nomor yang kalian pilih : ")

if tipe in ('1', '2', '3', '4'):
    try:
        angka1 = float(input("Angka pertama : "))
        angka2 = float(input("Angka kedua   : "))
        print("----------------")

        if tipe == '1':
            print("Jawabannya adalah :", penjumlahan(angka1, angka2))
        elif tipe == '2':
            print("Jawabannya adalah :", pengurangan(angka1, angka2))
        elif tipe == '3':
            print("Jawabannya adalah :", perkalian(angka1, angka2))
        elif tipe == '4':
            print("Jawabannya adalah :", pembagian(angka1, angka2))

        print("----------------")

    except ValueError:
        print("Error: Masukkan angka yang valid!")
else:
    print("Pilihan tidak tersedia!")
