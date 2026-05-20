"""
Planet Class

A simple Python class that models planets and their orbit behavior.

This project was completed as part of the freeCodeCamp Python Certification.
"""


class Planet:
    """
    Represent a planet and its associated star system.
    """

    """
        Initialize a Planet object.

        Args:
            name (str): Name of the planet.
            planet_type (str): Type/category of the planet.
            star (str): Star the planet orbits.

        Raises:
            TypeError: If any argument is not a string.
            ValueError: If any argument is an empty string.
        """

    def __init__(self, name, planet_type, star):
        

        # Validate argument types
        for parameter in [name, planet_type, star]:
            if not isinstance(parameter, str):
                raise TypeError(
                    "name, planet type, and star must be strings"
                )

        # Validate non-empty strings
        for parameter in [name, planet_type, star]:
            if parameter == "":
                raise ValueError(
                    "name, planet_type, and star must be non-empty strings"
                )

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        """
        Describe the planet orbiting its star.

        Returns:
            str: Orbit description.
        """

        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        """
        Return a readable string representation of the planet.

        Returns:
            str: Formatted planet information.
        """

        return (
            f"Planet: {self.name} | "
            f"Type: {self.planet_type} | "
            f"Star: {self.star}"
        )


# Create planet objects
planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Kepler-22b", "Exoplanet", "Kepler-22")


# Display planet information
print(planet_1)
print(planet_2)
print(planet_3)

# Display orbit behavior
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())