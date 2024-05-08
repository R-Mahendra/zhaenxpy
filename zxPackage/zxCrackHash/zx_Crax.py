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
        fileWordList = os.path.join(current_directory,"WD.txt")

        
        _Input_md5Hash = input((("""
┌──[𝙯HaEN✘]-[Masukkan Nilai Hash]
└─➣  """)))

        # Kondisi apakah nilai hash kosong, jika iya, minta pengguna untuk mengulangi
        if not _Input_md5Hash.strip():
            Tanya = input(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!\n ULANG LAGI?(y/n): " + Style.BRIGHT + Style.RESET_ALL)
            if Tanya == "y" or Tanya == "Y":
                continue 
            else:
                exit(Fore.RED + "NILAI HASH TIDAK BOLEH KOSONG...!!!" + Style.BRIGHT + Style.RESET_ALL)
        break
    # Meminta pengguna untuk memasukkan path wordlist
    wordlist = input((("""
┌──[𝙯HaEN✘]-[Masukkan Path WordList]
└─➣  """)))
    # Jika pengguna tidak memasukkan path wordlist, maka gunakan file yang ada =>  default WD.txt
    if not wordlist:
        wordlist = fileWordList
    try:
        # Membuka file wordlist
        wordlist_pswd = open(wordlist,"r",encoding="utf-8",errors='ignore')
    except:
        # Jika file wordlist tidak ditemukan, keluar dari program
        exit(Fore.RED+"FILE TIDAK DI TEMUKAN...!!!"+Style.BRIGHT+Style.RESET_ALL)

    try:
        # Melakukan brute force dengan membandingkan nilai hash MD5 dengan hash yang dihasilkan dari setiap kata sandi dalam wordlist
        for paswd in wordlist_pswd:
            md5 = hashlib.md5()
            md5.update(paswd.strip().encode('utf-8'))
            try:
                print(Fore.RED+"[%d] MEMPROSES BRUTE_FORCE : %s" %(counter, paswd)+Style.BRIGHT)
                counter += 1
            except KeyboardInterrupt:
                # Jika ada interupsi keyboard (Ctrl+C), keluar dari program
                exit()
            # Jika nilai hash MD5 cocok dengan hash yang dihasilkan, print hasilnya
            if _Input_md5Hash.strip() == md5.hexdigest():
                table = [['MD5 Encrypt',f'{_Input_md5Hash}'],
                ['MD5 Decrypt',f'{paswd.strip()} '],
                ['DATE TIME',(jam_sekarang)+(tgl_sekarang)]]
                print(Fore.GREEN+(tabulate(table, tablefmt="double_grid"))+Style.BRIGHT+Style.RESET_ALL)
                break
        else:
            # Jika tidak ada kata sandi yang cocok, keluar dari program
            exit(Fore.RED+(("""
╔═══════════════════════════════════════════════════════╗
║             PASSWORD TIDAK DITEMUKAN                  ║
╚═══════════════════════════════════════════════════════╝"""))+Style.BRIGHT+Style.RESET_ALL)
    except KeyboardInterrupt:
        # Jika ada interupsi keyboard (Ctrl+C), keluar dari program
        exit()
    wordlist_pswd.close()


#==================== MD5 END ====================


# def sha1_Crax():
#    print("INI ADALAH sha1")
   
# def sha224_Crax():
#    print("INI ADALAH sha224")
   
# def sha256_Crax():
#    print("INI ADALAH sha256")
   
# def sha384_Crax():
#    print("INI ADALAH sha384")
   
# def sha1_Crax():
#    print("INI ADALAH sha1")
   
# def sha512_Crax():
#    print("INI ADALAH sha512")