# Forms

## Установка приложения
```
1.git clone Репозиторий проекта
2.python3 -m venv venv
3.Windows - .\venv\Scripts\activate / Linux - source venv/bin/activate
4.pip install -r requirements.txt
```

## Запуск приложения
Для запуска FastAPI используется веб-сервер uvicorn. Команда для запуска выглядит так:  
```
uvicorn main:app --reload
```

### Тесты(В роли тестового скрипта)
```
- В корне проекта: pytest
```

### Документация
```
- http://IP/docs#/
```

### Стек
```
Python 3.7, FastApi, tinyDB, Tests.
```
