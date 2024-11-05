# Base class: Atlet
class Atlet:
    def __init__(self, nama, usia, jenis_kelamin):
        self.nama = nama                       # Public attribute
        self._usia = usia                    # Protected attribute
        self.__jenis_kelamin = jenis_kelamin # Private attribute

    # Getter dan Setter untuk usia
    def get_usia(self):
        return self._usia

    def set_usia(self, usia):
        self._usia = usia

    # Getter untuk jenis kelamin
    def get_jenis_kelamin(self):
        return self.__jenis_kelamin

    # Method untuk menampilkan info atlet
    def info(self):
        return (f"Nama: {self.nama}, Usia: {self._usia}, Jenis Kelamin: {self.__jenis_kelamin}")


# Derived class: Perenang
class Perenang(Atlet):
    def __init__(self, nama, usia, jenis_kelamin, gaya, rekor):
        super(). __init__(nama, usia, jenis_kelamin)
        self._gaya = gaya               # Protected attribute untuk gaya renang
        self.__rekor = rekor            # Private attribute untuk rekor waktu renang

    # Getter dan Setter untuk gaya
    def get_gaya(self):
        return self._gaya

    def set_gaya(self, gaya):
        self._gaya = gaya

    # Getter untuk rekor
    def get_rekor(self):
        return self.__rekor

    # Setter untuk rekor dengan validasi
    def set_rekor(self, rekor):
        self.__rekor = rekor

    # Method untuk menampilkan info perenang
    def info(self):
        return (f"{super().info()}, Gaya: {self._gaya}, Rekor: {self.__rekor} detik")


# Contoh penggunaan
atlet1 = Atlet("Arianto", 25, "Laki-laki")
print(atlet1.info())  # Output: Nama: Arianto, Usia: 25, Jenis Kelamin: Laki-laki

# Menggunakan setter untuk mengubah usia
atlet1.set_usia(30)
print(atlet1.info())  # Output: Nama: Arianto, Usia: 30, Jenis Kelamin: Laki-laki

# Perenang
perenang1 = Perenang("Dina", 22, "Perempuan", "Gaya Bebas", 56.7)
print(perenang1.info())  # Output: Nama: Dina, Usia: 22, Jenis Kelamin: Perempuan, Gaya: Gaya Bebas, Rekor: 56.7 detik

# Menggunakan setter untuk mengubah rekor
perenang1.set_rekor(55.3)
print(perenang1.info())  # Output: Nama: Dina, Usia: 22, Jenis Kelamin: Perempuan, Gaya: Gaya Bebas, Rekor: 55.3 detik
