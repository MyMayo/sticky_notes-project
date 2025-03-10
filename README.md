Sticky Notes

A simple Django application managing sticky notes allowing users to:
  
    Create new notes
    View all notes
    Edit existing notes
    Delete notes

Requirements:

    Python 3.x
    Django 5.x

Installation:
1, Copy or download the repository files
2, Navigate project directory in CMD:
    cd your/project/path
3, Set up a virtual environment and activate it:
    python -m venv myenv
    myenv\Scripts\activate  #For Windows
    source myenv/bin/activate  #For Linux
4, Install dependencies: 
    pip install -r requirements.txt
5, Apply the migration:
    python manage.py migrate
6, Run the server:
    python manage.py runserver
7, Open your browser:
    http://127.0.0.1:8000/

Testing:
    python manage.py test

