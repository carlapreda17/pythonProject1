from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from AutoUtil.login import login


def adauga_masisna(driver="",nr_masina=""):
    email = "carla_preda@yahoo.com"
    passw = "Testare123@"
    baseUrl = "https://autoutil.thedemo.is/"
    driver.get(baseUrl)
    driver.maximize_window()
    driver.implicitly_wait(15)
    time.sleep(3)

    login(driver, email, passw)

    # adauga masina
    adauga = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[@role='button']")
    adauga.click()
    time.sleep(1)

    nr_inmatriculare = driver.find_element(By.XPATH, "/html//div[@id='__next']//input")
    nr_inmatriculare.send_keys(nr_masina)
    time.sleep(1)

    adauga_masina = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='ADAUGĂ MAȘINĂ']")
    adauga_masina.click()
    time.sleep(1)