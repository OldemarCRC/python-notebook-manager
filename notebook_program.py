# -*- coding: cp1252 -

import time
import pickle

def check_file(file_name):
    try:
        with open(file_name, "rb") as file_to_check:
            pass

    except FileNotFoundError:
        with open(file_name, "wb") as file_to_check:
            pickle.dump([], file_to_check)
            if file_name == "notebook.dat":
                print("No default notebook was found, created one.")

            else:
                print("No notebook with that name detected, created one.")

def main():

    file_name = "notebook.dat"
    check_file(file_name)

    while True:
        print("(1) Read the notebook")
        print("(2) Add note")
        print("(3) Edit a note")
        print("(4) Delete a note")
        print("(5) Save and Quit")
        print("")
        option = int(input("Please select one: "))

        if option == 1:
            with open(file_name, "rb") as file_to_check:
                loaded_data = pickle.load(file_to_check)
                for note in loaded_data:
                    print(f"{note}")

        elif option == 2:
            with open(file_name, "rb") as file_to_check:
                loaded_data = pickle.load(file_to_check)
            input_note=input("Write a new note: ")
            note_time = time.strftime("%X %x")
            new_note = input_note+":::"+note_time
            loaded_data.append(new_note)
            with open(file_name, "wb") as file_to_check:
                pickle.dump(loaded_data, file_to_check)
        
        elif option == 3:
            with open(file_name, "rb") as file_to_check:
                loaded_data = pickle.load(file_to_check)
            print(f"The list has {len(loaded_data)} notes.")
            index_note=int(input("Which of them will be changed?: "))
            print(f"{loaded_data[index_note]}")
            input_note=input("Give the new note: ") 
            note_time = time.strftime("%X %x")
            new_note = input_note+":::"+note_time
            loaded_data[index_note]=new_note
            with open(file_name, "wb") as file_to_check:
                pickle.dump(loaded_data, file_to_check)

        elif option == 4:
            with open(file_name, "rb") as file_to_check:
                loaded_data = pickle.load(file_to_check)
            print(f"The list has {len(loaded_data)} notes.")
            index_note=int(input("Which of them will be deleted?: "))
            if index_note==1 and len(loaded_data)==1:
                index_note=0
                print(f"Deleted note {loaded_data[index_note]}")
                loaded_data.pop(index_note)
                with open(file_name, "wb") as file_to_check:
                    pickle.dump(loaded_data, file_to_check)     
            else:
                print(f"Deleted note {loaded_data[index_note]}")
                loaded_data.pop(index_note)
                with open(file_name, "wb") as file_to_check:
                    pickle.dump(loaded_data, file_to_check)   
            
            
        elif option == 5:
            print("Notebook shutting down, thank you.")
            break

if __name__ == "__main__":
    main()
