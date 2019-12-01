import requests, re


req = requests.get("https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1")
# print(req.text)
all = req.text.splitlines()

# print(all)
for line in all:
    result = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", line)
    if result:
        ipaddress = line
        print(line) #get ip address from here 