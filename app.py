# import of libraries
import fastapi # pip install fastapi
# import of files
import database
import pydantic_models
import config

api = fastapi.FastAPI()

# Ответы на GET апросы, что указаны в декораторах

@api.get('/static/path')
def hello():
    return "hello"

@api.get('/user/{nick}') # Пер. в пути
def get_nick(nick):
    return {"user":nick}

@api.get('/userid/{id:int}') # Пер. с заданным типом данных
def get_id(id):
    return {"user":id}

@api.get('/test/{id:int}/{text:str}/{custom_path:path}') # Несколько пер. в запросе # http://127.0.0.1:8000/test/24/gleb/my/path
def get_test(id, text, custom_path):
    return {"id":id,
            "":text,
            "custom_path": custom_path}

# Для запуска сервера:
# uvicorn app:api --reload

