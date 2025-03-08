from django.db import models

from django.db import models

class Note(models.Model):
    text = models.TextField(verbose_name="Текст заметки")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")
    is_secret = models.BooleanField(default=False, verbose_name="Секретная")

    def __str__(self):
        return f"{'🔒 ' if self.is_secret else ''}{self.text[:20]}..."
