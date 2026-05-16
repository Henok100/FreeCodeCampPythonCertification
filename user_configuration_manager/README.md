# User Configuration Manager

A simple Python-based configuration manager that allows users to manage application settings such as themes, language preferences, and notifications.

This project was completed as part of the freeCodeCamp Python Certification labs.

## Features

- Add new settings
- Update existing settings
- Delete settings
- View all current settings
- Automatic lowercase normalization for consistency
- Error handling for duplicate or missing settings

## Technologies Used

- Python 3
- Dictionaries
- Functions
- String manipulation

## Functions

### `add_setting(settings, setting_pair)`

Adds a new setting to the configuration dictionary.

### `update_setting(settings, setting_pair)`

Updates an existing setting.

### `delete_setting(settings, key)`

Deletes a setting from the configuration.

### `view_settings(settings)`

Displays all current user settings in a readable format.

## Example Usage

```python
settings = {
    "theme": "dark",
    "language": "english"
}

add_setting(settings, ("notifications", "enabled"))
update_setting(settings, ("theme", "light"))
delete_setting(settings, "language")

print(view_settings(settings))
```

## Example Output

```text
Current User Settings:
Theme: light
Notifications: enabled
```

## Project Structure

```text
.
├── main.py
├── README.md
└── .gitignore
```

## What I Learned

Through this project, I practiced:

- Working with Python dictionaries
- Writing reusable functions
- Input normalization
- Conditional logic
- Basic software design principles
- Git and GitHub workflow

## How to Run

Clone the repository:

```bash
git clone git@github.com:Henok100/FreeCodeCampPythonCertification.git
```

Run the program:

```bash
python3 main.py
```