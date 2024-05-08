import hashlib,sys,time,os
from datetime import datetime
from tabulate import tabulate
from colorama import Fore,Style

def md5_Crax():
    while True:
        # Untuk mengambil data waktu sekarang
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S | ')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y')
        counter = 1
        
        # Untuk mengambil derektori sekarang
        current_directory = os.path.dirname(os.path.abspath(__file__))
    
        # Ambil File Wordlist di direktori yang sekarang
        fileWordList = os.path.join(current_directory,"wordlist.txt")
        
        _inputHash = input((("""
┌──[𝙯HaEN✘]-[Masukkan Nilai Hash]
└─➣  """)))

        # Kondisi apakah nilai hash kosong, jika iya, minta pengguna untuk mengulangi
        if not _inputHash.strip():
            Tanya = input(Fore.RED + "Nilai hash tidak boleh kosong.!\n Ulang lagi?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue 
            else:
                exit()
        break
    # Meminta pengguna untuk memasukkan path wordlist
    
    # Fungsi untuk meminta input path wordlist
    def get_wordlist_path():
        return input((("""
┌──[𝙯HaEN✘]-[Masukkan Path WordList]
└─➣  """)))
    
    pathWordlist = get_wordlist_path()
    
    # Jika pengguna tidak memasukkan path wordlist, maka gunakan file yang ada =>  default WD.txt
    if not pathWordlist:
        tanya_pathWordlist = input("Apakah Anda ingin menggunakan wordlist default? (y/n): ")
        if tanya_pathWordlist == "y" or tanya_pathWordlist == "Y":
            pathWordlist = fileWordList
        elif tanya_pathWordlist == "n" or tanya_pathWordlist == "N":
            # Jika pengguna tidak ingin menggunakan wordlist default, terus minta mereka memasukkan path wordlist sampai valid
            while not pathWordlist:
                pathWordlist = get_wordlist_path()
        else:
            exit()
    
    try:
        # Membuka file wordlist
        wordlist_pswd = open(pathWordlist, "r", encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        # Jika file wordlist tidak ditemukan, keluar dari program
        exit(Fore.RED + "File tidak ditemukan.!" + Style.BRIGHT + Style.RESET_ALL)

    try:
        # Melakukan brute force dengan membandingkan nilai hash MD5 dengan hash yang dihasilkan dari setiap kata sandi dalam wordlist
        for paswd in wordlist_pswd:
            nilaiHash = hashlib.md5()
            nilaiHash.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] Memproses BruteForce : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                # Jika ada interupsi keyboard (Ctrl+C), keluar dari program
                exit()
            # Jika nilai hash MD5 cocok dengan hash yang dihasilkan, print hasilnya
            if _inputHash.strip() == nilaiHash.hexdigest():
                table = [['MD5 Encrypt',f'{_inputHash}'],
                ['MD5 Decrypt',f'{paswd.strip()}'],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            # Jika tidak ada kata sandi yang cocok, keluar dari program
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             Password tidak ditemukan                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        # Jika ada interupsi keyboard (Ctrl+C), keluar dari program
        exit()
    wordlist_pswd.close()


#==================== MD5 END ====================


def sha1_Crax():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S | ')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y')
        counter = 1
        current_directory = os.path.dirname(os.path.abspath(__file__))
        fileWordList = os.path.join(current_directory,"wordlist.txt")

        _inputHash = input((("""
┌──[𝙯HaEN✘]-[Masukkan Nilai Hash]
└─➣  """)))

        if not _inputHash.strip():
            Tanya = input(Fore.RED + "Nilai hash tidak boleh kosong.!\n Ulang lagi?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue 
            else:
                exit()
        break
    
    def get_wordlist_path():
        return input((("""
┌──[𝙯HaEN✘]-[Masukkan Path WordList]
└─➣  """)))
    
    pathWordlist = get_wordlist_path()
    
    if not pathWordlist:
        tanya_pathWordlist = input("Apakah Anda ingin menggunakan wordlist default? (y/n): ")
        if tanya_pathWordlist == "y" or tanya_pathWordlist == "Y":
            pathWordlist = fileWordList
        elif tanya_pathWordlist == "n" or tanya_pathWordlist == "N":
            while not pathWordlist:
                pathWordlist = get_wordlist_path()
        else:
            exit()
    
    try:
        wordlist_pswd = open(pathWordlist, "r", encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        exit(Fore.RED + "File tidak ditemukan.!" + Style.BRIGHT + Style.RESET_ALL)

    try:
        for paswd in wordlist_pswd:
            nilaiHash = hashlib.sha1()
            nilaiHash.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] Memproses BruteForce : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                exit()
            if _inputHash.strip() == nilaiHash.hexdigest():
                table = [['SHA1 Encrypt',f'{_inputHash}'],
                ['SHA1 Decrypt',f'{paswd.strip()}'],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             Password tidak ditemukan                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        exit()
    wordlist_pswd.close()




def sha224_Crax():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S | ')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y')
        counter = 1
        current_directory = os.path.dirname(os.path.abspath(__file__))
        fileWordList = os.path.join(current_directory,"wordlist.txt")

        _inputHash = input((("""
┌──[𝙯HaEN✘]-[Masukkan Nilai Hash]
└─➣  """)))

        if not _inputHash.strip():
            Tanya = input(Fore.RED + "Nilai hash tidak boleh kosong.!\n Ulang lagi?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue 
            else:
                exit()
        break
    
    def get_wordlist_path():
        return input((("""
┌──[𝙯HaEN✘]-[Masukkan Path WordList]
└─➣  """)))
    
    pathWordlist = get_wordlist_path()
    
    if not pathWordlist:
        tanya_pathWordlist = input("Apakah Anda ingin menggunakan wordlist default? (y/n): ")
        if tanya_pathWordlist == "y" or tanya_pathWordlist == "Y":
            pathWordlist = fileWordList
        elif tanya_pathWordlist == "n" or tanya_pathWordlist == "N":
            while not pathWordlist:
                pathWordlist = get_wordlist_path()
        else:
            exit()
    
    try:
        wordlist_pswd = open(pathWordlist, "r", encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        exit(Fore.RED + "File tidak ditemukan.!" + Style.BRIGHT + Style.RESET_ALL)

    try:
        for paswd in wordlist_pswd:
            nilaiHash = hashlib.sha224()
            nilaiHash.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] Memproses BruteForce : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                exit()
            if _inputHash.strip() == nilaiHash.hexdigest():
                table = [['SHA224 Encrypt',f'{_inputHash}'],
                ['SHA224 Decrypt',f'{paswd.strip()}'],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             Password tidak ditemukan                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        exit()
    wordlist_pswd.close()

def sha256_Crax():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S | ')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y')
        counter = 1
        current_directory = os.path.dirname(os.path.abspath(__file__))
        fileWordList = os.path.join(current_directory,"wordlist.txt")

        _inputHash = input((("""
┌──[𝙯HaEN✘]-[Masukkan Nilai Hash]
└─➣  """)))

        if not _inputHash.strip():
            Tanya = input(Fore.RED + "Nilai hash tidak boleh kosong.!\n Ulang lagi?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue 
            else:
                exit()
        break
    
    def get_wordlist_path():
        return input((("""
┌──[𝙯HaEN✘]-[Masukkan Path WordList]
└─➣  """)))
    
    pathWordlist = get_wordlist_path()
    
    if not pathWordlist:
        tanya_pathWordlist = input("Apakah Anda ingin menggunakan wordlist default? (y/n): ")
        if tanya_pathWordlist == "y" or tanya_pathWordlist == "Y":
            pathWordlist = fileWordList
        elif tanya_pathWordlist == "n" or tanya_pathWordlist == "N":
            while not pathWordlist:
                pathWordlist = get_wordlist_path()
        else:
            exit()
    
    try:
        wordlist_pswd = open(pathWordlist, "r", encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        exit(Fore.RED + "File tidak ditemukan.!" + Style.BRIGHT + Style.RESET_ALL)

    try:
        for paswd in wordlist_pswd:
            nilaiHash = hashlib.sha256()
            nilaiHash.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] Memproses BruteForce : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                exit()
            if _inputHash.strip() == nilaiHash.hexdigest():
                table = [['SHA256 Encrypt',f'{_inputHash}'],
                ['SHA256 Decrypt',f'{paswd.strip()}'],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             Password tidak ditemukan                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        exit()
    wordlist_pswd.close()

def sha384_Crax():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S | ')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y')
        counter = 1
        current_directory = os.path.dirname(os.path.abspath(__file__))
        fileWordList = os.path.join(current_directory,"wordlist.txt")

        _inputHash = input((("""
┌──[𝙯HaEN✘]-[Masukkan Nilai Hash]
└─➣  """)))

        if not _inputHash.strip():
            Tanya = input(Fore.RED + "Nilai hash tidak boleh kosong.!\n Ulang lagi?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue 
            else:
                exit()
        break
    
    def get_wordlist_path():
        return input((("""
┌──[𝙯HaEN✘]-[Masukkan Path WordList]
└─➣  """)))
    
    pathWordlist = get_wordlist_path()
    
    if not pathWordlist:
        tanya_pathWordlist = input("Apakah Anda ingin menggunakan wordlist default? (y/n): ")
        if tanya_pathWordlist == "y" or tanya_pathWordlist == "Y":
            pathWordlist = fileWordList
        elif tanya_pathWordlist == "n" or tanya_pathWordlist == "N":
            while not pathWordlist:
                pathWordlist = get_wordlist_path()
        else:
            exit()
    
    try:
        wordlist_pswd = open(pathWordlist, "r", encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        exit(Fore.RED + "File tidak ditemukan.!" + Style.BRIGHT + Style.RESET_ALL)

    try:
        for paswd in wordlist_pswd:
            nilaiHash = hashlib.sha384()
            nilaiHash.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] Memproses BruteForce : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                exit()
            if _inputHash.strip() == nilaiHash.hexdigest():
                table = [['SHA384 Encrypt',f'{_inputHash}'],
                ['SHA384 Decrypt',f'{paswd.strip()}'],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             Password tidak ditemukan                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        exit()
    wordlist_pswd.close()

def sha512_Crax():
    while True:
        waktu_sekarang = datetime.now()
        jam_sekarang = waktu_sekarang.strftime('%H:%M:%S | ')
        tgl_sekarang = waktu_sekarang.strftime('%d-%m-%Y')
        counter = 1
        current_directory = os.path.dirname(os.path.abspath(__file__))
        fileWordList = os.path.join(current_directory,"wordlist.txt")

        _inputHash = input((("""
┌──[𝙯HaEN✘]-[Masukkan Nilai Hash]
└─➣  """)))

        if not _inputHash.strip():
            Tanya = input(Fore.RED + "Nilai hash tidak boleh kosong.!\n Ulang lagi?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue 
            else:
                exit()
        break
    
    def get_wordlist_path():
        return input((("""
┌──[𝙯HaEN✘]-[Masukkan Path WordList]
└─➣  """)))
    
    pathWordlist = get_wordlist_path()
    
    if not pathWordlist:
        tanya_pathWordlist = input("Apakah Anda ingin menggunakan wordlist default? (y/n): ")
        if tanya_pathWordlist == "y" or tanya_pathWordlist == "Y":
            pathWordlist = fileWordList
        elif tanya_pathWordlist == "n" or tanya_pathWordlist == "N":
            while not pathWordlist:
                pathWordlist = get_wordlist_path()
        else:
            exit()
    
    try:
        wordlist_pswd = open(pathWordlist, "r", encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        exit(Fore.RED + "File tidak ditemukan.!" + Style.BRIGHT + Style.RESET_ALL)

    try:
        for paswd in wordlist_pswd:
            nilaiHash = hashlib.sha512()
            nilaiHash.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] Memproses BruteForce : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                exit()
            if _inputHash.strip() == nilaiHash.hexdigest():
                table = [['SHA512 Encrypt',f'{_inputHash}'],
                ['SHA512 Decrypt',f'{paswd.strip()}'],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             Password tidak ditemukan                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        exit()
    wordlist_pswd.close()