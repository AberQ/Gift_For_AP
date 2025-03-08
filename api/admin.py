from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_read', 'is_secret', 'photo')  # Поля для отображения в списке
    list_filter = ('is_read', 'is_secret')  # Фильтры по этим полям
    search_fields = ('text',)  # Поиск по тексту заметки
    list_per_page = 20  # Количество элементов на странице в списке

admin.site.register(Note, NoteAdmin)
