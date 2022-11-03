from helpers import BKBotHelpers
import time

from datetime import datetime


class BKBotPages ():
    def __init__(self, _store_number: str, _time: str, _day: int = datetime.now().day) -> None:
        self.store_number = _store_number
        self.time = _time
        self.day =_day

        self.BKBotH = BKBotHelpers()
        self.BKBotH.StartChrome()

        self.driver = self.BKBotH.driver

    
    def page (self,  _num) -> None:
        if _num == 1:
            """
                Actions on Page 1
            """

            self.driver.find_element("id", 'QR~QID4').send_keys(self.store_number)
            time.sleep(2)
            self.BKBotH.NextPage()


        elif _num == 2:
            time.sleep(3)
            self.BKBotH.datepicker( _day = self.day)
            time.sleep(3)
            self.BKBotH.timepicker(self.BKBotH.time_convert24to12(self.time))
            self.BKBotH.NextPage()


        elif _num == 3:
            """
                Page 3
                - QID12-1-label --> Self-Service
                - QID12-2-label --> Counter
                - QID12-3-label --> App
            """
        
        
            _css_id_ordermethod = "QID12-1-label"
            time.sleep(2)
            self.driver.find_element("id", _css_id_ordermethod).click()
            time.sleep(2)
            self.BKBotH.NextPage()


        elif _num == 4:
            """ Page 4
            # QID14-2-label --> on site
            # QID14-3-label --> take away
            """

            _css_id_locationtarget = "QID14-2-label"
            time.sleep(2)
            self.driver.find_element("id", _css_id_locationtarget).click()
            time.sleep(2)
            self.BKBotH.NextPage()



        elif _num == 5:
            """# Page 5
            # QID18-17-label --> high order satisfaction
            #       .
            #       .
            #       .
            # QID18-21-label --> very low order satisfaction
            # """
            _css_id_satfac = "QID18-18-label"
            time.sleep(2)
            self.driver.find_element("id", _css_id_satfac).click()
            time.sleep(2)
            self.BKBotH.NextPage()
            
        elif _num == 6:
            # Page 6
            # reason for previous decison
            reason = "Das Essen hat mich gesättigt"
            #time.sleep(2)
            #driver.find_element("id", "QR~QID117").send_keys(reason)
            time.sleep(2)
            self.BKBotH.NextPage()

        elif _num == 7:
            # Page 7
            # service matrix
            self.BKBotH.servicematrixpicker()
            self.BKBotH.NextPage()
            time.sleep(2)

        elif _num == 8:
            # Page 8
            # cleaness matrix
            self.BKBotH.cleanessmatrixpicker()
            self.BKBotH.NextPage()
            time.sleep(2)
        
        elif _num == 9:
            # Page 7
            # hygene
            self.BKBotH.hygenematrixpicker()
            self.BKBotH.NextPage()
            time.sleep(2)

        elif _num == 10:
            # Page 8
            # meal
            self.BKBotH.mealmatrixpicker()
            self.BKBotH.NextPage()
            time.sleep(2)
        
        elif _num == 10:
            # Page 9
            # meal
            self.BKBotH.mealsatfacmatrixpicker()
            self.BKBotH.NextPage()
            time.sleep(2)

        elif _num == 25:
            """
            where should they clean? (indoors)
            """
            if self.BKBotH.pagecheck("Außenbereich"):
                self.driver.find_element("id", 'QID25-1-label').click()
                time.sleep(1)
                self.driver.find_element("id", 'QID25-2-label').click()
                time.sleep(1)
                self.driver.find_element("id", 'QID25-5-label').click()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 26:
            # Page 11
            # where should they clean? (outdoors)
            if self.BKBotH.pagecheck("Außenbereich"):
                self.driver.find_element("id", 'QID26-5-label').click()
                time.sleep(1)
                self.driver.find_element("id", 'QID26-7-label').click()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)




        elif _num == 27:
            if self.BKBotH.pagecheck("Servicegeschwindigkeit"):
                self.driver.find_element("id", 'QID27-1-label').click()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 28:
            if self.BKBotH.pagecheck("Genauigkeit"):
                self.driver.find_element("id", 'QID28-2-label').click()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)


        elif _num == 29:
            # Page 12
            # what to improve?
            if self.BKBotH.pagecheck("QID29"):
                self.driver.find_element("id", 'QID29-9-label').click()
                time.sleep(1)
                self.driver.find_element("id", 'QID29-12-label').click()
                time.sleep(1)
                self.driver.find_element("id", 'QID29-14-label').click()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 30:
            if self.BKBotH.pagecheck("QID30"):
                self.driver.find_element("id", 'QID30-6-label').click()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)
            
        
        elif _num == 34:
            if self.BKBotH.pagecheck("Freundlichkeit"):
                self.driver.find_element("id", 'QID34-4-label').click()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 35:
            if self.BKBotH.pagecheck("QID35"):
                self.driver.find_element("id", 'QID35-2-label').click()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)
            
        elif _num == 37:
            if self.BKBotH.pagecheck("Hygienemaßnahmen"):
                self.driver.find_element("id", 'QID37-3-label').click()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)
        
        elif _num == 38:
            # Page 13
            # did problem occur? --> NO QID38-2-label
            self.driver.find_element("id", 'QID38-2-label').click()
            time.sleep(1)
            self.BKBotH.NextPage()
            time.sleep(2)
        

        elif _num == 39:
            # Page 14
            # recomendations
            self.BKBotH.recomendationmatrixpicker()
            time.sleep(1)
            self.BKBotH.NextPage()
            time.sleep(2)
        

        #
        elif _num == 40:
            self.BKBotH.orderditemsmatrixpicker_p1()
            time.sleep(1)
            self.BKBotH.NextPage()
            time.sleep(2)
        
        #
        elif _num == 41:
            self.BKBotH.orderditemsmatrixpicker_p2()
            time.sleep(1)
            self.BKBotH.NextPage()
            time.sleep(2)
        
        #
        elif _num == 47:
            if self.BKBotH.pagecheck("QID55"):
                self.BKBotH.visitorselection()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 48:
            if self.BKBotH.pagecheck("QID48"):
                self.BKBotH.whopperrating()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 49:
            if self.BKBotH.pagecheck("QID49"):
                self.BKBotH.whoppermatrixpicker()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 50:
            if self.BKBotH.pagecheck("QID50"):
                self.BKBotH.whopperbuyagain()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 53:
            if self.BKBotH.pagecheck("QID53"):
                self.BKBotH.NextPage()
                time.sleep(2)


        elif _num == 55:
            if self.BKBotH.pagecheck("QID55"):
                self.BKBotH.groupesize()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 56:
            if self.BKBotH.pagecheck("QID56"):
                self.BKBotH.meal4kids()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 57:
            if self.BKBotH.pagecheck("QID57"):
                self.BKBotH.customizationcheck()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 58:
            if self.BKBotH.pagecheck("QID58"):
                self.BKBotH.yes()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)
        
        elif _num == 61:
            if self.BKBotH.pagecheck("QID61"):
                self.BKBotH.visitsthismonth()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)
        
        elif _num == 62:
            if self.BKBotH.pagecheck("QID62"):
                self.BKBotH.reasonforvisit()
                time.sleep(1)
                self.BKBotH.NextPage()
                time.sleep(2)

        elif _num == 63:
            self.BKBotH.favoritefastfood()
            time.sleep(1)
            self.BKBotH.NextPage()
            time.sleep(2)
            self.BKBotH.NextPage()
            time.sleep(2)

        elif _num == 64:
            self.BKBotH.incomeevaluation()
            time.sleep(1)
            self.BKBotH.NextPage()
            time.sleep(2)
