def get_input():
    return int(input('Enter house price: '))

def get_tax_bracket(house_price:int) -> float:
    """returns float multiplier of house price depending on
    which tax bracket house_price falls into"""
    # use if-else loops or dict
    multiplier = 0.02
    return multiplier

def get_tax_amount(house_price:int, multiplier:float) -> float:
    return house_price * multiplier