# A/X rock | B/Y paper | C/Z scissors, score = loose(0)/draw(3)/win(6) + rock(1)/paper(2)/scissors(3)
score = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,}
total_score = 0
with open('input.txt') as input:
    for game in input.readlines():
        total_score += score[game.rstrip()]
print(total_score)
