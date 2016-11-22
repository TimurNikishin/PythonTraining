while True:
    try:
        addr = raw_input('\n\nPlease enter IP address: ')
        octets = addr.split(".")

        for i, j in enumerate(octets):
            octets[i] = int(j)

        if len(octets) <> 4:
            print "Invalid IP address. Must be in format x.x.x.x"

        elif octets[0] < 1 or octets[0] > 223 or octets[0] == 127:
            print "Invalid IP address. First octet must be between 1 and 223 and can't be equal to 127"

        elif octets[0] == 169 and octets[1] == 254:
            print "Invalid IP address. It can't be 169.254.x.y"

        elif octets[1] < 0 or octets[2] < 0 or octets[3] < 0:
            print "Invalid IP address. The last three octets must range between 0 - 255."

        elif octets[1] > 255 or octets[2] > 255 or octets[3] > 255:
            print "Invalid IP address. The last three octets must range between 0 - 255."

        else:
            for i, j in enumerate(octets):
                octets[i] = str(j)

            print "\n\n%-20s %-20s" % ('.'.join(octets), "Valid")
            break
    except ValueError:
        print '\n\nPlease enter valid IP address'
    except KeyboardInterrupt:
        print '\n\nProgramm has been interrupted!!!'
        break
    except EOFError:
        break





