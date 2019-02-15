from bs4 import BeautifulSoup

with open("iplist.xml", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    ips = soup.findAll('ipv4')
    for ip in ips:
        print(ip.text)


