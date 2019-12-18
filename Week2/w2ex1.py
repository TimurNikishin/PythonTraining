addr = input("\n\nPlease enter IP address: ")
octets = addr.split(".")[0:3]
octets.append("0")
subnet = ".".join(octets)
print("\n\nThe subnet is: %s" % subnet)
print("\n\n%-20s %-20s %-20s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX"))
print("{:^20}{:^20}{:^20}".format(subnet, bin(int(octets[0])), hex(int(octets[0]))))
print("{:^20}{:^20}{:^20}".format(subnet, bin(int(octets[0])), hex(int(octets[0]))))





