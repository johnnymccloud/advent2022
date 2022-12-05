
def priority(item :str) -> int:
    if 'a' <= item <= 'z':
        return int(ord(item) - ord('a')) + 1
    else:
        return int(ord(item) - ord('A')) + 27

sum_of_priorities = 0
with open('input.txt') as input:
    for rucksack in input.read().splitlines():
        compartment_size = len(rucksack)//2
        compartment_1, compartment_2 = rucksack[:compartment_size], rucksack[compartment_size:]
        for item in compartment_1:
            if item in compartment_2:
                sum_of_priorities += priority(item)
                break
print(sum_of_priorities)
