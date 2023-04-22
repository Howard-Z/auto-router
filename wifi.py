import os
import platform
import macwifi #python3 -m pip install macwifi
import socket

import subprocess

#import objc #need to run 'python3 -m pip install pyobjc'

#connecting to a known wifi network (password known)
def known_wifi(SSID=None):
    #get name from andy's function, if it returns fail code, then ask user for input
    if SSID is not None:
        router_name=SSID
    else:
        router_name=input('Please enter the name/SSID of your Wifi network: ')

    #windows
    if platform.system()=="Windows":
        os.system('cmd /c "netsh wlan show networks"')
        os.system(f'''cmd /c "netsh wlan connect name={router_name}"''')
    #mac
    if platform.system()=="Darwin":
        os.system('networksetup -setairportnetwork en0 ' + router_name)
        print("complete")
#known_wifi(SSID="UCLA_WIFI")



#connecting to a new wifi network (password not known)
    
def createNewConnection(name, SSID, password):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+password+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
    with open(name+".xml", 'w') as file:
        file.write(config)
    os.system(command)
 
# function to display avavilabe Wifi networks   
def displayAvailableNetworks():
    command = "netsh wlan show networks interface=Wi-Fi"
    os.system(command)
 
def new_wifi(SSID=None,pswd=None):
    if SSID is not None:
        router_name=SSID
    else:
        router_name=input('Please enter the name/SSID of your Wifi network: ')
    if pswd is not None:
        password=pswd
    else:
        password=input('Please enter the password: ')
    #windows
    if platform.system()=="Windows":
        displayAvailableNetworks()
        createNewConnection(router_name, router_name, password)
        command = "netsh wlan connect name=\""+router_name+"\" ssid=\""+router_name+"\" interface=Wi-Fi"
        os.system(command)      
        displayAvailableNetworks()  
        print("If you aren't connected, please try again")
    #mac
    if platform.system()=="Darwin":
        macwifi.connect(router_name, password)

#returns string of ip address
def ip_address(SSID=None):
    #windows, not sure if this works
    if(platform.system()=="Windows"):
        address = subprocess.check_output('ifconfig | findstr /i "Gateway"', shell=True)
        string_address = address.decode('utf-8')
        index=string_address.rfind(' ')+1
        return string_address[index:]
    #mac
    if(platform.system()=="Darwin"):
        address = subprocess.check_output("route get default | grep gateway", shell=True)
        string_address = address.decode('utf-8')
        index=string_address.rfind(' ')+1
        return string_address[index:].strip()
    

#new_wifi(SSID="nicole",pswd="hellothere")
print(ip_address())