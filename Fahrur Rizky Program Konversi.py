bilangan = int(input("Masukkan Bilangan Yang Ingin Dikonversi: "))

konversi1 = bin(bilangan)[2:].zfill(8)
konversi2 = hex(bilangan)
konversi3 = oct(bilangan)

print("Bilangan Biner       : ", konversi1)
print("Bilangan Hexadecimal : ", konversi2)
print("Bilangan Octal       : ", konversi3)