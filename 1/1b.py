cals, max_cals = 0, [0] * 3
with open('input.txt') as input:
    for meal in input:
        try:
            cals += int(meal)
        except ValueError as err:
            max_cals = sorted(max_cals + [cals], reverse=True)[:3]
            cals = 0
print(sum(max_cals))