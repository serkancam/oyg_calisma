from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import os
# driver_path=os.path.join(os.getcwd(),"calismalar","chromedriver.exe")
driver_path=os.path.join(os.getcwd(),"calismalar","geckodriver.exe")
options = FirefoxOptions()
# options.add_argument("--headless")
Hes_kod=""
tc = ""
sifre = ""
browser=webdriver.Firefox(options=options, executable_path=driver_path)

browser.get("https://giris.turkiye.gov.tr/Giris/gir")

browser.find_element_by_xpath('//*[@id="tridField"]').send_keys(tc)
browser.find_element_by_xpath('//*[@id="egpField"]').send_keys(sifre)
browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input[4]').click()


browser.get("https://www.turkiye.gov.tr/saglik-bakanligi-hes-kodu-sorgulama")
Hes_kod = Hes_kod.upper()
browser.find_element_by_xpath('//*[@id="hes_kodu"]').send_keys(Hes_kod)
print("hes kodu girildi")
browser.find_element_by_xpath('//*[@id="contentStart"]/div[3]/form/div/input[1]').click()

time.sleep(5)
browser.quit()