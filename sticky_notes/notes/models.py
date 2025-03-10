from django.db import models


class Note(models.Model):
    """
    Represents a Sticky Note in the application.

    Attributes:
        title (str): The title of the note (max length: 255 characters).
        content (str): The main content of the note.
        created_at (datetime): Timestamp indicating when the note was created.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Returns s string of the title of the note
    def __str__(self):
        return self.title
