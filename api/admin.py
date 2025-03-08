from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "is_read", "is_secret")
    list_filter = ("is_read", "is_secret")
    search_fields = ("text",)
    ordering = ("id",)
