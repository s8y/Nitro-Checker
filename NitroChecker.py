import string, threading, os, requests, time, webbrowser, colorama, random
from colorama import Fore, init
init()

#made by lure. do not skid or sell this tool. this tool is free.
#follow xinj on insta lol

os.system("cls")
print(Fore.RED+"""
 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████  
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ 
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ 
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒  
         ░  ░              ░         ░ ░  
[+] Discord: Lure#0001
[+] Instagram: xinj
[+] Server: discord.gg/lies
[+] GitHub: @s8y
"""+Fore.WHITE)
file_name = input(f"[{Fore.GREEN}?{Fore.WHITE}] Enter Proxy File Name: ")
proxy = open(file_name).read().splitlines()
proxies = {
    "http" : proxy
}

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(1000000):
    giftcode = ''
    for i in range(16):
        giftcode += random.choice(characters)
    with open('valid.txt', 'a') as f:
        r = requests.get('https://discordapp.com/api/v9/entitlements/gift-codes/{}?with_application=false&with_subscription_plan=true'.format('discord.gift/' + giftcode))
    if r.status_code == 200:
            f.write('discord.gift/{} \n'.format(giftcode))
            print(f"[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}discord.gift/{giftcode}{Fore.WHITE}")
    else:
        print(f'[{Fore.RED}-{Fore.WHITE}] {Fore.RED}discord.gift/{giftcode}{Fore.WHITE}')
