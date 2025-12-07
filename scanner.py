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
    print(colored("              ~ Lucifer's Port Scanner ~", 'magenta'))
    print(colored("=========================================================\n", 'yellow'))

def scan(target, ports):
    print(colored(f"\n[*] Scanning {target}...", 'magenta'))
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.4)
            result = sock.connect_ex((ipaddress, port))
            if result == 0:
                print(colored(f"[+] Port {port:<5} OPEN", 'green'))
            # Comment out next line to silence closed ports entirely  
            # else:
            #     print(colored(f"[-] Port {port:<5} CLOSED", 'red'))

    except KeyboardInterrupt:
        print(colored("\n[!] Scan interrupted by user.", 'red'))
        exit()
    except Exception as e:
        print(colored(f"[!] Error scanning port {port}: {e}", 'red'))

print_banner()

target = input(colored("[*] Enter target(s) (comma-separated for multiple): ", 'yellow')).strip()
ports = int(input(colored("[*] Enter number of ports to scan (e.g., 1000): ", 'yellow')))

if ',' in target:
    print(colored("\n[*] Multiple targets detected. Unleashing NetReaper...\n", 'magenta'))
    for ip in target.split(','):
        scan(ip.strip(), ports)
else:
    print(colored("\n[*] Single target detected. Releasing NetReaper...\n", 'magenta'))
    scan(target.strip(), ports)

print(colored("\n[ ✔ ] Scan completed successfully!", 'green'))
