from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

opts = Options()
opts.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe", options=opts)

driver.get("https://www.google.co.in/")