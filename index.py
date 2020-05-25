from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import xlrd
import time

# Handle Excel File
workbook = xlrd.open_workbook('input.xlsx',encoding_override="cp1252")
sheet = workbook.sheet_by_index(0)
row = 0
input_array = []
while row<sheet.nrows:
    input_array.append((sheet.cell(row,0).value,float(sheet.cell(row,1).value)))
    row +=1
for data in input_array:
    print(data[0])
    print(data[1])
# Send message
chromedriver_location =r"C:\Users\DELL\Downloads\chromedriver"
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://www.instagram.com/')
facebook_login_button = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/button'
facebook_username = '//*[@id="email"]'
facebook_password = '//*[@id="pass"]'
facebook_login = '//*[@id="loginbutton"]'
notNow_button = '/html/body/div[4]/div/div/div[3]/button[2]'
inbox_page = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a'
vnntufoc = '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a'
input_textarea = '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'
send_button = '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button'
userName = "<your_facebook_username>"
password = "<your_facebook_password>"
WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, facebook_login_button))).click()
WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, facebook_username))).send_keys(userName)
WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, facebook_password))).send_keys(password)
WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, facebook_login))).click()
WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, notNow_button))).click()
WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, inbox_page))).click()
WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, vnntufoc))).click()
for data in input_array:
    for text in data[0]:
        driver.find_element_by_xpath(input_textarea).send_keys(text)
        time.sleep(0.1)
    driver.find_element_by_xpath(send_button).click()
    time.sleep(data[1])

