import colorama
from colorama import Fore
import os
import random
import secrets
import string
import time

#-------------------------------------------------------------------------------

os.system('clear')

print(Fore.GREEN + '███████╗ █████╗ ██╗      █████╗ ██████╗ ██╗     ██╗  ██╗')
time.sleep(0.1)
print(Fore.GREEN + '██╔════╝██╔══██╗██║     ██╔══██╗██╔══██╗██║     ╚██╗██╔╝')
time.sleep(0.1)
print(Fore.GREEN + '███████╗███████║██║     ███████║██║  ██║██║      ╚███╔╝ ')
time.sleep(0.1)
print(Fore.GREEN + '╚════██║██╔══██║██║     ██╔══██║██║  ██║██║      ██╔██╗ ')
time.sleep(0.1)
print(Fore.GREEN + '███████║██║  ██║███████╗██║  ██║██████╔╝███████╗██╔╝ ██╗')
time.sleep(0.1)
print(Fore.GREEN + '╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝')
time.sleep(0.6)
print(Fore.YELLOW + '- Made By The SaladLX Team')


#-------------------------------------------------------------------------

time.sleep(1)

print(' ')
wallet = input(Fore.WHITE + 'BTC Wallet Adress: ')

amount = input(Fore.WHITE + 'Amount Of Mining Attempts: ')
amount = int(amount)

print(Fore.RED + '-----------------------------------------------')

mined = 0
mined = int(mined)

profit = 0
profit = int(profit)

#---------------------------------------------------------------------------

for line in range(amount):
    
    time.sleep(0.7)
    
    mined = int(mined) + 1
    
    hash_profit = random.randint(3, 9) #This depends on your CPU power
    hash_profit = int(hash_profit)
    
    profit = int(profit) + hash_profit
    
    hash_id = ''.join(secrets.choice(string.ascii_letters + string.digits)
                      for i in range(12))
    
    print(Fore.GREEN + f'Mined: ${hash_profit}', '|', hash_id)
    
    if mined == amount:
        print(Fore.RED + '-----------------------------------------------')
        print(Fore.YELLOW + f'Successfully Mined: {amount} Hashes')
        print(' ')
        
        time.sleep(1)
        
        print(Fore.MAGENTA + f'Profit: ${profit}')
