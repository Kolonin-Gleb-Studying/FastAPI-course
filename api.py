import fastapi
import database # Импорт папки
import pydantic_models
import config

api = fastapi.FastAPI()

# Словарь вида:
# ключ: список (словарей)
fake_database = {'users':[

    {
        "id":1,             # число
        "name":"Anna",      # строка
        "nick":"Anny42",    # строка
        "balance": 15300    # int
     },

    {
        "id":2,             # число
        "name":"Dima",      # строка
        "nick":"dimon2319", # строка
        "balance": 160.23   # float
     }
    ,{
        "id":3,             # число
        "name":"Vladimir",  # строка
        "nick":"Vova777",   # строка
        "balance": "25000"     # строка - НЕВЕРНО
     }
],}

@api.get('/get_info_by_user_id/{id:int}')
def get_info_about_user(id):
    return fake_database['users'][id-1]

@api.get('/get_user_balance_by_id/{id:int}')
def get_info_about_user(id):
    return fake_database['users'][id-1]['balance']

@api.get('/get_total_balance')
def get_info_about_user():
    total_balance: float = 0.0
    for user in fake_database['users']:
        # Pydantic валидация, чтобы данные в неверном формате (иной тип) приводились к нужному согласно описанной модели
        total_balance += pydantic_models.User(**user).balance
    return total_balance

# Запуск сервера:
# uvicorn api:api --reload
