import requests
from bs4 import BeautifulSoup

query = "파이썬강좌"
url = "https://search.naver.com/search.naver?where=pos&query={}".format(query)
r = requests.get(url)
bs = BeautifulSoup(r.text, 'lxml')

lis = bs.select("li.sh_blog_top")
for li in lis:
    #print(li)
    thumbnail = li.select('img')[0]['src']
    title = li.select("dl > dt > a")[0]
    summary = li.select("dl > dd.sh_blog_passage")[0].text
    print(thumbnail, title, summary)
    print(("*" * 60))

