entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

entry1 = entry1.split()
entry2 = entry2.split()
entry3 = entry3.split()
entry4 = entry4.split()


print "\n\n%-20s %-20s" % ("ip_prefix", "as_path")
print "%-20s %-20s" % (entry1[1], " ".join(entry1[4:]))
print "%-20s %-20s" % (entry2[1], " ".join(entry2[4:]))
print "%-20s %-20s" % (entry3[1], " ".join(entry3[4:]))
print "%-20s %-20s" % (entry4[1], " ".join(entry4[4:]))

