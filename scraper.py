#!/usr/bin/env python3
import time
from datetime import datetime
import threading
import os, sys
from colorama import Fore, Style, init
from pystyle import Colors, Write, Center, Anime, System, Colorate
import random, requests
import base64

class Main():
    def __init__(self):
        self.api = "API.txt"
        self.file = "data/scraped_proxies.txt"
        self.title = "Proxy Scraper | 6 API's | Open Source"
        self.start_title = "PRESS ENTER TO START."
        self.author = "𝐖𝐗〢・GoKu xD . 🥀†¹ⱽ¹#0077"

    def random_line(file_txt):
        line = next(file_txt)
        for num, aline in enumerate(file_txt, 2):
            if random.randrange(num):
                continue
            line = aline
        return line

    def __scrape__(self):
        APIS = [
            # "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            # "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc",
            # "https://www.proxy-list.download/api/v1/get?type=http&anon=elite&country=US",
            # "https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https"
        ]
        
        randomized_api = random.choice(APIS)

        try:
            os.system("title "+self.title)
            API_IN_USE = randomized_api
            print(f"[{datetime.now()}] || [{Fore.LIGHTBLACK_EX}DEBUG{Fore.WHITE}] || [{Fore.GREEN}API{Fore.WHITE}] API IN USE : {API_IN_USE}")
            session = requests.Session()
            ID = session.get("https://wtfismyip.com/text").text.strip("\n")
            print(f"[{datetime.now()}] || [{Fore.LIGHTBLACK_EX}DEBUG{Fore.WHITE}] || [{Fore.GREEN}SESSION{Fore.WHITE}] Created Session {ID}")
            time.sleep(1)
            for i in range(1, 6):
                print(f"[{datetime.now()}] || [{Fore.LIGHTBLACK_EX}DEBUG{Fore.WHITE}] || [{Fore.GREEN}TIME{Fore.WHITE}] Time Remaining To Complete Scraping {i}s", end="\r")
                time.sleep(1)

            response_from_api = requests.get(randomized_api)
            data = response_from_api.text

            print(f"[{datetime.now()}] || [{Fore.BLUE}INFO{Fore.WHITE}] || [{Fore.GREEN}SCRAPED{Fore.WHITE}] Proxies Scraped from {API_IN_USE}")
            with open("data/scraped_proxies.txt", "a") as f:
                start_line = """
                                                SCRAPED MADE BY GOKU CODEZ
                __________________________________________________________________________________________\n\n
                """
                f.write(f"{start_line}\n{data}")
                num_lines = sum(1 for line in open('data/scraped_proxies.txt'))

                print(f"[{datetime.now()}] || [{Fore.BLUE}INFO{Fore.WHITE}] || [{Fore.GREEN}TOTAL{Fore.WHITE}] Total Proxies Scraped {num_lines}")

            with open("raw_data.txt", "a") as f:
                f.write(f"{data}")

        except Exception as er:
            print(f"[{datetime.now()}] || [{Fore.LIGHTBLACK_EX}DEBUG{Fore.WHITE}] || [{Fore.RED}ERROR{Fore.WHITE}] Something Went Wrong Retrying... Exception: {er}")
            time.sleep(0.6)
            self.__scrape__()

    def console(self):
        os.system("title "+self.start_title)
        banner = r'''
 ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███  ▓█████  ██▀███  
▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░          ░░   ░   ░   ▒   ░░          ░     ░░   ░ 
      ░  ░ ░         ░           ░  ░            ░  ░   ░     
         ░                                                    
        '''

        System.Size(120, 30)
        System.Clear()
        Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, interval=0.030, enter=True)
        
        self.__scrape__()
        

if __name__ == "__main__":
    Main().console()
