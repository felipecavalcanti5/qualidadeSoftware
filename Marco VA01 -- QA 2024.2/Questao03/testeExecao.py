import pytest
from modulo2 import EmailService  # Substitua 'seu_modulo' pelo nome do seu arquivo

def test_enviar_email_com_email_invalido():
    email_service = EmailService()

    # Verifica se a ValueError é lançada para email inválido
    with pytest.raises(ValueError, match="Email inválido"):
        email_service.enviar_email("emailinvalido")  # email sem "@"

    with pytest.raises(ValueError, match="Email inválido"):
        email_service.enviar_email(None)  # email nulo

    with pytest.raises(ValueError, match="Email inválido"):
        email_service.enviar_email("alguma_coisa@hotmail.com")

    with pytest.raises(ValueError, match="Email inválido"):
        email_service.enviar_email(" ")  # email em branco

