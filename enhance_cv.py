import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

opts = Options()
opts.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe", options=opts)


def addProxy(ip_add, port):
    # PROXY "11.456.448.110:8080"
    proxy = "{}:{}".format(ip_add, port)
    opts.add_argument('--proxy-server=%s' % proxy)


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


def loginCV(temp_name, temp_mail, temp_pwd):
    driver.get("https://app.enhancv.com/login")
    driver.implicitly_wait(7)

    # go to create account page
    driver.find_element_by_xpath("//a[text()='Create an account']").click()

    # add details
    new_name = driver.find_element_by_xpath("//input[@name='name']")
    new_mail = driver.find_element_by_xpath("//input[@name='email']")
    new_pwd = driver.find_element_by_xpath("//input[@name='password']")

    # input credentials
    new_name.send_keys(temp_name)
    new_mail.send_keys(temp_mail)
    new_pwd.send_keys(temp_pwd)


def main():
    pass


if __name__ == '__main__':
    main()
