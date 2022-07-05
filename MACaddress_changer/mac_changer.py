import subprocess
import optparse
import re

def change_address(interface, mac_address):
    current_result = subprocess.check_output(["ifconfig", interface])
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(current_result))
    print("⌛ Changing MAC address for " + interface + " from "+current_mac.group(0))

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    result = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
    if new_mac:
        if new_mac == mac_address:
            print(" Failed to change MAC address")
        else:
            print("✅ MAC address changed to " + new_mac.group(0) + " for " + interface)
    else:
        print("❗ Failed to read MAC address")
        exit()

string = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest = "interface", help = "Interface for which mac address is to be changed")
parser.add_option("-m", "--mac", dest = "mac_address", help = "The new mac address")
(option, argument) = parser.parse_args()
interface = option.interface
mac_address = option.mac_address
if (not interface):
    interface = input("Enter interface name➤ ")
if (not mac_address):
    mac_address = input("Enter new mac address➤ ")
if (not interface) and (not mac_address):
    interface = input("Enter interface name➤ ")
    mac_address = input("Enter new mac address➤ ")
if re.match(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", mac_address):
    if re.match(r"^\d\d", mac_address):
        even_check = re.search(r"^\d\d", mac_address)
        iterate = even_check.group(0)
        for e in iterate:
            if int(e) % 2 != 0:
                print("❗ Invalid\nmac address must start with even number pair")
                exit()
            else:
                continue
        for i in mac_address:
            for j in string:
                if i.lower() == j:
                    print("❗ Invalid \nonly [0-9][a-f][A-F] are allowed in mac address")
                    exit()
                else:
                    continue
        change_address(interface, mac_address)
    else:
        print("❗ mac address must start with even number pair\nonly [0-9][a-f][A-F] are allowed in mac address")
        exit()
else:
    print("❗ Invalid\npossible ; used instead of : in new mac address\nor\nless than 6 pairs given for mac address")
    exit()
