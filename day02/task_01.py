from collections import Counter
import random

class Game(object):
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter({"Cheater": 0, "Cooperator": 0,
                                 "Copycat": 0, "Grudger": 0,
                                 "Detective": 0, "Random": 0})
    def play(self, player1, player2):
        for i in range(self.matches):
            res1 = player1.action()
            res2 = player2.action()
            player1.history.append(res2)
            player2.history.append(res1)
            if res1 == res2 == True:
                self.registry.update({player1.name: 2, player2.name: 2})
            elif res1 == False and res2 == True:
                self.registry.update({player1.name: 3, player2.name: -1})
            elif res1 == True and res2 == False:
                self.registry.update({player1.name: -1, player2.name: 3})
            elif res1 == res2 == False:
                self.registry.update({player1.name: 0, player2.name: 0})
    def top3(self):
        for i in self.registry.most_common(3):
            print(i)

class Player(object):
    history = list()
    def __int__(self):
        self.history = []

class Cheater(Player):
    name = "Cheater"
    def __int__(self):
        super().__init__()
    def action(self):
        return False

class Cooperator(Player):
    name = "Cooperator"
    def __int__(self):
        super().__init__()
    def action(self):
        return True

class Copycat(Player):
    name = "Copycat"
    def __int__(self):
        super().__init__()
    def action(self):
        if not self.history:
            return True
        else:
            return self.history[-1]

class Grudger(Player):
    name = "Grudger"
    def __int__(self):
        super().__init__()
    def action(self):
        if False not in self.history:
            return True
        else:
            return False

class Detective(Player):
    name = "Detective"
    def __int__(self):
        super().__init__()
    def action(self):
        if len(self.history) == 0 or len(self.history) == 2 or len(self.history) == 3:
            return True
        elif len(self.history) == 1:
            return False
        elif len(self.history) > 3 and False not in self.history:
            return False


class Random(Player):
    name = "Random"
    def __int__(self):
        super().__init__()
    def action(self):
        return random.choice([True, False])


def lets_play():
    players = [Cheater, Cooperator, Copycat, Grudger, Detective, Random]
    game = Game(12)
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            game.play(player1=players[i](), player2=players[j]())
    game.top3()


if __name__ == '__main__':
    lets_play()
