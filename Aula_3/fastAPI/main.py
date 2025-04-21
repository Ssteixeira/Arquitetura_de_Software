from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
users = []

@app.get("/users")
def get_users():
    return {"users": users}

@app.post("/users")
def create_user(name: str):
    users.append(name)
    return {"message": f"Usuário {name} criado com sucesso."}

client = TestClient(app)

def test_get_users():
    response = client.get("/users")
    print("GET /users response:", response.json())


def test_create_user():
    response = client.post("/users?name=Sabrinna")
    print("POST /users response:", response.json())

if __name__ == "__main__":
    test_get_users()
    test_create_user()
    test_get_users()   