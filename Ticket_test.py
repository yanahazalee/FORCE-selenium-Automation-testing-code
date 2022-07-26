import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#import datetime
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import Select


@pytest.fixture(scope="session", autouse=True)
def test_setup():
    global driver, a
    driver = webdriver.Chrome(executable_path="D:/force selenium/webdriver/chromedriver.exe") 
    driver.get("http://58.26.233.223/#!/login")
    driver.implicitly_wait(10)
    driver.maximize_window()
    a = ActionChains(driver)


def test_login():
    #enter username
    username = driver.find_element(By.CSS_SELECTOR, '[placeholder="MY USERNAME"]')
    username.send_keys('R10018')
    time.sleep(2)

    #enter password
    password = driver.find_element(By.CSS_SELECTOR, '[placeholder="PASSWORD"]')
    password.send_keys('force123')
    time.sleep(2)

    #login
    login_btn = driver.find_element(By.CSS_SELECTOR, '[type = "button"]')
    login_btn.click()
    time.sleep(2)

# TESTING ON TICKET (TICKET LIST)  
def test_Ticket1():

    #identify element Ticket
    #t1 = driver.find_element_by_link_text("TICKET")
    t1 = driver.find_element_by_xpath("//a[text()='TICKET']")	
    #hover over element
    a.move_to_element(t1).perform()
    #identify sub menu element
    ticketlist = driver.find_element_by_link_text("Ticket List")
    # hover over element and click
    a.move_to_element(ticketlist).click().perform()
    time.sleep(3)

def test_TicketList():

    #identify element ticket category for Ticket List
    #ticketcategory = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/span")
    ticketcategory = driver.find_element_by_xpath("//label[text()='Ticket Category']")
    a.move_to_element(ticketcategory).click().perform()
    # COMPLAINT = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[1]")
    COMPLAINT = driver.find_element_by_xpath("//div[@webix_l_id='COMPLAINT']")
    a.move_to_element(COMPLAINT).click().perform()
    time.sleep(1)
    
    #identify element ticket number
    ticketnumber = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    ticketnumber.send_keys('T0000028624')

    #identify element ticket status
    #tickectstatus = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/div/input")
    tickectstatus = driver.find_element_by_xpath("//label[text()='Ticket Status']")
    a.move_to_element(tickectstatus).click().perform()
    #new = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div[1]")
    new = driver.find_element_by_xpath("//div[@webix_l_id='New']")
    a.move_to_element(new).click().perform()
    time.sleep(1)
 
    #identify element case category
    #casecategory = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/input")
    casecategory = driver.find_element_by_xpath("//label[text()='Case Category']")
    a.move_to_element(casecategory).click().perform()
    #OTHERS = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]")
    OTHERS = driver.find_element_by_xpath("//div[@webix_l_id='OTHERS']")
    a.move_to_element(OTHERS).click().perform()
    time.sleep(1)

    #search the input data
    #search_btn = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/button")
    search_btn = driver.find_element_by_xpath("//button[text()='Search']")
    search_btn.click()
    time.sleep(4)

    #download data in pdf
    #savepdf_btn = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/button")
    savepdf_btn = driver.find_element_by_xpath("//button[text()='Save to PDF']")
    savepdf_btn.click()
    time.sleep(3)

    #download data in excel
    #saveexcel_btn = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/div/div[3]/div/button")
    saveexcel_btn = driver.find_element_by_xpath("//button[text()='Save to Excel']")
    saveexcel_btn.click()
    time.sleep(3)

    #reset the data
    #reset_btn = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/button")
    reset_btn = driver.find_element_by_xpath("//button[text()='Reset']")
    reset_btn.click()
    time.sleep(3)
    driver.close()