from selenium import webdriver
import time 


class WhatsAppBot:
    def __init__(self)
        self.mensagem = "tESTE"
        self.grupos =  [""]
        options = webdriver.ChromeOptions()
        options.add_argument("lan=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
    
    def EnviarMensagens(self):
        # <span dir="auto" title="POLÍCIA MALUCO" class="_1wjpf _3NFp9 _3FXB1">POLÍCIA MALUCO</span>
        # <div tabindex="-1" class="_1Plpp">
        # <span data-icon="send" class="">
        for grupo in self.grupos: 
                 grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
                 time.sleep(3)
                 grupo.click()
                 chat_box  =  self.driver.find_element_by_class_name('_1Plpp')
                 time.sleep(3)
                 chat_box.click()
                 chat_box.send_keys(self.mensagem)
                 botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                 time.sleep(3)
                 botao_enviar.click()
                 time.sleep(5)
