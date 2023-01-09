# Dynamic Web Crawling with Selenium
To make lists of accepted papers in multiple conferenes, we use dynamic web crawling with selenium.

## Introduction
### Selenium
파이썬을 통해 동작을 자동으로 시키는 역할을 한다. 
셀레니움으로 동작을 지시하면 웹드라이버에서 동작을 수행한다.
```py
from selenium import webdriver
```

## Installation
```py
pip install BeaurifulSoup
pip install webdriver
pip install selenium
pip install csv
pip install sleep
```

## Code
csv_filename = "Paper list.csv"
csv_open = open(csv_filename, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("Title","Author"))


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://openreview.net/group?id=ICLR.cc/2022/Conference#poster-submissions')

site_body = driver.find_element(By.CSS_SELECTOR, 'body')

for ii in range(18):
   
    for i in range(6):
        site_body.send_keys(Keys.PAGE_DOWN)
        sleep(0.1)
    html = driver.page_source
    #driver.quit()
    bs = BeautifulSoup(html, "html.parser")
    total_list = bs.select("#poster-submissions > ul > li")
    print(len(total_list))
    
    for i in total_list:
        title = i.select_one("#poster-submissions > ul > li > h4 > a:nth-child(1)").text
        author = i.select_one("#poster-submissions > ul > li > div.note-authors > a").text
        csv_writer.writerow((title,author))
           
    sleep(1)

    
    if ii != 17:
        driver.find_element(By.CSS_SELECTOR,'#poster-submissions > nav > ul > li:nth-child(13) > a').click()
    
csv_open.close()
```
