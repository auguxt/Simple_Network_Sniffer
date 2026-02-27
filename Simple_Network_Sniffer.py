# 🛡️ Secure Packet Analyzer (Google Colab)
# ⚠️  WARNING: Only analyze pcap files you own or have permission to inspect.
#              Analyzing network traffic may expose sensitive data (passwords, cookies).
#              This aligns with security best practices: always use HTTPS to prevent exposure.

# ─────────────────────────────────────────────────────────────────────────────
# 1. Installation & Imports
# ─────────────────────────────────────────────────────────────────────────────
!pip install scapy -q

from google.colab import files
from scapy.all import rdpcap, IP, TCP, UDP, Raw
import os

# ─────────────────────────────────────────────────────────────────────────────
# 2. File Upload
# ─────────────────────────────────────────────────────────────────────────────
print("📂 Please upload a .pcap file...")
uploaded = files.upload()

if not uploaded:
    raise Exception("❌ No file uploaded. Please run the cell again and select a file.")

pcap_file = list(uploaded.keys())[0]
print(f"✅ Uploaded file: {pcap_file}")

# ─────────────────────────────────────────────────────────────────────────────
# 3. Packet Processing Function
# ─────────────────────────────────────────────────────────────────────────────
def process_packet(packet):
    """Process each packet from the pcap file with safety checks."""
    try:
        # Check for IP layer
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            print(f"\n🌐 Source IP: {src_ip} → Destination IP: {dst_ip}")

            # Check for TCP layer
            if TCP in packet:
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
                print(f"   🔹 TCP: Port {src_port} → {dst_port}")
                
                # Check for payload (Raw data)
                if packet.haslayer(Raw):
                    payload = bytes(packet[Raw].load)
                    # Try to decode as text, ignore errors
                    try:
                        decoded_payload = payload.decode('utf-8', errors='ignore')
                        # Security Note: If you see passwords here, the service is insecure (HTTP vs HTTPS)
                        if decoded_payload.strip():
                            print(f"   📄 Payload (preview): {decoded_payload[:100]}...")
                    except Exception:
                        print(f"   📄 Payload: [Binary Data - {len(payload)} bytes]")

            # Check for UDP layer
            elif UDP in packet:
                src_port = packet[UDP].sport
                dst_port = packet[UDP].dport
                print(f"   🔹 UDP: Port {src_port} → {dst_port}")
        
        else:
            print(f"\n⚪ Non-IP packet detected (Type: {packet.name})")
            
    except Exception as e:
        print(f"⚠️  Error processing packet: {e}")

# ─────────────────────────────────────────────────────────────────────────────
# 4. Execution & Analysis
# ─────────────────────────────────────────────────────────────────────────────
try:
    print("\n⏳ Reading pcap file...")
    packets = rdpcap(pcap_file)
    total_packets = len(packets)
    print(f"📦 Total packets found: {total_packets}")
    
    # Analyze first 10 packets (adjust count as needed)
    analyze_count = min(10, total_packets)
    print(f"\n🔍 Packet Analysis (Showing first {analyze_count} packets):")
    print("=" * 60)
    
    for i, pkt in enumerate(packets[:analyze_count], 1):
        print(f"\n--- Packet #{i} ---")
        process_packet(pkt)
        
    print("\n" + "=" * 60)
    print("✅ Analysis Complete!")
    
    # Security Reminder based on best practices
    print("\n🛡️  Security Note:")
    print("   If you see plain-text passwords or credentials in the payload,")
    print("   the service is using unencrypted HTTP. Always use HTTPS to protect")
    print("   user data in transit (as per secure communication best practices).")
    
    # Cleanup uploaded file to save space
    os.remove(pcap_file)
    print(f"🗑️  Temporary file '{pcap_file}' removed.")

except Exception as e:
    print(f"\n❌ Fatal Error: {e}")
    print("💡 Tip: Ensure the uploaded file is a valid .pcap or .pcapng format.")
