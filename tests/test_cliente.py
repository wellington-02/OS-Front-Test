import time

from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = Firefox()
browser.maximize_window()


class TestCliente:

    def test_cancelButton_returnsEnebledButton_whenPageCreateIsAccessed(self):
        browser.get("http://localhost:4200/clientes/create")
        time.sleep(0.5)

        button = browser.find_element(By.ID, "cancelar")
        time.sleep(0.5)

        assert button.is_enabled() is True
        time.sleep(0.5)

        browser.quit()

    def test_createCliente_returnsClienteCadastrado_whenSuccessful(self):
        browser.get("http://localhost:4200/clientes/create")
        time.sleep(0.5)

        browser.find_element(By.ID, "mat-input-0").send_keys("teste")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-1").send_keys("926.076.200-66")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-2").send_keys("(88) 98545-3685")
        time.sleep(0.5)
        browser.find_element(By.ID, "criarCliente").click()
        time.sleep(0.5)
        message = browser.find_element(By.CLASS_NAME, "mat-mdc-snack-bar-label")
        time.sleep(0.5)

        expectMessage = "Cliente criado com sucesso!"
        time.sleep(0.5)

        assert expectMessage in message.text
        time.sleep(0.5)

        browser.quit()

    def test_createCliente_returnsClienteJaCadastrado_whenCpfIsAlreadyRegistred(self):
        browser.get("http://localhost:4200/clientes/create")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-0").send_keys("teste2")
        time.sleep(0.4)
        browser.find_element(By.ID, "mat-input-1").send_keys("926.076.200-66")
        time.sleep(0.4)
        browser.find_element(By.ID, "mat-input-2").send_keys("(88) 98545-3685")
        time.sleep(0.4)
        browser.find_element(By.ID, "criarCliente").click()
        time.sleep(0.4)
        message2 = browser.find_element(By.CLASS_NAME, "mat-mdc-snack-bar-label")
        time.sleep(0.5)

        expectMessage2 = "CPF já cadastrado na base de dados!"
        time.sleep(0.5)

        assert expectMessage2 in message2.text
        time.sleep(0.5)

        browser.quit()

    def test_createCliente_returnsDisabledButton_whenNomeHasLessThan5Characters(self):
        browser.get("http://localhost:4200/clientes/create")
        time.sleep(0.5)

        browser.find_element(By.ID, "mat-input-0").send_keys("test")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-1").send_keys("926.076.200-66")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-2").send_keys("(88) 98545-3685")
        time.sleep(0.5)

        button = browser.find_element(By.ID, "criarCliente")
        time.sleep(0.5)

        assert button.is_enabled() is False
        time.sleep(0.5)

        browser.quit()

    def test_createCliente_returnsDisabledButton_whenCpfHasLessThan11Characters(self):
        browser.get("http://localhost:4200/clientes/create")
        time.sleep(0.5)

        browser.find_element(By.ID, "mat-input-0").send_keys("teste")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-1").send_keys("0123456789")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-2").send_keys("(88) 98545-3685")
        time.sleep(0.5)

        button = browser.find_element(By.ID, "criarCliente")
        time.sleep(0.5)

        assert button.is_enabled() is False
        time.sleep(0.5)

        browser.quit()

    def test_createCliente_returnsdisabledButton_whenTelefoneHasLessThan11Characters(self):
        browser.get("http://localhost:4200/clientes/create")
        time.sleep(0.5)

        browser.find_element(By.ID, "mat-input-0").send_keys("teste")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-1").send_keys("926.076.200-66")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-2").send_keys("0123456789")
        time.sleep(0.5)

        button = browser.find_element(By.ID, "criarCliente")
        time.sleep(0.5)

        assert button.is_enabled() is False
        time.sleep(0.5)

        browser.quit()

    def test_createCliente_returnsCpfInvalido_whenCpfIsNotValid(self):
        browser.get("http://localhost:4200/clientes/create")
        time.sleep(0.5)

        browser.find_element(By.ID, "mat-input-0").send_keys("teste")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-1").send_keys("000.000.000-00")
        time.sleep(0.5)
        browser.find_element(By.ID, "mat-input-2").send_keys("(88) 98545-3685")
        time.sleep(0.5)
        browser.find_element(By.ID, "criarCliente").click()
        time.sleep(0.5)
        message = browser.find_element(By.CLASS_NAME, "mat-mdc-snack-bar-label")
        time.sleep(0.5)

        expectMessage = "CPF inválido"
        time.sleep(0.5)

        assert expectMessage in message.text
        time.sleep(0.5)

        browser.quit()

    def test_updateCliente_returnsClienteAtualizado_whenSuccessful(self):
        browser.get("http://localhost:4200/clientes")
        time.sleep(1)
        browser.find_element(By.ID, "edit").click()
        time.sleep(1)
        nome = browser.find_element(By.ID, "mat-input-0")
        time.sleep(1)
        nome.click()
        time.sleep(1)
        nome.send_keys("testado")
        time.sleep(1)
        browser.find_element(By.ID, "atualizar").click()
        time.sleep(1)
        UpdateMessage = browser.find_element(By.CLASS_NAME, "mat-mdc-snack-bar-label")
        time.sleep(1)

        expectMessage = "Cliente atualizado com sucesso!"
        time.sleep(1)

        assert expectMessage in UpdateMessage.text
        time.sleep(1)

        browser.quit()

    def test_cancelButton_returnsEnebledButton_whenPageDeleteIsAccessed(self):
        browser.get("http://localhost:4200/clientes")
        time.sleep(0.5)

        browser.find_element(By.ID, "delete").click()
        time.sleep(0.5)

        button = browser.find_element(By.ID, "cancelarDelete")
        time.sleep(0.5)

        assert button.is_enabled() is True
        time.sleep(0.5)

        browser.quit()

    def test_deleteCliente_returnsClienteDeletado_whenSuccessful(self):
        browser.get("http://localhost:4200/clientes")
        time.sleep(0.5)

        browser.find_element(By.ID, "delete").click()
        time.sleep(0.5)
        browser.find_element(By.ID, "deletar").click()
        time.sleep(0.5)
        message = browser.find_element(By.CLASS_NAME, "mat-mdc-snack-bar-label")
        time.sleep(0.5)

        expectMessage = "Cliente deletado com sucesso!"
        time.sleep(0.5)

        assert expectMessage in message.text
        time.sleep(0.5)

        browser.quit()