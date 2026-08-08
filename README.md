# Simple Network Sniffer 🌐

A simple Python script that reads a `.pcap` file and
shows what's inside each network packet.

> ⚠️ For learning only. Only analyze files you own or
> have permission to inspect.

---

## What's Inside

```
Simple_Network_Sniffer/
│
├── sniffer.py
├── sample.pcapng
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## How It Works

It reads each packet from a `.pcap` file and shows:
- Source and destination IP
- Protocol (TCP or UDP)
- Port numbers
- Any readable data in the payload

```
--- Packet #1 ---
  From: 192.168.1.5  →  To: 142.250.183.78
  Protocol: TCP
  Port: 51512 → 443

--- Packet #2 ---
  From: 192.168.1.5  →  To: 224.0.0.251
  Protocol: UDP
  Port: 5353 → 5353
```

---

## Setup

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python sniffer.py
```

To use your own `.pcap` file, change this line in `sniffer.py`:

```python
analyze_file("your_file.pcap", count=10)
```

---

## What Each Part Does

```python
rdpcap("file.pcap")       # Read the pcap file
packet[IP].src            # Get source IP
packet[IP].dst            # Get destination IP
packet[TCP].sport         # Get source port
packet[Raw].load          # Get raw payload data
```

---

## Requirements

- Python 3.6+
- `scapy`

---

## License

MIT — see [LICENSE](LICENSE)
