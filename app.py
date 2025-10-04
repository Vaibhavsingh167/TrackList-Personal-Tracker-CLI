import json
import os

# Define a constant for the data file name for easy configuration.
DATA_FILE = 'tinylist_data.json'

def load_data():
    """
    Loads the list of items from the JSON data file.
    Handles FileNotFoundError and JSONDecodeError gracefully by returning an empty list.
    """
    # Check if the file exists before trying to read it.
    if not os.path.exists(DATA_FILE):
        return  # Return an empty list if the file doesn't exist.
    
    try:
        # Use a context manager to ensure the file is closed properly.
        with open(DATA_FILE, 'r') as f:
            # Attempt to load and return the data from the JSON file.
            return json.load(f)
    except json.JSONDecodeError:
        # If the file is corrupted or empty, it's not valid JSON.
        print("Warning: Data file is corrupted or empty. Starting with a new list.")
        return
    except IOError as e:
        # Handle other potential file reading errors.
        print(f"Error reading data file: {e}. Starting with an empty list.")
        return

def save_data(items):
    """
    Saves the list of items to the JSON data file.
    Handles IOError if the file cannot be written.
    """
    try:
        # Use a context manager to open the file in write mode ('w').
        # This will overwrite the file with the current state of the list.
        with open(DATA_FILE, 'w') as f:
            # Use json.dump to write the list to the file with human-readable formatting.
            json.dump(items, f, indent=4)
    except IOError as e:
        # Inform the user if the data could not be saved.
        print(f"Error: Could not save data to file: {e}")

def display_menu():
    """Prints the main menu of options to the console."""
    print("\n--- TinyList Menu ---")
    print("1. List items")
    print("2. Add item")
    print("3. Update item")
    print("4. Delete item")
    print("5. Exit")
    print("---------------------")

def list_items(items):
    """Displays all items in the list, numbered."""
    print("\n--- Your List ---")
    if not items:
        print("The list is empty.")
    else:
        # Use enumerate to get both index and item, starting from 1 for user-friendliness.
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item}")
    print("-----------------")

def add_item(items):
    """Prompts the user for a new item and adds it to the list."""
    item = input("Enter the new item: ").strip()
    if item:
        items.append(item)
        save_data(items)
        print(f"Successfully added: '{item}'")
    else:
        print("Cannot add an empty item.")

def update_item(items):
    """Updates an existing item in the list."""
    if not items:
        print("The list is empty. Nothing to update.")
        return

    list_items(items)
    try:
        choice_str = input("Enter the number of the item to update: ")
        choice = int(choice_str)

        # Proactive bounds checking to prevent IndexError.
        if 1 <= choice <= len(items):
            new_item = input(f"Enter the new text for item {choice}: ").strip()
            if new_item:
                # Adjust for 0-based indexing.
                original_item = items[choice - 1]
                items[choice - 1] = new_item
                save_data(items)
                print(f"Successfully updated '{original_item}' to '{new_item}'.")
            else:
                print("Cannot update to an empty item.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_item(items):
    """Deletes an item from the list."""
    if not items:
        print("The list is empty. Nothing to delete.")
        return

    list_items(items)
    try:
        choice_str = input("Enter the number of the item to delete: ")
        choice = int(choice_str)

        # Proactive bounds checking.
        if 1 <= choice <= len(items):
            # Adjust for 0-based indexing and remove the item.
            removed_item = items.pop(choice - 1)
            save_data(items)
            print(f"Successfully deleted: '{removed_item}'")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """The main function and application loop."""
    items = load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            list_items(items)
        elif choice == '2':
            add_item(items)
        elif choice == '3':
            update_item(items)
        elif choice == '4':
            delete_item(items)
        elif choice == '5':
            print("Exiting TinyList. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Standard entry point for a Python script.
if __name__ == "__main__":
    main()