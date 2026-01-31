# 1) PROGRAM MEMBALIK STRING
def balik_string(s: str) -> str:
    return s[::-1]

# contoh penggunaan
if __name__ == "__main__":
    teks = input("Masukkan string: ")
    print("Hasil dibalik:", balik_string(teks))

print("\n")
# 2) PROGRAM MENGHAPUS SEMUA KEMUNCULAN TARGET DARI LIST
def hapus_semua(data: list, nilai) -> list:
    """Kembalikan list baru tanpa elemen yang sama dengan nilai."""
    return [x for x in data if x != nilai]

# contoh penggunaan
if __name__ == "__main__":
    raw = input("Masukkan elemen list dipisah koma ( a,b,c,a): ").strip()
    # ubah input menjadi list (tanpa spasi berlebih)
    lst = [item.strip() for item in raw.split(",") if item.strip() != ""]
    target = input("Masukkan nilai yang ingin dihapus: ").strip()
    hasil = hapus_semua(lst, target)
    print("List setelah penghapusan:", hasil)

print("\n")
# 3) PROGRAM MENGGABUNGKAN LIST MENJADI KALIMAT

# Langkah 1: Input berupa string daftar kata
raw = input("Masukkan kata-kata (pisahkan dengan koma): ")

# Langkah 2: Mengubah input menjadi list
words = [w.strip() for w in raw.split(",")]

# Langkah 3: Gabungkan dengan pemisah spasi
# " ".join(list) menggabungkan setiap elemen list dengan spasi di antaranya
hasil = " ".join(words)

# Langkah 4: Tampilkan hasil
print("Hasil gabungan:", hasil)
