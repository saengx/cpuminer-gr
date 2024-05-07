import os
import json
import time
import pip
from config import banner


# check import module
try:
    with open("setip/ip.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            ip = loads['ip']

    os.system(f"cd set-miner && wget -N --timeout 10 --connect-timeout=15 -t 2 http://{ip}/online.json")
    time.sleep(2)
    from progress.bar import ShadyBar
except ImportError:
    pip.main(['install', '--user', 'progress'])
    from progress.bar import ShadyBar

try:
    import requests
except ImportError:
    pip.main(['install', '--user', 'requests'])
    import requests
    
    
zergpool = ["stratum+tcp://verushash.mine.zergpool.com:3300","stratum+tcp://verushash.na.mine.zergpool.com:3300","stratum+tcp://verushash.eu.mine.zergpool.com:3300","stratum+tcp://verushash.asia.mine.zergpool.com:3300"]
ghostrider = ["gr"]
verushash = ["verus"]
cpuminer = ["scrypt","scryptn2","scryptn11","sha256d","allium","axiom","bastion","bitcore","blake","blake2s","blake2b","bmw","bmw512","cpupower","curve","cryptonight","cryptonight-light","decred","dedal","dmd-gr","fresh","geek","groetl","jha","lbry"]
cpuminer = ["lyra2RE","lyra2REv2","lyra2REv3","megabtx","meme","memehash","myr-gr","minotaur","minotaurx","neoscrypt","nist5","pentablake","pluck","power2b","quark","qubit","skein","skein2","s3","sia","sib","timetravel","tribus","vanilla","veltor"]
cpuminer = ["velvet","xevan","x11evo","x11","x12","x13","x14","x15","x16r","x16rv2","x17","x20r","yespower","yespowerR16","yespowerIC","yespowerLITB","yespowerIOTS","yespowerITC","yespowerMGPC","yespowerSUGAR","yespowerTIDE","yespowerURX"]
cpuminer = ["yescrypt","yescryptR8","yescryptR16","yescryptR32","zr5"]
def runOffline():
    banner()
    try:
        with open("set-miner/online.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            algo = loads['algo']
            wallet = loads['wallet']
            password = loads['pass']
        if pool == "" or wallet == "":
            print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-miner\033[0m\n\n")

        with open("set-miner/offline.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            name = loads['name']
            cpu = loads['cpu']
        if name == "":
           name = "noname"
        if cpu == "":
           cpu = "1"
        with open("setip/ip.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            ip = loads['ip']

        print("\033[93mCONNECT NETWORK\033[00m\n  http://",ip)
        print("\033[1;34;40m")   
        print("WALLET =",wallet)
        print("NAME   =",name)
        print("POOL   =",pool)
        print("ALGO   =",algo)
        print("CPU    =",cpu)
        if algo in cpuminer:
           os.system(f"cd CPUMINER && ./cpuminer -a {algo} -o {pool} -u {wallet}.{name} -p {password} -t {cpu}")
        if algo in ghostrider:
           os.system(f"cd cpuminer-gr && ./cpuminer -a {algo} -o {pool} -u {wallet}.{name} -p {password} -t {cpu}")
        if pool in zergpool:

           print("PASS   =",password +",id="+name)
           print("\033[00m\n")

         #  time.sleep(2)
           os.system(f"cd ccminer && ./ccminer -a {algo} -o {pool} -u {wallet}.{name} -p {password},ID={name} -t {cpu}")
       
        else:
        	
         print("PASS   =",password)
         print("\033[00m\n")
         os.system(f"cd ccminer && ./ccminer -a {algo} -o {pool} -u {wallet}.{name} -p {password} -t {cpu}")
        
    except:
        push = {'pool': '','algo': '','wallet': '','pass': ''}
        with open("set-miner/online.json", "w") as set:
            json.dump(push, set, indent=4)
        push = {'name': '','cpu': ''}
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)
        
        
        
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-miner\033[0m\n\n")




while True:   
    os.system("@cls||clear")
    with ShadyBar("\033[32m Start Mining\033[00m") as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()
            
        runOffline()
        break
else:
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner\033[0m\n\n")
