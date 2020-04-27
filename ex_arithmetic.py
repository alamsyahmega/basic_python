# Example of arithmetic operator



# Definisi variable
a = 10
b = 20
c = 30
d = 40
e = 50

pkt = 3

print("""
Defined variable
a = 10
b = 20
c = 30
d = 40
e = 50
pkt = 3
	""")

# Penjumlahan
print("<== Penjumlahan ==>")
f = a + e
g = c + d
print("a + e =",f)
print("c + d =",g)
print("", end=("\n" * 3))


# Pengurangan
print("<== Pengurangan ==>")
k = e - a
l = a - c
print("e - a =",k)
print("a - c =",l)
print("", end=("\n" * 3))


# Perkalian
print("<== Perkalian ==>")
m = b * c
n = d * e
print("b * c =",m)
print("d * e =",n)
print("", end=("\n" * 3))


# Pembagian
print("<== Pembagian ==>")
o = d / b
p = e / a
print("d / b =",o)
print("e / a =",p)
print("", end=("\n" * 3))


# Modulus
print("<== Modulus ==>")
q = e % b
r = c % b
print("e % b =", q)
print("c % b  =", r)
print("", end=("\n" * 3))


# Floor Division / Pembagian floor
print("<== Floor Division ==>")
s = e // d
t = e // c
print("e // d =", s)
print("e // c =", t)
print("", end=("\n" * 3))


# Exponent / Pangkat
print("<== Pangkat ==>")
u = a ** pkt
v = b ** pkt
print("a ** pkt =", u)
print("b ** pkt =", v)
print("", end=("\n" * 3))
