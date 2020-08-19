import subprocess
import os, sys, ctypes
import time


def mapped():
    print('Currently Mapped Ports : ')
    cmd = subprocess.Popen('netsh interface portproxy show all', shell=True)
    time.sleep(1)
    input('Press enter to continue...')


def map():
    rip = input('Enter target IP: ')
    rport = input('Enter target port: ')
    hport = input('Enter host port: ')
    print('Select protocol:')
    print('0 TCP')
    print('1 UDP')
    proto = input('0 Selected :')
    if proto is not '1':
        proto = 'TCP'
    else:
        proto = 'UDP'
    cmd = 'netsh interface portproxy add v4tov4 listenport=' + hport + ' connectport=' + rport + ' connectaddress=' + rip
    print('>', cmd)
    cmd = subprocess.Popen(cmd, shell=True)
    time.sleep(1)
    cmd = 'netsh advfirewall firewall add rule name="pymap-' + hport + '" dir=in action=allow protocol=' + proto + ' localport=' + hport
    print('>', cmd)
    cmd = subprocess.Popen(cmd, shell=True)
    time.sleep(1)
    choice = input('Map port again ?[Y/n] ')
    if choice.upper() is 'Y':
        map()


def clear():
    os.system('cls')


def unmap():
    print('Currently Mapped Ports : ')
    cmd = subprocess.Popen('netsh interface portproxy show all', shell=True)
    time.sleep(1)
    hport = input('Enter port no. to unmap: ')
    cmd = 'netsh interface portproxy delete v4tov4 listenport=' + hport
    print('>', cmd)
    cmd = subprocess.Popen(cmd, shell=True)
    time.sleep(1)
    cmd = 'netsh advfirewall firewall delete rule name="pymap-' + hport + '"'
    cmd = subprocess.Popen(cmd, shell=True)
    print('>', cmd)
    time.sleep(1)
    input('Press enter to continue...')


if __name__ == "__main__":
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if not is_admin:
        print('Run as Administrator required')
        input('Press enter to continue...')
        sys.exit()

    while True:
        clear()
        print('Python windows port mapper v1')
        print('1. Show mapped ports')
        print('2. Map a new port')
        print('3. Delete a mapping')
        print('4. Exit')
        choice = input('Enter choice : ')
        print()
        if choice is '1':
            mapped()
        elif choice is '2':
            map()
        elif choice is '3':
            unmap()
        elif choice is '4':
            sys.exit()
