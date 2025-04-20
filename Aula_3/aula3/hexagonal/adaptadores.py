# adaptadores.py - Implementação da porta de acesso a dados
from dominio import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def save(self, user):
        self.users.append(user)
        print(f"Usuário {user.name} salvo com sucesso.")

