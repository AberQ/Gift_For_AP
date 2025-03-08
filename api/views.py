from django.shortcuts import render
from .models import Note
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def note_list(request):
    notes = Note.objects.all()
    return render(request, "note_list.html", {"notes": notes})

def mark_note_read(request, note_id):
    if request.method == "POST":
        note = get_object_or_404(Note, id=note_id)
        note.is_read = True
        note.save()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)


def toggle_note_read(request, note_id):
    if request.method == "POST":
        note = get_object_or_404(Note, id=note_id)
        note.is_read = not note.is_read  
        note.save()
        return JsonResponse({"success": True, "is_read": note.is_read})
    return JsonResponse({"success": False}, status=400)