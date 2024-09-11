from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()

driver.get('https://forms.gle/7rjszTDJGzSQeS9i8')
time.sleep(2)

element_nome = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
element_sobre_nome = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
element_email = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
actions = ActionChains(driver)

actions.send_keys_to_element(element_nome, 'Wandeilson')
actions.pause(1)
actions.send_keys_to_element(element_sobre_nome, 'Gomes da Silva')
actions.pause(1)
actions.send_keys_to_element(element_email, 'wandeilson.silva@academico.ifpb.edu.br')
actions.pause(1)

element_texto = driver.find_element(By.XPATH, '//*[@id="i13"]/span[1]/div[2]')
time.sleep(1)
texto_copiado = element_texto.text

time.sleep(1)

element_input_texto = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
time.sleep(1)
actions.send_keys_to_element(element_input_texto, texto_copiado)
actions.pause(1)

div_opcoes1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div')

div_opcoes_radio = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div'


opcao_1 = driver.find_element(By.XPATH, "//span[contains(text(), 'opção 1')]")
opcao_3 = driver.find_element(By.XPATH, "//span[contains(text(), 'opção 3')]")

radio_opcao_4 = driver.find_element(By.XPATH, f"{div_opcoes_radio}//span[contains(text(), 'opção 4')]")

actions.click(opcao_1)
actions.pause(1)
actions.click(opcao_3)
actions.pause(1)
actions.click(radio_opcao_4)
actions.pause(1)

botao_prox = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
actions.pause(1)
actions.click(botao_prox)
actions.pause(1)
actions.perform()
########## SEGUNDA PAGINA ###########
time.sleep(1)
actions = ActionChains(driver)
element_texto_2pagina = driver.find_element(By.XPATH, '//*[@id="i1"]/span[1]/div[2]')

texto_copiado2 = element_texto_2pagina.text

element_input_texto2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
actions.pause(1)
actions.send_keys_to_element(element_input_texto2, texto_copiado2)
actions.pause(1)
opcao_2 = driver.find_element(By.XPATH, "//span[contains(text(), 'opção 2')]")
opcao_4 = driver.find_element(By.XPATH, "//span[contains(text(), 'opção 4')]")

div_opcoes_radio2 =  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div'

radio_opcao_1 = driver.find_element(By.XPATH, f"{div_opcoes_radio2}//span[contains(text(), 'opção 1')]")

actions.click(opcao_2)
actions.pause(1)
actions.click(opcao_4)
actions.pause(1)
actions.click(radio_opcao_1)
actions.pause(1)

botao_enviar = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
actions.pause(5)
actions.click(botao_enviar)
actions.perform()

time.sleep(5)

driver.quit()