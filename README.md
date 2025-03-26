# python-notebook-manager
Notebook manager implemented in Python with editing, deletion, and storage capabilities in a binary format.

## Version 2.0: Object-Oriented Implementation

This Python program now uses an object-oriented approach to implement a simple notebook, enhancing code structure, readability, and maintainability. It continues to utilize the pickle module to save and load data in a bitwise mode.

### Key Features:
- Read the Notebook (Option 1):
  Displays existing notes stored in the notebook.

- Add Note (Option 2):
  Allows the user to add a new note with a timestamp.

- Edit a Note (Option 3):
  Enables the user to edit an existing note by selecting its index.

- Delete a Note (Option 4):
  Permits the deletion of a note by selecting its index.

- Save and Quit (Option 5):
  Saves the current notebook to a file and exits the program.

### What's New in Version 2.0:
- Implemented using Object-Oriented Programming (OOP) principles
- Improved code modularity and encapsulation
- Enhanced error handling
- More organized and maintainable codebase

### Instructions:
- When the program starts, it checks for a notebook data file ("notebook.dat").
- If the file exists, it loads the existing notebook; otherwise, it creates a new one.
- Editing and deleting notes involve selecting the note by its index in the list.
- The program provides feedback on operations like creating a new notebook or deleting a note.
- The notebook is saved automatically when the user chooses to quit.

### Prerequisites:
- Python 3.x installed on your system
- Download Python from: https://www.python.org/downloads/

### Usage:
Run the program in the command prompt (terminal):
```
python notebook_v2_oop.py
# or
py notebook_v2_oop.py
```

Follow the on-screen menu to perform notebook operations.

### Version History:
- v1.0: Initial procedural implementation
- v2.0: Object-oriented refactoring with improved structure

### Note:
This program serves as an educational exercise in Python programming, demonstrating the evolution from procedural to object-oriented design.
