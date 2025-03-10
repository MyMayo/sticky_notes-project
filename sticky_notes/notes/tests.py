from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note", content="This is a test note."
        )

    def test_note_creation(self):
        """Test that the note is created correctly"""
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test note.")

class NoteViewsTest(TestCase):
    def test_notes_list_view(self):
        """Test that the notes list view returns a 200 status code"""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_note_view(self):
        """Test that we can create a note"""
        response = self.client.post(
            reverse('note_create'),
            {'title': 'New Note', 'content': 'Some content'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Note.objects.count(), 1)

