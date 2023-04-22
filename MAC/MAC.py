from mac_vendor_lookup import MacLookup

# quick function that takes a MAC adress string formatted as:
# "00:80:41:12:FE"
# returns a string of the vendor of the mac address
def lookup(MAC):
    return MacLookup().lookup(MAC)


#this quick function (ON WINDOWS) gets the mac address of the default gateway
import subprocess
def get_mac_address(ip_address):
    arp_command = ['arp', '-a', ip_address]
    output = subprocess.check_output(arp_command).decode()
    mac_address = output.split()[-2]
    return mac_address



#print(lookup(get_mac_address('128.97.250.5')))