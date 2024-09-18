from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Edge()

driver.get('https://estudante.ifpb.edu.br/cursos/')

select_monteiro = Select(driver.find_element(By.ID, 'id_cidade'))
select_modalidade = Select(driver.find_element(By.ID, 'id_modalidade'))

select_monteiro.select_by_visible_text('Monteiro/PB')

select_modalidade.select_by_visible_text('Presencial')

button_submit = driver.find_element(By.XPATH, '//*[@id="search_cursos"]/div[1]/button')

button_submit.click()

time.sleep(5)

curso = driver.find_element(By.XPATH, '//*[@id="conteudo"]/div[4]/div[1]/div/a')

curso.click()
