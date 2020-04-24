# Python Output

print("====> Python Output <====", end=('\n' * 2))
umur = 22
nama = "Hasri"
kuliah = "Unpas"
jurusan = "Akuntansi"
siapa = "kalian semua"
semester = 8.002
print("Halo semuanya, selamat pagi")
print("Perkenalkan nama saya adalah", nama)
# dengan formatting
print("Umur saya saat ini adalah {}".format(umur))
print("saya kuliah di {0} jurusan {1}".format(kuliah, jurusan))
print(f"Senang bisa berkenalan dengan {siapa}")
print("oh ya btw sekarang aku sedang skripsi semester %d" %semester, end="\n \n")

print("=" * 4,"end", "end", "end", "=" * 4, sep="=====", end=("\n" * 5))
