from bs4 import BeautifulSoup
import requests

istenen = requests.get('http://www.meb.gov.tr/meb_duyuruindex.php')
kaynak = BeautifulSoup(istenen.content,"lxml")
print(kaynak)
