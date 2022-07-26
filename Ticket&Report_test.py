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
    #driver.close()

    # TESTING ON TICKET (TICKET ACTIVITY LIST)  
def test_Ticket2():

    #identify element Ticket
    #t2 = driver.find_element_by_link_text("TICKET")
    t2 = driver.find_element_by_xpath("//a[text()='TICKET']")
    a.move_to_element(t2).perform()
    ticketactivitylist = driver.find_element_by_link_text("Ticket Activity List")
    a.move_to_element(ticketactivitylist).click().perform()
    time.sleep(5)

def test_TicketActivityList():

    #identify element ticket category for Ticket Activity List
    #ticketcategory2 = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/span")
    ticketcategory2 = driver.find_element_by_xpath("//label[text()='Ticket Category']")
    a.move_to_element(ticketcategory2).click().perform()
    #COMPLAINT2 = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[1]")
    COMPLAINT2 = driver.find_element_by_xpath("//div[@webix_l_id='COMPLAINT']")
    a.move_to_element(COMPLAINT2).click().perform()
    time.sleep(1)

    #identify element activity category for Ticket Activity List
    #activitycategory = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/span")
    activitycategory = driver.find_element_by_xpath("//label[text()='Activity Category']")
    a.move_to_element(activitycategory).click().perform()
    #high_pressure = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div")
    high_pressure = driver.find_element_by_xpath("//div[@webix_l_id='HP - HIGH PRESSURE']")
    a.move_to_element(high_pressure).click().perform()
    time.sleep(1)

    #identify element activity status for Ticket Activity List
    #activitystatus = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[3]/div/div/span")
    activitystatus = driver.find_element_by_xpath("//label[text()='Activity Status']")
    a.move_to_element(activitystatus).click().perform()
    #inprogress = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]")
    inprogress = driver.find_element_by_xpath("//div[@webix_l_id='InProgress']")
    a.move_to_element(inprogress).click().perform()
    time.sleep(1)

    #search input for ticket category, activity category and activity status
    #search_btn2 = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/button")
    search_btn2 = driver.find_element_by_xpath("//button[text()='Search']")
    search_btn2.click()
    time.sleep(4)

    #download pdf for the display data
    #savepdf_btn2 = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/button")
    savepdf_btn2 = driver.find_element_by_xpath("//button[text()='Save to PDF']")
    savepdf_btn2.click()
    time.sleep(4)

    #download excel for the display data
    #saveexcel_btn2 = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/div/div[3]/div/button")
    saveexcel_btn2 = driver.find_element_by_xpath("//button[text()='Save to Excel']")
    saveexcel_btn2.click()
    time.sleep(4)

    #reset the data
    #reset_btn2 = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/button")
    reset_btn2 = driver.find_element_by_xpath("//button[text()='Reset']")
    reset_btn2.click()
    time.sleep(4)

    #enter ticket number
    ticketnumber2 = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/div/input")
    #ticketnumber2 = driver.find_element_by_xpath("//label[text()='Ticket Number']")
    #ticketnumber2 = driver.find_element_by_xpath("//input[@id='1652843191267']")
    #ticketnumber2 = driver.find_element_by_xpath("//*[contains(@id,'1652843191267')]")
    #ticketnumber2 = driver.find_element_by_xpath(" //label[contains(text(),'Ticket Number')]")
    #ticketnumber2 = driver.find_element_by_xpath("//input[starts-with(@id,'1652856454677')]")
    # a.move_to_element(ticketnumber2).click().perform()
    #ticketnumber2 = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    #ticketnumber2 = driver.find_element_by_xpath("(//input[@id='1652923674254'])[1]")
    ticketnumber2.send_keys('T0000028671')
    time.sleep(1)

    #enter activity id
    activityid = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/input")
    #activityid = driver.find_element(By.ID, '1652856454679')
    activityid.send_keys('A00000000001731')
    time.sleep(1)

    #search input of ticket number and activity id
    #search_btn3 = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/button")
    search_btn3 = driver.find_element_by_xpath("//button[text()='Search']")
    search_btn3.click()
    time.sleep(2)
    #driver.close()

    # TESTING ON REPORT (TICKET REPORT)  
def test_Report1():

    #identify element Ticket
    r1 = driver.find_element_by_xpath("//a[text()='REPORTS']")	
    #hover over element
    a.move_to_element(r1).perform()
    #identify sub menu element
    ticketreport = driver.find_element_by_link_text("Ticket Report")
    # hover over element and click
    a.move_to_element(ticketreport).click().perform()
    time.sleep(3)

def test_TicketReport():

    #identify element ticket category for Ticket Report
    region = driver.find_element_by_xpath("//label[text()='Region']")
    a.move_to_element(region).click().perform()
    AlorGajah = driver.find_element_by_xpath("//div[@webix_l_id='1018']")
    a.move_to_element(AlorGajah).click().perform()
    time.sleep(1)

    #identify element ticket category for Ticket Report
    area = driver.find_element_by_xpath("//label[text()='Area']")
    a.move_to_element(area).click().perform()
    MasjidTanah = driver.find_element_by_xpath("//div[@webix_l_id='MASJID TANAH|3']")
    a.move_to_element(MasjidTanah).click().perform()
    time.sleep(1)
    
    #identify element ticket category for Ticket Report
    sub_area = driver.find_element_by_xpath("//label[text()='Sub-Area']")
    a.move_to_element(sub_area).click().perform()
    AirMolek = driver.find_element_by_xpath("//div[@webix_l_id='AIR MOLEK ( MH )|209']")
    a.move_to_element(AirMolek).click().perform()
    time.sleep(1)

## SAME VARIABLE- PASS
    #identify element ticket category for Ticket Report
    casecategory = driver.find_element_by_xpath("//label[text()='Case Category']")
    a.move_to_element(casecategory).click().perform()
    OTHERS = driver.find_element_by_xpath("//div[@webix_l_id='2607']")
    a.move_to_element(OTHERS).click().perform()
    time.sleep(1)

    #identify element ticket category for Ticket Report
    casetype = driver.find_element_by_xpath("//label[text()='Case Type']")
    a.move_to_element(casetype).click().perform()
    SUPPORT_WORKS = driver.find_element_by_xpath("//div[@webix_l_id='SUPPORT WORKS|2608']")
    a.move_to_element(SUPPORT_WORKS).click().perform()
    time.sleep(1)

    search_btn = driver.find_element_by_xpath("//button[text()='Search']")
    search_btn.click()
    time.sleep(3)

    #download pdf for the display data
    savepdf_btn = driver.find_element_by_xpath("//button[text()='Save to PDF']")
    savepdf_btn.click()
    time.sleep(3)

    #download excel for the display data
    saveexcel_btn = driver.find_element_by_xpath("//button[text()='Save to Excel']")
    saveexcel_btn.click()
    time.sleep(3)

    reset_btn = driver.find_element_by_xpath("//button[text()='Reset']")
    reset_btn.click()
    time.sleep(2)

def test_Report2():

    #identify element Report
    r2 = driver.find_element_by_xpath("//a[text()='REPORTS']")	
    #hover over element
    a.move_to_element(r2).perform()
    #identify sub menu element
    teamreport = driver.find_element_by_link_text("Team Report")
    # hover over element and click
    a.move_to_element(teamreport).click().perform()
    time.sleep(3)

def test_TeamReport():

    region = driver.find_element_by_xpath("//label[text()='Region']")
    a.move_to_element(region).click().perform()
    JASIN_region = driver.find_element_by_xpath("//div[@webix_l_id='1']")
    a.move_to_element(JASIN_region).click().perform()
    time.sleep(1)

    area = driver.find_element_by_xpath("//label[text()='Area']")
    a.move_to_element(area).click().perform()
    JASIN_area = driver.find_element_by_xpath("//div[@webix_l_id='JASIN|6']")
    a.move_to_element(JASIN_area).click().perform()
    time.sleep(1)

    sub_area = driver.find_element_by_xpath("//label[text()='Sub-Area']")
    a.move_to_element(sub_area).click().perform()
    BEMBAN = driver.find_element_by_xpath("//div[@webix_l_id='BEMBAN|266']")
    a.move_to_element(BEMBAN).click().perform()
    time.sleep(1)

    casecategory = driver.find_element_by_xpath("//label[text()='Case Category']")
    a.move_to_element(casecategory).click().perform()
    BIL = driver.find_element_by_xpath("//div[text()='BIL']")
    a.move_to_element(BIL).click().perform()
    time.sleep(1)

    activitycategory = driver.find_element_by_xpath("//label[text()='Activity Category']")
    a.move_to_element(activitycategory).click().perform()
    HP = driver.find_element_by_xpath("//div[@webix_l_id='23']")
    a.move_to_element(HP).click().perform()
    time.sleep(1)

    activitytype = driver.find_element_by_xpath("//label[text()='Activity Type']")
    a.move_to_element(activitytype).click().perform()
    HP01 = driver.find_element_by_xpath("//div[@webix_l_id='HP01 - HIGH PRESSURE|61']")
    a.move_to_element(HP01).click().perform()
    time.sleep(1)

    # casetype = driver.find_element_by_xpath("//label[text()='Case Type']")
    # a.move_to_element(casetype).click().perform()
    # BE = driver.find_element_by_xpath("//div[@view_id='$suggest24_list']")
    # a.move_to_element(BE).click().perform()
    # time.sleep(2)

    search_btn = driver.find_element_by_xpath("//button[text()='Search']")
    search_btn.click()
    time.sleep(3)

    #download pdf for the display data
    savepdf_btn = driver.find_element_by_xpath("//button[text()='Save to PDF']")
    savepdf_btn.click()
    time.sleep(3)

    #download excel for the display data
    saveexcel_btn = driver.find_element_by_xpath("//button[text()='Save to Excel']")
    saveexcel_btn.click()
    time.sleep(3)

    reset_btn = driver.find_element_by_xpath("//button[text()='Reset']")
    reset_btn.click()
    time.sleep(3)
    driver.close()

































    






















    

 

    

    
    




    
   

