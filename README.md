# 🌐 Simple Network Packet Sniffer (Scapy)

<div align="center">

A beginner-friendly Python script that captures and displays live network packets  
using the powerful **Scapy** library.

</div>

---

## 📖 Overview

This project is a minimal network packet sniffer built with Python and Scapy.

It captures packets from a specified network interface and prints a summary of each packet to the console.

This tool is intended for:

- 🎓 Learning how packet sniffing works  
- 🛡️ Cybersecurity beginners  
- 🧪 Networking experiments in lab environments  
- 🏁 CTF practice  

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**.

Packet sniffing without permission on networks you do not own or manage may be illegal.  
Always use this tool in:

- Your own lab
- A virtual machine
- An authorized testing environment

---

## 🛠️ Requirements

- Python 3.x
- Scapy

---

## 📦 Installation

### 1️⃣ Install Scapy

If using Jupyter Notebook:

```python
!pip install scapy
```

If using terminal:

```bash
pip install scapy
```

---

## 🚀 How It Works

```python
from scapy.all import *

def packet_callback(packet):
    print(packet.summary())

sniff(prn=packet_callback, iface="eth0", count=10)
```

### 🔍 Explanation

- `sniff()` → Captures network packets
- `prn=packet_callback` → Calls a function for every captured packet
- `iface="eth0"` → Specifies the network interface
- `count=10` → Captures only 10 packets
- `packet.summary()` → Prints a short summary of each packet

---

## 🖥️ Running the Script

```bash
python sniffer.py
```

You may need elevated privileges:

```bash
sudo python sniffer.py
```

---

## 📡 Example Output

```
Ether / IP / TCP 192.168.1.5:51512 > 142.250.183.78:https
Ether / ARP who has 192.168.1.1 says 192.168.1.5
Ether / IP / UDP 192.168.1.5:5353 > 224.0.0.251:mdns
```

Each line represents a captured packet summary.

---

## 🔧 Customization

### Capture More Packets

```python
sniff(prn=packet_callback, iface="eth0", count=50)
```

### Capture Indefinitely

```python
sniff(prn=packet_callback, iface="eth0")
```

### Filter Specific Traffic (e.g., TCP Only)

```python
sniff(filter="tcp", prn=packet_callback, iface="eth0")
```

### Capture on Different Interface

Find your interfaces:

```bash
ifconfig
```

or

```bash
ip a
```

Then replace `"eth0"` with your interface name (e.g., `"wlan0"`).

---

## 🧠 Learning Concepts

This project helps you understand:

- Packet sniffing fundamentals
- Network interfaces
- TCP/IP basics
- Real-time traffic monitoring
- How Scapy works

---

## 🛡️ Security Note

Modern operating systems require:

- Root/admin privileges for packet capture
- Proper network permissions
- Legal authorization

Always follow ethical hacking guidelines.

---

## 📂 Repository Structure

```
simple-network-sniffer/
└── sniffer.py
```

---

## 🚀 Future Improvements

- Save captured packets to a `.pcap` file
- Display packet details instead of summary
- Add protocol-based filtering
- Build a GUI using Tkinter
- Detect suspicious traffic patterns

---

## 👨‍💻 Author

Syed Sameer  
Aspiring Cybersecurity Enthusiast  

---

<div align="center">

Made with ❤️ by ChatGPT  
Prompted by Syed Sameer  

⭐ If you found this useful, consider starring the repository!

</div>
