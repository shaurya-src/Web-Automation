from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
opts = Options()
opts.add_argument('--start-maximized')
driver = webdriver.Chrome(options=opts)

driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(10)

cookie = driver.find_element_by_xpath('//div[@id = "bigCookie"]')
c_count = driver.find_element_by_id('cookies')
items = [driver.find_element_by_xpath('//span[contains(@id, "productPrice{}")]'.format(i)) for i in range(2)]

driver.implicitly_wait(2)

i = 0
while i < 100000:
    cookie.click()
    count = int(c_count.text.split()[0])
    if count >= 100:
        for upgrade in items:
            cost = int(upgrade.text.replace(',', ''))
            if cost <= count:
                ac = ActionChains(driver)
                ac.move_to_element(upgrade).click().perform()
    i += 1
