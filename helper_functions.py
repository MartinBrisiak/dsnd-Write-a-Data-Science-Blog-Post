def fix_percentage(value):
    """
    Takes integer value as string parameter in format 99% and converts it to 0.99 float format.
    """
    if type(value) == str:
        return int(value.replace("%", "")) / 100
    else:
        return float(value)


def fix_boolean(value):
    """
    Takes bool value as char in format 't' or 'f' and converts it to True/False boolean format.
    """
    if value == "t":
        return True 
    elif value == "f":
        return False
    else:
        return value


def fix_money(value):
    """
    Takes money value as string in format '99$' and converts it to float value format.
    """
    if type(value) == str:
        return float(value.replace("$", "").replace(",", ""))
    else:
        return float(value)


def count_items(value):
    """
    Counts items in amenities in format
    {TV, wifi etc}
    provides integer as output.
    """
    if type(value) == str:
        return len(value.split(','))
    else:
        return 0


def check_wifi(value):
    """
    Checks if host is providing wifi.
    """
    if type(value) == str:
        return "Wireless Internet" in value
    else:
        return False
