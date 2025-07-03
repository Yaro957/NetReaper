
# 🐸 NetPepep - Lucifer’s Chaotic Port Scanner

![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg?style=flat-square)
---

## 🔥 What is NetPepep?

**NetPepep** is a simple yet *chaotic* terminal-based **port scanner** written in Python.  
It was forged in the flames of madness by Lucifer himself (😈).  

Built for fun, quick scans, and learning basic network socket programming.

---

## 🧠 Features

- 🎯 Scan a single IP or multiple IPs (comma-separated)
- ⚡ Specify number of ports (scans from 1 to N)
- 🟢 Displays open ports
- 🔴 Optionally shows closed ports too
- 💀 Ctrl+C safe (clean exit with message)
- 🌈 Colored output using `termcolor`
- 🐸 Chaotic ASCII banner with attitude

---

## 🖥️ Preview

```
    _   __     __  ____                              
   / | / /__  / /_/ __ \___  ____ _____  ___  _____  
  /  |/ / _ \/ __/ /_/ / _ \/ __ \`/ __ \/ _ \/ ___/  
 / /|  /  __/ /_/ _, _/  __/ /_/ / /_/ /  __/ /      
/_/ |_|\___/\__/_/ |_|\___/\__,_/ .___/\___/_/       
                                /_/   🐸 NETPEPEP

            ~ Lucifer's Chaotic Port Scanner ~
=========================================================

[*] Enter target(s) (comma-separated for multiple): 127.0.0.1
[*] Enter number of ports to scan (e.g., 1000): 100

[~] Scanning IP: 127.0.0.1
[+] Port 22 is OPEN
[-] Port 23 is CLOSED
...
```

---

## ⚙️ Requirements

- Python 3.6 or higher
- `termcolor` package

Install it using pip:

```bash
pip install termcolor
```

---

## 🚀 Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/netpepep.git
cd netpepep
```

2. Run the script:

```bash
python netpepep.py
```

3. Follow the prompts to start scanning.

---

## 🧩 To-Do / Future Features

- [ ] Multithreaded scanning for speed ⚡
- [ ] Export results to a file 📁
- [ ] Port-to-service detection (like Nmap) 🧠
- [ ] Quiet mode (only show open ports)

---

## ⚠️ Disclaimer

> This tool is for **educational purposes only**.  
> Use it only on systems you **own** or have **explicit permission** to scan.  
> Unauthorized port scanning may be illegal.

---

## 🤝 Credits

Made with sockets, chaos, and caffeine by **Lucifer** 🐸  
Star ⭐ the repo if you like it!
