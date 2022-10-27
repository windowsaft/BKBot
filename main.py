# Import the required modules
from selenium import webdriver
from functions import *
import time
import re
  
# Main Function
if __name__ == '__main__':
  
    # Provide the email and password
  
    options = webdriver.ChromeOptions()
    #options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
  
    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path=".\\chromedriver_win32\\chromedriver.exe",
                              chrome_options=options)
    driver.set_window_size(500,400)
  
    # Send a get request to the url
    driver.get('https://bk-feedback-de.com')

    # Page 1
    rcode = 11609
    driver.find_element("id", 'QR~QID4').send_keys(rcode)
    time.sleep(2)
    driver.find_element("id", 'NextButton').click()

    # Page 2
    dates = "26102022"
    time.sleep(3)
    datepicker(_driver = driver, _day = 26)
    time.sleep(3)
    timepicker(_driver = driver, _time_array = time_convert24to12("11:30"))
    driver.find_element("id", 'NextButton').click()

    # Page 3
    # QID12-1-label --> Self-Service
    # QID12-2-label --> Counter
    # QID12-3-label --> App
    _css_id_ordermethod = "QID12-1-label"
    time.sleep(2)
    driver.find_element("id", _css_id_ordermethod).click()
    time.sleep(2)
    driver.find_element("id", 'NextButton').click()


    # Page 4
    # QID14-2-label --> on site
    # QID14-3-label --> take away
    _css_id_locationtarget = "QID14-2-label"
    time.sleep(2)
    driver.find_element("id", _css_id_locationtarget).click()
    time.sleep(2)
    driver.find_element("id", 'NextButton').click()

    # Page 5
    # QID18-17-label --> high order satisfaction
    #       .
    #       .
    #       .
    # QID18-21-label --> very low order satisfaction
    _css_id_satfac = "QID18-18-label"
    time.sleep(2)
    driver.find_element("id", _css_id_satfac).click()
    time.sleep(2)
    driver.find_element("id", 'NextButton').click()
    
    # Page 6
    # reason for previous decison
    reason = "Das Essen hat mich gesättigt"
    #time.sleep(2)
    #driver.find_element("id", "QR~QID117").send_keys(reason)
    time.sleep(2)
    driver.find_element("id", 'NextButton').click()

    # Page 6
    # service matrix
    servicematrixpicker(_driver = driver)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)

    # Page 6
    # cleaness matrix
    cleanessmatrixpicker(_driver = driver)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)
    
    # Page 7
    # hygene
    hygenematrixpicker(_driver = driver)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)


    # Page 8
    # meal
    mealmatrixpicker(_driver = driver)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)
    
    # Page 9
    # meal
    mealsatfacmatrixpicker(_driver = driver)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)

    
    # Page 10
    # where should they clean? (indoors)
    get_source = driver.page_source
  
    # Text you want to search
    search_text = "Innenbereich"
    
    if search_text in get_source:
        driver.find_element("id", 'QID25-1-label').click()
        time.sleep(1)
        driver.find_element("id", 'QID25-2-label').click()
        time.sleep(1)
        driver.find_element("id", 'QID25-5-label').click()
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)


    # Page 11
    # where should they clean? (outdoors)
    if pagecheck(driver, "Außenbereich"):
        driver.find_element("id", 'QID26-5-label').click()
        time.sleep(1)
        driver.find_element("id", 'QID26-7-label').click()
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    #
    if pagecheck(driver, "Servicegeschwindigkeit"):
        driver.find_element("id", 'QID27-1-label').click()
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    #
    if pagecheck(driver, "Genauigkeit"):
        driver.find_element("id", 'QID28-2-label').click()
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)


    # Page 12
    # what to improve?
    if pagecheck(driver, "QID29"):
        driver.find_element("id", 'QID29-9-label').click()
        time.sleep(1)
        driver.find_element("id", 'QID29-12-label').click()
        time.sleep(1)
        driver.find_element("id", 'QID29-14-label').click()
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    if pagecheck(driver, "QID30"):
        driver.find_element("id", 'QID30-6-label').click()
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)
        
    
    if pagecheck(driver, "Freundlichkeit"):
        driver.find_element("id", 'QID34-4-label').click()
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    if pagecheck(driver, "QID35"):
        driver.find_element("id", 'QID35-2-label').click()
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)
        
    if pagecheck(driver, "Hygienemaßnahmen"):
        driver.find_element("id", 'QID37-3-label').click()
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)
    
    
    # Page 13
    # did problem occur? --> NO QID38-2-label
    driver.find_element("id", 'QID38-2-label').click()
    time.sleep(1)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)
    

    # Page 14
    # recomendations
    recomendationmatrixpicker(_driver = driver)
    time.sleep(1)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)
    

    #
    orderditemsmatrixpicker_p1(_driver = driver)
    time.sleep(1)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)
    
    #
    orderditemsmatrixpicker_p2(_driver = driver)
    time.sleep(1)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)
    
    #
    if pagecheck(driver, "QID55"):
        visitorselection(_driver = driver)
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    if pagecheck(driver, "QID48"):
        whopperrating(_driver = driver)
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    if pagecheck(driver, "QID49"):
        whoppermatrixpicker(_driver = driver)
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    if pagecheck(driver, "QID50"):
        whopperbuyagain(_driver = driver)
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)


    if pagecheck(driver, "QID53"):
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)


    if pagecheck(driver, "QID55"):
        groupesize(_driver = driver)
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    if pagecheck(driver, "QID56"):
        meal4kids(_driver = driver)
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    if pagecheck(driver, "QID57"):
        customizationcheck(_driver = driver)
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

        
    if pagecheck(driver, "QID58"):
        yes(_driver = driver)
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    if pagecheck(driver, "QID61"):
        visitsthismonth(_driver = driver)
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    if pagecheck(driver, "QID62"):
        reasonforvisit(_driver = driver)
        time.sleep(1)
        driver.find_element("id", 'NextButton').click()
        time.sleep(2)

    favoritefastfood(_driver = driver)
    time.sleep(1)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)

    incomeevaluation(_driver = driver)
    time.sleep(1)
    driver.find_element("id", 'NextButton').click()
    time.sleep(2)

    

    code = driver.find_element("xpath", '//*[@id="EndOfSurvey"]').get_attribute("innerHTML")
    m = re.split("\s", code)
    m = m[41][0:7]
    print (m)
        
    
    
    
    

    


  