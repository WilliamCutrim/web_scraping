from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH='C:\\Program Files (x86)\\geckodriver.exe'

print(PATH)
driver = webdriver.Firefox(executable_path=PATH)
driver.get('http://techwithtim.net')

search = driver.find_element_by_name('s')
search.send_keys("test")
search.send_keys(Keys.RETURN)

#print(driver.page_source)
time.sleep(10)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
    
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    print('bla')
    driver.quit()

#main = driver.find_elements_by_id("main")

#time.sleep(15)

#driver.quit()
