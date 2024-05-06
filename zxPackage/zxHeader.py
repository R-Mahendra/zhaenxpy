import random
from colorama import init, Fore

init(autoreset=True)


def Header():
    wrn = Fore.LIGHTYELLOW_EX + f"""[WRN]\033[3m Disclaimer :: Script ini untuk pembelajaran, Segala sesuata hal apapun tanggung jawab sendiri.\033[0m"""

    inf = f"""
  [INF] Created by Zhaenx 
  [INF] Latest version 2.1.2  
  [INF] Release 2023/05 
  [INF] Usage :: python(3) zhaenx.py -h
  {wrn}
  """

    header1 = f"""
           _                 _       _    _                   _            _             _      _      
         /\ \               / /\    / /\ / /\                /\ \         /\ \     _   /_/\    /\ \    
        /  \ \             / / /   / / // /  \              /  \ \       /  \ \   /\_\ \ \ \   \ \_\   
     __/ /\ \ \           / /_/   / / // / /\ \            / /\ \ \     / /\ \ \_/ / /  \ \ \__/ / /   
    /___/ /\ \ \         / /\ \__/ / // / /\ \ \          / / /\ \_\   / / /\ \___/ /    \ \__ \/_/    
    \___\/ / / /        / /\ \___\/ // / /  \ \ \        / /_/_ \/_/  / / /  \/____/      \/_/\__/\    
          / / /        / / /\/___/ // / /___/ /\ \      / /____/\    / / /    / / /        _/\/__\ \ 
         / / /    _   / / /   / / // / /_____/ /\ \    / /\____\/   / / /    / / /        / _/_/\ \ \  
         \ \ \__/\_\ / / /   / / // /_________/\ \ \  / / /______  / / /    / / /        / / /   \ \ \ 
          \ \___\/ // / /   / / // / /_       __\ \_\/ / /_______\/ / /    / / /        / / /    /_/ / 
           \/___/_/ \/_/    \/_/ \_\___\     /____/_/\/__________/\/_/     \/_/         \/_/     \_\/
    {inf}
    """
    header2 = f"""

     ▄███████▄     ▄█    █▄       ▄████████    ▄████████ ███▄▄▄▄   ▀████    ▐████▀ 
    ██▀     ▄██   ███    ███     ███    ███   ███    ███ ███▀▀▀██▄   ███▌   ████▀  
          ▄███▀   ███    ███     ███    ███   ███    █▀  ███   ███    ███  ▐███    
     ▀█▀▄███▀▄▄  ▄███▄▄▄▄███▄▄   ███    ███  ▄███▄▄▄     ███   ███    ▀███▄███▀    
      ▄███▀   ▀ ▀▀███▀▀▀▀███▀  ▀███████████ ▀▀███▀▀▀     ███   ███    ████▀██▄     
    ▄███▀         ███    ███     ███    ███   ███    █▄  ███   ███   ▐███  ▀███    
    ███▄     ▄█   ███    ███     ███    ███   ███    ███ ███   ███  ▄███     ███▄  
     ▀████████▀   ███    █▀      ███    █▀    ██████████  ▀█   █▀  ████       ███▄
     {inf}
    """
    header3 = f"""

    ███████╗██╗  ██╗ █████╗ ███████╗███╗   ██╗██╗  ██╗
    ╚══███╔╝██║  ██║██╔══██╗██╔════╝████╗  ██║╚██╗██╔╝
      ███╔╝ ███████║███████║█████╗  ██╔██╗ ██║ ╚███╔╝ 
     ███╔╝  ██╔══██║██╔══██║██╔══╝  ██║╚██╗██║ ██╔██╗ 
    ███████╗██║  ██║██║  ██║███████╗██║ ╚████║██╔╝ ██╗
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝
    {inf}
    """
    daftar_header = [
        header1,
        header2,
        header3,
    ]
    banner_Acak = random.choice(daftar_header)

    daftar_warna = [
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        Fore.LIGHTRED_EX,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTYELLOW_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTMAGENTA_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTWHITE_EX,
    ]
    Warna_Random = random.choice(daftar_warna)
    print(Warna_Random + banner_Acak)


# ZX_Banner()
