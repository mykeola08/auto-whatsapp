from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome(executable_path=r'C:\Users\Michael Oladimeji\Desktop\chromedriver.exe')
browser.get('web.whatsapp.com')

with open('contacts.txt', 'r', encoding='utf8') as f:
    contacts = [contact.strip() for contact in f.readlines()]

msg = ""
time.sleep(10)

for contact in contacts:
    search_box = browser.find_element('//div[@contenteditable="true"][@data-table="3"]')
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By))
    search_box.send_keys(contact)
