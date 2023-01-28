import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/"

response=requests.get(url)

html=response.content

soup=BeautifulSoup(html,"html.parser")  #URL üzerindeki her şeyi buraya aldık.

baslıklar=soup.find_all("td",{"class":"titleColumn"})   #İncele kısmından elde edilen başlıklar ile film isimlerini aldık.
reytingler=soup.find_all("td",{"class":"ratingColumn imdbRating"})

for baslik , reyting in zip(baslıklar,reytingler):
    baslik=baslik.text
    reyting=reyting.text
    baslik=baslik.strip()               #İlk ve son kısımları sildik.
    baslik=baslik.replace("\n","")      #Alt satıra geçmeleri iptal ettik

    reyting=reyting.strip()
    reyting=reyting.replace("\n","")

    print("Film Adı: ",baslik)
    print("Reyting: ",reyting)

