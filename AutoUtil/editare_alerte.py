from selenium import webdriver
from AutoUtil.login import login
from selenium.webdriver.common.by import By
import time
from datetime import date,timedelta
from AutoUtil.Calendar_v2 import transformare_luna

class Editare():

    def test(self):
        email = "carla_preda@yahoo.com"
        passw = "Testare123@"
        baseUrl = "https://autoutil.thedemo.is/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.set_window_position(0,0)
        driver.maximize_window()
        driver.implicitly_wait(15)
        time.sleep(3)

        login(driver,email,passw)


        #modifica alerte
        driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='Modifică Alerte']").click()
        time.sleep(1)




    #ITP

        reinoieste_itp = driver.find_elements(By.XPATH, "/html//div[@id='__next']//img").__getitem__(5).click()
        time.sleep(2)

        ziua_1 = date.today() + timedelta(days=2)
        ziua_1_luna = ziua_1.strftime("%B")
        luna_1 = transformare_luna(ziua_1_luna)
        ziua_1_ziua = ziua_1.strftime("%d")
        if ziua_1_ziua[0] == '0':
            ziua_1_ziua = ziua_1_ziua[1]

        luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
        luna_calendar = luna_curenta_calendar.split()[0]

        if luna_1 == luna_calendar:
            data_itp = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(ziua_1_ziua) + "']")
            data_itp.click()
            time.sleep(2)

            o_zi = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='1 zi']")
            o_zi.click()
            time.sleep(0.2)

            o_zi = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='1 zi']")
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
            time.sleep(2)


        else:
            while (luna_1 != luna_calendar):
                slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]")
                slider.click()
                luna_curenta_calendar = driver.find_elements(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']//div").__getitem__(5).get_attribute("innerHTML")
                luna_calendar = luna_curenta_calendar.split()[0]

            data_itp = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='button']/div[.='" + str(ziua_1_ziua) + "']")
            data_itp.click()
            time.sleep(0.8)
            o_zi = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='1 zi']")
            o_zi.click()
            time.sleep(0.2)

            o_zi = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='1 zi']")
            o_zi.click()
            time.sleep(0.2)

            sms = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[1]/label/div[2]/div/div[2]/div")
            sms.click()
            time.sleep(0.2)

            email2 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/label/div[2]/div/div[2]")
            email2.click()
            time.sleep(0.2)

            adaugare_alerta = driver.find_elements(By.XPATH,"/html//div[@id='__next']//div[@role='button']").__getitem__(-1)
            adaugare_alerta.click()
            time.sleep(1)

        #RCA

        buton_modifica = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='Modifică Alerte']").click()
        time.sleep(1)

        renoieste_rca = driver.find_elements(By.XPATH, "/html//div[@id='__next']//img").__getitem__(7).click()
        time.sleep(1)

        ziua_5 = date.today() + timedelta(days=10)
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


            adaugare_alerta = driver.find_elements(By.XPATH,"/html//div[@id='__next']//div[@role='button']").__getitem__(-1)
            adaugare_alerta.click()
            time.sleep(1)

        # Rovinieta
        buton_modifica = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='Modifică Alerte']").click()
        time.sleep(1)

        renoieste_rovinieta = driver.find_elements(By.XPATH, "/html//div[@id='__next']//img").__getitem__(10).click()

        time.sleep(2)

        ziua_15 = date.today() + timedelta(days=17)
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

             adaugare_alerta = driver.find_elements(By.XPATH,"/html//div[@id='__next']//div[@role='button']").__getitem__(-1)
             adaugare_alerta.click()
             time.sleep(1)


         #Casco
        driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='Modifică Alerte']").click()
        time.sleep(1)

        driver.find_elements(By.XPATH,"/html//div[@id='__next']//img").__getitem__(13).click()

        ziua_30 = date.today() + timedelta(days=32)
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
            time.sleep(0.3)

            treizeci_zile = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='30 zile']")
            treizeci_zile.click()
            time.sleep(0.3)

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

            data_casco = driver.find_elements(By.XPATH, "/html//div[@id='choice-calendar']//div[.='" + str(ziua_30_ziua) + "']").__getitem__(-1)
            data_casco.click()
            time.sleep(1)

            treizeci_zile = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='30 zile']")
            treizeci_zile.click()
            time.sleep(0.3)

            treizeci_zile = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='30 zile']")
            treizeci_zile.click()
            time.sleep(0.3)

            sms = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[1]/label/div[2]/div/div[2]/div")
            sms.click()
            time.sleep(0.2)

            email2 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/label/div[2]/div/div[2]")
            email2.click()
            time.sleep(0.2)

            adaugare_alerta = driver.find_elements(By.XPATH,"/html//div[@id='__next']//div[@role='button']").__getitem__(-1)
            adaugare_alerta.click()
            time.sleep(1)


run_tests=Editare()
run_tests.test()