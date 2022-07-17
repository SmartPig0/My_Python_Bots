# Aqui vamos fazer um robô que acessa o instagram, procura uma hastag e curte as fotos da página.
# Começamos instalando o selenium na máquina pip intall selenium
# Instalar o geckodriver neste link: https://github.com/mozilla/geckodriver/releases/tag/v0.31.0
# Instalar o Pycharm.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = 'username'
        self.password = 'password'
        self.driver = webdriver.Firefox(
            executable_path=r'C:\Users\Felipe\Desktop\Estudos Python\my_first_robot\geckodriver\geckodriver.exe')
    # //input[@name="username"]
    # //input[@name="password"]

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(5)
        user_element = driver.find_element(
            By.XPATH, "//input[@name='username']")
        user_element.click()
        user_element.clear()
        user_element.send_keys(self.username)
        user_password = driver.find_element(
            By.XPATH, "//input[@name='password']")
        user_password.clear()
        user_password.send_keys(self.password)
        time.sleep(2)
        user_password.send_keys(Keys.ENTER)
        time.sleep(5)
        self.curtir_fotos('pikachu')
        time.sleep(2)
        hastag_foto = driver.find_element(By.CLASS_NAME, '_aagw')
        hastag_foto.click()
        time.sleep(5)
        i = 0
        while i <= 5:
            curtir_foto = driver.find_element(By.CLASS_NAME, '_aamw')
            curtir_foto.click()
            time.sleep(2)
            proxima_pagina = driver.find_element(By.CLASS_NAME, '_abl-')
            proxima_pagina.send_keys(Keys.ARROW_RIGHT)
            time.sleep(5)
            i += 1
# Aqui fazemos uma função para acessar a hastag selecionada

    def curtir_fotos(self, hastag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hastag + '/')
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            i += 1


# Fazendo instanciamento do código
myInstaRobot = InstagramBot('username', 'password')
myInstaRobot.login()
