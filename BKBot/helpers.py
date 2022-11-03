# Import the required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

from datetime import datetime
import random
import time

def PrintHelp() -> None:
    print("Usage: bkbot [OPTIONS]")
    print()
    print(f"""Options:                                                                                               REQUIERD
                            -h  /  --help          Display this message
                            -t  /  --time          The time of your visit - Format: HH:MM eg. {datetime.now().hour}:{datetime.now().minute}        x
                            -s  /  --store_number  Number of the store you visited (on your receed)        x
                            -d  /  --day           The day of your visit -  by default value: {datetime.now().day}
                            """)

class BKBotHelpers ():
    """
    
    """

    def __init__(self) -> None:
        pass

    def time_convert24to12(self, _time: str) -> list[str]:
        _t = datetime.strptime(_time, "%H:%M")
        _hour = _t.strftime("%I")
        _minutes = _t.strftime("%M")
        _ampm = _t.strftime("%p")
        _result = [_hour, _minutes, _ampm]

        return _result

    def StartChrome(self) -> None:
        _options = Options()
        #options.add_argument("start-maximized")
        _options.add_argument('--log-level=3')

        # Provide the path of chromedriver present on your system.
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                    options=_options)

        self.driver.set_window_size(500,400)

        # Send a get request to the url
        self.driver.get('https://bk-feedback-de.com')
        
    
    def NextPage (self) -> None:
        self.driver.find_element("id", 'NextButton').click()


    def pagecheck(self, _querry) -> bool:
        _source = self.driver.page_source
        if _querry in _source:
            _result = True

        else:
            _result = False
        
        return _result


    def datepicker(self, _day) -> None:
        _element = "//a[text()=" + str(_day) + "]"
        self.driver.implicitly_wait(3) 
        self.driver.find_element("id", "QR~QID118~2").click()
        self.driver.find_element("xpath", _element).click()


    def timepicker(self, _time_array) -> None:
        # Hour
        _css_id_hour = "QR~QID8#1~1~" + str(int(_time_array[0])) #str(int( ... )) --> get rid of a leading 0
        self.driver.find_element("id", "QR~QID8#1~1").click()
        self.driver.find_element("id", _css_id_hour).click()

        # Minutes
        _css_id_minutes = "QR~QID8#2~1~" + _time_array[1]
        self.driver.find_element("id", "QR~QID8#2~1").click()
        self.driver.find_element("id", _css_id_minutes).click()


        # AM / PM
        if _time_array[2] == "AM":
            _css_id_ampm = "QR~QID8#3~1~1"

        else:
            _css_id_ampm = "QR~QID8#3~1~2"
            
        self.driver.find_element("id", "QR~QID8#3~1").click()
        self.driver.find_element("id", _css_id_ampm).click()


    def servicematrixpicker(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(12, 16) --> random.randint(13, 15)
        """
        _xpath_array = ["4", "5", "10", "11", "13", "16"]
        for i in range(6):
            _xpath = "//label[@for='QR~QID121~" + _xpath_array[i] + "~" + str(random.randint(13, 14)) + "']"
            self.driver.find_element("xpath", _xpath).click()
            time.sleep(2)

    def cleanessmatrixpicker(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(12, 16) --> random.randint(13, 15)
        """
        _xpath_array = ["7", "9"]
        for i in range(2):
            _xpath = "//label[@for='QR~QID123~" + _xpath_array[i] + "~" + str(random.randint(13, 14)) + "']"
            self.driver.find_element("xpath", _xpath).click()
            time.sleep(2)

    def hygenematrixpicker(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(29, 33)
        """
        _id = "QID122-" + str(random.randint(29, 33)) + "-label"
        self.driver.find_element("id", _id).click()
        time.sleep(2)

    def mealmatrixpicker(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(12, 16) --> random.randint(13, 15)
            QR~QID21~1~12
        """
        _xpath_array = ["1", "2", "3", "20"]
        for i in range(4):
            _xpath = "//label[@for='QR~QID21~" + _xpath_array[i] + "~" + str(random.randint(13, 14)) + "']"
            self.driver.find_element("xpath", _xpath).click()
            time.sleep(2)

    def mealsatfacmatrixpicker(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(8, 13) --> random.randint(9, 11)
            8 bis 12 Bewertung, 13 nicht bestellt.
            QR~QID21~1~12
        """
        for i in range(4):
            _pickedchoice = [random.randint(9, 11), 13]
            _xpath = "//label[@for='QR~QID22~" + str(i + 1) + "~" + str(_pickedchoice[random.randint(0, 1)]) + "']"
            self.driver.find_element("xpath", _xpath).click()
            time.sleep(2)

    def recomendationmatrixpicker(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(6, 10) --> random.randint(7, 9)
        """
        for i in range(2):
            _xpath = "//label[@for='QR~QID41~" + str(i + 1) + "~" + str(random.randint(7, 9)) + "']"
            self.driver.find_element("xpath", _xpath).click()
            time.sleep(2)

    def orderditemsmatrixpicker_p1(self) -> None:
        if random.randint(0, 1) == 1:
            self.driver.find_element("id", "QID46-169-label").click()

        else:
            self.driver.find_element("id", "QID46-312-label").click()


    def orderditemsmatrixpicker_p2(self) -> None:
        if random.randint(0, 1) == 1:
            self.driver.find_element("id", "QID47-124-label").click()

        else:
            self.driver.find_element("id", "QID47-128-label").click()

    def visitorselection(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(6, 10) --> random.randint(7, 9)
        """
        _id = "QID55-" + str(random.randint(1, 4)) + "-label"
        self.driver.find_element("id", _id).click()
        time.sleep(2)

    def whopperrating(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(12, 15) --> random.randint(13, 14)
        """
        _id = "QID48-" + str(random.randint(13, 14)) + "-label"
        self.driver.find_element("id", _id).click()
        time.sleep(2)

    def whoppermatrixpicker(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(12, 16) --> random.randint(13, 14)
        """
        for i in range(9):
            _xpath = "//label[@for='QR~QID49~" + str(i + 1) + "~" + str(random.randint(13, 14)) + "']"
            self.driver.find_element("xpath", _xpath).click()
            time.sleep(2)

    def whopperbuyagain(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
        """
        _id = "QID50-" + str(random.randint(3, 4)) + "-label"
        self.driver.find_element("id", _id).click()
        time.sleep(2)

    def groupesize(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
        """
        _id = "QID55-" + str(random.randint(1, 4)) + "-label"
        self.driver.find_element("id", _id).click()
        time.sleep(2)

    def meal4kids(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
        """
        _id = "QID56-2-label"
        self.driver.find_element("id", _id).click()
        time.sleep(2)

    def visitsthismonth(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
        """
        _id = "QID61-" + str(random.randint(1, 5)) + "-label"
        self.driver.find_element("id", _id).click()
        time.sleep(2)

    def reasonforvisit(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
        """
        if random.randint(0, 1) == 0:
            self.driver.find_element("id", "QID62-1-label").click()

        else:
            self.driver.find_element("id", "QID62-4-label").click()

    def yes(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
        """
        self.driver.find_element("id", "QID58-1-label").click()

    def customizationcheck(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
        """
        self.driver.find_element("id", "QID57-2-label").click()

    def favoritefastfood(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
        """
        _id = "QID111-" + str(random.randint(1, 3)) + "-label"
        self.driver.find_element("id", _id).click()
        time.sleep(2)

    def incomeevaluation(self) -> None:
        """
            Für weniger extreme ergebnisse statt random.randint(1, 5) --> random.randint(3, 4)
        """
        _id = "QID67-" + str(random.randint(1, 9)) + "-label"
        self.driver.find_element("id", _id).click()
        time.sleep(2)

    def GetCode (self) -> int:
        code = self.driver.find_element("xpath", '//*[@id="EndOfSurvey"]').get_attribute("innerHTML")
        c = re.split("\s", code)
        c = c[41][0:7]

        self.driver.quit()

        return c