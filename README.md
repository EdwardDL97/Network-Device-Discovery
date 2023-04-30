# Network-Device-Discovery
Python script that uses `Scapy` and `manuf` libraries to sniff (detect) ARP Requests and Replies to find new devices. There is also an option to print known devices (ip address, mac address, and manufacturer name)

## Steps to run ARP_monitor.py in Linux

1. install the following libraries using `pip3`
  1. `pip3 install manuf`
  2. `pip3 install scapy`
  
## How This Works
The python script focuses on the `Scapy` library to do all the heavy lifting. Scapy will sniff packets that are pertaining to ARP and will extract the mac address and ip address when the ARP packet is an ARP request or ARP reply. By having the MAC address, we can then use it to locate who is the manufacturer by using the `manuf` library to locate the manufacturer of the device. Once we get the manufacturer name, IP address, and MAC address, it will then be saved to a dictionary where it can be used as a reference to determine whether there is a new device on the network. The same dictionary is used for option 1 to print out all the known devices that are connected to the network.
  
## Future Updates

- Use Twilio or some sort of library to connect to email to get notifications when there is a new device
- Have option 2 run in the background
- Plan to save known devices as a file and have an option to rerun script with known devices file so it doesn't have to scan from the beginning
- Would like to filter out MAC addresses that don't have a manufacturer name. Either make a second file that has all the unknown manufacturer names or keep it in the same file as the devices list, but have a seperate section
- What happens when there is a device that is already connected to the network??? Need to figure out a way to get devices that are already in the network.


## Notes

- Address Resolution Protocol (ARP) - Protocol used to map the ip address to the mac address. The host device first checks its ARP cache (IP address and MAC address mapping table) to determine if it knows the MAC address. If the host device does not have the MAC address, it will send out an ARP request by broadcasting (sending a message to everyone in the network) and asking "Hey! who has this IP address?". Only the device with the associated IP address will send an ARP reply by saying "I have this IP address and here is my MAC address.". Since the other devices didn't have the IP address, then they won't reply back. Now that the original host device has the MAC address of the device it wants to communicate, it will then send data to the destination device.
