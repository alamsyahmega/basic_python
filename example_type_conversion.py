# Konversi Implisit

a = 10
b = 13.33

print("Tipe data 'a' adalah:", type(a))
print("Tipe data 'b' adalah:", type(b))

c = a + b
print("Tipe data 'c' adalah:", type(c)) # menjadi higher (float)

print("==" * 5)

# Konversi Eksplisit

nilai_float = 3.14
nilai_string = "198"

try:
    hasil = nilai_float + nilai_string
except Exception as error:
    print("Terjadi error:", error)

print("mengubah nilai_string ke integer dengan: nilai_string = int(nilai_string)")
nilai_string = int(nilai_string)

hasil = nilai_string + nilai_float
print("Hasilnya adalah:", hasil)

