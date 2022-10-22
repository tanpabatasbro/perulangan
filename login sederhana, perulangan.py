nama = "kaco"
sandi = "1234"
lagi = "iya"
a = 4

while lagi == "iya":
    user_name = str(input("masukkan  user  name :"))
    password = str(input("masukkan password :"))
    if user_name == nama and password == sandi :
        print("anda berhasil login")
        break 
    else:
        print("user name atau password yang anda masukkan salah")
    a = a-1
    if a == 0:
        print("kesempatan login saat ini sudah habis silahka coba lagi besok")
        break
    print()
    print("percobaan login tersisa :", a)
    lagi = str(input("ingin mencoba login ulang? iya/tidak:"))
    print()
