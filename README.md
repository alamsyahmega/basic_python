# Python Input, Output dan Import

Pada edisi kali ini kita akan fokuskan kepada dua fungsi *build-in* `print()` dan `input()` untuk melakukan tugas I/O di python. Juga akan dijelaskan mengenai cara mengimport modul-modul dan menggunakannya dalam program.

Python menyediakan banyak sekali fungsi bawaan yang tersedia untuk digunakan pada Python prompt.

Beberapa fungsi seperti `input()` dan `print()` banyak digunakan untuk operasi input dan output standar. Mari kita lihat bagian output terlebih dahulu

## Python Output menggunakan fungsi `print()`

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

----

### Output formatting

Kadang-kadang kita ingin memformat output kita untuk menjadikannya terlihat lebih interaktif. ini dapat dilakukan dengan menggunakan metode `str.format()`. 
```
>>> x = 5; y = 10
>>> print('Nilai dari x adalah {} dan y adalah {}'.format(x,y))
Nilai dari x adalah 5 dan y adalah 10
```
Disini, kurung kurawal `{}` digunakan sebagai *placeholder*. Kita dapat menentukan urutan pencetakannya menggunakan angka (index tuple).
```
print('aku suka {0} dan {1}'.format('roti', 'mentega'))
print('aku suka {1} dan {0}'.format('roti', 'mentega'))
```
Output:
```
aku suka roti dan mentega
aku suka mentega dan roti
```

Kita dapat menggunakan *keyword argument* untuk memformat string
```
>>> print('Halo {nama}, {sapaan}'.format(sapaan='selamat pagi!', nama='Hasri'))
Halo Hasri, selamat pagi!
```
Kita juga dapat memformat string menggunakan gaya lama `sprintf()` yang dipakai di bahasa pemrograman C. Kita menggunakan operator `%` untuk menyelesaikan ini.
```
>>> x = 12.3456789
>>> print('Nilai dari x adalah %3.2f' %x)
Nilai dari x adalah 12.35
>>> print('Nilai dari x adalah %3.4f' %x)
Nilai dari x adalah 12.3457
```
-----

## Python Input

Sampai sekarang, program kita masih statik. Nilai dari variabel telah didefinisikan sebelumnya atau didefinisikan secara *hardcore* ke dalam *source code*.

Untuk memungkinkan fleksibilitas, kita mungkin ingin mengambil input dari user. Di python, kita memiliki fungsi `input()` untuk melakukan ini. Sintaks untuk `input()` dalah:
```
input([prompt])
```
dimana `prompt` adalah string yang kita ingin tampilkan ke screen. prompt ini sifatnya optional.
```
>>> num = input('Masukkan sebuah nomor:')
Masukkan sebuah nomor: 10
>>> num
'10'
```
Kita dapat melihat bahwa nilai yang dimasukkan 10 adalah sebuah *string*, bukan *number*. Untuk mengkonversi ini ke *number* kita dapat menggunakan fungsi `int()` atau `float()`.
```
>>> int('10)
10
>>> float('10)
10.0
```

Operasi yang sama bisa kita lakukan menggunakan fungsi `eval()`. Tapi `eval()` lebih jauh dari itu, eval dapat mengevaluasi bahkan untuk sebuah ekspresi, asalkan inputnya adalah string.
```
>>> int('2+3')
>>> int('2+3')
Traceback (most recent call last):
  File "<string>", line 301, in runcode
  File "<interactive input>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '2+3'
>>> eval('2+3')
5
```
----

## Python Import

Ketika program kita menjadi lebih besar, adalah ide bagus untuk memecahnya menjadi beberapa modul.

Modul adalah sebuah file yang berisi definisi (*definitions*) dan pernyataan (*statements*) Python. Modul python memiliki sebuah nama file dan diakhiri dengan ekstensi `.py`.

Definisi didalam sebuah modul dapat diimport ke modul lainnya atau interpreter interaktif dengan python. Kita menggunakan kata kunci `import` untuk melalukan itu.

Contohnya, kita dapat mengimport modul `math` dengan menuliskan line berikut:
```
import math
```
Kita dapat menggunakan modul dengan cara seperti berikut
```
import math
print(math.pi)
```
Output:
```
3.141592653589793
```

Sekarang semua definisi didalam `math()` tersedia di *scope* kita. Kita juga dapat megimport beberapa atribut dan fungsi tertentu saja, menggunakan kata kunci `from`. Contohnya:
```
>>> from math import pi
>>> pi
3.141592653589793
```

Saat mengimport modul, python melihat beberapa tempat yang didefinisikan didalam `sys.path`. Itu merupakan daftar dari lokasi direktori.
```
>>> import sys
>>> sys.path
['', 
 'C:\\Python33\\Lib\\idlelib', 
 'C:\\Windows\\system32\\python33.zip', 
 'C:\\Python33\\DLLs', 
 'C:\\Python33\\lib', 
 'C:\\Python33', 
 'C:\\Python33\\lib\\site-packages']
```

Kita juga dapat menambahkan lokasi kita pada list tersebut.

-----

Untuk informasi lebih lanjut [Programiz: input-output-import](https://www.programiz.com/python-programming/input-output-import)
