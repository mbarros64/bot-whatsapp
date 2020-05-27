# -*- Coding: UTF-8 -*-
#coding: utf-8
from selenium import webdriverp
import time 


class WhatsAppBot:
    def __init__(self):
        self.mensagem = "wirley eh gay"
        self.grupos =  [""]
        options = webdriver.ChromeOptions()
        options.add_argument("lan=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver',  chrome_options=options)
        # <span dir="auto" title="POLÍCIA MALUCO" class="_1wjpf _3NFp9 _3FXB1">POLÍCIA MALUCO</span>#
        # <div tabindex="-1" class="_1Plpp">#
        # <span data-icon="send" class="">#
        def EnviarMensagens(self):
            self.driver.get('https://web.whatsapp.com')
            time.sleep(30)
            for grupo_ou_pessoa in self.grupos_ou_pessoas:
                campo_grupo = self.driver.find_element_by_xpath(
                    f"//span[@title='{grupo_ou_pessoa}']")
                time.sleep(3)
                campo_grupo.click()
                chat_box = self.driver.find_element_by_class_name('_13mgZ')
                time.sleep(3)
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element_by_xpath(
                    "//span[@data-icon='send']")
                time.sleep(3)
                botao_enviar.click()
                time.sleep(5)



bot = WhatsAppBot()
bot.EnviarMensagens()