## KONVERSI TIPE DATA

### Konversi Tipe Data
Proses konversi nilai dari sebuah tipe data(integer, string, float, dll) kedalam tipe data lainnya disebut dengan _**Type Conversion**_. Python memiliki dua tipe dari konversi ini, yaitu
1. Konversi Tipe Data Implisit (*Implicit Type Conversion*)
2. Konversi Tipe Data Eksplisit (*Explicit Type Conversion*)

### Konversi secara Implisit (*Implicit Type Conversion*)
Dalam konversi secara implisit, Python secara otomatis merubah satu tipe data ke tipe data lainnya. Proses ini tidak membutuhkan keterlibatan user atau pengguna secara langsung

Mari kita lihat sebuah contoh dimana Python 'mempromosikan' tipe data rendah(*lower data type*) berupa `integer` ke tipe data tinggi(*higher data type*) berupa `float` untuk menghindari kehilangan data.

#### Contoh 1: Konversi integer ke float
```
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("tipe data dari num_int:",type(num_int))
print("tipe data dari num_flo:",type(num_flo))

print("nilai dari num_new:",num_new)
print("tipe data dari num_new:",type(num_new))
```

ketika kita menjalankan program diatas, keluarannya akan seperti berikut:
```
tipe data dari num_int: <class 'int'>
tipe data dari num_flo: <class 'float'>

nilai dari num_new: 124.23
tipe data dari num_new: <class 'float'>
```

Dari program diatas,
- Kita menambahkan num_int dan num_float, lalu menyimpan hasilnya pada num_new.
- Kita akan melihat tipe data dari masing-masing objek tersebut.
- Dari nilai keluarannya, kita dapat melihat tipe data dari `num_int` adalah `integer` sementara data dari `num_flo` adalah `float`
- Lalu kita bisa melihat bahwa `num_new` bertipe data float karena python selalu mengkonversi tipe data terendah ke tipe data yang lebih tinggi untuk menghindari hilangnya data (dalam kasus ini adalah angka setelah koma)

---

Sekarang, kita coba menambahkan string dengan integer, dan kita lihat bagaimana python menangani hal ini.

#### Contoh 2: Penjumlahan antara string (*higher data type*) dan integer (*lower data type*)
```
num_int = 123
num_str = "456"

print("Tipe data dari num_int:",type(num_int))
print("Tipe data dari num_str:",type(num_str))

print(num_int+num_str)
```

Ketika program diatas dijalankan, keluarannya akan seperti berikut:
```
Tipe data dari num_int: <class 'int'> 
Tipe data dari num_str: <class 'str'> 

Traceback (most recent call last): 
  File "python", line 7, in <module> 
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Dari program diatas,
- Kita menambahkan dua varibel `num_int` dan `num_str`
- Seperti yang bisa kita lihat pada keluarannya, kita mendapatkan `TypeError`. Python tidak dapat menggunakan konversi implisit dalam kondisi tersebut
- Namun, Python memiliki sebuah solusi untuk situasi semacam itu yang dikenal sebagai **Konversi Secara Explisit (*Explicit Conversion*)**


### Konversi secara Explisit (*Implicit Type Conversion*)

Pada konversi tipe data eksplisit, user mengkonversi tipe data dari sebuah objek ke tipe data yang dibutuhkan. Kita menggunakan fungsi yang sudah ditentukan sebelumnya seperti `int()`, `float()`, `str()`, dll untuk melakukan konversi eksplisit.

Tipe konversi seperti ini juga disebut dengan *Typecasting* karena user mengubah tipe data dari objek.

syntax:
```
<tipe_data_yang_diperlukan>(expression)
```
*Typecasting* dapat dilakukan dengan menetapkan fungsi tipe data yang diperlukan (seperti `int()`, dll) untuk expressi (misalnya "132.02")

#### Contoh 3: Penjumlahan antara string dan integer menggunakan konversi ekplisit
```
num_int = 123
num_str = "456"

print("Tipe data dari num_int:",type(num_int))
print("Tipe data dari num_str sebelum Type Casting:",type(num_str))

num_str = int(num_str)
print("Tipe data dari num_str sesudah Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Hasil Penjumlahan dari num_int dan num_str:",num_sum)
print("Tipe data dari hasil penjumlahan:",type(num_sum))
```

Ketika kita menjalankan kode diatas, maka keluarannya akan seperti berikut:
```
Tipe data dari num_int: <class 'int'>
Tipe data dari num_str sebelum Type Casting: <class 'str'>

Tipe data dari num_str sesudah Type Casting: <class 'int'>

Hasil Penjumlahan dari num_int dan num_str: 579
Tipe data dari hasil penjumlahan: <class 'int'>
```

Dari program diatas, 
- Kita menjumlahkan `num_str` dan `num_int`
- Kita mengkonversikan `num_str` dari string(*higher*) ke integer(*lower*) menggunakan fungsi `int()` untuk melakukan penjumlahan
- Setelah mengkonversi `num_str` ke sebuah nilai integer, Python bisa melakukan penjumlahan dari kedua variabel tersebut.
- Kita mendapatkan nilai `num_sum` dan tipe datanya adalah integer

### Point-Point Penting Untuk Diingat
1. Konversi Tipe Data adalah konversi sebuah objek dari satu tipe data ke tipe data lainnya
2. Konversi Implisit secara otomatis dilakukan oleh Interpreter Python
3. Python menghindari kehilangan data pada Konversi Implisit
4. Konversi Eksplisit juga dipanggil dengan *Type Casting*, tipe data dari objek dikonversikan dengan *predefined functions* oleh user
5. Pada *Type Casting*, kehilangan data mungkin terjadi saat kita melakukan konversi objek ke tipe data tertentu.