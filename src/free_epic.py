from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

opts = Options()
opts.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opts)
driver.minimize_window()

driver.get('https://www.epicgames.com/store/en-US/free-games')
sleep(5)
free = driver.find_elements_by_xpath('//span[@data-testid="offer-title-info-title"]')
for sn, game in enumerate(free):
    print('{}. {}'.format(sn + 1, game.text))
sleep(2)

driver.quit()
