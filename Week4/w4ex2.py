import pprint

sh_ver = '''
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102
'''

sh_ver_list = sh_ver.split('\n')

router_dict = {}

for line in sh_ver_list:
    if 'Cisco IOS Software' in line:
        router_dict['vendor'] = 'Cisco'
        os_version = line.split(',')[2]
        router_dict['os_version'] = os_version.split('Version ')[1]
    if 'bytes of memory' in line:
        router_dict['model'] = line.split('processor')[0]
    if 'Processor board ID' in line:
        router_dict['serial'] = line.split('Processor board ID ')[1]
    if 'uptime is ' in line:
        router_dict['uptime'] = line.split('uptime is ')[1]

print router_dict['vendor']
print router_dict['os_version']
print router_dict['model']
print router_dict['serial']
print router_dict['uptime']


pprint.pprint(router_dict)




