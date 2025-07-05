import requests 
from bs4 import BeautifulSoup



url = 'https://www.alibaba.com/event/app/mainAction/desc.htm?detailId=60484948494&language=en'

headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Accept':'*/*',
        'Accept-Language':'en-US,en;q=0.8',
        'connection':'keep-alive'
}

response = requests.get(url,headers=headers,timeout = 10)
status = response.status_code
#print(f'The status code is {status}')


if status == 200:
    html = response.text
    with open('html.html','w') as f:
        f.write(html)

soup = BeautifulSoup(html,'html.parser')
pretty_alibaba = soup.prettify()

with open ('prettified alibaba.html','w') as f:
    f.write(pretty_alibaba)

