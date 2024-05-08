import hashlib
from tabulate import tabulate

def HashAnalyer(): 
    def print_hash_info(hash_value, hash_type):
        # Mendapatkan informasi tentang panjang hash, jenis hash, dan karakter hash
        hash_length = len(hash_value)
        bit_length = hash_length * 4  # Karena setiap karakter hex setara dengan 4 bit
        character_type = "hexadecimal"

        # Menampilkan informasi hash
        print(tabulate([
            ["Hash", hash_value],
            ["Hash type", hash_type],
            ["Bit length", bit_length],
            ["Character length", hash_length],
            ["Character type", character_type]
        ], tablefmt="double_grid"))

    # Fungsi untuk memeriksa jenis hash
    def check_hash_type(hash_value):
        # Mendapatkan algoritma hash yang tersedia
        hash_algorithms = hashlib.algorithms_guaranteed

        # Melakukan iterasi pada setiap algoritma hash
        for algorithm in hash_algorithms:
            try:
                # Memeriksa apakah algoritma hash ini dapat digunakan
                hashlib.new(algorithm, b'').digest_size
            except ValueError:
                continue

            # Membuat objek hash dengan algoritma yang sedang diperiksa
            hash_obj = hashlib.new(algorithm)

            # Memeriksa panjang hash yang cocok dengan panjang objek hash
            if len(hash_value) == hash_obj.digest_size * 2:
                return algorithm

        return None

    # Contoh penggunaan
    hash_value = input((("""
┌──[𝙯HaEN✘]-[Masukkan nilai hash]
└─➣  """)))  # Contoh hash MD5 "test">> 098f6bcd4621d373cade4e832627b4f6
    hash_type = check_hash_type(hash_value)

    # Menampilkan hasil jenis hash
    if hash_type:
        print_hash_info(hash_value, hash_type)
    else:
        print("Tipe hash tidak ditemukan".title())
