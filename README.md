# Python Operator

Pada sesi kali ini, kamu akan mempelajari semua tentang perbedaan antara tipe-tipe operator di Python, sintaks operator dan bagaimana cara menggunakannya

## Apa itu Python Operator

Operator adalah spesial simbol di Python yang menjalankan komputasi aritmatik dan logika. Nilai dari operator disebut dengan operand.
Contoh:
```
>>> 2+3
5
```
Disini, `+` adalah operator yang melakukan penjumlahan. `2` dan `3` merupakan operand dan `5` adalah keluaran dari operasi tersebut.

## Operasi Aritmatika

Operasi aritmatika digunakan untuk melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dll.

| Operator | Arti | Contoh |
| -------- | ---- | ------ |
| + | Menambahkan dua operand atau *unary plus* | x + y + 2 |
| - | Mengurangi operand kanan dari kiri atau *unary minus* | x - y - 2 |
| * | Mengalikan dua operand | x * y |
| / | Membagi operang kiri oleh operand kanan (hasilnya selalu float) | x / y |
| % | Modulus - sisa pembagian operand kiri oleh operand kanan | x % y (sisa bagi x/y)
| // | Floor division - pembagian yang menghasilkan bilangan bulat disesuaikan ke kiri di garis bilangan | x // y |
| ** | Exponen - Operand kiri pangkat operand kanan | x ** y (x pangkat y) |

#### Contoh 1: Operasi Aritmatika di Python
```
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)
```

Ketika program dijalankan, keluarannya akan seperti berikut:
```
x + y = 19
x - y = 11
x * y = 60
x / y = 3.75
x // y = 3
x ** y = 50625
```

