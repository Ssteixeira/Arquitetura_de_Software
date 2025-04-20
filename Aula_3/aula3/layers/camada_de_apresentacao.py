# camada_de_apresentacao.py
from camada_de_negocio import UserService
def main():
    service = UserService()
    users = service.list_users()
    print("Lista de usuários:", users)
if __name__ == "__main__":
    main()