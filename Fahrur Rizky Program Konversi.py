def konversi_biner(nilai):
    return bin(nilai)

def konversi_oktal(nilai):
    return oct(nilai)

def konversi_heks(nilai):
    return hex(nilai)

def main():
    nilai = int(input("Masukkan Nilai Desimal: "))

    biner = konversi_biner(nilai)
    oktal = konversi_oktal(nilai)
    heks = konversi_heks(nilai)

    print("Nilai Biner          :", biner)
    print("Nilai Oktal          :", oktal)
    print("Nilai Heksadesimal   :", heks)

if __name__ == "__main__":
    main()
