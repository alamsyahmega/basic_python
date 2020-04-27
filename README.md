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
-----

## Operator Pembanding

Operator pembanding (*comparison operator*) digunakan untuk membandingkan nilai-nilai. Ini akan menghasilkan keluaran berupa `True` atau `False` berdasarkan kondisinya.

| Operator | Arti | Contoh |
| -------- | ---- | ------ |
| > | Lebih besar dari - True jika operand kiri lebih besar daripada yang kanan | x > y |
| < | Lebih kecil dari - True jika operand kiri lebih kecil daripada yang kanan | x < y |
| == | Sama dengan - Benar jika kedua operand nilainya sama | x == y |
| != | Tidak sama dengan - True jika operand tidak sama | x != y |
| >= | Lebih besar sama dengan - True jika operand kiri lebih besar atau sama dengan operand kanan | x >= y |
| <= | Lebih kecil sama dengan - True jika operand kiri lebih kecil atau sama dengan operand kanan | x >= y |

#### Contoh 2: Operaor Pembanding di Python
```
x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)
```
Output:
```
x > y is False
x < y is True
x == y is False
x != y is True
x >= y is False
x <= y is True
```

## Operasi Logika

Logika operasi adalah operator `and` , `or` dan `not`.

| Operator | Arti | Contoh |
| -------- | ---- | ------ |
| and | True jika kedua operand adalah true atau 1 | x and y  |
| or | True jika diantara operand adalah true atau 1 | x or y |
| not | not | True jika operand sama dengan false (melengkapi operand) | not x |

#### Contoh 3: Operator Logika di Python
```
x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)
```
Output:
```
x and y is False
x or y is True
not x is False
```

## Operator Bitwise

Operator bitwise bertindak sebagai operand seolah-olah mereka adalah string dari binary. Mereka beroperasi bit demi bit, itulah mengapa dinamakan bitwise.

Contohnya, 2 adalah `10` di dalam biner dan 7 adalah `111`


__Pada Tabel di bawah__: let `x = 10`(0000 1010 pada biner) dan `y = 4`(0000 0100 pada biner)

| Operator | Arti | Contoh |
| -------- | ---- | ------ |
| `&` | Bitwise AND | `x & y = 0 (0000 0000)` |
| `\|` | Bitwise OR | `x \| y = 14 (0000 1110)` |
| `~` | Bitwise NOT | `~x = -11 (1111 0101)` |
| `^` | Bitwise XOR | `x ^ y = 14 (0000 1110)` |
| `>>` | Bitwise right shift | `x >> 2 = 2 (0000 0010)` |
| `<<` | Bitwise left shift | `x << 2 = 40 (0010 1000)` |


## Operator Penugasan (*Assignment Operator*)

Operator penugasan digunakan di Python untuk menugaskan atau memasukkan nilai pada variabel.

`a = 5` adalah contoh sederhana dari operator penugasan yang menugaskan nilai 5 dikanan menjadi nilai variable a dikiri.

Ada beberapa operator gabungan di Python seperti `a += 5` yang menambahkan variabel kemudian menetapkan nilai yang sama. ini sama dengan `a = a + 5`.


| Operator | Contoh | Sama dengan |
| -------- | ------ | ----------- |
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `//=` | `x //= 5` | `x = x // 5` |
| `**=` | `x **= 5` | `x = x ** 5` |
| `&=` | `x &= 5` | `x = x & 5` |
| `\|=` | `x \|= 5` | `x = x \| 5` |
| `^=` | `x ^= 5` | `x = x ^ 5` |
| `>>=` | `x >>= 5` | `x = x >> 5` |
| `<<=` | `x <<= 5` | `x = x << 5` |


## Operator Spesial (*Special Operator*)

Bahasa Python menawarkan beberapa spesial operator seperti operator identitas (*identity operator*) atau operator keanggotaan (*membership operator*). Operator-operator tersebut akan dibahas dibawah dengan contohnya.


### Operator Identitas (*Identity Operator*)
`is` dan `is not` merupakan operator identitas di Python. Mereka digunakan untuk mengecek apakah dua nilai (atau variabel) disimpan pada memory yang Sama. Dua variabel yang sama tidak menyiratkan mereka identik.


| Operator | Arti | Contoh |
| -------- | ---- | ------ |
| `is` | True jika operand identik (mengacu pada objek yang sama) | x is True |
| `is not` | True jika operand tidak identik (tidak mengacu pada objek yang sama) | x is not True |

#### Contoh 4: Opetor identitas di Python
```
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)
```
Output:
```
False
True
False
```

Disini, dapat kita lihat bahwa `x1` dan `y1` adalah integer dengan nilai yang sama, sehingga mereka sama dan identik. Sama seperti pada kasus `x2` dan `y2`(string).

Tapi `x3` dan `y3` merupakan list. mereka sama tapi tidak identik. Itu karena Interpreter menyimpan mereka secara terpisah pada memory meskipun mereka sama.

-------

### Operator Keanggotaan (*Membership Operator*)
`in` dan `not in` merupakan operator keanggotaan di Python. Keduanya digunakan untuk melakukan tes apakan sebuah nilai atau variabel ditemukan pada sebuah *sequence*(_**string, list, tuple**_ dan _**dictionary**_ ).

Dalam *dictionary* kita hanya bisa melakukan tes untuk ada tidaknya dari *key*, bukan *value*-nya.

| Operator | Arti | Contoh |
| -------- | ---- | ------ |
| `in` | True jika *value/variable* ditemukan pada *sequence* | 5 in x|
| `not in` | True jika *value/variable* tidak ditemukan pada *sequence* | 5 not in x|

#### Contoh 5: Membership Operator di Python
```
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)
```
Output:
```
True
True
True
False
```
Disini, `H` ada pada `x` tapi `hello` tidak ada pada `x`(ingat, Python memperhatikan *case sensitive*). Sama halnya, `1` adalah key dan `a` adalah nilai dari *dictionary* `y`. Karenanya, `a in y` me-return nilai `False`.