from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()


soup = BeautifulSoup(html, "html.parser")

count = 0
numbers = []

tags = soup('span')

for tag in tags:
# remember to read right to left so
# first: look for the string within the <span> tag... that is the number in text
# second: convert that string into integers
# third: add to the list, which is empty but defined with [] above this number

    numbers.append(int(span.string))
    
    count = count + 1


    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)

print ('Sum', sum(numbers))
print ('Count', count)
