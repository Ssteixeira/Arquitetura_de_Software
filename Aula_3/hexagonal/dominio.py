# dominio.py - Lógica de negócio pura
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user: User):
        raise NotImplementedError

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register_user(self, name: str):
        user = User(name)
        self.repository.save(user)
        return user