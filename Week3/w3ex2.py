entry = list()

entry.append("*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i")
entry.append("*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i")
entry.append("*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i")
entry.append("*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i")

print "\n\n%-20s %-20s" % ("ip_prefix", "as_path")

for i in entry:
    j = i.split()
    j.remove('i')
    print "%-20s %-20s" % (j[1], " ".join(j[4:]))


