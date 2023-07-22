import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) <5:
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')





    
numbers = soup.find_all('span', string=re.compile('\d+'))
sum = 0
for number in numbers:
    sum += int(number.text)

print(sum)