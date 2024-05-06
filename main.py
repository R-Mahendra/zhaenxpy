from zxPackage.zxHeader import Header
from zxPackage.zxPortScan import portScanner
from zxPackage.zxWPS import zxWPS_191
from zxPackage.zxWPS import zxWPS_632
from zxPackage.zxExtractEmail import zxEmail
import subprocess, sys, argparse


# def clearSys():
#   sis = sys.platform
#   if sis == "win32":
#      subprocess.run("cls", shell=True)
#   elif sis == "linux" or sis == "darwin":
#      subprocess.run("clear", shell=True)

def zxInstallR():
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

def zxArgs():
    parser = argparse.ArgumentParser(description="Author :: ZHAENX (Latest version 2.1.2)")
    # Menambahkan argumen
    parser.add_argument("-Ps", "--portScanner", action="store_true", help="Untuk scanning port yang terbuka/tertutup & mendeteksi versi layanan port. [Default Port 1 - 65535]")
    parser.add_argument("-Wp632", "--wpEmail", action="store_true", help="Pengungkapan Email Penulis Postingan Tidak Diautentikasi, memungkinkan penyerang yang tidak diautentikasi mengetahui alamat email pengguna yang telah memublikasikan postingan publik di situs web yang terpengaruh. Jika berhasil dieksploitasi, penyerang dapat mengumpulkan alamat email, sehingga membahayakan privasi pengguna.")
    parser.add_argument("-Wp191", "--wpLogin", action="store_true", help="(WPS-Hide-Login) Bypass Perlindungan dengan Referer-Header. Plugin ini memiliki bug yang  memungkinkan untuk mendapatkan halaman login rahasia dengan mengatur string referensi acak dan membuat permintaan ke /wp-admin/options.php sebagai pengguna yang tidak diautentikasi.")
    parser.add_argument("-Em", "--exMail", action="store_true", help="Opsi ini hanya untuk memudahkan mencari tiap-tiap email yang terdapat di situsweb target.")
    parser.add_argument("-Ch", "--cxH", action="store_true", help="Skrip Python ini alat untuk melakukan [Dictionary Attacks] pada nilai hash. Ini meminta nilai hash dan path ke wordlist dari pengguna. Kemudian, mencoba setiap password dalam wordlist, mengubahnya menjadi hash, dan membandingkannya dengan hash yang diberikan oleh pengguna. Jika ada kecocokan, program mencetak password yang cocok dan waktu saat ini. Jika tidak ada kecocokan, program mencetak pesan bahwa password tidak ditemukan.")
    parser.add_argument("--install", action="store_true")

    # Parsing argumen
    args = parser.parse_args()

    if args.portScanner:
        Header()
        portScanner()
    # Jika argumen -Wp632 atau --wpEmail diberikan, jalankan script zxWPS_632
    elif args.wpEmail:
        Header()
        zxWPS_632()
        
    # Jika argumen -Wp191 atau --wpLogin diberikan, jalankan script zxWPS_191
    elif args.wpLogin:
        Header()
        zxWPS_191()

    # Jika argumen -Em atau --exMail diberikan, jalankan script Extract Email
    elif args.exMail:
        Header()
        zxEmail()
    # Jika argumen -Ch atau --cxH diberikan, jalankan script Cracking Hash
    elif args.exMail:
        Header()
        
    # Jika argumen --install atau -install diberikan, jalankan script zxInstallR
    elif args.install:
        zxInstallR()
        #Jika tidak memberikan argumen apapun, Tmapilkan Banner
    else:
        Header()
