# 🕵️‍♂️ Network Packet Analyzer — Task 05

This project was created as part of my **Prodigy InfoTech Cyber Security Internship (Task-05)**.  
The tool captures live network packets and displays useful details such as:

- 🔹 Source IP Address  
- 🔹 Destination IP Address  
- 🔹 Protocol Type (TCP, UDP, ICMP, etc.)  
- 🔹 Small preview of payload data (if available)

It serves as a beginner-friendly way to understand how data travels across networks.

---

## ⚠️ Ethical & Legal Notice

This tool is intended **only for learning and ethical use**.  
Do **not** use it on networks or devices you do not own or have permission to test.

Unauthorized packet sniffing may violate:

- 🔸 Privacy laws  
- 🔸 Computer misuse regulations  
- 🔸 Organizational policies  

Use responsibly.

---

## 🛠 Requirements

Install the necessary dependency:
pip install scapy
Windows users must also install Npcap (WinPcap-compatible mode):
👉 https://npcap.com/#download

---

▶️ How to Run

1.Run the script as Administrator (Windows) or root (Linux) : python network_packet_analyzer.py
2.Press Ctrl + C anytime to stop capturing packets.
Example Output

================================================================================
Time      : 2025-12-06 14:23:11
Source IP : 192.168.1.10
Dest IP   : 142.250.183.100
Protocol  : TCP
Payload   : GET / HTTP/1.1 Host: google.com

---

📚 What I Learned

Through this task, I explored:
 - How packets are structured at the network level
 - How tools like Wireshark and IDS systems capture traffic
 -  How packet sniffing can aid in security monitoring and analysis
 - Why safe and ethical usage of sniffing tools is important

---
👩‍💻 Author

Vinitha G
Cyber Security Student | Prodigy InfoTech Intern
🔗 GitHub: @Vinitha024
