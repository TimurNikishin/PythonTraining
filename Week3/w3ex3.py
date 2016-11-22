entry = list()
intbr = list()

entry.append("FastEthernet0   unassigned      YES     unset          up          up")
entry.append("FastEthernet1   unassigned      YES     unset          up          up")
entry.append("FastEthernet2   unassigned      YES     unset          down      down")
entry.append("FastEthernet3   unassigned      YES     unset          up          up")
entry.append("FastEthernet4    6.9.4.10          YES     NVRAM       up          up")
entry.append("NVI0                  6.9.4.10          YES     unset           up          up")
entry.append("Tunnel1            16.25.253.2     YES     NVRAM       up          down")
entry.append("Tunnel2            16.25.253.6     YES     NVRAM       up          down")
entry.append("Vlan1                unassigned      YES    NVRAM       down      down")
entry.append("Vlan10              10.220.88.1     YES     NVRAM       up          up")
entry.append("Vlan20              192.168.0.1     YES     NVRAM       down      down")
entry.append("Vlan100            10.220.84.1     YES     NVRAM       up          up")

for i in entry:
    j = tuple(i.split())
    if j[4] == 'up' and j[5] == 'up':
        intbr.append(j)
        print ' '.join(j)


