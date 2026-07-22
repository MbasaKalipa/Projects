def tip(percent, meal):
    percent_decimal = percent / 100
    result = meal * percent_decimal
    return result

meal = float(input("How much was the meal?:($)"))
percent = float(input("What percentage would you like to tip?:(%)"))
result = tip(percent, meal)
print(f"Leave ${result:.2f}")