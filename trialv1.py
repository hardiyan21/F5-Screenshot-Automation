from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def dashboard():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/dashboard/F5Dashboard.html"

    driver.get(new_page)
    driver.fullscreen_window()
    time.sleep(80)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='dashboard.png')
    print(img_url)
    driver.close()
    driver.quit()

def performance():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/system/stats/list.jsp?subset=All"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='performance.png')
    print(img_url)
    driver.close()
    driver.quit()

def network():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/overview/stats/network.jsp?reset_section_list=true"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='network.png')
    print(img_url)
    driver.close()
    driver.quit()


def vserver():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/locallb/virtual_server/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='vserver.png')
    print(img_url)
    driver.close()
    driver.quit()

def lt_pool():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/locallb/pool/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='lt_pool.png')
    print(img_url)
    driver.close()
    driver.quit()

def lt_nodes():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/locallb/node/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='lt_nodes.png')
    print(img_url)
    driver.close()
    driver.quit()

def devices():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/devmgmt/device/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='devices.png')
    print(img_url)
    driver.close()
    driver.quit()

def net_interfaces():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/locallb/network/interface/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='net_interfaces.png')
    print(img_url)
    driver.close()
    driver.quit()

def net_routes():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/locallb/network/route/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='net_routes.png')
    print(img_url)
    driver.close()
    driver.quit()

def net_selfip():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/locallb/network/self_ip/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='net_selfip.png')
    print(img_url)
    driver.close()
    driver.quit()

def net_trunks():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/locallb/network/trunk/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='net_trunks.png')
    print(img_url)
    driver.close()
    driver.quit()

def net_routedomain():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/locallb/network/route_domain/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='net_routedomain.png')
    print(img_url)
    driver.close()
    driver.quit()

def net_vlan():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/locallb/network/vlan/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='net_vlan.png')
    print(img_url)
    driver.close()
    driver.quit()

def net_ipsec():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/ipsec/ike/peers/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='net_ipsec.png')
    print(img_url)
    driver.close()
    driver.quit()

def ntp():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/system/device/properties_ntp.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='ntp.png')
    print(img_url)
    driver.close()
    driver.quit()

def user_list():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/system/user/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='user_list.png')
    print(img_url)
    driver.close()
    driver.quit()

def partition_list():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/system/partition/list.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='partition_list.png')
    print(img_url)
    driver.close()
    driver.quit()

def authentication():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path="C:\\Users\\hkramadhan\\Downloads\\Chromedriver\\chromedriver.exe")
    url = "https://your-ip/"
    driver.get(url)

    driver.find_element_by_id('username').send_keys('your-username')
    driver.find_element_by_id('passwd').send_keys('your-passwd')
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()

    new_page = "https://your-ip/tmui/Control/jspmap/tmui/system/user/authproperties.jsp"
    driver.get(new_page)
    driver.maximize_window()
    time.sleep(5)
    img_url=ob.full_Screenshot(driver, save_path='C:\\Users\\hkramadhan\\Downloads\\your-folder\\', image_name='authentication.png')
    print(img_url)
    driver.close()
    driver.quit()

dashboard()
performance()
network()
vserver()
lt_pool()
devices()
net_interfaces()
net_routes()
net_selfip()
net_trunks()
net_routedomain()
net_vlan()
net_ipsec()
ntp()
user_list()
partition_list()
authentication()


