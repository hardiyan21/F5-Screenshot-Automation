from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium.webdriver.support.select import Select
import time
import string
import itertools

url = 'your-ip'

def pool_properties():
    # open list folder and VS
    g = open("C:\\Users\\hkramadhan\\PycharmProjects\\F5-Automate-Capture\\venv\\list.txt")

    for line1 in g:
        print("--------------------------------------------------")
        print("Getting Pool Properties " + (line1))
        virtualserver = line1.strip()
        lokasi = line1.strip()
        lokasi2 = "your-folder"
        path = lokasi2 + lokasi

        ob = Screenshot_Clipping.Screenshot()
        driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
        driver.get(url)

        driver.find_element_by_id('username').send_keys('your-account')
        driver.find_element_by_id('passwd').send_keys('your-password')
        driver.find_element_by_xpath("//*[@id='loginform']/button").click()

        detail = "/tmui/Control/jspmap/tmui/locallb/virtual_server/resources.jsp?name=/Common/"
        new_page = url + detail + virtualserver

        driver.get(new_page)
        driver.maximize_window()

        time.sleep(1)
        driver.switch_to.frame("contentframe")
        user_selected = Select(driver.find_element_by_xpath('//*[@id="default_pool"]'))
        print(user_selected.first_selected_option.text.replace(" ", ""))
        mantul = user_selected.first_selected_option.text.replace(" ", "")

        if mantul.strip('\n') == 'None':
            driver.close()
            driver.quit()
            print("Pool tidak ditemukan rekan :(")
            spasi = ' ';
            print(20 * spasi)
        else:
            driver.switch_to.default_content()
            detail2 = "/tmui/Control/jspmap/tmui/locallb/pool/properties.jsp?name=/Common/"
            next_page = url + detail2 + mantul
            print(next_page)
            driver.get(next_page)
            driver.maximize_window()

            time.sleep(2)
            driver.switch_to.frame("contentframe")
            driver.find_element_by_xpath('//*[@id="/tmui/locallb/pool/properties.jsp?.configuration_tabletoggle"]/option[2]').click()
            driver.switch_to.default_content()

            time.sleep(1)
            element= driver.find_element_by_xpath('//*[@id="contentframe"]')
            """img_url = ob.full_Screenshot(driver, save_path=path, image_name='pool_properties.png')"""
            img_url = ob.get_element(driver, element, path)
            print(img_url)
            spasi = ' ';
            print(20*spasi)
            driver.close()
            driver.quit()

def pool_member():
    # open list folder and VS
    g = open("C:\\Users\\hkramadhan\\PycharmProjects\\F5-Automate-Capture\\venv\\list.txt")

    for line1 in g:
        print("--------------------------------------------------")
        print("Getting Pool Member " + (line1))
        virtualserver = line1.strip()
        lokasi = line1.strip()
        lokasi2 = "your-folder"
        path = lokasi2 + lokasi

        ob = Screenshot_Clipping.Screenshot()
        driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
        driver.get(url)

        driver.find_element_by_id('username').send_keys('your-account')
        driver.find_element_by_id('passwd').send_keys('your-password')
        driver.find_element_by_xpath("//*[@id='loginform']/button").click()

        detail = "/tmui/Control/jspmap/tmui/locallb/virtual_server/resources.jsp?name=/Common/"
        new_page = url + detail + virtualserver

        driver.get(new_page)
        driver.maximize_window()

        time.sleep(1)
        driver.switch_to.frame("contentframe")
        user_selected = Select(driver.find_element_by_xpath('//*[@id="default_pool"]'))
        print(user_selected.first_selected_option.text.replace(" ", ""))
        mantul = user_selected.first_selected_option.text.replace(" ", "")

        if mantul.strip('\n') == 'None':
            driver.close()
            driver.quit()
            print("Pool tidak ditemukan rekan :(")
            spasi = ' ';
            print(20 * spasi)
        else:
            driver.switch_to.default_content()
            detail2 = "/tmui/Control/jspmap/tmui/locallb/pool/resources.jsp?name=/Common/"
            next_page = url + detail2 + mantul
            print(next_page)
            driver.get(next_page)
            driver.maximize_window()

            time.sleep(5)
            element = driver.find_element_by_xpath('//*[@id="contentframe"]')
            """img_url = ob.full_Screenshot(driver, save_path=path, image_name='pool_member.png')"""
            img_url = ob.get_element(driver, element, path)

            print(img_url)
            spasi = ' ';
            print(20*spasi)
            driver.close()
            driver.quit()

def pool_stat():
    # open list folder and VS
    g = open("C:\\Users\\hkramadhan\\PycharmProjects\\F5-Automate-Capture\\venv\\list.txt")

    for line1 in g:
        print("--------------------------------------------------")
        print("Getting Pool Statistics " + (line1))
        virtualserver = line1.strip()
        lokasi = line1.strip()
        lokasi2 = "your-folder"
        path = lokasi2 + lokasi

        ob = Screenshot_Clipping.Screenshot()
        driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
        driver.get(url)

        driver.find_element_by_id('username').send_keys('your-account')
        driver.find_element_by_id('passwd').send_keys('your-password')
        driver.find_element_by_xpath("//*[@id='loginform']/button").click()

        detail = "/tmui/Control/jspmap/tmui/locallb/virtual_server/resources.jsp?name=/Common/"
        new_page = url + detail + virtualserver

        driver.get(new_page)
        driver.maximize_window()

        time.sleep(1)
        driver.switch_to.frame("contentframe")
        user_selected = Select(driver.find_element_by_xpath('//*[@id="default_pool"]'))
        print(user_selected.first_selected_option.text.replace(" ", ""))
        mantul = user_selected.first_selected_option.text.replace(" ", "")

        if mantul.strip('\n') == 'None':
            driver.close()
            driver.quit()
            print("Pool tidak ditemukan rekan :(")
            spasi = ' ';
            print(20 * spasi)
        else:
            driver.switch_to.default_content()
            detail2 = "/tmui/Control/jspmap/tmui/locallb/pool/stats.jsp?name=/Common/"
            next_page = url + detail2 + mantul
            print(next_page)
            driver.get(next_page)
            driver.maximize_window()

            time.sleep(5)
            element = driver.find_element_by_xpath('//*[@id="contentframe"]')
            """img_url = ob.full_Screenshot(driver, save_path=path, image_name='pool_stat.png')"""
            img_url = ob.get_element(driver, element, path)
            print(img_url)
            spasi = ' ';
            print(20*spasi)
            driver.close()
            driver.quit()

pool_properties()
pool_member()
pool_stat()


