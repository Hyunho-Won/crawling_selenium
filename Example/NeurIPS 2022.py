from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
from time import sleep

csv_filename = "NeurIPS 2022.csv"
csv_open = open(csv_filename, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("Title","Author"))


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://openreview.net/group?id=NeurIPS.cc/2022/Conference')

site_body = driver.find_element(By.CSS_SELECTOR, 'body')

for ii in range(54):
   
    for i in range(6):
        site_body.send_keys(Keys.PAGE_DOWN)
        sleep(0.1)
    html = driver.page_source
    #driver.quit()
    bs = BeautifulSoup(html, "html.parser")
    total_list = bs.select("#accepted-papers > ul > li")
    print(len(total_list))
    
    for i in total_list:
        title = i.select_one("#accepted-papers > ul > li > h4 > a:nth-child(1)").text
        author = i.select_one("#accepted-papers > ul > li > div.note-authors > a").text
        csv_writer.writerow((title,author))
    sleep(1)

    if ii != 53:
        driver.find_element(By.CSS_SELECTOR,'#accepted-papers > nav > ul > li:nth-child(13) > a').click()
    
csv_open.close()
