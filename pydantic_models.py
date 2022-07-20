import pydantic # Для валидации данных

# Модель пользователя, по которой fastAPI будет валидировать данные

class User(pydantic.BaseModel):
    id: int
    name: str
    nick: str
    balance: float



