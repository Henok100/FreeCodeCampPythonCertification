def add_setting(settings, setting):
    """
    Add a new setting to the settings dictionary.
    """

    key = setting[0].lower()
    value = setting[1].lower()

    if key in settings.keys():
        return (
            f"Setting '{key}' already exists! "
            "Cannot add a new setting with this name."
        )
    
    settings[key] = value


    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, setting):
    """
    Update an existing setting in the settings dictionary.
    """

    key = setting[0].lower()
    value = setting[1].lower()

    if key in settings:
        settings[key] = value

        return (
            f"Setting '{key}' updated to '{value}' successfully!"
        )

    return (
        f"Setting '{key}' does not exist! "
        "Cannot update a non-existing setting."
    )

def delete_setting(settings, key):
    """
    Delete a setting from the settings dictionary.
    """

    key = key.lower()

    if key in settings:
        del settings[key]

        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"

def view_settings(settings):
    """
    Display all current user settings.
    """

    if not settings:
        return "No settings available."

    view = "Current User Settings:\n"

    for key, value in settings.items():
        view += f"{key.capitalize()}: {value}\n"

    return view

test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high",
}


print(view_settings(test_settings))