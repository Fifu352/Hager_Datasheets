# this is going to be a well written code to give few informations about a particular word

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys
import os

def script(mail, passw, name1):
    url_hager = "http://www.hager.pl/"
    url_projects = "https://www.hager.pl/moje-projekty/39037.htm"
    email = mail
    password = passw
    name = name1
    csv = os.path.join(os.path.expanduser("~"), "Desktop")+"\Eksport.csv"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(executable_path=r"C:\Users\Fifu\Documents\untitled1\venv\Include\chromedriver.exe")
    driver.get(url_hager)

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='button small index__meta__login']"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.click()

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@name='CUG_Username']"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.send_keys(email)

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@name='CUG_Password']"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.send_keys(password)

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='twelve small with-icon-right']"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.click()
    time.sleep(0.2)
    driver.get(url_projects)
    time.sleep(0.2)
    driver.execute_script("ProjectList2011Action('projectlistImportChoice')")

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='project-layer-button-0-0']"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.click()

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "projectlistTitleImport"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.send_keys(name)
    time.sleep(0.5)

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='project-layer-button-3-0']"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.click()

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@type='file']"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.send_keys(csv)


    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@title='Importuj wybrane projekty/produkty']"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.click()

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "boxaccordion-header-wrapper-link"))
        )
    except:
        quit()
    time.sleep(0.2)
    driver.find_elements_by_class_name('boxaccordion-header-wrapper-link')[-1].click()

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "tab-1"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.click()

    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "selectall"))
        )
    except:
        quit()
    time.sleep(0.2)
    element.click()


    driver.implicitly_wait(5)

    driver.execute_script("ProjectList2011Download('#project-detail-documents-form');return false;")


if __name__ == "__main__":
    a = str(sys.argv[1])
    b = str(sys.argv[2])
    c = str(sys.argv[3])
    script(a,b,c)