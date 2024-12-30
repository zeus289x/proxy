import os
import requests
from colorama import Fore
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
    print(Fore.RED + banner + Fore.RESET)

def check_proxy(proxy):
    url = "https://www.ipsorgu.com/?ip="  
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(Fore.GREEN + f"Proxy {proxy} is live!" + Fore.RESET)
            return "live", proxy  
        else:
            print(Fore.RED + f"Proxy {proxy} failed with status code: {response.status_code}" + Fore.RESET)
            return "deactive", proxy  
    except requests.exceptions.RequestException:
        print(Fore.RED + f"Proxy {proxy} - deactive" + Fore.RESET)
        return "deactive", proxy  

def test_proxies(proxies):
    live_proxies = []
    deactive_proxies = []
    
    for proxy in proxies:
        status, result = check_proxy(proxy)
        if status == "live":
            live_proxies.append(result)
        else:
            deactive_proxies.append(result)
    

    with open("live.txt", "w") as f:
        for proxy in live_proxies:
            f.write(f"{proxy}\n")
    
    with open("deactive.txt", "w") as f:
        for proxy in deactive_proxies:
            f.write(f"{proxy}\n")
    

    print(Fore.CYAN + "\nProxy checklendi!" + Fore.RESET)
    print(Fore.GREEN + f"{len(live_proxies)} live proxies found." + Fore.RESET)
    print(Fore.RED + f"{len(deactive_proxies)} deactivated proxies found." + Fore.RESET)

    subprocess.run(["python", "proxy.py"])

def proxy_checker():
    clear_terminal()
    
    with open("289.txt", "r") as f:
        proxies = [line.strip() for line in f.readlines()]
    
    print(Fore.YELLOW + "Proxyler kontrol ediliyor..." + Fore.RESET)
    test_proxies(proxies)

if __name__ == "__main__":
    proxy_checker()
