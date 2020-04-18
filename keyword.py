# ada beberapa keyword di python 3
# disini akan menjelaskan pengertian dan contohnya


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
print("\n" * 5)




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
print("\n" * 5)




# =============== ==> and, or, not <== =============== #
penjelasan = """
'and, or, not' adalah operasi logika dalam python, seperti halnya pada gerbang logika, terdapat &&, ||, !=

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

1.3 Tabel 'not' atau !=
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
print("\n" * 5)

# =============== ==> None <== =============== #
# =============== ==> End <== =============== #

# =============== ==> None <== =============== #
# =============== ==> End <== =============== #

# =============== ==> None <== =============== #
# =============== ==> End <== =============== #

# =============== ==> None <== =============== #
# =============== ==> End <== =============== #

# =============== ==> None <== =============== #
# =============== ==> End <== =============== #

# =============== ==> None <== =============== #
# =============== ==> End <== =============== #

# =============== ==> None <== =============== #
# =============== ==> End <== =============== #

# =============== ==> None <== =============== #
# =============== ==> End <== =============== #

# =============== ==> None <== =============== #
# =============== ==> End <== =============== #

# =============== ==> None <== =============== #
# =============== ==> End <== =============== #