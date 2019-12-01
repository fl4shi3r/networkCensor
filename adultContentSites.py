from lxml import html
import requests

page = requests.get('https://allpornsites.net/')
webpage = html.fromstring(page.content)

names = webpage.xpath('//a/@href')
domainNameList = set()
# print(len(names))
for name in names:
    if "http" in name:
        domainName = name.split('/')[2]
        if domainName == "allpornsites.net":
            domainNameList.add(name.split('/')[-1])
            # print(name.split('/')[-1])
        else:
            # print(domainName)
            domainNameList.add(domainName)
domainNameList.add("allpornsites.net")
# for naem in domainNameList:
#     print(naem)
for name in domainNameList:
    with open('./squidFiles/adultContentSites.txt') as fileobj: # location for squid blocked text file for adultContentSites
        if name in fileobj.read():
            continue
        else:
            with open('./newContentFiles/adultContentSites.txt', 'a') as fileobj1:
                fileobj1.write(name + '\n')

fileobj.close()
fileobj1.close()
