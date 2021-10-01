from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import os
import pandas as pd
import time

tarayici_yolu = os.path.join(os.getcwd(),"veri_madenciligi","geckodriver")
dosya_yolu=os.path.join(os.getcwd(), "veri_madenciligi", "meb_twits.csv")
ayarlar = FirefoxOptions()
# ayarlar.add_argument("--headless")
surucu = webdriver.Firefox(options=ayarlar,executable_path=tarayici_yolu)
surucu.get(url="https://twitter.com/search?q=python&src=typed_query")
time.sleep(10)
icerik=surucu.page_source
# print(icerik)
soup = BeautifulSoup(icerik,"html.parser")
# print(soup)
t=[]
k=[]
b=[]
rt=[]
y=[]
adr=[]
zmn=[]
for a in soup.find_all("div",attrs={"data-testid":"tweet"}):      
    twit = a. find("div",attrs={"class":"css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}).text
    kisi= a.find("div",attrs={"class":"css-901oao css-bfa6kz r-9ilb82 r-18u37iz r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0"}).text
    yorum_sayisi=a.find("div",attrs={"class":"css-1dbjc4n r-xoduu5 r-1udh08x"}).text
    rt_sayisi=a.find("div",attrs={"class":"css-1dbjc4n r-xoduu5 r-1udh08x"}).text
    begeni=a.find("div",attrs={"class":"css-1dbjc4n r-xoduu5 r-1udh08x"}).text
    adres=a.find("a",attrs={"class":"css-4rbku5 css-18t94o4 css-901oao r-9ilb82 r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0"})
    t.append(twit)
    k.append(kisi)
    b.append(begeni)
    rt.append(rt_sayisi)
    y.append(yorum_sayisi)
    zmn.append(adres.find("time").get("datetime"))
    adr.append(adres.get("href"))
   
veri = {"kisi":k,"zaman":zmn,"adres":adr,"twit":t,"begeni_saysi":b,"rt_sayisi":rt,"yorum_sayisi":y}
veri = pd.DataFrame(veri)
veri.to_csv(dosya_yolu,index=False)
 

   