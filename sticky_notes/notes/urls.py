from django.urls import path
from .views import note_list, note_create, note_update, note_delete, note_view

urlpatterns = [
    # Displays a list of all notes
    path("", note_list, name="note_list"),
    # Allows users to create a new note
    path("new/", note_create, name="note_create"),
    # Enables users to edit an existing note by specifying its primary key
    path("<int:pk>/edit/", note_update, name="note_update"),
    # Allows users to delete a note by its primary key
    path("<int:pk>/delete/", note_delete, name="note_delete"),
    # Allows users to view notes
    path("<int:pk>/view/", note_view, name="note_view"),
]
