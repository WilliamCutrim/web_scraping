from selenium import webdriver
PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
print(PATH)
chrome = webdriver.Chrome(executable_path=PATH)

chrome.get("https:///www.youtube.com")
# exemplo
print(chrome.title)
#chrome.quit()
