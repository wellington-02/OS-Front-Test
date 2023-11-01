from selenium import webdriver
from selenium.webdriver.common.by import By


class ClientePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def acessarCadastro(self):
        self.driver.get("http://localhost:4200/clientes/create")

    def acessarHomePage(self):
        self.driver.get("http://localhost:4200/clientes")

    def botaoCancelarCadastro(self):
        return self.driver.find_element(By.ID, "cancelar")

    def botaoCriarCliente(self):
        return self.driver.find_element(By.ID, "criarCliente")

    def botaoAtualizarCliente(self):
        return self.driver.find_element(By.ID, "atualizar")

    def botaoEditarCliente(self):
        return self.driver.find_element(By.ID, "edit")

    def botaoDeletarCliente(self):
        return self.driver.find_element(By.ID, "deletar")

    def botaoDeleteCliente(self):
        return self.driver.find_element(By.ID, "delete")

    def botaoCancelarDelete(self):
        return self.driver.find_element(By.ID, "cancelarDelete")

    def fecharNavegador(self):
        self.driver.quit()

    def nomeClicar(self):
        self.driver.find_element(By.ID, "mat-input-0").click()

    def nome(self, nome):
        self.driver.find_element(By.ID, "mat-input-0").send_keys(nome)

    def cpf(self, cpf):
        self.driver.find_element(By.ID, "mat-input-1").send_keys(cpf)

    def telefone(self, telefone):
        self.driver.find_element(By.ID, "mat-input-2").send_keys(telefone)

    def mensagem(self):
        return self.driver.find_element(By.CLASS_NAME, "mat-mdc-snack-bar-label")
