# Ini komentar
# Tidak akan dieksekusi
# print("apakah aku dieksekusi?")
print("Ternyata aku yang dieksekusi")
# yang diatas udah termasuk multiline komentar lho
# coba yang pakai kutip
"""
Ini juga komentar, tidak dieksekusi, tapi bisa dijadikan
multiline string, dibawah contohnya"""
a = """
Halo selamat pagi!
Ini dieksekusi loh
bisa jadi multiline string hoho
"""
print(a)

# contoh docstring
def multiple(number):
    """ini dalah docstring, jadi fungsi ini bisa mengalikan 2x angka yang dimasukkan"""
    return number * 2

print(multiple.__doc__) # untuk akses docstringnya guys
# docstring jg bisa berlaku untuk class 
