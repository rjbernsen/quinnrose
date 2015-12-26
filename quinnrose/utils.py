def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def km_to_miles(km):
    return km * 0.62137

def miles_to_km(miles):
    return miles / 0.62137
