from os import name


def format_name(name: str) -> tuple[str, str, str]:
    return (name.lower(), name.upper(), name.capitalize())

