__author__ = 'Jason Vanzin'
import sys
import re


def exists(ipaddress):
    if 'linux' in sys.platform:
        filename = '/etc/hosts'
    else:
        filename = 'c:\windows\system32\drives\etc\hosts'
    f = open(filename, 'r')
    hostfiledata = f.readlines()
    f.close()
    for item in hostfiledata:
        if ipaddress in item:
            #print(ipaddress, 'already exists')
            return True
    return False


def update(ipaddress, hostname):
    if 'linux' in sys.platform:
        filename = '/etc/hosts'
    else:
        filename = 'c:\windows\system32\drives\etc\hosts'
    outputfile = open(filename, 'a')
    entry = "\n" + ipaddress + "\t" + hostname
    outputfile.writelines(entry)
    outputfile.close()


def validIP(ipaddress):
    parts = ipaddress.split(".")
    if len(parts) != 4:
        return False
    if ipaddress[-2:] == '.0': return False
    if ipaddress[-1] == '.': return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True


def isValidHostname(hostname):
    # from http://stackoverflow.com/questions/2532053/validate-a-hostname-string
    if len(hostname) > 255:
        return False
    if hostname[0].isdigit(): return False
    if hostname[-1:] == ".":
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))


def main():
    args = sys.argv
    if len(args) != 3:
        print('usage: hostfileupdate.py [ipadddress] [hostmame]')
        sys.exit(2)
    hostname = args[-1]
    ipaddress = args[-2]

    if not validIP(ipaddress):
        print(ipaddress, "is not a valid IP address. Usage: hostfileupdate.py [ipadddress] [hostmame]")
        sys.exit(2)

    if not isValidHostname(hostname):
        print(hostname, "is not a valid hostname. Usage: hostfileupdate.py [ipadddress] [hostmame]")
        sys.exit(2)

    if exists(ipaddress):
        print(ipaddress, 'already exists in the hostfile.')
        sys.exit(2)

    update(ipaddress, hostname)


if __name__ == '__main__':
    main()





