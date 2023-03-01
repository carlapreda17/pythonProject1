from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from datetime import date,timedelta
from AutoUtil.Calendar_v2 import transformare_luna
from AutoUtil.inregistrare import inregistrare
from AutoUtil.login import login
from AutoUtil.adauga_masina import adauga_masisna


class AutoUtil():

    def inregistrare(self):
        inregistrare()

    def alerte(self):
        nr_masina="VN 06 HRK"
        baseUrl = "https://autoutil.thedemo.is/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(15)
        time.sleep(3)


        adauga_masisna(driver,nr_masina)

        #alerte
        ziua_1 = date.today() + timedelta(days=2)
        ziua_1_luna = ziua_1.strftime("%B")
        luna_1 = transformare_luna(ziua_1_luna)
        ziua_1_ziua = ziua_1.strftime("%d")
        if ziua_1_ziua[0] == '0':
            ziua_1_ziua = ziua_1_ziua[1]

        # ITP
        itp = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[3]/div/div[3]/div[.='adaugă alertă']")
        itp.click()
        time.sleep(0.7)

        luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
        luna_calendar = luna_curenta_calendar.split()[0]

        if luna_1 == luna_calendar:
            data_itp = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_1_ziua) + "']")
            data_itp.click()
            time.sleep(1)

            o_zi = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='1 zi']")
            o_zi.click()
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

            ok = driver.find_element(By.XPATH,"/html//div[@id='__next']/div/div[2]/div[2]//div[@role='dialog']//div[@role='button']")
            ok.click()
            time.sleep(10)

            confirmare = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='CONTINUĂ']")
            confirmare.click()
            time.sleep(1)

            adaugare_alerta.click()
            time.sleep(1)

        else:
            while (luna_1 != luna_calendar):
                slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]")
                slider.click()
                luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
                luna_calendar = luna_curenta_calendar.split()[0]
                

            slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]")
            time.sleep(2)
            data_itp = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='button']/div[.='" + str(ziua_1_ziua) + "']")
            data_itp.click()
            time.sleep(0.8)
            ziua_1 = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='1 zi']")
            ziua_1.click()
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

            ok = driver.find_element(By.XPATH,"/html//div[@id='__next']/div/div[2]/div[2]//div[@role='dialog']//div[@role='button']")
            ok.click()
            time.sleep(10)

            confirmare = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='CONTINUĂ']")
            confirmare.click()
            time.sleep(2)

            adaugare_alerta.click()
            time.sleep(2)

         #RCA

        rca = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[5]/div/div[3]/div[.='adaugă alertă']")
        rca.click()
        time.sleep(1)

        ziua_5 = date.today() + timedelta(days=6)
        ziua_5_luna = ziua_5.strftime("%B")
        luna_5 = transformare_luna(ziua_5_luna)
        ziua_5_ziua = ziua_5.strftime("%d")
        if ziua_5_ziua[0] == '0':
            ziua_5_ziua = ziua_5_ziua[1]

        luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
        luna_calendar = luna_curenta_calendar.split()[0]

        if luna_5 == luna_calendar:
             data_rca = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_5_ziua) + "']")
             data_rca.click()
             time.sleep(1)

             cinci_zile = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='5 zile']")
             cinci_zile.click()
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
            while (luna_5 != luna_calendar):
                slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]")
                slider.click()
                luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
                luna_calendar = luna_curenta_calendar.split()[0]


            data_rca = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_5_ziua) + "']")
            data_rca.click()
            time.sleep(1)

            cinci_zile = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='5 zile']")
            cinci_zile.click()
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

        # Rovinieta
        rovinieta = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[7]/div/div[3]/div[.='adaugă alertă']")
        rovinieta.click()
        time.sleep(2)

        ziua_15 = date.today() + timedelta(days=16)
        ziua_15_luna = ziua_15.strftime("%B")
        luna_15 = transformare_luna(ziua_15_luna)
        ziua_15_ziua = ziua_15.strftime("%d")
        if ziua_15_ziua[0] == '0':
             ziua_15_ziua = ziua_15_ziua[1]

        luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
        luna_calendar = luna_curenta_calendar.split()[0]

        if luna_15 == luna_calendar:
                data_rovinieta = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_15_ziua) + "']")
                data_rovinieta.click()
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
                    luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
                    luna_calendar = luna_curenta_calendar.split()[0]

                data_rovinieta = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_15_ziua) + "']")
                data_rovinieta.click()
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

        # CASCO
        casco = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[9]/div/div[3]/div[.='adaugă alertă']")
        casco.click()

        alerta = driver.find_element(By.XPATH,"/html//div[@id='__next']//select")
        alerta.click()

        textToSelect = "CASCO"
        elemente = alerta.find_elements(By.TAG_NAME, "option")

        for element in elemente:
           if textToSelect in element.text:
                    element.click()
                    time.sleep(5)

        ziua_30 = date.today() + timedelta(days=31)
        ziua_30_luna = ziua_30.strftime("%B")
        luna_30 = transformare_luna(ziua_30_luna)
        ziua_30_ziua = ziua_30.strftime("%d")
        if ziua_30_ziua[0] == '0':
                ziua_30_ziua = ziua_30_ziua[1]

        luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
        luna_calendar = luna_curenta_calendar.split()[0]

        if luna_30 == luna_calendar:
                data_casco = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_30_ziua) + "']")
                data_casco.click()
                time.sleep(1)

                treizeci_zile = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='30 zile']")
                treizeci_zile.click()
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
            if luna_30 != luna_calendar:
                 slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]")
                 slider.click()
                 luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
                 luna_calendar = luna_curenta_calendar.split()[0]

                 if luna_30 != luna_calendar:
                        slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]")
                        slider.click()
                        luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
                        luna_calendar = luna_curenta_calendar.split()[0]

            data_casco = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_30_ziua) + "']").__getitem__(-1)
            data_casco.click()
            time.sleep(1)

            treizeci_zile = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='30 zile']")
            treizeci_zile.click()
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

        #documente
        meniu = driver.find_elements(By.XPATH,"/html//div[@id='__next']//div/img").__getitem__(1)
        meniu.click()
        time.sleep(3)

        documentele_mele = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='Documentele mele']")
        documentele_mele.click()
        time.sleep(2)

        adaugare_document = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='ADAUGĂ DOCUMENT']")
        adaugare_document.click()
        time.sleep(3)

        document = driver.find_element(By.XPATH, "/html//div[@id='__next']//select")
        document.click()
        time.sleep(3)

        textToSelect = "Pasaport"
        elemente = document.find_elements(By.TAG_NAME, "option")

        for element in elemente:
            if textToSelect in element.text:
                element.click()
        time.sleep(5)

        ziua_1 = date.today() + timedelta(days=2)
        ziua_1_luna = ziua_1.strftime("%B")
        luna_1 = transformare_luna(ziua_1_luna)
        ziua_1_ziua = ziua_1.strftime("%d")
        if ziua_1_ziua[0] == '0':
            ziua_1_ziua = ziua_1_ziua[1]

        luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
        luna_calendar = luna_curenta_calendar.split()[0]

        if luna_1 == luna_calendar:
            data_pasaport = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_1_ziua) + "']")
            data_pasaport.click()
            time.sleep(1)

            o_zi = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='1 zi']")
            o_zi.click()
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
            while (luna_1 != luna_calendar):
                slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]")
                slider.click()
                luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
                luna_calendar = luna_curenta_calendar.split()[0]


            data_pasaport = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='button']/div[.='" + str(ziua_1_ziua) + "']")
            data_pasaport.click()
            time.sleep(3)
            ziua_1 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='1 zi']")
            ziua_1.click()
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


        driver.back()



run_tests=AutoUtil()
run_tests.alerte()