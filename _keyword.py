# ada beberapa keyword di python 3
# disini akan menjelaskan pengertian dan contohnya
import keyword
print("list dari keyword adalah: ","\n", keyword.kwlist, "\n"*4)

# =============== ==> True and False <== =============== #

penjelasan = """
True dan False (dengan Capitalize) adalah nilai kebenaran dalam python
Mereka ini adalah hasil operasi perbandingan pada dan operasai logika(Boolean)
"""

# Contohnya
a = 10 > 9 # True
b = 11 < 10 # False
# contoh dalam perbandingan dan operasi logika
if 10 > 11:
    print('Salah') # atau lakukan hal lain
if a == True: # membandingkan apabila variable "a" sama dengan True, maka operasi dalam "if" akan dijalankan
    print(a) # akan True
    a = False # merubah isi a menjadi false
    print(a) # akan False
# contoh menggunakan while 
var = 0 # deklarasi variable dengan nama var
while var < 3: # perbandingan var terhadap angka 3
    print('var lebih kecil dari 3') # jika benar atau "True" maka akan dijankan
    var += 1 # menambahkan var dengan angka 1

# dalam python, True juga berarti == 1 dan False == 0, sebagai contoh
print("hasil 1 == True adalah:", 1 == True) # True, karena 1 adalah True
print("hasil 1 == False adalah:", 1 == False) # False, karena 1 tidak sama dengan False
print("hasil 0 == False adalah:", 0 == False) # True, karena 0 adalah False


# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> None <== =============== #

penjelasan = """
'None' adalah konstanta khusus dalam python yang merepresentasikan ketidakadaan nilai
atau nilai sama dengan null

'None' adalah sebuah objek dengan tipe data tersendiri, yaitu NoneType.
Kita tidak bisa membuat multiple None objek, tetapi 'None' bisa dimasukkan kedalam nilai
suatu variabel. misalnya 'a = None' atau 'null = None'.

Kita harus berhati-hati, None tidak sama dengan False, 0, atau array/list kosong, dictionary
kosong, ataupun string kosong, dll.
"""
# Contoh
print("hasil None == 0  adalah: ", None == 0) # False, karena None tidak sama dengan 0
print("hasil None == []  adalah: ", None == []) # False, karena None tidak sama dengan list kosong
print("hasil None == {}  adalah: ", None == {}) # False, karena None tidak sama dengan dictionary kosong
print("hasil None == ""  adalah: ", None == "") # False, karena None tidak sama dengan string kosong
print("hasil None == None  adalah: ", None == None) # True, karena None sama dengan None

# dalam kasus lain, pada sebuah fungsi void atau fungsi yang tidak mengembalikan apapun (tanpa return)
# maka apabila kita mengeprint() fungsi tersebut (bisa juga dijadikan sebagai value dari variable) maka
# fungsi tersebut akan mengembalikan nilai None, walaupun didalamnya terdapat operasi apapun itu. Contoh:

def a_void_function():
    a = 1
    b = 2
    c = a + b
    c += 1

print("hasil print() a_void_function() adalah: ", a_void_function()) # None, karena fungsi tidak mengembalikan nilai apapun
# contoh lain
def improper_return_function(a):
    if (a % 2) == 0:
        return True

print("hasil print() improper_return_function(10) adalah: ", improper_return_function(10)) # True, karena a dibagi 2 sisa 0, dan me-return True
print("hasil print() improper_return_function(11) adalah: ", improper_return_function(11)) # None, karena a dibagi 2 sisa 1, dan tidak me-return apa-apa a.k.a None

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> and, or, not <== =============== #

penjelasan = """
'and, or, not' adalah operasi logika dalam python, seperti halnya pada gerbang logika, terdapat &&, ||, !

1. Logika 'and' akan me-return True atau 1 apabila kedua operand yang dibandingkan adalah True atau 1.

1.1 Tabel 'and' atau &&
-------------------------------
|   A   |   B   |   A and B   |
-------------------------------
| True  | True  |    True     |
| True  | False |    False    |  
| False | True  |    False    |
| False | False |    False    |
-------------------------------


2. Logika or akan me-return True apabila salah satu operand bernilai True

1.2 Tabel 'or' atau ||
-------------------------------
|   A   |   B   |   A and B   |
-------------------------------
| True  | True  |    True     |
| True  | False |    True     |  
| False | True  |    True     |
| False | False |    False    |
-------------------------------


2. Logika 'not' atau tidak sama dengan adalah kebalikan dari kebenaran nilai.

1.3 Tabel 'not' atau !
-------------------------------
|      A     |      not A     |
-------------------------------
|    True    |      False     |
|    False   |      True      |
-------------------------------
"""
print("True and False adalah:", True and False) # False
print("True and True adalah:", True and True) # True
print("True or False adalah:", True or False) # True
print("False or False adalah:", False or False) # False
print("not False adalah:", not False) # True
print("not True adalah:", not True) # False

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> as <== =============== #

penjelasan = """
'as' digunakan untuk membuat sebuah alias ketika saat mengimport modul, Itu berarti
memberikan nama yang berbeda (yang ditentukan pengguna) ke modul saat mengimportnya

Sebagai contoh kita akan mengimpot sebuah modul bernama 'time' lalu kita gunakan
'as' untuk memberikan nama yang berbeda yaitu waktu. maka akan menjadi seperti ini:
'import time as waktu'
"""
# Contoh
import time as waktu
print("waktu sekarang dalam format time-stamp adalah:", waktu.time()) # mendapatkan waktu sekarang dengan format timestamp\

import math as matematika # mengimport math dengan nama matematika
print("cosinus phi adalah:", matematika.cos(matematika.pi)) # -1.0

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> assert <== =============== #

penjelasan = """
'assert' digunakan untuk tujuan debugging.

Saat memprogram, terkadang kita ingin mengetahui keadaan internal atau memeriksa
apakah asumsi kita benar. 'assert' membantu kita untuk melakukannya dan menemukan
bug lebih nyaman. 'assert' diikuti oleh suatu kondisi.

Jika kondisinya benar, maka tidak akan ada yang terjadi. Tapi jika kondisinya salah,
maka 'AssertionError' akan dinaikkan.
"""
# contoh
a = 10
assert a > 5 # tidak akan terjadi apa2
# assert a < 10, "nilai a lebih kecil dari 10" # <== akan error AssertionError dengan message "nilai a lebih kecil dari 10"
# note: dijadikan komentar agar yang bawah masih jalan, silahkan untuk di uncomment sendiri

# untuk pehaman lebih baik "assert kondisi, pesan" atau "assert condition, message"
# sama dengan
# if not a < 10:
#     raise AssertionError("a sama dengan 10")

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> async, await <== =============== #

penjelasan = """
'async' dan 'await' adalah keyword yang disediakan oleh library python yaitu asyncio.
Mereka digunakan untuk menulis kode secara bersamaan/mengeksekusi secara asyncronus
"""
print(penjelasan)
import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(0.1) # menunggu 0.1 detik sebelum print("world") dijalankan
    print("World")

loop = asyncio.get_event_loop()
loop.run_until_complete(main()) # blocking
# Note: pembahasan selanjutnya akan dijelaskan lebih terperinci di bagian yang terpisah

# =============== ==> End <== =============== #
print("\n" * 3)



# =============== ==> break, continue <== =============== #

penjelasan = """
'break, continue' digunakan didalam perulangan baik for-loop maupun while-loop untuk
mengubah prilaku normal dari mereka (perulangannya).

'break' akan mengakhiri loop terkecil (apabila ada loop didalam loop) dan akan melanjutkan
pernyataan dibawah loopnya, karena loopnya telah berakhir (akibat break).
'continue' akan mengakhiri iterasi saat loop, tetapi tidak mengakhiri loopnya, dia akan mengakhiri
hanya dikeadaan tertentu (yang telah ditentukan oleh pengguna/pemrogram)
"""

# Contoh
for x in range(1,4): # loop 1
    for z in range(0, 10): # loop 2
        if z == 3: # Jika z == 3, maka loop 2 akan diakhiri
            break # break untuk mengakhiri loop
        print(z, end=" ")
    if x == 2: # Jika x == 2 atau saat x = 2, print(", x adalah:", x) tidak akan dieksekusi dan loop berlanjut
        continue # continue untuk mengakhiri loop saat x = 2, lalu loop dilanjukan ke x = 3
    print(", x adalah:", x)

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> class <== =============== #
penjelasan = """
'class' digunakan untuk mendefinisikan sebuah kelas yang telah ditentukan oleh programmer.

'class' ini merupakan kumpulan atribut dan metode terkait yang mencoba merepresentasikan
dunia nyata. Gagasan menempatkan data dan fungsi/metode bersama-sama dalam 'class' adalah 
inti dari konsep pemrograman berorientasi objek atau OOP

Kelas dapat didefinisikan dimana saja dalam suatu program, tetapi best-practice-nya adalah
hanya mendefinisikan satu kelas untuk sebuah modul.

Mendefinisikan 'class' biasanya menggunakan Capitalize atau huruf awal dari 'class' adalah
huruf kapital
"""
# Contoh:
class ExampleClass:
    x = 10
    
    def __init__(self, name): 
        self.name = name
    
    def method_call_name(self):
        print("Hello my name is {}".format(self.name))
    
ex = ExampleClass("Bejon") # memanggil class ExampleClass ke dalam ex dengan parameter nama = "Bejon"
print("x dalam ExampleClass adalah: ", ex.x) # print ex.x yaitu x = 10
ex.method_call_name() # memanggil method
# print

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> def <== =============== #
penjelasan = """
'def' adalah kata kunci untuk mendefinisikan sebuah fungsi. Fungsi ini merupakan
suatu blok pemrograman yang dimaksudkan untuk melakukan suatu tugas tertentu dan biasanya
tugas tersebut dilakukan secara berulang (jadi tidak perlu 2x menulis program yang sama)

Untuk penjelasan mendalam akan dijelaskan pada bagian terpisah
"""
def selamat_pagi(name="Sony"):
    print("Selamat pagi {}".format(name))

selamat_pagi("Cecil") # memanggil fungsi dengan argument "Cecil"
# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> del <== =============== #
penjelasan = """
'del' digunakan untuk menghapus referensi ke suatu objek. Semuanya objek dalam python.
Kita bisa menghapus sebuah variable dengan 'del'
"""
# contoh
variable = 10
del variable

if "variable" in globals():
    print('ada variabel dengan nama variabel')
else:
    print('tidak ada variabel dengan nama variabel')

# contoh lain
arr = [1 , 2 , 3]
del arr[1]
print("arr sekarang adalah:", arr) # [1,3], karena 2 telah dihapus

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> if, else, elif <== =============== #
penjelasan = """"
'if, else, elif' digunakan untuk percabangan bersyarat atau pengambilan keputusan

Saat kita ingin menjalankan blok pemrograman pada kondisi tertentu, maka menggunakan
pernyataan 'if'. Jika kita ingin menjalankan blok pemgrograman pada kondisi tertentu yang
tidak memenuhi kondisi pertama atau cabang kondisi lain, maka menggunakan pernyataan 'elif'
atau dengan nama lain 'else if'. Dan apabila ingin menjalankan blok permrograman saat
kondisi-kondisi yang telah ditentukan tidak terpenuhi, maka menggunakan pernyataan 'else'.
"""
# contoh
def if_elif_else_example(number):
    if number <= 10:
        print("number is 10 or under 10")
    elif number > 10 and number <= 20:
        print("number is in range 11 - 20")
    else:
        print("number is above 20")

if_elif_else_example(1) 
if_elif_else_example(11)
if_elif_else_example(110)

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> except, raise, try <== =============== #

penjelasan = """
'except, raise, try' digunakan dengan 'Exception' dalam python.

'Exception' pada dasarnya adalah error yang menunjukkan ada kesalahan saat
menjalankan program kita. IOError, ValueError, ZeroDivisionError, ImportError,
NameError, TypeError, dll. adalah beberapa contoh 'Exception' dalam python.
try-except blok digunakan untuk 'menangkap' pengecualian/exception di python.
"""
# contoh

def pembagian(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "Tidak bisa dibagi dengan 0"

print(pembagian(10,0)) # Tidak bisa dibagi dengan 0
print(pembagian(10,4)) # 2.5

# kita juga bisa menggunakan raise error:
def pembagian_20_dengan_pembagi(pembagi):
    if pembagi == 0:
        raise ZeroDivisionError('tidak dapat dibagi dengan 0 !')
    else:
        return 20 / pembagi

print(pembagian_20_dengan_pembagi(10))
# print(pembagian_20_dengan_pembagi(0)) # akan ada error ZeroDivisionError
# boleh dicoba dengan un-commentar

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> finally <== =============== #
penjelasan = """
'finally' merupakan bagian dari try-except, dimana finally biasanya digunakan
untuk menutup resource atau aliran file (seperti open(), kemudian di .close())

'finally' akan dijalankan apapun yang terjadi, meskipun ada 'Exception' yang
tidak tertangani.
Penjelasan mengenai handling error atau exception akan dijelaskan pada bagian khusus.
"""
# contoh
def finally_example():
    try:
        f = open('keyword.txt', encoding='utf-8')
        # perfome file operation
    finally:
        f.close()

finally_example()

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> for <== =============== #
penjelasan = """
for digunakan untuk perulangan, umumnya digunakan ketika kita tahu berapa
kali kita ingin mengulang. (sebagai conton menggunakan for x in range())

Didalam python kita juga bisa melakukan perulangan untuk semua jenis urutan
seperti daftar(list) ataupun string.
"""
# contoh
for x in range(0,3):
    print("x bernilai : ", x)

# atau
for x in ['Ana', 'Bob', 'Carlsen', 'David', 'Evelyn', 'Fabiano', 'Galardia']:
    print(x, end=" ")

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> from, import <== =============== #
penjelasan = """
'import' digunakan ketika kita ingin mengimport modul, library, ataupun mengakses
file python lain baik di derektori maupun diluar direktori. sekarang apa fungsi dari
from ... import ... ? 
Seperti yang sudah kita tahu, untuk mengakses suatu modul kita perlu meng-importnya,
sebagai contoh kita ingin menggunakan fungsi cos() ataupun pi. Maka yang dilakukan
adalah import math, kemudian menggunakan math.cos() dan math.pi.
Tetapi apabila kita hanya ingin mengimport fungsi tertentu saja (semisal hanya cos() saja),
maka yang harus dilakukan adalah 'from math import cos'. Jadi hanya fungsi cos() yang di-
import, dan untuk menggunakannya hanya tinggal memangging fungsinya yaitu cos(), bukan math.cos()
"""
# contoh
import math # mengimport math
from math import pi # menggunakan from untuk mengimport pi saka
nilai_cos_phi = math.cos(pi) # pi tanpa math.pi
print("nilai cos phi adalah: {}".format(nilai_cos_phi))

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> global <== =============== #
penjelasan = """
'global' digunakan untuk menyatakan bahwa variabel didalam fungsi adalah global
(diluar fungsi). Jika kita perlu membaca nilai variabel global, kita tidak perlu
mendefinisikannya sebagai global (ini perlu dipahami)

ini penting: Jika kita perlu untuk memodifikasi nilai variabel global didalam suatu
fungsi, maka kita perlu mendeklarasikannya dengan global. Kalau tidak, variabel lokal
dengan nama yang sama dengan variabel global akan terdeklarasi sebagai variabel baru
di lokal.
"""
# contoh
var_global = 10 # nilai variabel awal : 10
def read_var():
    print("nilai var_global adalah :", var_global)

def write1(): # fungsi mengubah nilai var_global
    global var_global # mengakses variabel global
    var_global = 20

def write2(): # fungsi mengubah nilai var_global tanpa mengakses variabel global
    var_global = 15

read_var() # nilai awal = 10
write1() # mengganti nilai jadi 20
read_var() # nilai = 20
write2() # mengganti nilai jadi 15, tetapi karena tanpa keyword global, jadi mendeklarasikan variabel baru
read_var() # nilai tetap = 20

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> in <== =============== #
penjelasan = """
'in' digunakan untuk menguji apakah suatu sequence (list, tuple, string)
berisi nilai tertentu. Akan mereturn True apabila ada, dan False apabila tidak ada.

Penggunakan selanjutnya adalah untuk melintasi urutan dalam sebuah for-loop
"""
# contoh
sebuat_list = ['Arda', 'Baladewa', 'Cruax', 'Devidena', 'Efrat', 'Flux']
print("apakah 'Raya' in sebuah_list? :", 'Raya' in sebuat_list) # False
print("apakah 'Arda' in sebuah_list? :", 'Arda' in sebuat_list) # True

# atau bisa digunakan untuk percabangan
if 'Arda' in sebuat_list:
    print('Ada pada list')
else:
    print('Tidak ada pada list')

# untuk for-loop
for x in sebuat_list:
    print(x, end=", ")

# =============== ==> End <== =============== #
print("\n" * 30)




# =============== ==> is <== =============== #
penjelasan = """
'is' digunakan untuk menguji identitas objek. Sementara operator == digunakan untuk
menguji apakah dua variabel bernilai sama atau tidak. 'is' digunakan untuk menguji
apakah dua variabel merujuk ke objek yang sama.
me-return True apabila objek identik, dan False apabila tidak.

*list '[]' dan dictionary kosong '{}' sama dengan dictionary atau list kosong lainnya. Tetapi mereka
bukan objek yang identik, karena mereka berada secara terpisah didalam memory (bukan
pada memory yang sama). Ini karena list dan dictionary dapat berubah nilai(mutable)

*string dan tuple tidak dapat dirubah(immutable). Oleh karena itu, dua string atau dua tuple yang bernilai sama
masing-masing dari mereka identik satu sama lain. Karena mereka merujuk ke memory yang sama.
"""
# contoh
print("True is True? :", True is True)
print("False is False? :", False is False)
print("None is None? :", None is None)
print("{} is {} ? :", {} is {}, ", {} == {} ? :", {} == {})
print("[] is [] ? :", [] is [], ", [] == [] ? :", [] == [])
print("() is () ? :", () is (), ", () == () ? :", () == ())
print("empty-string is empty-string ? :", '' is '', ", empty-string == empty-string  ? :", '' == '')

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> lambda <== =============== #
penjelasan = """
'lambda' merupakan sebuah fungsi anonim atau sering disebut 'function expression'
yang tidak mengandung pernyataan 'return'. lambda merupakan fungsi sebaris
yang sudah terdiri dari sebuah expression yang divaluasi dan dikembalikan. (tidak perlu
di return karena sudah direturn)
lambda terdiri dari list parameter dan expression, atau:
var = lambda parameter_list: expression
"""
# contoh
lambda_example = lambda x : x + 1
for i in range(0,4):
    print(f"i ke-{i}, nilai lambda={lambda_example(i)}",end=", " )

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> nonlocal <== =============== #
penjelasan="""
penggunaan 'nonlocal' sangat mirip denga 'global'. nonlocal digunakan untuk menyatakan
bahwa variabel didalam fungsi bersarang (fungsi didalam fungsi) tidak bersifat lokal, artinya
terletak pada fungsi diluarnya. Jika kita perlu memodifikasi nilai variabel non-lokal, maka
kita harus mendeklarasikannya dengan 'nonlocal'. Kalau tidak, variabel lokal dengan nama tersebut
akan terdefinisi didalam fungsinya(fungsi yang didalam fungsi)
"""
print("contoh dengan nonlokal")
def outer_function():
    m = 10
    print(f"Outer function before: {m}")
    def inner_function():
        nonlocal m
        m = 15
        print(f"Inner function: {m}")
    inner_function()
    print(f"Outer function after: {m}")

outer_function()
print("\n")

print("contoh tanpa nonlokal")
def _outer_function():
    m = 10
    print(f"Outer function before: {m}")
    def inner_function():
        m = 15
        print(f"Inner function: {m}")
    inner_function()
    print(f"Outer function after: {m}")

_outer_function()
# silahkan untuk berspekulasi sendiri kenapa bisa terjadi
# note: nonlokal bukan berarti mengambil variabel global ya

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> pass <== =============== #
penjelasan = """
'pass' adalah null statement di python. Tidak ada yang terjadi ketika itu dieksekusi.
'pass' digunakan sebagai placeholder.

Sebagai contoh kita ingin membuat sebuah fungsi tanpa mengeksekusi apa-apa. apila hanya
dibuat seperti ini:

def fungsi(args):

maka akan terjadi 'IndentationError'. sebagai gantinya, menggunakan pass untuk mencegah
adanya error tersebut. Contohnya seperti berikut:

def fungsi(args):
    pass

Kita juga bisa menggunakan hal yang sama untuk sebuah 'class'

class Kelas:
    pass

"""
print(penjelasan)
# contoh
def fungsi_contoh():
    pass

fungsi_contoh() # tidak akan mengeksekusi apa-apa

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> return <== =============== #
penjelasan="""
'return' statement digunakan didalam fungsi untuk keluar dari fungsi dan mengembalikan
nilai dari fungsi tersebut. Apabila tidak menggunakan return secara eksplisit, maka fungsi
akan mengembalikan nilai 'None' secara otomatis.
"""
# contoh
def func_return():
    a = 11
    return a

def func_no_return():
    a = 15

print("fungsi dengan return: ", func_return())
print("fungsi tanpa return: ", func_no_return())

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> while <== =============== #
penjelasan="""
'while' digunakan untuk for-loop.
statement didalam while akan terus dijalankan secara berulang sampai kondisi untuk
'while' sama dengan False atau menggunakan 'break' statement.
note: 0 sama dengan False
"""
# contoh
i = 5
while(i):
    print("i adalah:", i)
    i -= 1

# =============== ==> End <== =============== #
print("\n" * 3)




# =============== ==> with <== =============== #
# =============== ==> End <== =============== #

# =============== ==> yield <== =============== #
# =============== ==> End <== =============== #
