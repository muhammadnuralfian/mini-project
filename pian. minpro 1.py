while True:
    Nama = "muhammad Nur alfian"
    NIM = "2409116105"

    print("selamat datang di program ini")
    Nama = input("masukkan nama anda:")
    NIM = input("Masukkan nim:")

    if Nama == "muhammad nur alfian" and NIM == "2409116105":
        print("login berhasil selamat datang")
    else:
        print ("login gagal, Nama/Nim salah")

    print(f"halo {Nama}, selamat datang")

    gaji = float(input(" masukkan gaji: "))
    jam = float(input(" masukkan jam kerja:"))

    if jam > 160:
        Bonus = 0.1 * gaji 
        gaji += Bonus
        print(f"anda dapat bonus Rp.{Bonus}")
        print(f"Gaji yang anda terima adalah Rp.{gaji}")
    else: 
        print("Anda tidak mendapatkan bonus")
    
    ulang = input("mau ulang lagi ga program ini? ya/tidak ").lower()

    if ulang == "tidak": 
        print("kerja bagus Anak Buah")
        break
