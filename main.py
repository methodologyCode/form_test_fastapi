import datetime
import re

from fastapi import FastAPI
from pydantic import BaseModel
from tinydb import TinyDB


class FormData(BaseModel):
    email: str
    phone: str
    date: str
    text: str


app = FastAPI()
db = TinyDB('forms_db.json')
forms_table = db.table('forms')


@app.post("/get_form")
def main(form_data: FormData):
    # Поиск шаблона формы в базе данных
    form_data = form_data.model_dump()
    matching_forms = forms_table.storage.read()['forms']

    for form in matching_forms:
        match = all([
            form["email"] == form_data["email"],
            form["date"] == form_data["date"],
            form["phone"] == form_data["phone"],
            form["text"] == form_data["text"]
        ])

        if match:
            return {"form_template_name": form['name']}

    # Если подходящего шаблона нет, производим типизацию полей на лету
    field_types = {}
    if validate_date(form_data["date"]):
        field_types['date'] = 'date'
    if validate_phone(form_data["phone"]):
        field_types['phone'] = 'phone'
    if validate_email(form_data["email"]):
        field_types['email'] = 'email'
    if form_data["text"]:
        field_types['text'] = 'text'

    return field_types


def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False


def validate_phone(phone):
    phone_pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    return bool(phone_pattern.match(phone))


def validate_email(email):
    email_pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_pattern.match(email))
