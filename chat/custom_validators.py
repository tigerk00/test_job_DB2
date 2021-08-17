from django.core.exceptions import ValidationError
import re

def validate_message(value):
    if len(value) < 100 and value != "":
        return value
    else:
        raise ValidationError("Сообщение не должно быть пустым, и его длина не должна превышать 100 символов")


def validate_email(value):
    email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    if len(value) > 7:
        if re.match(email_regex, value):
            return value
    raise ValidationError("Введите корректный емейл")
