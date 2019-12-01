import os

with open ("./defaultFiles/adultContentSites.txt", 'r') as fileobj1:

    for line in fileobj1.readlines():
        # print(line.strip())
        with open("/etc/squid/adultContentSites.txt", 'a+')  as fileobj2:
            fileobj2.write('*' + line.strip() + '*\n')
        fileobj2.close()
fileobj1.close()

with open ("./defaultFiles/torServers.txt", 'r') as fileobj1:

    for line in fileobj1.readlines():
        with open("/etc/squid/torServers.txt", 'a+')  as fileobj2:
            fileobj2.write('*' + line.strip() + '*\n')
        fileobj2.close()
fileobj1.close()

with open ("./defaultFiles/webProxies_domainName_.txt", 'r') as fileobj1:

    for line in fileobj1.readlines():
        with open("/etc/squid/webProxies_domainName_.txt", 'a+')  as fileobj2:
            fileobj2.write('*' + line.strip() + '*\n')
        fileobj2.close()
fileobj1.close()

with open ("./defaultFiles/webProxies_IP_.txt", 'r') as fileobj1:

    for line in fileobj1.readlines():
        with open("/etc/squid/webProxies_IP_.txt", 'a+')  as fileobj2:
            fileobj2.write('*' + line.strip() + '*\n')
        fileobj2.close()
fileobj1.close()

with open ("./defaultFiles/torrentAndVpn.txt", 'r') as fileobj1:

    for line in fileobj1.readlines():
        with open("/etc/squid/torrentAndVpn.txt", 'a+')  as fileobj2:
            fileobj2.write('*' + line.strip() + '*\n')
        fileobj2.close()
fileobj1.close()

print("Done")

print("Restarting SQUID server......")
os.system('service squid restart')