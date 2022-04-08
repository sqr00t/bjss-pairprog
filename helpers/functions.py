def get_input():
    return int(input('Enter house price: '))

#def get_tax_bracket(house_price:int) -> float:
#    """returns float multiplier of house price depending on
#    which tax bracket house_price falls into"""
#    # use if-else loops or dict
#    multiplier = 0.02
#    return multiplier

def get_tax_amount(house_price:int) -> float:
    tax_bracket = [{'minimum': 0, 'maximum': 125000, 'tax_multiplier': 0},
                   {'minimum': 125000, 'maximum': 250000, 'tax_multiplier': 0.02},
                   {'minimum': 250000, 'maximum': 925000, 'tax_multiplier': 0.05}]
    #if house_price <= 125000:
    #    tax_amount = 0
    #elif 125000 < house_price <= 250000:
    #    tax_amount = (house_price - 125000) * 0.02
    #elif 250000 < house_price <= 925000:
    #    tax_amount = (125000 * 0.02) + ((house_price - 250000) * 0.05)
    tax_amount = 0
    for bracket in tax_bracket:
    # calculate portion of houseprice total within tax bracket, multiply with applicable multiplier
    # add to tax_amount
    # if houseprice < minimum of bracket, continue
        if house_price < bracket['minimum']:
            break
        if house_price > bracket['maximum']:
            tax_amount += (bracket['maximum'] - bracket['minimum']) * bracket['tax_multiplier']
            continue
        tax_amount += (house_price - bracket['minimum']) * bracket['tax_multiplier']
    
    return tax_amount