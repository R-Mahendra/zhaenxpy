from zxPackage.zxHeader import Header
from zxPackage.zxPortScan import portScanner
from zxPackage.zxWPS import zxWPS_632
from zxPackage.zxWPS import zxWPS_191
from zxPackage.zxExtractEmail import zxEmail
from zxPackage.zxCrackHash import md5_Crax
from zxPackage.zxCrackHash import sha1_Crax
from zxPackage.zxCrackHash import sha224_Crax
from zxPackage.zxCrackHash import sha256_Crax
from zxPackage.zxCrackHash import sha384_Crax
from zxPackage.zxCrackHash import sha512_Crax
import subprocess
import argparse


# Fungsi untuk menginstal semua requirements
def zxInstallR():
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])


# Fungsi untuk menangani argumen --TypeHash tanpa nilai
def handleTypeHashWithoutValue():
    print("Error: Nilai untuk argumen --TypeHash diperlukan.")
    print("Contoh penggunaan: python zhaenx.py --TypeHash md5")


# Fungsi untuk menangani argumen --TypeHash dengan nilai
def handleTypeHashWithValue(type_hash):
    if type_hash == "md5":
        md5_Crax()
    elif type_hash == "sha1":
        sha1_Crax()
    elif type_hash == "sha224":
        sha224_Crax()
    elif type_hash == "sha256":
        sha256_Crax()
    elif type_hash == "sha384":
        sha384_Crax()
    elif type_hash == "sha512":
        sha512_Crax()


# Daftar argumen yang diterima beserta fungsi yang sesuai
zxArguments = {
    "portScanner": portScanner,
    "wpEmail": zxWPS_632,
    "wpLogin": zxWPS_191,
    "exMail": zxEmail,
    "install": zxInstallR
}


def zxArgs():
    parser = argparse.ArgumentParser(description="Author :: ZHAENX (Latest version 2.1.2)")

    # Menambahkan argumen
    parser.add_argument("-Ps", "--portScanner", action="store_true", help="Untuk scanning port yang terbuka/tertutup & mendeteksi versi layanan port. [Default Port 1 - 65535]")

    parser.add_argument("-Wp632", "--wpEmail", action="store_true", help="Pengungkapan Email Penulis Postingan Tidak Diautentikasi, memungkinkan penyerang yang tidak diautentikasi mengetahui alamat email pengguna yang telah memublikasikan postingan publik di situs web yang terpengaruh. Jika berhasil dieksploitasi, penyerang dapat mengumpulkan alamat email, sehingga membahayakan privasi pengguna.")

    parser.add_argument("-Wp191", "--wpLogin", action="store_true", help="(WPS-Hide-Login) Bypass Perlindungan dengan Referer-Header. Plugin ini memiliki bug yang  memungkinkan untuk mendapatkan halaman login rahasia dengan mengatur string referensi acak dan membuat permintaan ke /wp-admin/options.php sebagai pengguna yang tidak diautentikasi.")

    parser.add_argument("-Em", "--exMail", action="store_true", help="Opsi ini hanya untuk memudahkan mencari tiap-tiap email yang terdapat di situsweb target.")

    parser.add_argument("-Ts", "--TypeHash", nargs="?", choices=["md5", "sha1", "sha224", "sha256", "sha384", "sha512"], help="Script Python ini untuk melakukan Dictionary Attacks pada hash MD5,SHA1,SHA224,SHA256,SHA384,SHA512. Program ini meminta input berupa nilai hash dari pengguna dan mencoba mencocokkan hash tersebut dengan password yang ada di dalam wordlist. Jika cocok, program akan mencetak password yang cocok. Jika tidak ada yang cocok, program akan mencetak pesan bahwa password tidak ditemukan.")

    parser.add_argument("--install", action="store_true", help="Untuk installasi semua requirements yang dibutuhkan.")

    # Parsing argumen
    args = parser.parse_args()

    # Memeriksa argumen TypeHash
    if args.TypeHash is not None:
        handleTypeHashWithValue(args.TypeHash)
        return  # Menggunakan return untuk keluar dari fungsi setelah memanggil fungsi yang sesuai

    # Memanggil fungsi yang sesuai berdasarkan argumen yang diberikan
    for _zxArg, zx_Function in zxArguments.items():
        if getattr(args, _zxArg):
            if zx_Function:
                zx_Function()
            else:
                print("Masih Tahap Development")
            return

    # Jika tidak ada argumen yang diberikan, Tampilkan Banner
Header()