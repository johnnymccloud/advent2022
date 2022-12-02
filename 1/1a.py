cals, max_cals = 0, 0
with open('input.txt') as input:
    for meal in input:
        try:
            cals += int(meal)
        except ValueError as err:
            max_cals = max(cals, max_cals)
            cals = 0
print(max_cals)