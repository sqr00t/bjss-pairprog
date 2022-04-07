from helpers import functions as funcs

def main():
    house_price = funcs.get_input()
    multiplier = funcs.get_tax_bracket(house_price)
    print(funcs.get_tax_amount(house_price, multiplier))

if __name__ == '__main__':
    main()
