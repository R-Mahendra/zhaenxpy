from main import zxArgs
import sys
import time
import requests


def zxPrint(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10.0 / 280)
        
def main():
    try:
        zxArgs()

        # Memeriksa koneksi internet
        response = requests.get("http://www.google.com", timeout=5)
        response.raise_for_status()
        # zxPrint("\n════════ Happy Hacking ════════\n")
        return
        # Jika koneksi internet terputus
    except requests.exceptions.ConnectionError:
        zxPrint("\n\n════════ The Internet is not connected. ════════\n")
        return False
        # Jika koneksi internet ada kesalahan, timeout, atau kesalahan server.
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False
        # Jika  ada kesalahan kodingan
    except TypeError:
        zxPrint("\n\n════════ Type Error, Kesalahan Codingan ════════\n")
        sys.exit()

    except KeyboardInterrupt:
        zxPrint("\n\n════════ The Program was terminated by user ════════\n")
        sys.exit()


if __name__ == "__main__":
    main()
