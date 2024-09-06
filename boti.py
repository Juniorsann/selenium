from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

try:
    for _ in range(500):
        time.sleep(5)
        
        print("Esperando o botão de pesquisa...")
        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div[2]/div[3]/button[1]')))
        print("Botão de pesquisa encontrado.")
        search_button.click()
        print("Botão de pesquisa clicado.")


except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

