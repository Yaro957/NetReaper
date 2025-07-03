import socket
from termcolor import colored

def print_banner():
    banner = r"""
    _   __     __  ____                              
   / | / /__  / /_/ __ \___  ____ _____  ___  _____  
  /  |/ / _ \/ __/ /_/ / _ \/ __ `/ __ \/ _ \/ ___/  
 / /|  /  __/ /_/ _, _/  __/ /_/ / /_/ /  __/ /      
/_/ |_/\___/\__/_/ |_|\___/\__,_/ .___/\___/_/       
                                /_/   
    """
    print(colored(banner, 'cyan'))
    print(colored("            ~ Lucifer's Port Scanner ~", 'magenta'))
    print(colored("=========================================================", 'yellow'))

# 🛠️ Scans all ports up to `ports` on a given target
def scan(target, ports):
    try:
        print(colored("\n[*] Scanning port for IP."+target, 'magenta'))
        for port in range(1, ports + 1):
            scan_port(target, port)
    except KeyboardInterrupt:
        print(colored("\n[!] Scan interrupted by user.", 'red'))
        exit()

# 🔍 Scans a single port and prints if open
def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print(colored(f"[+] Port {port} is OPEN", 'green'))
        sock.close()
    except:
        print(colored(f"[-] Port {port} is CLOSE", 'red'))
        # pass


print_banner()
target = input(colored("[*] Enter target(s) (comma-separated for multiple): ", 'yellow')).strip()
ports = int(input(colored("[*] Enter number of ports to scan (e.g., 1000): ", 'yellow')))

# 🔁 Scan Logic
if ',' in target:
    print(colored("\n[*] Multiple targets detected. NetReaper goes wild...\n", 'magenta'))
    for ip_addr in target.split(','):
        scan(ip_addr.strip(), ports)
else:
    print(colored("\n[*] Single target detected. Unleashing NetReaper...\n", 'magenta'))
    scan(target.strip(), ports)

print(colored("\n[ ✔ ] Scan complete.", 'green'))
