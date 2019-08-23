from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium.webdriver.support.select import Select
import time
import string
import itertools

url = 'your-ip'

def monitor_properties():
    # open BRN2-10-F5-list folder and VS
    g = open("C:\\Users\\hkramadhan\\PycharmProjects\\F5-Automate-Capture\\venv\\list.txt")

    for line1 in g:
        print("--------------------------------------------------")
        print("Getting Monitor Properties " + (line1))
        virtualserver = line1.strip()
        lokasi = line1.strip()
        lokasi2 = "your-folder"
        path = lokasi2 + lokasi

        ob = Screenshot_Clipping.Screenshot()
        driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
        driver.get(url)

        # Masuk ke halaman awal F5 untuk login
        driver.find_element_by_id('username').send_keys('your-account')
        driver.find_element_by_id('passwd').send_keys('your-password')
        driver.find_element_by_xpath("//*[@id='loginform']/button").click()

        detail = "/tmui/Control/jspmap/tmui/locallb/virtual_server/resources.jsp?name=/Common/"
        new_page = url + detail + virtualserver

        # Masuk ke halaman virtual server
        driver.get(new_page)
        driver.maximize_window()

        time.sleep(1)
        # Membaca text dari option yang dipilih
        driver.switch_to.frame("contentframe")
        user_selected = Select(driver.find_element_by_xpath('//*[@id="default_pool"]'))
        print(user_selected.first_selected_option.text.replace(" ", ""))
        mantul = user_selected.first_selected_option.text.replace(" ", "")

        # Jika text dari option adalah None, langsung keluar, jika tidak masuk ke halaman pool
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

            # Masuk ke halaman pool
            driver.get(next_page)
            driver.maximize_window()

            time.sleep(2)
            driver.switch_to.frame("contentframe")
            driver.find_element_by_xpath('//*[@id="/tmui/locallb/pool/properties.jsp?.configuration_tabletoggle"]/option[2]').click()

            time.sleep(2)
            # Membaca health monitor yang dipilih
            print(driver.find_element_by_xpath('//*[@id="monitor_rule/Common"]').text.replace(" ", ""))
            yuhu = driver.find_element_by_xpath('//*[@id="monitor_rule/Common"]').text.replace(" ", "")

            # Menuju halaman health monitor properties
            driver.switch_to.default_content()
            detail3 = "/tmui/Control/jspmap/tmui/locallb/monitor/properties.jsp?name=/Common/"
            hal_berikut = url + detail3 + yuhu
            print(hal_berikut)
            driver.get(hal_berikut)
            driver.maximize_window()
            time.sleep(2)

            # Memilih advanced option dari health monitor properties
            driver.switch_to.frame("contentframe")
            detail4 = '//*[@id="/tmui/locallb/monitor/properties.jsp?name=/Common/'
            aye = '.configuration_tabletoggle"]/option[2]'
            yuhu2 = yuhu.replace("\n", "")
            top = detail4 + yuhu2 + aye
            print(top)
            driver.find_element_by_xpath(top).click()
            time.sleep(2)

            driver.switch_to.default_content()
            time.sleep(2)
            element = driver.find_element_by_xpath('//*[@id="contentframe"]')
            img_url = ob.get_element(driver, element, path)
            """img_url = ob.full_Screenshot(driver, save_path=path, image_name='monitor_properties.png')"""
            print(img_url)
            spasi = ' ';
            print(20*spasi)
            driver.close()
            driver.quit()

monitor_properties()