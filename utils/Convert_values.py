def convert_values(value: str):
    """
    The function `convert_values` in Python converts a string value into either an integer, float, or
    fraction.
    """

    # Fractions
    if "/" in value:
        parts = value.split("/")
        if len(parts) != 2:
            raise ValueError("The fraction must consist of two parts, the numerator and the denominator.")
        
        numerator, denominator = parts
        if "." in numerator:
            numerator = float(numerator)
        else:
            numerator = int(numerator)

        if "." in denominator:
            denominator =float(denominator)
        else:
            denominator = int(denominator)

        if denominator == 0:
            raise ZeroDivisionError("The denominator must be differento to 0.")
        
        return numerator, denominator
        
    # Decimal
    elif "." in value:
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Invalid value {value}")
        
    # Integer
    else:
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Invalid value {value}")
        
def convert_to_fraction(value: str):
    int_part, decimal_part = value.split(".")

    decimal_places = len(decimal_part)

    denominator = 10**decimal_places

    numerator_string = int_part + decimal_part
    numerator = int(numerator_string)

    return numerator, denominator