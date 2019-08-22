from selenium import webdriver
from Screenshot import Screenshot_Clipping
import time
import string
import itertools

url = 'https://your-ip'

def vs_properties():
    # open list folder and VS
    g = open("your-file-path")

    for line1 in g:
        print("--------------------------------------------------")
        print("Getting Virtual Server Properties " + (line1))
        virtualserver = line1.strip()
        lokasi = line1.strip()
        lokasi2 = "your-folder"
        path = lokasi2 + lokasi

        ob = Screenshot_Clipping.Screenshot()
        driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
        driver.get(url)

        driver.find_element_by_id('username').send_keys('username')
        driver.find_element_by_id('passwd').send_keys('passwd')
        driver.find_element_by_xpath("//*[@id='loginform']/button").click()

        detail = "/tmui/Control/jspmap/tmui/locallb/virtual_server/properties.jsp?name=/Common/"
        new_page = url + detail + virtualserver

        driver.get(new_page)
        driver.maximize_window()
        time.sleep(1)
        img_url = ob.full_Screenshot(driver, save_path=path, image_name='vs_properties.png')
        print(img_url)

        spasi = ' ';
        print(20*spasi)

        driver.close()
        driver.quit()

def vs_resources():
    # open list folder and VS
    g = open("your-file-path")

    for line1 in g:
        print("--------------------------------------------------")
        print("Getting Virtual Server Resources " + (line1))
        virtualserver = line1.strip()
        lokasi = line1.strip()
        lokasi2 = "your-folder"
        path = lokasi2 + lokasi

        ob = Screenshot_Clipping.Screenshot()
        driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
        driver.get(url)

        driver.find_element_by_id('username').send_keys('username')
        driver.find_element_by_id('passwd').send_keys('passwd')
        driver.find_element_by_xpath("//*[@id='loginform']/button").click()

        detail = "/tmui/Control/jspmap/tmui/locallb/virtual_server/resources.jsp?name=/Common/"
        new_page = url + detail + virtualserver

        driver.get(new_page)
        driver.maximize_window()
        time.sleep(1)
        img_url = ob.full_Screenshot(driver, save_path=path, image_name='vs_resources.png')
        print(img_url)
        driver.close()
        driver.quit()

def vs_statistics():
    # open list folder and VS
    g = open("your-file-path")

    for line1 in g:
        print("--------------------------------------------------")
        print("Getting Virtual Server Statistics " + (line1))
        virtualserver = line1.strip()
        lokasi = line1.strip()
        lokasi2 = "your-folder"
        path = lokasi2 + lokasi

        ob = Screenshot_Clipping.Screenshot()
        driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
        driver.get(url)

        driver.find_element_by_id('username').send_keys('username')
        driver.find_element_by_id('passwd').send_keys('passwd')
        driver.find_element_by_xpath("//*[@id='loginform']/button").click()

        detail = "/tmui/Control/jspmap/tmui/locallb/virtual_server/stats_detail.jsp?name=/Common/"
        new_page = url + detail + virtualserver

        driver.get(new_page)
        driver.maximize_window()
        time.sleep(1)
        img_url = ob.full_Screenshot(driver, save_path=path, image_name='vs_statisctics.png')
        print(img_url)
        driver.close()
        driver.quit()

vs_properties()
vs_resources()
vs_statistics()