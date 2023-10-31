from selenium import webdriver


class ClientePage:
    def __init__(self, driver: webdriver):
        self.driver = driver()

    def acessarCadastro(self):
        self.driver.get("http://localhost:4200/clientes/create")
