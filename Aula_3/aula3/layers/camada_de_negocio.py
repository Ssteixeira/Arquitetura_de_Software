# camada_de_negocio.py
from camada_de_dados import Database
class UserService:
    def __init__(self):
        self.db = Database()
    def list_users(self):
        # Regras de negócio, validações, etc.
        return self.db.get_users()