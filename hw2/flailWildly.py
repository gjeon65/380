from pegGame import Game
import random

game = Game()
game.refBoard()
rules = game.applicableRules()
while rules:
    game.describeState()
    for i, rule in enumerate(rules):
        print('{}:\t{}'.format(i, rule))
    rule = random.choice(rules)
    game.describeRule(rule)
    game.applyRule(rule)

    rules = game.applicableRules()

if game.goal():
    print "Congratulations, you have won!"
else:
    print "Unfortunately, you have lost!"