# camada_de_dados.py
class Database:
    def __init__(self):
        self.data = {"users": ["Raffael", "Filipe", "Joao", "Ariane"]}

    def get_users(self):
        return self.data["users"]