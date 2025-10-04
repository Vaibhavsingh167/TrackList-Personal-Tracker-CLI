# TrackList: A Personal Tracker CLI

TrackList is a simple, crash-safe command-line interface (CLI) tool designed to help you manage small personal lists like tasks, habits, or expenses. It stores all your data in a plain text file, ensuring that your lists are always accessible and easy to manage. Built with only Python’s standard library, it’s lightweight, beginner-friendly, and reliable.

The interface is designed to be responsive and provides a friendly, emoji-enhanced user experience. ✨

![ View of Tool](https://ibb.co/ns9XXn8Y)

-----

## Features

  * **Multiple Lists**: Manage separate sections for **Tasks**, **Habits**, and **Expenses** all in one place.
  * **CRUD Operations**: Easily **C**reate (Add), **R**ead (View), **U**pdate, and **D**elete items in your lists.
  * **Data Persistence**: Your data is safely stored in `files/records.txt` and is reloaded every time you run the app.
  * **Robust & User-Friendly**: Handles invalid inputs gracefully without crashing and provides helpful, friendly messages to guide you.
  * **Zero Dependencies**: Runs on any system with Python 3, as it uses only the standard library. No external packages are needed\!
  * **Responsive UI**: The display, including the ASCII art and menus, adapts to your terminal window size for a better user experience.

-----

## How to Run

Follow these simple steps to get the tracker up and running.

**Prerequisites:**

  * Ensure you have **Python 3** installed on your system.

**Execution:**

1.  Save the code provided as `app.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved `app.py`.
4.  Run the application using the command:

    ```bash
    python3 app.py
    ```

5.  That's it\! Follow the on-screen prompts to manage your lists. The application will automatically create the necessary files and directories on the first run.

-----

## File Structure and Format

The application maintains a very simple file structure.

  * `app.py`: The main Python script that runs the application.
  * `files/records.txt`: This is the plain text file where all your data is stored. The application automatically creates this file inside a `files` directory.

### Data Format

The `records.txt` file uses a simple, human-readable format to store your data:

  * The file is organized into sections, each marked with a header in square brackets (e.g., `[TASKS]`).
  * Each item you add to a list is stored on a new line right below its section header.

Here is an example of what the `files/records.txt` file might look like:

```
[TASKS]
Finish the project report
Buy groceries for the week

[HABITS]
Read 10 pages daily
Go for a 30-minute walk

[EXPENSES]
Coffee - $5
Lunch with a friend - $20

```

-----

## Note on AI Usage

AI assistance (ChatGPT) was used for the initial design of the ASCII art.