import requests

r = requests.get("http://faq.syncanswer.jp/aiful/detail?site=CBG4IM5O&category=1&id=79")

#ここでスクレイピングできるサイトか確認
print(r.text)

#スクレイピングが出来るとわかったのでBeautifulSoupを使ってサイト内の特定文言を抽出
from bs4 import  BeautifulSoup
r = requests.get("http://faq.syncanswer.jp/aiful/detail?site=CBG4IM5O&category=1&id=79")

soup = BeautifulSoup(r.text, "html.parser")
print(soup.select('.standard-h2'))

#余分なタグ等を切り捨てて本文だけを抽出
aihuru =soup.select('.standard-h2')
for ai in aihuru:
    print(ai.text)

#1ページ毎に抽出するのは面倒なのでリストを使ってページIDを振り一気にスクレイピング
for i in range(100):
    r = requests.get("http://faq.syncanswer.jp/aiful/detail?site=CBG4IM5O&category=1&id="+str(i))
    soup = BeautifulSoup(r.text, "html.parser")
    aihuru =soup.select('.standard-h2')
    for ai in aihuru:
        print(ai.text)
