"""import optparse
import scapy.all as scapy

def arp_req_res(ip):
    print(ip)
    arp_req = scapy.ARP(pdst=ip)
    brdcst_ethfrm = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_pkt = brdcst_ethfrm/arp_req
    response = scapy.srp(arp_req_pkt, timeout=1, verbose=False)[0]
    output_lst = []
    print(response)
    for r in response:
        packet_dict = {"ip":r[1].psrc, "mac":r[1].hwsrc}
        output_lst.append(packet_dict)
    print(f"output:\n{output_lst}")
    return output_lst

def output_print(output_list):
    flag = 1
    for o in output_list:
        print("\n______________ 📦 ["+str(flag)+"] ______________")
        print(o["ip"] + "\t" + o["mac"])
        flag = flag+1


parser = optparse.OptionParser()
parser.add_option("-i", "--ip", dest = "input_ip", help = "ip or ip range to be scanned")
(option, argument) = parser.parse_args()
result = arp_req_res(option.input_ip)
print(f"IP:\n{option.input_ip}")
output_print(result)
"""
import scapy.all as scapy
def scan(ip):
	scapy.arping(ip)
scan('192.168.43.1/24')

