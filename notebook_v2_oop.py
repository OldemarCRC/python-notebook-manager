import time
import pickle

class Notebook:
    def __init__(self, file_name="notebook.dat"):
        self.file_name = file_name
        self._check_file()

    def _check_file(self):
        """Internal method to check and create file if it doesn't exist."""
        try:
            with open(self.file_name, "rb") as file_to_check:
                pass

        except FileNotFoundError:
            with open(self.file_name, "wb") as file_to_check:
                pickle.dump([], file_to_check)
                print("No default notebook was found, created one.")

    def _load_notes(self):
        """Load notes from the file."""
        with open(self.file_name, "rb") as file_to_check:
            return pickle.load(file_to_check)

    def _save_notes(self, notes):
        """Save notes to the file."""
        with open(self.file_name, "wb") as file_to_check:
            pickle.dump(notes, file_to_check)

    def read_notes(self):
        """Read and display all notes."""
        notes = self._load_notes()
        for note in notes:
            print(f"{note}")

    def add_note(self, input_note):
        """Add a new note to the notebook."""
        notes = self._load_notes()
        note_time = time.strftime("%X %x")
        new_note = f"{input_note}:::{note_time}"
        notes.append(new_note)
        self._save_notes(notes)

    def edit_note(self, index, new_note):
        """Edit an existing note."""
        notes = self._load_notes()
        if 0 <= index < len(notes):
            note_time = time.strftime("%X %x")
            notes[index] = f"{new_note}:::{note_time}"
            self._save_notes(notes)
        else:
            print("Invalid note index.")

    def delete_note(self, index):
        """Delete a note by its index."""
        notes = self._load_notes()
        if 0 <= index < len(notes):
            deleted_note = notes.pop(index)
            self._save_notes(notes)
            print(f"Deleted note: {deleted_note}")
        else:
            print("Invalid note index.")

    def run(self):
        """Main interaction loop for the notebook."""
        while True:
            print("\n(1) Read the notebook")
            print("(2) Add note")
            print("(3) Edit a note")
            print("(4) Delete a note")
            print("(5) Save and Quit")
            
            try:
                option = int(input("Please select one: "))

                if option == 1:
                    self.read_notes()
                elif option == 2:
                    input_note = input("Write a new note: ")
                    self.add_note(input_note)
                elif option == 3:
                    notes = self._load_notes()
                    print(f"The list has {len(notes)} notes.")
                    index = int(input("Which note will be changed?: "))
                    if 0 <= index < len(notes):
                        print(f"Current note: {notes[index]}")
                        new_note = input("Give the new note: ")
                        self.edit_note(index, new_note)
                    else:
                        print("Invalid note index.")
                elif option == 4:
                    notes = self._load_notes()
                    print(f"The list has {len(notes)} notes.")
                    index = int(input("Which note will be deleted?: "))
                    self.delete_note(index)
                elif option == 5:
                    print("Notebook shutting down, thank you.")
                    break
                else:
                    print("Invalid option. Please try again.")
            
            except ValueError:
                print("Please enter a valid number.")

def main():
    notebook = Notebook()
    notebook.run()

if __name__ == "__main__":
    main()