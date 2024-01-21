# python-notebook-manager
Notebook manager implemented in Python with editing, deletion, and storage capabilities in a binary format.

This Python program implements a simple notebook using a list data structure for note manipulation. It utilizes the pickle module to save and load data in a bitwise mode. The notebook has the following features:

Read the Notebook (Option 1):

Displays existing notes stored in the notebook.
Add Note (Option 2):

Allows the user to add a new note with a timestamp.
Edit a Note (Option 3):

Enables the user to edit an existing note by selecting its index in the list.
Delete a Note (Option 4):

Permits the deletion of a note by selecting its index in the list.
Save and Quit (Option 5):

Saves the current notebook to a file ("notebook.dat") and exits the program.
Instructions:
When the program starts, it checks for a notebook data file ("notebook.dat").
If the file exists, it loads the existing notebook; otherwise, it creates a new one.
Editing and deleting notes involve selecting the note by its index in the list.
The program notifies the user of successful operations, such as creating a new notebook or deleting a note.
The notebook is saved automatically when the user chooses to quit.
Usage:
Run the program and follow the on-screen menu to perform notebook operations.
Note:
This program is designed to be a comprehensive exercise, implementing concepts learned throughout the procedural programming course.
