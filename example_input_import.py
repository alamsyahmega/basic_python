
# Import
import datetime
now = datetime.datetime.now()
now_year = str(now.year)
# Python Input

print("====> Python Input <====", end=('\n' * 2))

nama = input("Siapa nama kamu? ")
tahun_lahir = input("Kamu lahir tahun berapa? ")
sekolah = input("Kamu masih sekolah?")
umur = eval("{1} - {0}".format(tahun_lahir ,now_year))
sekolah = sekolah.lower()

print("Jadi nama kamu adalah {}".format(nama))
print(f"Umur kamu tahun ini adalah {umur}")
if sekolah == "masih":
    print("Kamu masih sekolah :D")
else:
    print("Kamu udah ga sekolah :(")