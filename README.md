## Python Input, Output dan Import

Pada edisi kali ini kita akan fokuskan kepada dua fungsi *build-in* `print()` dan `input()` untuk melakukan tugas I/O di python. Juga akan dijelaskan mengenai cara mengimport modul-modul dan menggunakannya dalam program.

Python menyediakan banyak sekali fungsi bawaan yang tersedia untuk digunakan pada Python prompt.

Beberapa fungsi seperti `input()` dan `print()` banyak digunakan untuk operasi input dan output standar. Mari kita lihat bagian output terlebih dahulu

#### Python Output menggunakan fungsi `print()`

Kita menggunakan fungsi `print()` untuk menampilkan data perangkat (layar) output standar. Kita juga bisa menampilkan data ke file, tapi itu akan dibahas nanti.

Contoh penggunaannya adalah sebagai berikut:
```
print('Kalimat ini akan ditampilkan ke layar')
```
Output:
```
Kalimat ini akan ditampilkan ke layar
```

Contoh lain:
```
a = 5
print('nilai dari a adalah:', a)
```
Output:
```
nilai dari a adalah: 5
```

Pada statement `print()` yang kedua, kita bisa perhatikan bahwa `space` telah ditambahkan diantara string dan nilai variable a. Itu adalah defaultnya, tapi kita bisa mengubahnya.

Aktual sintaks dari fungsi `print()` adalah:
```
print(*object, sep=' ', end='\n', file=sys.stdout, flush=false)
```
Disini, _**Object**_ adalah nilai yang akan dicetak(di print).
_**Sep**_ adalah pemisah yang digunakan diantara nilai/values. Defaultnya adalah karakter spasi.
Setelah semua *value(s)* dicetak, _**end**_ kemudian dicetak. Defaultnya adalah *newline* atau garis baru.
_**file**_ adalah objek dimana nilai-nilai (values) akan dicetak dan secara default adalah `sys.stdout` (screen). Ini adalah contoh untuk mengilustrasikannya.
```
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')
```
Output:
```
1 2 3 4
1*2*3*4
1#2#3#4&
```

---

#### Output formatting