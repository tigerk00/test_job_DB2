from django.db import models
from .custom_validators import validate_email, validate_message

class Message(models.Model):
    author = models.CharField(verbose_name='Автор', db_index=True, max_length=64)
    email = models.EmailField(verbose_name='Емейл', max_length=64, validators=[validate_email])
    text = models.CharField(verbose_name='Текст сообщения', max_length=100, validators=[validate_message])
    create_date = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Время обновления', auto_now=True)

    def __str__(self):
        return f"[{self.pk}] {self.author} - {self.text[:6]}..."

    class Meta:
        ordering = ['-pk']