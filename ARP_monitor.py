from scapy.all import *
from manuf import manuf


# Create a manufacturer lookup object
mac_lookup = manuf.MacParser()

# Tracks known devices in a dictionsary
known_devices = {}

# Define a function to print the seen_devices dictionary in the desired format
def print_seen_devices():
    for ip_address, device in known_devices.items():
        mac_address = device['mac']
        manufacturer = device['manufacturer']
        print(f"IP address - {ip_address}")
        print(f"MAC address - {mac_address} ({manufacturer})\n")

# Define a function to process ARP packets
def arp_monitor_callback(packet):
  # Checks if packet is an ARP packet and the ARP operation code (op) is either ARP request (1) or ARP reply (2)
    if ARP in packet and packet[ARP].op in (1,2):
        # Extract the MAC and IP addresses from the packet
        mac_address = packet[ARP].hwsrc
        ip_address = packet[ARP].psrc

        # Use manuf to look up the manufacturer of the device
        manufacturer = mac_lookup.get_manuf(mac_address)

        # Checks if the device has been seen before
        if ip_address not in known_devices:
          known_devices[ip_address] = {'mac': mac_address, 'manufacturer': manufacturer}

          # Print the device information
          print(f"Device connected: ip: {ip_address} mac: {mac_address} ({manufacturer})")

def print_menu():
  print("\n-----Welcome to Device Finder-----")
  print("| 1, Print known devices         |")
  print("| 2. Start sniff                 |")
  print("| 3. Exit                        |")
  print("----------------------------------\n")

while True:
  # Display option screen
  print_menu()

  # Get user input
  choice = input("Enter option number: ")

  if choice == '1':
    print_seen_devices()
  elif choice == '2':
    # Use Scapy to listen for ARP packets on the network
    print("Press CTRL+C to go back to Option Menu.\n")
    sniff(prn=arp_monitor_callback, filter="arp", store=0)
  elif choice == '3':
    print("Goodbye!\n")
    break
  else:
    print("Invalid option. Please try again.")