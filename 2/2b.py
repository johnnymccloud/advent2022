# A rock | B paper | C scissors : X loose | Y draw | Z win 
# score = loose(0)/draw(3)/win(6) + rock(1)/paper(2)/scissors(3)
score = {  
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,}
total_score = 0
with open('input.txt') as input:
    for game in input.readlines():
        total_score += score[game.rstrip()]
print(total_score)
