from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from datetime import date,timedelta
from AutoUtil.Calendar_v2 import transformare_luna
from AutoUtil.login import login

class Adauga():

    def test(self):

        email="carla_preda@yahoo.com"
        passw="Testare123@"
        baseUrl = "https://autoutil.thedemo.is/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(15)
        time.sleep(3)

        login(driver,email,passw)

        #adauga alerta

        buton_adauga=driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='Adaugă Alertă']").click()
        time.sleep(0.5)

        adauga = driver.find_element(By.XPATH, "/html//div[@id='__next']//select")
        adauga.click()
        time.sleep(0.5)

        textToSelect = "Trusa medicala"
        elemente = adauga.find_elements(By.TAG_NAME, "option")

        for element in elemente:
            if textToSelect in element.text:
                element.click()
        time.sleep(0.6)

        ziua_15 = date.today() + timedelta(days=16)
        ziua_15_luna = ziua_15.strftime("%B")
        luna_15 = transformare_luna(ziua_15_luna)
        ziua_15_ziua = ziua_15.strftime("%d")
        if ziua_15_ziua[0] == '0':
            ziua_15_ziua = ziua_15_ziua[1]

        luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
        luna_calendar = luna_curenta_calendar.split()[0]

        if luna_15 == luna_calendar:
            data_trusa = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_15_ziua) + "']")
            data_trusa.click()
            time.sleep(1)

            cincisprezece_zile = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='15 zile']")
            cincisprezece_zile.click()
            time.sleep(0.2)

            sms = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[1]/label/div[2]/div/div[2]/div")
            sms.click()
            time.sleep(0.2)

            email2 = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[3]/label/div[2]/div/div[2]")
            email2.click()
            time.sleep(0.2)

            adaugare_alerta = driver.find_elements(By.XPATH,"/html//div[@id='__next']//div[@role='button']").__getitem__(-1)
            adaugare_alerta.click()
            time.sleep(1)
        else:
            while (luna_15 != luna_calendar):
                slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]")
                slider.click()
                luna_curenta_calendar = driver.find_elements(By.XPATH, "/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
                luna_calendar = luna_curenta_calendar.split()[0]

            data_trusa = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_15_ziua) + "']")
            data_trusa.click()
            time.sleep(1)
            cincisprezece_zile = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='15 zile']")
            cincisprezece_zile.click()
            time.sleep(0.2)
            sms = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[1]/label/div[2]/div/div[2]/div")
            sms.click()
            time.sleep(0.2)

            email2 = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[3]/label/div[2]/div/div[2]")
            email2.click()
            time.sleep(0.2)

            adaugare_alerta = driver.find_elements(By.XPATH,"/html//div[@id='__next']//div[@role='button']").__getitem__(-1)
            adaugare_alerta.click()
            time.sleep(1)




run_tests=Adauga()
run_tests.test()