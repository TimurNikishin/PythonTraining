import pprint


uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

uptime_list = [uptime1, uptime2, uptime3, uptime4]

uptime_dict = {}

for line in uptime_list:
    time_non_sec = line.split('uptime is ')[1].split(', ')
    uptime = 0
    for i in time_non_sec:
        if i.split()[1] == 'year':
            uptime = 31557600
        if i.split()[1] == 'years':
            uptime = int(i.split()[0]) * 31557600
        if i.split()[1] == 'week':
            uptime = uptime + 604800
        if i.split()[1] == 'weeks':
            uptime = uptime + (int(i.split()[0]) * 604800)
        if i.split()[1] == 'day':
            uptime = uptime + 86400
        if i.split()[1] == 'days':
            uptime = uptime + (int(i.split()[0]) * 86400)
        if i.split()[1] == 'hour':
            uptime = uptime +  3600
        if i.split()[1] == 'hours':
            uptime = uptime + (int(i.split()[0]) * 3600)
        if i.split()[1] == 'minute':
            uptime = uptime + 60
        if i.split()[1] == 'minutes':
            uptime = uptime + (int(i.split()[0]) * 60)

    uptime_dict[line.split('uptime')[0]] = uptime

pprint.pprint(uptime_dict)
