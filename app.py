import os
import shutil
import time

ASCII_ART = r""" 
   ____    __    ____  _______  __        ______   ______   .___  ___.  _______                   
   \   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|                  
    \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__                     
     \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|                    
      \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____                   
       \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|                  
                                                                                                  
         .___________.  ______                                                                    
         |           | /  __  \                                                                   
         `---|  |----`|  |  |  |                                                                  
             |  |     |  |  |  |                                                                  
             |  |     |  `--'  |                                                                  
             |__|      \______/                                                                   
                                                                                                  
   .___________..______          ___       ______  __  ___  __       __       _______.___________.
   |           ||   _  \        /   \     /      ||  |/  / |  |     |  |     /       |           |
   `---|  |----`|  |_)  |      /  ^  \   |  ,----'|  '  /  |  |     |  |    |   (----`---|  |----`
       |  |     |      /      /  /_\  \  |  |     |    <   |  |     |  |     \   \       |  |     
       |  |     |  |\  \----./  _____  \ |  `----.|  .  \  |  `----.|  | .----)   |      |  |     
       |__|     | _| `._____/__/     \__\ \______||__|\__\ |_______||__| |_______/       |__|     
"""
DESCRIPTION = "Tip: For the best experience, maximize your terminal or command prompt window.\n"
INFO = ("TrackList is a simple, crash-safe CLI tool to manage small lists like tasks, habits, or expenses. "
        "It supports add, list, and update operations while storing everything in a plain text file. "
        "Built with only Python’s standard library, it’s lightweight, beginner-friendly, and reliable.")

def get_terminal_width(default=100):
    try:
        return shutil.get_terminal_size((default, 30)).columns
    except Exception:
        return default

def responsive_art_block(art_block, term_w, margin=2):
    allowed = max(10, term_w - margin)
    out = []
    for raw in art_block.splitlines():
        line = raw.rstrip("\n")
        if not line.strip():
            out.append("".center(term_w))
            continue
        if len(line) <= allowed:
            out.append(line.center(term_w))
        else:
            out.append(line[:allowed].center(term_w))
    return "\n".join(out)

def print_centered_box(text, term_w, margin=4):
    max_width = term_w - margin
    words, lines, current = text.split(), [], ""
    for word in words:
        if len(current) + len(word) + 1 <= max_width - 4:
            current += (" " if current else "") + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    box_width = max(len(line) for line in lines) + 4
    border = "+" + "-" * (box_width - 2) + "+"
    box = [border] + [f"| {line.ljust(box_width - 4)} |" for line in lines] + [border]
    for bline in box:
        print(bline.center(term_w))

def intro_screen():
    term_w = get_terminal_width()
    print()
    print(responsive_art_block(ASCII_ART, term_w))
    print()
    time.sleep(1.2)
    for char in DESCRIPTION:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()
    time.sleep(1)
    print_centered_box(INFO, term_w)
    print("\n")
    time.sleep(1)

FILES_DIR = "files"
RECORDS_FILE = os.path.join(FILES_DIR, "records.txt")
os.makedirs(FILES_DIR, exist_ok=True)

SECTIONS = ["TASKS", "HABITS", "EXPENSES"]

def init_file():
    if not os.path.exists(RECORDS_FILE):
        with open(RECORDS_FILE, "w") as f:
            for sec in SECTIONS:
                f.write(f"[{sec}]\n\n")

def load_section(section):
    items, current = [], None
    try:
        with open(RECORDS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    current = line[1:-1]
                elif current == section and line:
                    items.append(line)
    except Exception as e:
        print(f"Oops! Couldn't read {section.lower()} 😅 Error: {e}")
    return items

def save_section(section, items):
    try:
        with open(RECORDS_FILE, "r") as f:
            lines = f.readlines()
        new_lines, current = [], None
        for line in lines:
            if line.strip().startswith("[") and line.strip().endswith("]"):
                current = line.strip()[1:-1]
                new_lines.append(line)
            elif current == section:
                continue
            else:
                new_lines.append(line)
        idx = None
        for i, line in enumerate(new_lines):
            if line.strip() == f"[{section}]":
                idx = i
                break
        if idx is not None:
            new_lines.insert(idx+1, "\n".join(items) + ("\n" if items else "") + "\n")
        with open(RECORDS_FILE, "w") as f:
            f.writelines(new_lines)
    except Exception as e:
        print(f"Oops! Couldn't save {section.lower()} 😅 Error: {e}")

def display_items(items, section):
    if not items:
        print(f"\nNo {section.lower()} yet! Maybe add some? 🤔\n")
    else:
        print(f"\nHere are your {section.lower()}:")
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. {item}")
        print()

def menu(section):
    time.sleep(1)
    term_w = shutil.get_terminal_size((100, 30)).columns
    menu_lines = [
        f"------- {section.upper()} MANAGER MENU -------",
        "1. View all items",
        "2. Add new item",
        "3. Remove an item",
        "4. Update an item",
        "5. Exit Program",
        "6. Go back to choose section"
    ]
    
    box_width = max(len(line) for line in menu_lines) + 4  
    border = "+" + "-" * (box_width - 2) + "+"
    
    box = [border] + [f"| {line.ljust(box_width - 4)} |" for line in menu_lines] + [border]
    
    for line in box:
        print(line.center(term_w))

def section_loop(section):
    items = load_section(section)
    while True:
        try:
            menu(section)
            choice = input("Enter your choice (1-6): ").strip()
            if not choice.isdigit() or int(choice) not in range(1,7):
                raise ValueError(f"Oops! '{choice}' is not a valid option 😅 Pick a number between 1 and 6.")
            choice = int(choice)

            if choice == 1:
                display_items(items, section)
            elif choice == 2:
                new_item = input(f"Type the new {section.lower()[:-1]} (be creative!): ").strip()
                if new_item:
                    items.append(new_item)
                    save_section(section, items)
                    print(f"Yay! '{new_item}' added to {section.lower()} ✅")
                else:
                    print("Oops! You didn’t type anything 😅 Give it another shot!")
            elif choice == 3:
                display_items(items, section)
                idx = input(f"Enter the number of the item to remove (e.g., 1, 2, 3): ").strip()
                if not idx.isdigit() or int(idx) not in range(1, len(items)+1):
                    print("Hmm, that number doesn’t match any item 🤔 Try again with a valid number.")
                else:
                    removed = items.pop(int(idx)-1)
                    save_section(section, items)
                    print(f"Removed '{removed}' successfully! 🗑️")
            elif choice == 4:
                display_items(items, section)
                idx = input(f"Enter the number of the item to update: ").strip()
                if not idx.isdigit() or int(idx) not in range(1, len(items)+1):
                    print("Hmm, that number doesn’t match any item 🤔 Try again with a valid number.")
                else:
                    new_item = input("Type the updated value: ").strip()
                    if new_item:
                        old_item = items[int(idx)-1]
                        items[int(idx)-1] = new_item
                        save_section(section, items)
                        print(f"Sweet! '{old_item}' updated to '{new_item}' ✅")
                    else:
                        print("Oops! You didn’t type anything 😅 Give it another shot!")
            elif choice == 5:
                print("Okay, exiting program. Catch you later! 👋")
                exit(0)
            elif choice == 6:
                print("Cool, returning to section selection... 🔄")
                break
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except Exception as e:
            print(f"Runtime Error: {e}")

def main():
    intro_screen()
    init_file()
    while True:
        print("\nWhich list do you want to access? Pick a number:")
        for i, sec in enumerate(SECTIONS, start=1):
            print(f"{i}. {sec.capitalize()}")
        
        section = ""
        while True:
            choice = input("Enter the number of your choice: ").strip()
            if not choice.isdigit() or int(choice) not in range(1, len(SECTIONS)+1):
                print(f"Oops! '{choice}' is not valid 😅 Pick a number between 1 and {len(SECTIONS)}.")
            else:
                section = SECTIONS[int(choice)-1]
                break
        
        section_loop(section)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye! Exiting program safely 👋")
        exit(0)
