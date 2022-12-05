included_count = 0
with open('input.txt') as input:
    for pair in input.read().splitlines():
        values = [int(value) for value in pair.replace('-',',').split(',')]
        first_lower, first_upper, second_lower, second_upper = values[0], values[1], values[2], values[3]
        if (first_lower <= second_lower and first_upper >= second_upper) \
        or (first_lower >= second_lower and first_upper <= second_upper):
            included_count += 1
print(included_count)
