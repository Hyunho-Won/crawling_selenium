from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
from time import sleep

csv_filename = "Paper list.csv"
csv_open = open(csv_filename, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("Title","Author"))


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('User path')

site_body = driver.find_element(By.CSS_SELECTOR, 'body')

for ii in range(18):
   
    for i in range(6):
        site_body.send_keys(Keys.PAGE_DOWN)
        sleep(0.1)
    html = driver.page_source
    #driver.quit()
    bs = BeautifulSoup(html, "html.parser")
    total_list = bs.select("User selector")
    print(len(total_list))
    
    for i in total_list:
        title = i.select_one("User selector").text
        author = i.select_one("User selector").text
        csv_writer.writerow((title,author))
           
    sleep(1)

    
    if ii != 17:
        driver.find_element(By.CSS_SELECTOR,'#poster-submissions > nav > ul > li:nth-child(13) > a').click()
    
csv_open.close()
