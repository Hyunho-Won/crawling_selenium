# Dynamic web crawling with selenium
To make lists of accepted papers in multiple conferenes, we use dynamic web crawling with selenium.

## Introduction
#### Dynamic website
This refers to a site where additional information is updated only when the user performs a specific action (ex. click, scroll).
Therefore, in order to obtain the desired information, specific actions must be performed to update the data in html.

#### Selenium
https://www.selenium.dev/   
It is a framework for web automation.
When instructing the action with the selenium, the operation is performed in the web driver.

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

```py
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
from time import sleep
```
Save as a csv file.
```py
csv_filename = "Paper list.csv"
csv_open = open(csv_filename, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("Title","Author"))
```
Open a browser with a specific url through webdriver. Then 단일 element에 접근한다.
```py
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://openreview.net/group?id=ICLR.cc/2022/Conference#poster-submissions')
site_body = driver.find_element(By.CSS_SELECTOR, 'body')
```
Just detemine the range for the number of pages(ii) and use the selector to determine desired list items. It scrolls down to look up the data and saves the title of the paper and the author's name. Then go to next page by .click().
```py
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

# Result
We can make accepted paper list easily.    
![화면 캡처 2023-01-09 202605](https://user-images.githubusercontent.com/122242141/211298174-f60e50e1-d5a4-47b4-aaeb-02688795018d.png)
