import random
import sys
from subprocess import call
from sys import platform
import time
import datetime
from colorama import Fore
def clear():
    if platform not in ('win32', 'cygwin'):
        command = 'clear'
    else:
        command = 'cls'
    try:
        call(command, shell=True)
    except OSError as e:
        print(type(e).__name__, e)

red='\033[31m'
green='\033[32m'
blue='\033[36m'
pink='\033[35m'
#requments
dscripts = ['https://github.com/Mrhackerha/mrhackergod/blob/main/Dxprit-mrhacker.py','https://github.com/Mrhackerha/mrhackergod/blob/main/Dxprit.py','https://github.com/Mrhackerha/mrhackergod/blob/main/Filter.py','https://github.com/Mrhackerha/mrhackergod/blob/main/Malicious-javascript.js','https://github.com/Mrhackerha/mrhackergod/blob/main/Malicious.zip','https://github.com/Mrhackerha/mrhackergod/blob/main/Mrhacker-god.cs','https://github.com/Mrhackerha/mrhackergod/blob/main/Mrhacker.json','https://github.com/Mrhackerha/mrhackergod/blob/main/Mrhackergod.cs','https://github.com/Mrhackerha/mrhackergod/blob/main/Php-malicious.php','https://github.com/Mrhackerha/mrhackergod/blob/main/Sexy.py','https://github.com/Mrhackerha/mrhackergod/blob/main/Yftt100k','https://github.com/Mrhackerha/mrhackergod/blob/main/Yftt12k.py','https://github.com/Mrhackerha/mrhackergod/blob/main/Yftt15k.py','https://github.com/Mrhackerha/mrhackergod/blob/main/index.html','https://github.com/Mrhackerha/mrhackergod/blob/main/iyftt15k.py','https://github.com/Mrhackerha/mrhackergod/blob/main/malicious%20.html','https://github.com/Mrhackerha/mrhackergod/blob/main/malicious-pdf.py','https://github.com/Mrhackerha/mrhackergod/blob/main/traport.rubika.reset.yttks58k.im009','https://github.com/Mrhackerha/mrhackergod/blob/main/yftt15k-mrhacker-dscript.py','https://github.com/Mrhackerha/mrhackergod/blob/main/yftt15k-rubika-dscript.py','https://github.com/Ytthacker/dscript-rubika','https://github.com/mr-hacker-king/DXPRIT']
linksxs = ['https://github.com/Mrhackerha/mrhackergod/blob/main/4f453f300c2fe-full-6.jpg', 'https://github.com/Mrhackerha/mrhackergod/blob/main/IMG-20220704-WA0032.jpg', 'https://github.com/Mrhackerha/mrhackergod/blob/main/IMG-20220823-WA0054.jpg', 'https://github.com/Mrhackerha/mrhackergod/blob/main/IMG_20220726_041439_396.jpg', 'https://github.com/Mrhackerha/mrhackergod/blob/main/IMG_20220825_030904_525.jpg', 'https://github.com/Mrhackerha/mrhackergod/blob/main/VID-20220712-WA0020.mp4', 'https://github.com/Mrhackerha/mrhackergod/blob/main/VID-20220712-WA0020.mp4', 'https://github.com/Mrhackerha/mrhackergod/blob/main/VID-20220712-WA0054.mp4','https://github.com/Mrhackerha/mrhackergod/blob/main/VID-20220712-WA0057.mp4','https://github.com/Mrhackerha/mrhackergod/blob/main/VID-20220824-WA0072.mp4','https://github.com/Mrhackerha/mrhackergod/blob/main/casey-kisses-grooby-girls-06.jpg','https://github.com/Mrhackerha/mrhackergod/blob/main/images%20(1)%20(3).jpeg','https://github.com/Mrhackerha/mrhackergod/blob/main/images%20(24).jpeg','https://github.com/Mrhackerha/mrhackergod/blob/main/images%20(31).jpeg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-26-43.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-26-50.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-26-55.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-27-00.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-27-04.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-27-10.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B6-%DB%B0%DB%B6-%DB%B0%DB%B8_%DB%B0%DB%B8-%DB%B0%DB%B7-%DB%B1%DB%B2.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B6-%DB%B0%DB%B6-%DB%B0%DB%B8_%DB%B0%DB%B8-%DB%B0%DB%B7-%DB%B2%DB%B7.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B7-%DB%B0%DB%B3-%DB%B1%DB%B0_%DB%B2%DB%B3-%DB%B5%DB%B3-%DB%B2%DB%B1.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B7-%DB%B0%DB%B5-%DB%B1%DB%B2_%DB%B1%DB%B0-%DB%B5%DB%B9-%DB%B4%DB%B3.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B7-%DB%B0%DB%B8-%DB%B0%DB%B6_%DB%B2%DB%B1-%DB%B1%DB%B4-%DB%B1%DB%B5.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B7-%DB%B0%DB%B8-%DB%B1%DB%B1_%DB%B1%DB%B6-%DB%B0%DB%B6-%DB%B5%DB%B8.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B7-%DB%B0%DB%B8-%DB%B1%DB%B1_%DB%B1%DB%B6-%DB%B0%DB%B6-%DB%B5%DB%B8.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B7-%DB%B0%DB%B8-%DB%B2%DB%B5_%DB%B1%DB%B1-%DB%B0%DB%B5-%DB%B0%DB%B6.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B7-%DB%B0%DB%B9-%DB%B0%DB%B7_%DB%B2%DB%B1-%DB%B0%DB%B8-%DB%B4%DB%B2.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B1-%DB%B2%DB%B7_%DB%B1%DB%B4-%DB%B4%DB%B8-%DB%B2%DB%B5.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B1-%DB%B2%DB%B7_%DB%B1%DB%B4-%DB%B4%DB%B8-%DB%B4%DB%B7.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B2-%DB%B1%DB%B9_%DB%B1%DB%B7-%DB%B1%DB%B0-%DB%B2%DB%B7.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B2-%DB%B2%DB%B1_%DB%B2%DB%B1-%DB%B1%DB%B8-%DB%B0%DB%B0.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B4-%DB%B0%DB%B1_%DB%B1%DB%B8-%DB%B5%DB%B9-%DB%B0%DB%B0.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B7-%DB%B0%DB%B8_%DB%B1%DB%B1-%DB%B4%DB%B6-%DB%B1%DB%B8.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B8-%DB%B0%DB%B2_%DB%B2%DB%B3-%DB%B0%DB%B1-%DB%B4%DB%B6.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B8-%DB%B0%DB%B3_%DB%B0%DB%B3-%DB%B2%DB%B8-%DB%B1%DB%B4.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B8-%DB%B1%DB%B9_%DB%B1%DB%B5-%DB%B3%DB%B6-%DB%B2%DB%B8.jpg']
num = ['0','1','2','3','4','5','6','7','8','9','10']
bug_num = ['05','13','62','63','49','l5','64','67','38','39','46','87','4','56','568','795','368','85','658','254','345','775','355','754','447','745','357']
letter = ['a','f','e','n','h','x','u','t','w','m','z']
slashes = ['/', '//', '///']
letterhss = ['sex','xxx','porn','spam','hack','fil','filter',' scamming-users',' violent-content','threaten','intimidate','harass-users','Violation-of-Islamic','fuck-Islamic-Republic','pornhub','fuck-rubika','Malicious-link',]
adad_hasas = 'https://'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+''+random.choice(slashes)+''+random.choice(letter)+''+random.choice(slashes)+''+random.choice(letter)+''+random.choice(slashes)+''+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+''
bug = 'https://'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'/'+random.choice(letter)+'//'+random.choice(letter)+'/'+random.choice(letter)+'/'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'/)\''
ltterhss = random.choice(letterhss)+'.'+random.choice(letterhss)+'.'+random.choice(letterhss)+'.'+random.choice(letterhss)
codereal =  adad_hasas+bug+ltterhss+random.choice(dscripts)+random.choice(linksxs)
color='\033[34m'

print(f"{green} ")
print(f"{green} ")

print (Fore.WHITE + "")

print(f"{blue} ")
print ("   ")
print (Fore.YELLOW + "")
print(f"\033[35m")
x = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡻⠓⠊⠉⠉⠑⠚⢫⢟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠛⢛⣍⣙⣻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠳⡹⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠏⢁⣼⠋⠉⠀⠀⠀⠉⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡿⠁⢀⠞⠈⣇⣼⡆⠀⠀⠀⠀⠀⠹⡹⣿⣿⣿⣿⣿⣿⣿⢹⣧⠀⠀⠀⠀⣀⣀⡀⠀⠀⣸⢸⡱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠧⠔⠚⠒⠲⣄⡼⠀⠀⠀⠀⠀⠀⠀⢇⣿⣿⣿⣿⣿⣿⣿⣿⢟⣀⣤⣴⣖⠓⠒⣭⣄⡘⢟⣾⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡀⢀⡀⣠⢒⣯⣅⣀⠠⢶⡤⢤⡀⠀⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢹⠿⣿⣿⣿⣷⣽⣿⣿⣿⣿⣿⣿⣿⠋⠁⢀⠈⢺⡽⢿⣿
⣧⠛⠠⢞⣿⣿⣿⣿⣿⣇⣈⣽⣭⣙⡽⣿⣿⣿⣿⣿⣿⣿⣿⣈⠿⠟⠋⣴⣿⡆⠸⠿⠿⢿⣾⣿⣿⣿⣿⣿⣟⣯⣴⠿⣿⣶⣮⣿⡞⢿
⣿⣿⢛⣦⠚⠻⠛⡏⢙⣾⡟⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡲⠛⠿⡿⠟⠀⢷⣶⣾⣿⣿⣿⣿⣿⣿⣿⡿⣿⣗⡉⠻⣿⣻⣿⢸
⣿⣿⡟⣸⣷⢧⡄⠘⠿⣿⠇⠈⡝⣾⣿⣿⠋⠀⣀⡙⣿⣿⣿⣟⡿⣿⣷⣖⣗⣖⣖⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣷⣾⡯⠿⣾
⣿⡿⠁⣿⣿⣷⣯⣺⡲⣷⢤⣷⣿⣿⣿⣿⣿⣿⣿⢿⢿⣿⣿⣿⣦⠛⠻⡯⠿⠯⠽⠟⣹⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣛⣽
⣿⣷⡀⠿⣿⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣼⣿⣶⣽⣿⣿⣿⣿⣧⣄⣧⣀⣀⣠⣾⢫⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⣶⣶
⣿⣾⢷⣴⠃⠉⠓⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⠶⣾⣖⢺⣿⣝⣟⠻⣿⣿⠿⠟⣛⡛⠛⠻⣟⢯⣸⣿⣿
⣟⡿⣯⣾⣿⣶⣾⣽⠿⢋⣹⣿⣿⣿⣿⣯⣅⣤⣭⣷⣦⣭⣿⡵⣿⣿⣿⣿⠛⠻⡞⠛⣻⣿⠿⠛⢋⣡⣴⣶⣿⣿⡿⠖⠛⢻⣿⣥⡈⣳
⣯⣟⡶⢤⡉⣿⠛⢭⢶⣿⣿⠌⣿⡟⢏⠀⠀⠙⣿⣿⣿⣿⣿⠻⣦⣄⣨⣟⠉⠉⠉⠉⣟⣒⣶⣾⣿⠇⣸⣿⣿⣿⣯⢚⢳⢰⣿⡿⠶⣟
⣿⣿⣿⣷⣿⣿⣆⣠⣿⣿⣜⡄⣿⣷⠘⡆⣼⣴⣿⣿⣿⢱⣿⣧⣌⠛⠛⠯⣶⣤⣀⣤⣾⣿⠿⢛⣫⣴⢿⣿⣿⢟⣽⠻⣎⡆⢿⣿⠶⢿
⠿⠿⠿⠛⠛⠻⢏⠁⡼⣟⢃⡇⢻⢻⣼⠁⣿⣭⣿⣿⣷⡠⡿⢿⣿⣿⣷⣴⢯⠀⠉⢣⣤⣶⣿⣿⣿⡿⠏⣿⣏⣿⣿⡇⡟⡼⡜⣿⣿⣿

█▀▀ █▀█ █▀▄ █▀▀   █▀▀ █ █░░ ▀█▀ █▀█   █▀▄▀█ ▄▀█ █▄▀ █▀▀ █▀█
█▄▄ █▄█ █▄▀ ██▄   █▀░ █ █▄▄ ░█░ █▀▄   █░▀░█ █▀█ █░█ ██▄ █▀▄ v1.0
"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.0000001)
#i'm god
print(Fore.GREEN + str(datetime.datetime.now()))
print(f"{red} ")


time.sleep(1)
print(f"{green} ")
print ("welcome ")
print (Fore.YELLOW + "")
time.sleep(0.1)
print (Fore.LIGHTGREEN_EX + " programing by DMNHACKER        ")
print (Fore.BLUE + "Supports rubika v3.11 ")
print (Fore.RED + " servers.....ON          ")
print(Fore.WHITE+'\n'+Fore.LIGHTBLUE_EX)
print(f"{blue} ")
time.sleep(2.5)
print ("")
time.sleep(0.7)
print (".........")
time.sleep(0.6)
print ("........")
time.sleep(0.5)
print (".......")
time.sleep(0.4)
print ("......")
time.sleep(0.3)
print (".....")
time.sleep(0.2)
print ("....")
time.sleep(0.1)
print ("...")
time.sleep(0.5)
print ("..")
time.sleep(0.1)
print (".")
time.sleep(0.5)
print (Fore.LIGHTYELLOW_EX + "installed!")
time.sleep(3)
print ("")
clear()
try:
    get = int(input("inter 1 for give new code >>>   "))

if get == 1:
    print(Fore.blue + codereal)
    
    time.sleep(1)
    print(f"{red}")
    print((' 20 sayer 30 mostahjan '))
    print(f"{green}")
    time.sleep(1)
    
time.sleep(0.6)

exit1=input(color.green+"Enter key For back >>> ")
print('ok')
time.sleep(2)
system("clear")
time.sleep(2)
