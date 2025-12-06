
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime


def process_packet(packet):
       # Capture time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Default values
    src_ip = dst_ip = "N/A"
    protocol_name = "Unknown"
    payload_preview = ""

    # Check if this packet has an IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Identify protocol
        if TCP in packet:
            protocol_name = "TCP"
        elif UDP in packet:
            protocol_name = "UDP"
        elif ICMP in packet:
            protocol_name = "ICMP"
        else:
            protocol_name = f"IP proto {packet[IP].proto}"

    # Try to get some payload data (if present)
    if Raw in packet:
        raw_data = bytes(packet[Raw].load)
        # Show first few bytes for preview
        payload_preview = raw_data[:32]  # first 32 bytes
        try:
            payload_preview = payload_preview.decode(errors="replace")
        except Exception:
            # If not decodable, keep as bytes string
            payload_preview = str(payload_preview)
    else:
        payload_preview = ""

    # Print nicely
    print("=" * 80)
    print(f"Time      : {timestamp}")
    print(f"Source IP : {src_ip}")
    print(f"Dest IP   : {dst_ip}")
    print(f"Protocol  : {protocol_name}")
    if payload_preview:
        print(f"Payload   : {payload_preview}")
    else:
        print("Payload   : <no visible data>")


def main():
    print("=== Network Packet Analyzer ===")
    print("This tool will capture packets on your default network interface.")
    print("Press Ctrl + C to stop.\n")

    # You can also specify iface='eth0' or 'Wi-Fi' depending on OS
    try:
        # store=False means we don't keep packets in memory, we just process them on the fly
        sniff(prn=process_packet, store=False)
    except PermissionError:
        print("❌ Permission denied: You need to run this script as Administrator / root.")
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user (Ctrl + C).")
    except Exception as e:
        print("❌ Error while sniffing packets:", e)


if __name__ == "__main__":
    main()
