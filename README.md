# Forms

## Краткое ТЗ
```
Входные данные для веб-приложения:
Список полей со значениями в теле POST запроса.

Выходные данные:
- Имя наиболее подходящей данному списку полей формы
- При отсутствии совпадений с известными формами произвести типизацию полей на лету и вернуть список полей с их типами.

```

## Запуск приложения
Для запуска FastAPI используется веб-сервер uvicorn. Команда для запуска выглядит так:  
```
uvicorn main:app --reload
```

### Тесты
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
