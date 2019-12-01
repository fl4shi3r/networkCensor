from lxml import html
import requests, re


sites = ['https://www.proxy-site.net/web-proxy.html', 'https://free-proxy-list.net/web-proxy.html', 'https://www.sslproxies.org/','http://free-proxy.cz/en/web-proxylist/', 'https://piratebay-proxylist.se/']

domainNameList = set()
ipNameList = set()
for site in sites:
    page = requests.get(site)
    webpage = html.fromstring(page.content)

    names = webpage.xpath('//a/@href')
    
    # print(names)
    # print("Hello")
    # print(len(names))
    for name in names:
        try:
            if "http" in name:
                if 'facebook' in name or 'youtube' in name or "twitter" in name:
                    continue
                else:
                    domainName = name.split('/')[2]
                    domainNameList.add(domainName)
        except:
            print("Error")

    
    req = requests.get(site)
    # print(req.text)
    all = req.text

    # print(all)
    # result = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", all)
    result = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', all)
    for ip in result:
        ipNameList.add(ip)
print(ipNameList)
# with open('./defaultFiles/webProxies_IP_.txt', 'a') as ipFileobj:
#     for i in result:
#         ipFileobj.write(i + '\n')
# ipFileobj.close()

# with open('./defaultFiles/webProxies_domainName_.txt', 'a') as ipFileobj:
#     for i in domainNameList:
#         ipFileobj.write(i + '\n')
# ipFileobj.close()
print(domainNameList)

'''







            if domainName == "allpornsites.net":
                domainNameList.add(name.split('/')[-1])
                # print(name.split('/')[-1])
            else:
                # print(domainName)
                domainNameList.add(domainName)
    domainNameList.add("allpornsites.net")
    for naem in domainNameList:
        print(naem)
    # for name in domainNameList:
    #     with open('./squidFiles/adultContentSites.txt') as fileobj: # location for squid blocked text file for adultContentSites
    #         if name in fileobj.read():
    #             continue
    #         else:
    #             with open('./newContentFiles/adultContentSites.txt', 'a') as fileobj1:
    #                 fileobj1.write(name + '\n')

    # fileobj.close()
    # fileobj1.close()
'''