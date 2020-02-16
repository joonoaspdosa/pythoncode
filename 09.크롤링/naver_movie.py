import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/point/af/list.nhn?&page=1"
r = requests.get(url)
bs = BeautifulSoup(r.text, 'lxml')

trs = bs.select("table.list_netizen > tbody > tr")
for tr in trs:
    # print(tr)
    tds = tr.select("td")
    print(tds[0].text)
