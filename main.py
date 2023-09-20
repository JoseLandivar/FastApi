from fastapi import FastAPI

app = FastAPI()

# Url local: http://127.0.0.1:8000
# Inicia el server: uvicorn main:app --reload
# Documentacion con Swagger: http://127.0.0.1:8000/docs
# Documantacion con Redocly: http://127.0.0.1:8000/redoc

@app.get("/")
async def root():
    return "Hola Fast API"

@app.get("/url")
async def url():
    return { "url_curso":"https://mouredev.com/python" } 
