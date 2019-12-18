addr = raw_input("\n\nPlease enter the IP address: ")
octets = addr.split(".")
print(type(octets[1]))
print("\n\n%-20s %-20s %-20s %-20s" % ("first_octet", "second_octet", "third_octet", "fourth_octet"))
print("%-20s %-20s %-20s %-20s" % (bin(int(octets[0]))[2:], bin(int(octets[1]))[2:], bin(int(octets[2]))[2:], bin(int(octets[3]))[2:]))


