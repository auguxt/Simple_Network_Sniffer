# Simple Network Packet Sniffer
# Reads a .pcap file and shows what's inside

from scapy.all import rdpcap, IP, TCP, UDP, Raw

def analyze_packet(packet, number):
    print(f"\n--- Packet #{number} ---")

    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        print(f"  From: {src}  →  To: {dst}")

        # TCP packet
        if TCP in packet:
            print(f"  Protocol: TCP")
            print(f"  Port: {packet[TCP].sport} → {packet[TCP].dport}")

            # Show payload if exists
            if packet.haslayer(Raw):
                payload = packet[Raw].load.decode('utf-8', errors='ignore')
                if payload.strip():
                    print(f"  Data: {payload[:100]}")

        # UDP packet
        elif UDP in packet:
            print(f"  Protocol: UDP")
            print(f"  Port: {packet[UDP].sport} → {packet[UDP].dport}")

    else:
        print(f"  Non-IP packet: {packet.name}")


def analyze_file(pcap_file, count=10):
    print(f"Reading: {pcap_file}\n")

    packets = rdpcap(pcap_file)
    total   = len(packets)
    show    = min(count, total)

    print(f"Total packets found: {total}")
    print(f"Showing first {show} packets")
    print("=" * 40)

    for i, pkt in enumerate(packets[:show], 1):
        analyze_packet(pkt, i)

    print("\n" + "=" * 40)
    print("Done!")


# --- Try it out ---
analyze_file("sample.pcapng", count=10)
