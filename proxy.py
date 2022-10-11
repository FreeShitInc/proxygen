import os
try:
    import asyncio
    import aiohttp as aiohttp
    import time
    from bs4 import BeautifulSoup
    import requests
    import threading
    from pystyle import Colorate, Colors, Center
except:
    os.system('pip install pystyle threading requests bs4 aiohttp asyncio')
    import asyncio
    import aiohttp as aiohttp
    import time
    from bs4 import BeautifulSoup
    import requests
    import threading
    from pystyle import Colorate, Colors, Center
    
working = []
checked = []
proxy_list = []

os.system('cls' if os.name == 'nt' else 'clear')

print(Colorate.Vertical(Colors.purple_to_blue, """


                                              ▄▄         ▄▄                                   
▀███▀▀▀███                            ▄█▀▀▀█▄███         ██   ██      ▀████▀                  
  ██    ▀█                           ▄██    ▀███              ██        ██                    
  ██   █ ▀███▄███  ▄▄█▀██  ▄▄█▀██    ▀███▄    ███████▄ ▀███ ██████      ██ ▀████████▄  ▄██▀██ 
  ██▀▀██   ██▀ ▀▀ ▄█▀   ██▄█▀   ██     ▀█████▄██    ██   ██   ██        ██   ██    ██ ██▀  ██ 
  ██   █   ██     ██▀▀▀▀▀▀██▀▀▀▀▀▀   ▄     ▀████    ██   ██   ██        ██   ██    ██ ██      
  ██       ██     ██▄    ▄██▄    ▄   ██     ████    ██   ██   ██        ██   ██    ██ ██▄    ▄
▄████▄   ▄████▄    ▀█████▀ ▀█████▀   █▀█████▀████  ████▄████▄ ▀████   ▄████▄████  ████▄█████▀ 
                                                                                              
  _ \                                  ___|             
 |   |  __|   _ \   \  /  |   |       |      _ \  __ \  
 ___/  |     (   |    <   |   |       |   |  __/  |   | 
_|    _|    \___/  _/\_\ \__. |      \____|\___| _|  _| 
                         ____/                          

Created By FreeShit ║ getfreeshit.today 


""",1))

### --------- Proxy Scraper --------- ###

def proxy_scrape():
    global proxy_list
    proxy_list = []
    funni_list = requests.get('https://www.proxy-list.download/api/v1/get?type=http').text
    lines = funni_list.splitlines()
    for i in lines:
        if i not in proxy_list:
            proxy_list.append(i)
            
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    lines = text.splitlines()  
    for i in range(299):
        if lines[i+3] not in proxy_list:
            proxy_list.append(lines[i+3])
    html = requests.get('https://us-proxy.org/').text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    lines = text.splitlines()  
    for i in range(199):
        if lines[i+3] not in proxy_list:
            proxy_list.append(lines[i+3])
            
### ------------ Proxy Checker ------------- ###

async def checker(url, proxy):
    global checked
    timeout = 10
    try:
        session_timeout = aiohttp.ClientTimeout(
            total = None,
            sock_connect = timeout,
            sock_read = timeout,
        )
        async with aiohttp.ClientSession(timeout = session_timeout) as session:
            async with session.get(url, proxy = f'http://{proxy}', timeout = timeout) as resp:
                pass
    except Exception as error:
        pass
    else:
        checked.append(proxy)

        
        
async def main():
    proxy_scrape()
    global working, proxy_list, checked
    tasks = []
    count = 0
    for proxy in proxy_list:
        task = asyncio.create_task(checker('https://api.ipify.org/', proxy))
        tasks.append(task)
    await asyncio.gather(*tasks)
    for i in checked:
        if i not in working:
            working.append(i)

### ------------- Input and other stuff ------------- ###

def gen(reps,e):
    global working
    final = ''
    for i in range(reps):
        asyncio.run(main())
        time.sleep(60*10)
    f = open(e).read()
    old = f.splitlines()
    for i in working:
        if i not in old:
            final = final + '\n' + i
    final = final + f
    final = ''.join(final.splitlines(keepends=True)[1:])
    f = open(e,'w+')
    f.write(final)
    f.close()
    
re = int(input('# of times to scrape: '))
file = input('filepath of text file to save proxies to (if in same dir just put file name, also make sure to include .txt): ')
gen(re,file)