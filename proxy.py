import os
import random
import requests
import time
from colorama import Fore, Back, Style
import subprocess

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  
    banner = '''
                          ████████  ████████   ██████  █████ █████ █████ ████
                          ░░███░░███░░███░░███ ███░░███░░███ ░░███ ░░███ ░███ 
                          ░███ ░███ ░███ ░░░ ░███ ░███ ░░░█████░   ░███ ░███ 
                          ░███ ░███ ░███     ░███ ░███  ███░░░███  ░███ ░███ 
                          ░███████  █████    ░░██████  █████ █████ ░░███████ 
                          ░███░░░  ░░░░░      ░░░░░░  ░░░░░ ░░░░░   ░░░░░███ 
                          ░███                                      ███ ░███ 
                          █████                                    ░░██████  
                          ░░░░░                                      ░░░░░░  
                                          İnstagram: xzeus289 
                                          Discord: zeus289x
                                          discord.gg/289
    '''
    print(Fore.GREEN + banner + Fore.RESET)

def generate_proxies(num_proxies):
    proxy_list = []
    for _ in range(num_proxies):
        ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        port = random.randint(8080, 65535)
        proxy = f"http://{ip}:{port}"
        proxy_list.append(proxy)
    return proxy_list

def proxy_generator():
    clear_terminal()
    num_proxies = int(input(Fore.YELLOW + "Kaç tane proxy oluşturmak istersin " + Fore.RESET))
    print(Fore.YELLOW + f"Proxy {num_proxies} Oluşturuluyor..." + Fore.RESET)
    proxies = generate_proxies(num_proxies)
    with open("289.txt", "w") as f:
        for proxy in proxies:
            f.write(f"{proxy}\n")
    print(Fore.GREEN + f"{num_proxies} proxies generated and saved to 289.txt." + Fore.RESET)
    
    # Proxy oluşturma işlemi tamamlandıktan sonra proxy.py'yi yeniden başlat
    time.sleep(2)
    print(Fore.YELLOW + "Proxy generator tamamlandı. Program yeniden başlatılıyor..." + Fore.RESET)
    subprocess.run(["python", "proxy.py"])

def proxy_checker():
    clear_terminal()
    with open("289.txt", "r") as f:
        proxies = [line.strip() for line in f.readlines()]
    print(Fore.GREEN + "Proxyler Checkleniyor..." + Fore.RESET)
    subprocess.run(["python", "checker.py"])

def menu():
    clear_terminal()
    print(Fore.YELLOW + "289 Proxy" + Fore.RESET)
    print("1. Proxy oluştur")
    print("2. Proxy Checker")
    print("3. Çıkış")
    choice = input(Fore.YELLOW + "Bir seçenek girin: " + Fore.RESET)
    if choice == "1":
        proxy_generator()
    elif choice == "2":
        print(Fore.YELLOW + "Proxy kontrol ediliyor..." + Fore.RESET)
        proxy_checker()
    elif choice.lower() == "3":
        print(Fore.RED + "Program sonlandırılıyor..." + Fore.RESET)
        time.sleep(2)
        exit()
    else:
        print(Fore.RED + "Geçersiz seçenek kanka " + Fore.RESET)
        time.sleep(2)
        menu()

if __name__ == "__main__":
    menu()
