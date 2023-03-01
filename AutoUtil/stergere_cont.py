from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from AutoUtil.login import login

def stergere_cont():
    email = "carla_preda@yahoo.com"
    passw = "Testare123@"
    baseUrl = "https://autoutil.thedemo.is/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    time.sleep(3)
    driver.get(baseUrl)

    login(driver, email, passw)

    meniu = driver.find_elements(By.XPATH, "/html//div[@id='__next']//div/img").__getitem__(1)
    meniu.click()
    time.sleep(3)

    profilul_meu = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='Profilul meu']")
    profilul_meu.click()
    time.sleep(2)

    buton_stergere = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='ȘTERGE CONTUL']")
    buton_stergere.click()
    time.sleep(2)

    buton_da = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='DA']")
    buton_da.click()
    time.sleep(2)


stergere_cont()