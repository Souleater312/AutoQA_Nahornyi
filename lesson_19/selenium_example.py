import time

from selenium.webdriver import Chrome
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

'''def test_01():
    driver = Chrome()
    driver.get("https://www.google.com/")
    time.sleep(3)
    search_locator = '//textarea[@aria-label="Search"]'
    search_element = driver.find_element(by= "xpath",value=search_locator)
    search_element.send_keys("повернись живим")
    search_element.send_keys(Keys.ENTER)
    first_not_ad = '//*[@id="rso"]/div[1]/div/div/div/table/tbody/tr[1]/td/div/div/div/div/h3/a'
    first_elemetn = driver.find_element("xpath", first_not_ad)
    first_elemetn.click()
    time.sleep(3)'''


def test_actionchains():
    driver = Chrome()
    driver.get("https://www.google.com/")
    time.sleep(3)
    search_locator = '//textarea[@aria-label="Search"]'
    search_element = driver.find_element(by="xpath", value=search_locator)
    search_element.send_keys("повернись живим")
    actions = ActionChains(driver)
    time.sleep(2)
    actions.key_down(Keys.COMMAND).key_down("A").key_up(Keys.COMMAND).perform()
    time.sleep(2)
    actions.key_down(Keys.COMMAND).key_down("X").key_up(Keys.COMMAND).perform()
    search_element.click()
    time.sleep(2)
    actions.key_down(Keys.COMMAND).key_down("V").key_up(Keys.COMMAND).perform()