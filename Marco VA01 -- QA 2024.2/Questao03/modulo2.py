import re

class EmailService:
    def enviar_email(self, email):
        if email is None or not re.match(r'^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$', email):
            raise ValueError("Email inválido")
        # Lógica para enviar o email
