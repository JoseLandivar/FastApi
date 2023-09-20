from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/usersjson")
async def usersjson():
    return [{ "name": "Brais", "surname": "Moure" , "url": "https://moure.dev", "age": 35},
            { "name": "Jose", "surname": "Landivar" , "url": "https://jose.dev", "age": 27},
            { "name": "Sergio", "surname": "Apuri" , "url": "https://sergio.dev", "age": 25 }]

# Inicia el server: uvicorn users:app --reload

# Entidad User

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id = 1,name = "Brais",surname = "Moure",url = "https://moure.dev",age = 35),
         User(id = 2,name = "Jose",surname = "Landivar",url = "https://jose.dev", age = 27),
         User(id = 3,name = "Sergio",surname = "Landivar",url = "https://sergio.dev",age =  25)]

@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#Query
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "Nose ha encontrado el usuario"}