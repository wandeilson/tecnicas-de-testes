from selenium import webdriver
import time
driver = webdriver.Chrome()
time.sleep(2)
driver.get('https://google.com')
time.sleep(2)
driver.get('https://facebook.com')
time.sleep(2)
driver.get('https://stackoverflow.com')
time.sleep(2)
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.maximize_window()
time.sleep(2)

tamanho = driver.get_window_size()
time.sleep(2)
print(tamanho)
time.sleep(2)
driver.quit()