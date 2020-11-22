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


def getMail():
    driver.get("https://temp-mail.org/")
    cp = driver.find_elements_by_xpath('//button[@data-clipboard-action="copy"]')[0]
    cp.click()


def loginCV():
    # driver.get("")
    pass


def main():
    pass


if __name__ == '__main__':
    getClip()
