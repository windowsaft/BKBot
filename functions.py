import imp
from selenium import webdriver
from datetime import datetime
import random
import time

def time_convert24to12(_time):
    _t = datetime.strptime(_time, "%H:%M")
    _hour = _t.strftime("%I")
    _minutes = _t.strftime("%M")
    _ampm = _t.strftime("%p")
    _result = [_hour, _minutes, _ampm]

    return _result

def pagecheck(_driver, _querry) -> bool:
    _source = _driver.page_source
    if _querry in _source:
        _result = True

    else:
        _result = False
    
    return _result

def datepicker(_driver, _day) -> None:
    _element = "//a[text()=" + str(_day) + "]"
    _driver.implicitly_wait(3) 
    _driver.find_element("id", "QR~QID118~2").click()
    _driver.find_element("xpath", _element).click()


def timepicker(_driver, _time_array) -> None:
    # Hour
    _css_id_hour = "QR~QID8#1~1~" + _time_array[0]
    _driver.find_element("id", "QR~QID8#1~1").click()
    _driver.find_element("id", _css_id_hour).click()

    # Minutes
    _css_id_minutes = "QR~QID8#2~1~" + _time_array[1]
    _driver.find_element("id", "QR~QID8#2~1").click()
    _driver.find_element("id", _css_id_minutes).click()


    # AM / PM
    if _time_array[2] == "AM":
        _css_id_ampm = "QR~QID8#3~1~1"

    else:
        _css_id_ampm = "QR~QID8#3~1~" + _time_array[1]
        
    _driver.find_element("id", "QR~QID8#3~1").click()
    _driver.find_element("id", _css_id_ampm).click()

def servicematrixpicker(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(12, 16) --> random.randint(13, 15)
    """
    _xpath_array = ["4", "5", "10", "11", "13", "16"]
    for i in range(6):
        _xpath = "//label[@for='QR~QID121~" + _xpath_array[i] + "~" + str(random.randint(13, 14)) + "']"
        _driver.find_element("xpath", _xpath).click()
        time.sleep(2)

def cleanessmatrixpicker(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(12, 16) --> random.randint(13, 15)
    """
    _xpath_array = ["7", "9"]
    for i in range(2):
        _xpath = "//label[@for='QR~QID123~" + _xpath_array[i] + "~" + str(random.randint(13, 14)) + "']"
        _driver.find_element("xpath", _xpath).click()
        time.sleep(2)

def hygenematrixpicker(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(29, 33)
    """
    _id = "QID122-" + str(random.randint(29, 33)) + "-label"
    _driver.find_element("id", _id).click()
    time.sleep(2)

def mealmatrixpicker(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(12, 16) --> random.randint(13, 15)
        QR~QID21~1~12
    """
    _xpath_array = ["1", "2", "3", "20"]
    for i in range(4):
        _xpath = "//label[@for='QR~QID21~" + _xpath_array[i] + "~" + str(random.randint(13, 14)) + "']"
        _driver.find_element("xpath", _xpath).click()
        time.sleep(2)

def mealsatfacmatrixpicker(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(8, 13) --> random.randint(9, 11)
        8 bis 12 Bewertung, 13 nicht bestellt.
        QR~QID21~1~12
    """
    for i in range(4):
        _pickedchoice = [random.randint(9, 11), 13]
        _xpath = "//label[@for='QR~QID22~" + str(i + 1) + "~" + str(_pickedchoice[random.randint(0, 1)]) + "']"
        _driver.find_element("xpath", _xpath).click()
        time.sleep(2)

def recomendationmatrixpicker(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(6, 10) --> random.randint(7, 9)
    """
    for i in range(2):
        _xpath = "//label[@for='QR~QID41~" + str(i + 1) + "~" + str(random.randint(7, 9)) + "']"
        _driver.find_element("xpath", _xpath).click()
        time.sleep(2)

def orderditemsmatrixpicker_p1(_driver) -> None:
    if random.randint(0, 1) == 1:
        _driver.find_element("id", "QID46-169-label").click()

    else:
        _driver.find_element("id", "QID46-312-label").click()


def orderditemsmatrixpicker_p2(_driver) -> None:
    if random.randint(0, 1) == 1:
        _driver.find_element("id", "QID47-124-label").click()

    else:
        _driver.find_element("id", "QID47-128-label").click()

def visitorselection(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(6, 10) --> random.randint(7, 9)
    """
    _id = "QID55-" + str(random.randint(1, 4)) + "-label"
    _driver.find_element("id", _id).click()
    time.sleep(2)

def whopperrating(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(12, 15) --> random.randint(13, 14)
    """
    _id = "QID48-" + str(random.randint(13, 14)) + "-label"
    _driver.find_element("id", _id).click()
    time.sleep(2)

def whoppermatrixpicker(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(12, 16) --> random.randint(13, 14)
    """
    for i in range(9):
        _xpath = "//label[@for='QR~QID49~" + str(i + 1) + "~" + str(random.randint(13, 14)) + "']"
        _driver.find_element("xpath", _xpath).click()
        time.sleep(2)

def whopperbuyagain(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
    """
    _id = "QID50-" + str(random.randint(3, 4)) + "-label"
    _driver.find_element("id", _id).click()
    time.sleep(2)

def groupesize(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
    """
    _id = "QID55-" + str(random.randint(1, 4)) + "-label"
    _driver.find_element("id", _id).click()
    time.sleep(2)

def meal4kids(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
    """
    _id = "QID56-2-label"
    _driver.find_element("id", _id).click()
    time.sleep(2)

def visitsthismonth(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
    """
    _id = "QID61-" + str(random.randint(1, 5)) + "-label"
    _driver.find_element("id", _id).click()
    time.sleep(2)

def reasonforvisit(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
    """
    if random.randint(0, 1) == 0:
        _driver.find_element("id", "QID62-1-label").click()

    else:
        _driver.find_element("id", "QID62-4-label").click()

def yes(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
    """
    _driver.find_element("id", "QID58-1-label").click()

def customizationcheck(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
    """
    _driver.find_element("id", "QID57-2-label").click()

def favoritefastfood(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
    """
    _id = "QID111-" + str(random.randint(1, 3)) + "-label"
    _driver.find_element("id", _id).click()
    time.sleep(2)

def incomeevaluation(_driver) -> None:
    """
        Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
    """
    _id = "QID67-" + str(random.randint(1, 9)) + "-label"
    _driver.find_element("id", _id).click()
    time.sleep(2)

if __name__ == "__main__":
    timepicker("11:30")