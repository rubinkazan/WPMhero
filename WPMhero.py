from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time



def getWPM(url):
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get(url)

    actions = ActionChains(driver)
    actions.send_keys(Keys.ESCAPE)
    actions.perform()

    right_xpath = '/html/body/div[3]/div[3]/div/div/div[1]/div[1]/div/span[5]'
    current_xpath = '/html/body/div[3]/div[3]/div/div/div[1]/div[1]/div/span[3]'
    entry_xpath = '/html/body/div[3]/div[3]/div/div/div[1]/div[2]/form/input'

    time.sleep(2)

    right = driver.find_element_by_xpath(right_xpath).text
    current = driver.find_element_by_xpath(current_xpath).text
    entry = current + " " + right
    word = driver.find_element_by_xpath(entry_xpath).send_keys(entry)

    print(entry)

if __name__ == "__main__":
    smashKeys('https://www.keyhero.com/free-typing-test/')






