import random

import telebot.asyncio_helper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time
from setting import *
from main import *
from db import *
import urllib.request

async def getTeh(user, id_user):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
      "download.default_directory": r"/root/BOT_TAXI_SELENIUM-",
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "plugins.always_open_pdf_externally": True
    })
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://art.taxi.mos.ru')
    time.sleep(5)
    login = driver.find_element_by_css_selector('[class*="MuiInputBase-input MuiOutlinedInput-input"]')
    login.clear()
    login.send_keys("9265863701")
    pswd = driver.find_element_by_css_selector('[class*="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd MuiOutlinedInput-inputAdornedEnd"]')
    pswd.send_keys("KYAg14lj")
    driver.find_element_by_css_selector('[class*="MuiButton-label"]').click()
    time.sleep(5)
    driver.get('https://art.taxi.mos.ru/waybills')
    time.sleep(5)
    driver.find_element_by_css_selector('[value*="' + str(user) + '"]').click()
    time.sleep(2)
    driver.find_element_by_css_selector('[d*="M5 4v2h14V4H5zm0 10h4v6h6v-6h4l-7-7-7 7z"]').click()
    time.sleep(2)
    data = driver.find_element_by_css_selector('[name*="checkupData.odometerData"]')
    temp = random.randint(840000, 844000)
    data.send_keys(str(temp))
    time.sleep(2)
    driver.find_element_by_css_selector('[name*="checkupData.desinfected"]').click()
    elem = driver.find_elements_by_xpath("//div[@role='dialog']//span[@class='MuiButton-label']")[1]
    print(elem.text)
    webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
    time.sleep(4)
    elem_last = driver.find_element_by_css_selector('[class*="MuiButton-label"]')
    webdriver.ActionChains(driver).move_to_element(elem_last).click(elem_last).perform()
    time.sleep(5)
    driver.close()
    file_ = None
    for file in glob.glob("*.pdf"):
        file_ = file
    await send_file(id_user, file_)

async def RegUser(id, id_tg, db):
    driver = webdriver.Chrome()
    driver.get('https://art.taxi.mos.ru')
    time.sleep(5)
    login = driver.find_element_by_css_selector('[class*="MuiInputBase-input MuiOutlinedInput-input"]')
    login.clear()
    login.send_keys("9265863701")
    pswd = driver.find_element_by_css_selector('[class*="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd MuiOutlinedInput-inputAdornedEnd"]')
    pswd.send_keys("KYAg14lj")
    driver.find_element_by_css_selector('[class*="MuiButton-label"]').click()
    time.sleep(5)
    try:
        driver.get('https://art.taxi.mos.ru/drivers')
        time.sleep(5)
        driver.find_element_by_css_selector('[value*="' + str(id) + '"]').click()
        time.sleep(2)
        first_name = driver.find_element_by_css_selector('[name*="user.lastName"]').get_attribute('value')
        second_name = driver.find_element_by_css_selector('[name*="user.firstName"]').get_attribute('value')
        th_name = driver.find_element_by_css_selector('[name*="user.patronymic"]').get_attribute('value')
        FIO = str(first_name) + ' ' + str(second_name) + ' ' + str(th_name)
        db.register_new_user(FIO, id, id_tg)
        driver.close()
    except:
        driver.close()
        await ERROR(id_tg)
        return 0

async def getMed(user, id_user):
    driver = webdriver.Chrome()
    driver.get('https://art.taxi.mos.ru')
    time.sleep(5)
    login = driver.find_element_by_css_selector('[class*="MuiInputBase-input MuiOutlinedInput-input"]')
    login.clear()
    login.send_keys("9151127411")
    pswd = driver.find_element_by_css_selector('[class*="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd MuiOutlinedInput-inputAdornedEnd"]')
    pswd.send_keys("j5SYAk80")
    driver.find_element_by_css_selector('[class*="MuiButton-label"]').click()
    time.sleep(5)
    await getMed_step_2(user, driver, id_user)


async def getMed_step_2(user, driver, id_user):
    driver.get('https://art.taxi.mos.ru/waybills')
    try:
        driver.find_element_by_css_selector('[value*="' + str(user) + '"]').click()
        time.sleep(2)
        driver.find_element_by_css_selector('[d*="M5 4v2h14V4H5zm0 10h4v6h6v-6h4l-7-7-7 7z"]').click()
        time.sleep(2)
        elem_1 = driver.find_element_by_css_selector('[name*="checkupData.bodyTemperature"]')
        elem_2 = driver.find_element_by_css_selector('[name*="checkupData.bloodPressureSys"]')
        elem_3 = driver.find_element_by_css_selector('[name*="checkupData.bloodPressureDia"]')
        elem_1.send_keys("36.6")
        temp = random.randint(120, 130)
        elem_2.send_keys(str(temp))
        temp = random.randint(70, 90)
        elem_3.send_keys(str(temp))
        driver.find_element_by_css_selector('[name*="checkupData.alcoholTestPassed"]').click()
        time.sleep(4)
        elem = driver.find_elements_by_xpath("//div[@role='dialog']//span[@class='MuiButton-label']")[1]
        print(elem.text)
        webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
        time.sleep(4)
        elem_last = driver.find_element_by_css_selector('[class*="MuiButton-label"]')
        webdriver.ActionChains(driver).move_to_element(elem_last).click(elem_last).perform()
        time.sleep(5)
        driver.close()
        await getTeh(user, id_user)
    except:
        await ERROR_(id_user)
        driver.close()
        return 0

async def getAfterTeh(user, id_user):
    driver = webdriver.Chrome()
    driver.get('https://art.taxi.mos.ru')
    time.sleep(5)
    login = driver.find_element_by_css_selector('[class*="MuiInputBase-input MuiOutlinedInput-input"]')
    login.clear()
    login.send_keys("9151127411")
    pswd = driver.find_element_by_css_selector('[class*="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd MuiOutlinedInput-inputAdornedEnd"]')
    pswd.send_keys("j5SYAk80")
    driver.find_element_by_css_selector('[class*="MuiButton-label"]').click()
    time.sleep(5)
    driver.get('https://art.taxi.mos.ru/waybills')
    time.sleep(5)
    driver.find_element_by_css_selector('[value*="' + str(user) + '"]').click()
    time.sleep(2)
    driver.find_elements_by_css_selector('[d*="M5 4v2h14V4H5zm0 10h4v6h6v-6h4l-7-7-7 7z"]')[-1].click()
    time.sleep(2)
    driver.find_element_by_css_selector('[name*="checkupData.alcoholTestPassed"]').click()
    elem = driver.find_elements_by_xpath("//div[@role='dialog']//span[@class='MuiButton-label']")[1]
    print(elem.text)
    webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
    time.sleep(4)
    elem_last = driver.find_element_by_css_selector('[class*="MuiButton-label"]')
    webdriver.ActionChains(driver).move_to_element(elem_last).click(elem_last).perform()
    driver.close()
    await getAfterMed(user, id_user)

async def getAfterMed(user, id_user):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": r"C:\Users\nikit\TAXI_BOT_SLENIUM",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    })
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://art.taxi.mos.ru')
    time.sleep(5)
    login = driver.find_element_by_css_selector('[class*="MuiInputBase-input MuiOutlinedInput-input"]')
    login.clear()
    login.send_keys("9265863701")
    pswd = driver.find_element_by_css_selector('[class*="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd MuiOutlinedInput-inputAdornedEnd"]')
    pswd.send_keys("KYAg14lj")
    driver.find_element_by_css_selector('[class*="MuiButton-label"]').click()
    time.sleep(5)
    driver.get('https://art.taxi.mos.ru/waybills')
    time.sleep(5)
    driver.find_element_by_css_selector('[value*="' + str(user) + '"]').click()
    time.sleep(2)
    driver.find_elements_by_css_selector('[d*="M5 4v2h14V4H5zm0 10h4v6h6v-6h4l-7-7-7 7z"]')[-1].click()
    time.sleep(2)
    data = driver.find_element_by_css_selector('[name*="checkupData.odometerData"]')
    temp = random.randint(840000,844000)
    data.send_keys(str(temp))
    time.sleep(2)
    driver.find_element_by_css_selector('[name*="checkupData.washed"]').click()
    elem = driver.find_elements_by_xpath("//div[@role='dialog']//span[@class='MuiButton-label']")[1]
    print(elem.text)
    webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
    time.sleep(4)
    elem_last = driver.find_element_by_css_selector('[class*="MuiButton-label"]')
    webdriver.ActionChains(driver).move_to_element(elem_last).click(elem_last).perform()
    time.sleep(5)
    driver.close()
    file_ = None
    for file in glob.glob("*.pdf"):
        file_ = file
    await send_file(id_user, file_)


