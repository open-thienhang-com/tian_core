import re

NAME_REGEX = re.compile(r"^[a-zA-Z\s'-]+$")  # Allows letters, spaces, apostrophes, hyphens