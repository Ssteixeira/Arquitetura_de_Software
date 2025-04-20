
# main.py - Integração entre núcleo e adaptadores
from dominio import UserService
from adaptadores import InMemoryUserRepository

def main():
    repository = InMemoryUserRepository()
    service = UserService(repository)
    service.register_user("Sabrinna")
    service.register_user("Joao")

if __name__ == "__main__":
    main()