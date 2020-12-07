import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

opts = Options()
opts.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe", options=opts)


def getClip():
    # initialize tkinter
    root = tk.Tk()

    # keep the window from showing
    root.withdraw()

    # read the clipboard
    text = root.clipboard_get()

    return text


def getMail():
    driver.get("https://temp-mail.io/en")
    driver.implicitly_wait(7)
    action = ActionChains(driver)
    # cp = driver.find_element_by_xpath('//button[@data-original-title="Copy email"]')
    # cp.click()


def loginCV():
    # driver.get("")
    pass


def main():
    pass


if __name__ == '__main__':
    getMail()
    print(getClip())
