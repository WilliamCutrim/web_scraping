#https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


PATH='C:\\Program Files (x86)\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cokkie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]
try:
    upgrade_tools = [driver.find_element_by_id("upgradePrice" + str(i)) for i in range(0,-1,-1)]
except:
    upgrade_tools = []

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cokkie_count.text.split(" ")[0])
    print(count)

    for tool in upgrade_tools:
        value_tool = int(tool.text)
        if value_tool <= count:
            upgrade_tool_actions = ActionChains(driver)
            upgrade_tool_actions.move_to_element(tool)
            upgrade_tool_actions.click()
            upgrade_tool_actions.perform()

    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()


#actions.perform()

