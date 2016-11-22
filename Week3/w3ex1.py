import sys

print type(sys.argv)
print sys.argv

addr = sys.argv.pop()
octets = addr.split(".")

for i,j in enumerate(octets):
    octets[i] = bin(int(j))[2:]
    while len(octets[i]) < 8:
        octets[i] = "0" + octets[i]

print "%-20s %-20s" % ("IP_ADDRESS", "BINARY")
print "%-20s %-20s" % (addr, ".".join(octets))







