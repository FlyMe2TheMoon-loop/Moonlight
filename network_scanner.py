import scapy.all as scapy
def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for element in answered_list:
        print(f"{element[1].psrc}\t\t{element[1].hwsrc}")
target_ip = "192.168.1.1/24"
if __name__ == "__main__":
    scan_network("192.168.1.1/24") 
    scan_network(target_ip)