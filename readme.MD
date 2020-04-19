## Pernyataan, Indentasi dan Komentar di Pyton (__*Python Statement, Indentation and Comment*__)
### 1. Python Statement
definisi:
> Instruksi yang dapat dieksekusi oleh interpreter python disebut dengan
> _**Statement**_. Contohnya `a=1` adalah _assignment statement_. _if statement_, _for statement_, _while statement_, dll adalah beberapa contoh dari statement yang akan dibahas nanti.
#### pernyataan multi-baris (_multiline statements_)
Dalam python, akhir pernyataan ditandai oleh karakter garis baru. Tapi kita bisa membuat pernyataan lebih dari beberapa baris dengan karakter lanjutan garis ( \ ). Sebagai contoh:
```
a = 1 + 2 + 3 + \
	4 + 5 + 6 + \
	7 + 8 + 9
```
Ini adalah kelanjutan garis eksplisit. Dalam Python, kelanjutan garis tersirat di dalam tanda kurung (), tanda kurung [], dan tanda kurung {}. Sebagai contoh, kita dapat mengimplementasikan pernyataan multi-baris di atas sebagai:

```
a = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)
```

Di sini, tanda kurung sekitarnya () melakukan kelanjutan garis secara implisit. Sama halnya dengan [] dan {}. Sebagai contoh:
```
warna = ['merah',
         'biru',
         'hijau']
```
Kita juga dapat menempatkan beberapa pernyataan dalam satu baris menggunakan titik koma, sebagai berikut:
```
a = 1; b = 2; c = 3
```
-----------------------
### 2. Indentasi (_Indentation_)
Sebagian besar bahasa pemrograman seperti C, C ++, dan Java menggunakan kurung {} untuk mendefinisikan blok kode. Python, bagaimanapun, menggunakan indentasi (_indentation_, *lekukan).

Blok kode (badan fungsi, loop, dll.) Dimulai dengan indentasi dan berakhir dengan baris pertama yang tidak terindentasi. Jumlah indentatisi terserah Anda, tetapi harus konsisten di seluruh blok itu.

Secara umum, empat blank spasi digunakan untuk indentasi dan lebih disukai daripada tab. Berikut ini sebuah contoh.
```
for i in range(1,10):
    print(i)
    if i == 7:
        break
```

Penegakan indentasi dengan Python membuat kode terlihat rapi dan bersih. Ini menghasilkan program Python yang terlihat serupa dan konsisten.
```
if True:
    print('Hello')
    a = 5
```
dan
```
if True: print('Hello'); a = 5
```
keduanya valid dan melakukan tugas yang sama, akan tetapi gaya penulisan kode yang pertama lebih jelas dan bersih.

> Indentasi yang salah akan menghasilkan error `IndentationError`.
---
### 3.  Komentar di Python
Komentar sangat penting saat menulis sebuah program. Komentar dapat menjelaskan dan mendeskripsikan apa yang terjadi pada program, sehingga seseorang yang melihat _source code_ tidak kesulitan mencari tahu.

Anda mungkin lupa detail utama dari program yang baru saja Anda tulis dalam waktu satu bulan. Jadi meluangkan waktu untuk menjelaskan konsep-konsep ini dalam bentuk komentar selalu membuahkan hasil.

Dalam Python, kita menggunakan simbol _hash_ (#) untuk mulai menulis komentar.

Penggunaan _hash_ (#) hanya untuk satu baris komentar. Komentar digunakan untuk programmer agar lebih memahami suatu program. _Interpreter python_ mengabaikan komentar (komentar tidak akan dieksekusi/ditampilkan)
```
# ini adalah komentart
# mengeprint Halo
print('Halo')
```
#### Komentar multi-baris
Kita dapat membuat komentar hingga mencakup beberapa baris. Salah satu caranya yaitu dengan menggunakan simbol **_hash_ ( # )** pada awal setiap baris. sebagai contoh:
```
# Ini adalah komentar yang menggunakan hash diawal
# dan semakin banyak serta meluas menggunakan hash 
# untuk beberapa baris yang ingin anda komentari
```

Cara lain untuk melakukan ini adalah dengan menggunakan tiga tanda kutip, baik single quote ( ' ) ataupun double quote ( " ).

Kutipan rangkap tiga ini umumnya digunakan untuk _string multi-line_. Tetapi dapat juga digunakan sebagai komentar multi-baris. Kecuali mereka bukan _**docstring**_, mereka tidak menghasilkan kode tambahan.
```
""" Ini juga sebuah
contoh sempurna
komentar multi-baris """
```


#### Docstrings dengan Python
> Docstring adalah kependekan dari string dokumentasi.
>Dokumentasi python (string dokumentasi) adalah string literal yang muncul tepat setelah definisi fungsi, metode, kelas, atau modul.

Kutipan rangkap tiga digunakan saat menulis dokumen. Sebagai contoh:
```
def double(num):
    """Fungsi untuk membuat nilai num menjadi double atau dua kali dari nilai awalnya"""
    return 2*num
```
Docstrings dikaitkan dengan objek sebagai atribut (.__ doc __) mereka.


Sumber dan untuk informasi lebih lengkap: [Programiz](https://www.programiz.com/python-programming/statement-indentation-comments)