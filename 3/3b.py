
def priority(item :str) -> int:
    if 'a' <= item <= 'z':
        return int(ord(item) - ord('a')) + 1
    else:
        return int(ord(item) - ord('A')) + 27

sum_of_priorities = 0
with open('input.txt') as input:
    rucksacks = input.read().splitlines()
    groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
    for group in groups:
        unique_elements = [set(rucksack) for rucksack in group]
        common_element = set.intersection(*unique_elements)
        sum_of_priorities += priority(common_element.pop())
print(sum_of_priorities)
