import time

import pytest
from selenium import webdriver

from util.cliente import ClientePage

@pytest.fixture(scope="module")
def web_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def cliente(web_driver):
    cliente_page = ClientePage(web_driver)
    yield cliente_page


class TestCliente:

    def test_cancelButton_returnsEnebledButton_whenPageCreateIsAccessed(self, cliente):
        cliente.acessarCadastro()
        time.sleep(0.5)

        button = cliente.botaoCancelarCadastro()
        time.sleep(0.5)

        assert button.is_enabled() is True

    def test_createCliente_returnsClienteCadastrado_whenSuccessful(self, cliente):
        cliente.acessarCadastro()

        time.sleep(0.5)

        cliente.nome("teste")
        time.sleep(0.5)
        cliente.cpf("926.076.200-66")
        time.sleep(0.5)
        cliente.telefone("(88) 98545-3685")
        time.sleep(0.5)
        cliente.botaoCriarCliente().click()
        time.sleep(2)
        mensagem = cliente.mensagem()

        mensagemEsperada = "Cliente criado com sucesso!"

        assert mensagemEsperada in mensagem.text

    def test_createCliente_returnsClienteJaCadastrado_whenCpfIsAlreadyRegistred(self, cliente):
        cliente.acessarCadastro()
        time.sleep(0.5)
        cliente.nome("teste2")
        time.sleep(0.4)
        cliente.cpf("926.076.200-66")
        time.sleep(0.4)
        cliente.telefone("(88) 98545-3685")
        time.sleep(0.4)
        cliente.botaoCriarCliente().click()
        time.sleep(2)
        mensagem2 = cliente.mensagem()

        mensagemEsperada2 = "CPF já cadastrado na base de dados!"

        assert mensagemEsperada2 in mensagem2.text

    def test_createCliente_returnsDisabledButton_whenNomeHasLessThan5Characters(self, cliente):
        cliente.acessarCadastro()
        time.sleep(0.5)
        cliente.nome("test")
        time.sleep(0.5)
        cliente.cpf("926.076.200-66")
        time.sleep(0.5)
        cliente.telefone("(88) 98545-3685")
        time.sleep(0.5)
        botao = cliente.botaoCriarCliente()
        time.sleep(0.5)

        assert botao.is_enabled() is False

    def test_createCliente_returnsDisabledButton_whenCpfHasLessThan11Characters(self, cliente):
        cliente.acessarCadastro()
        time.sleep(0.5)

        cliente.nome("teste")
        time.sleep(0.5)
        cliente.cpf("0123456789")
        time.sleep(0.5)
        cliente.telefone("(88) 98545-3685")
        time.sleep(0.5)
        botao = cliente.botaoCriarCliente()
        time.sleep(0.5)

        assert botao.is_enabled() is False

    def test_createCliente_returnsdisabledButton_whenTelefoneHasLessThan11Characters(self, cliente):
        cliente.acessarCadastro()
        time.sleep(0.5)

        cliente.nome("teste")
        time.sleep(0.5)
        cliente.cpf("926.076.200-66")
        time.sleep(0.5)
        cliente.telefone("0123456789")
        time.sleep(0.5)
        button = cliente.botaoCriarCliente()
        time.sleep(0.5)

        assert button.is_enabled() is False

    def test_createCliente_returnsCpfInvalido_whenCpfIsNotValid(self, cliente):
        cliente.acessarCadastro()
        time.sleep(0.5)

        cliente.nome("teste")
        time.sleep(0.5)
        cliente.cpf("000.000.000-00")
        time.sleep(0.5)
        cliente.telefone("(88) 98545-3685")
        time.sleep(0.5)
        cliente.botaoCriarCliente().click()
        time.sleep(2)
        mensagem = cliente.mensagem()

        mensagemEsperada = "CPF inválido"

        assert mensagemEsperada in mensagem.text

    def test_updateCliente_returnsClienteAtualizado_whenSuccessful(self, cliente):
        cliente.acessarHomePage()
        time.sleep(1)
        cliente.botaoEditarCliente().click()
        time.sleep(1)
        cliente.nomeClicar()
        time.sleep(1)
        cliente.nome("testado")
        time.sleep(1)
        cliente.botaoAtualizarCliente().click()
        time.sleep(2)
        mensagem = cliente.mensagem()

        mensagemEsperada = "Cliente atualizado com sucesso!"

        assert mensagemEsperada in mensagem.text

    def test_cancelButton_returnsEnebledButton_whenPageDeleteIsAccessed(self, cliente):
        cliente.acessarHomePage()
        time.sleep(0.5)
        cliente.botaoDeleteCliente().click()
        time.sleep(2)
        botao = cliente.botaoCancelarDelete()
        time.sleep(0.5)

        assert botao.is_enabled() is True

    def test_deleteCliente_returnsClienteDeletado_whenSuccessful(self, cliente):
        cliente.acessarHomePage()
        time.sleep(0.5)
        cliente.botaoDeleteCliente().click()
        time.sleep(0.5)
        cliente.botaoDeletarCliente().click()
        time.sleep(2)
        mensagem = cliente.mensagem()

        mensagemEsperada = "Cliente deletado com sucesso!"

        assert mensagemEsperada in mensagem.text
