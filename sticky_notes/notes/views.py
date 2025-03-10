from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    Display a list of all notes.

    Retrieves all Note objects from the database, passing them
    to the 'note_list.html' template for rendering.
    """

    notes = Note.objects.all()
    return render(request, "notes/note_list.html", {"notes": notes})


def note_create(request):
    """
    Create a new note.

    - If the request method is POST, validate and save the form data.
    - If valid, redirect to the note list view.
    - If not POST, display an empty form.

    Renders 'note_form.html' with the form.
    """

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """
    Update an existing note.

    - Brings the note by primary key (pk).
    - If POST, updates the note with form data and saves it.
    - If GET, pre-fills the form with the existing note data.

    Renders 'note_form.html' with the form.
    """

    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """
    Delete an existing note.

    - Brings the note by primary key (pk).
    - If POST, deletes the note and redirects to the note list.
    - If GET, displays a confirmation page before deletion.

    Renders 'note_confirm_delete.html' with the note.
    """

    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})
