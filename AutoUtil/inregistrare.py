from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

def inregistrare():
    baseUrl = "https://autoutil.thedemo.is/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get(baseUrl)

    # creeaza contul
    inregistrare = driver.find_elements(By.XPATH, "/html//div[@id='__next']//div[.='CREEAZĂ CONT']").__getitem__(-1)
    inregistrare.click()

    email = driver.find_element(By.XPATH, "//input[@type='text']")
    email.send_keys("carla_preda@yahoo.com")

    time.sleep(0.5)
    parola = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/div[2]/input")
    parola.send_keys("Testare123@")

    confirmare_parola = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[5]/div[2]/input")
    confirmare_parola.send_keys("Testare123@")
    time.sleep(0.5)

    continua = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[@role='button']//div[@class='css-1dbjc4n']")
    continua.click()
    time.sleep(1)

    nume = driver.find_elements(By.XPATH, "/html//div[@id='__next']//input").__getitem__(-4)
    nume.send_keys("Carla")
    time.sleep(1)

    telefon = driver.find_elements(By.XPATH, "/html//div[@id='__next']//input").__getitem__(-3)
    telefon.send_keys("0737528681")
    time.sleep(1)

    buton1 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[2]/div/div[2]/div")
    buton1.click()

    buton2 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/div[2]/label")
    buton2.click()

    creeaza_cont = driver.find_elements(By.XPATH, "/html//div[@id='__next']//div[@role='button']/div").__getitem__(-1)
    creeaza_cont.click()
    time.sleep(2)

