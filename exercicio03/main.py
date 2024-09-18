from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()

driver.get('https://estudante.ifpb.edu.br')
links = driver.find_elements(By.TAG_NAME, 'a')
print("links", links)
count_link_validos = 0
for link in links:
    try:
        if(requests.head(link.get_attribute('href'), timeout=3).status_code < 400):
            count_link_validos = count_link_validos + 1
            print("Link válido", link.get_attribute('href'))
        else:
            print("Link quebrado", link.get_attribute('href'))
    except Exception as e:
        print(e)
print("Total de links válidos:", count_link_validos)
