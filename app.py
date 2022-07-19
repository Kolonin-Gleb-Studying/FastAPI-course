# import of libraries
import fastapi # pip install fastapi
# import of files
import database
import pydantic_models
import config

api = fastapi.FastAPI()

response = {"Ответ":"Который возвращает сервер"}

# Ответы на GET апросы, что указаны в декораторах

@api.get('/')
def index():
    return response

@api.get('/hello')
def hello():
    return "hello"

@api.get('/about/us')
def about():
    return {"We Are":"Legion"}

# Ввести команды в терминале проекта
# pip install uvicorn
# uvicorn app:api --reload

