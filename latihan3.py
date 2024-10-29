# Inisialisasi saldo awal
saldo = 1000000

while True:
    # Tampilkan saldo dan menu
    print(f"Saldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    
    # Minta input pilihan menu
    pilihan = input("Pilih menu (1/2): ")
    
    # Proses berdasarkan pilihan
    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah penarikan: "))
        # Cek apakah saldo mencukupi
        if jumlah <= saldo:
            saldo -= jumlah
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak mencukupi!")
            
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    
    else:
        print("Pilihan tidak valid!")