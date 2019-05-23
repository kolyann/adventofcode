from collections import namedtuple
from copy import copy
from pprint import pprint
import sys

part2 = True

spell = namedtuple("spell", ["name", "cost", "effect"])


class DuplicateException(Exception):
    pass


class effect:
    def __init__(self, parent, duration):
        self.parent = parent
        self.duration = duration

    def renew(self):
        raise NotImplementedError

    @property
    def active(self):
        return self.duration > 0

    def __repr__(self):
        return str({self.__class__.__name__, self.duration})

    def new_parent(self, new_parent):
        cp = copy(self)
        cp.parent = new_parent
        return cp

class poison(effect):
    def __init__(self, parent, duration=6):
        super().__init__(parent, duration)
        self.damage = 3

    def renew(self):
        if self.active:
            self.parent.take_damage(self.damage)
            self.duration -= 1

class shield(effect):
    def __init__(self, parent, duration=6):
        super().__init__(parent, duration)
        self.armor = 7

    def renew(self):
        if self.active:
            self.parent.armor = self.armor
            self.duration -= 1
            if not self.active:
                self.parent.armor = 0
        else:
            self.parent.armor = 0

class recharge(effect):
    def __init__(self, parent, duration=5):
        super().__init__(parent, duration)
        self.manaregen = 101

    def renew(self):
        if self.active:
            self.parent.mana += self.manaregen
            self.duration -= 1

spells = [
    spell("missile", 53, None),
    spell("drain", 73, None),
    spell("shield", 113, shield),
    spell("poison", 173, poison),
    spell("recharge", 229, recharge),
]

class mob:
    def __init__(self, hp, atk=0, mana=0, armor=0):
        self.hp = hp
        self.atk = atk
        self.mana = mana
        self.armor = armor
        self.effects = []

    def take_damage(self, dmg):
        self.hp -= max(1, dmg - self.armor)

    @property
    def alive(self):
        return self.hp > 0

    def __repr__(self):
        return str(dict((x,y) for x, y in self.__dict__.items() if y))

    def apply_effects(self):
        for e in self.effects:
            e.renew()
        self.effects = [e for e in self.effects if e.active]

    def __copy__(self):
        new = type(self)(self.hp, self.atk, self.mana, self.armor)
        new.__dict__.update(self.__dict__)
        new.effects = [e.new_parent(new) for e in self.effects]
        return new

    def add_effect(self, eff):
        self.effects.append(eff(self))
        z = [i.__class__ for i in self.effects]
        if len(set(z)) != len(z):
            raise DuplicateException("Duplicate Effect")

def mana_sum(seq):
    return sum(sum(x.cost for x in spells if x.name == f) for f in seq)

def round(hero:mob, boss:mob, history, step=0, limit=1000):
    win_conditions = []
    if part2:
        hero.take_damage(1)
    if not hero.alive:
        return [], []
    if step >= limit:
        return [], []

    hero.apply_effects()
    boss.apply_effects()
    if not boss.alive:
        win_conditions.append(history)
        return [], win_conditions

    #Check what we can cast
    possibles = []
    for sp in spells:
        if sp.cost <= hero.mana:
            possibles.append(sp)
    if not possibles:
        return [], []

    #Cast spell
    outcomes = []
    for sp in possibles:
        _hero = copy(hero)
        _boss = copy(boss)
        _hero.mana -= sp.cost
        if _hero.mana < 0:
            raise Exception("Negative mana")
        if sp.effect:
            if sp.name != "poison":
                target = _hero
            else:
                target = _boss
            try:
                target.add_effect(sp.effect)
            except DuplicateException:
                continue
            outcomes.append([_hero, _boss, (*history, sp.name), step+1])
        else:
            if sp.name == "missile":
                _boss.take_damage(4)
            elif sp.name == "drain":
                _hero.hp += 2
                _boss.take_damage(2)
            else:
                raise Exception("Wrong spell")
            outcomes.append([_hero, _boss, (*history, sp.name), step + 1])

    #Boss turn
    final_outcome = []

    for outcome in outcomes:
        hero, boss, history, step = outcome
        hero.apply_effects()
        boss.apply_effects()

        if not boss.alive:
            win_conditions.append(history)
        else:
            hero.take_damage(boss.atk)
            if hero.alive:
                final_outcome.append((hero, boss, history, step))

    return outcomes, win_conditions

def iter_fight(hero, boss):
    wins = []
    min_mana = sys.maxsize
    turns = [(hero, boss, (), 0)]
#    for i in range(100):
    while turns:
        n_turns = []
        for turn in turns:
            res, c_wins = round(*turn)
            if c_wins:
                wins.extend(c_wins)
                for r in res:
                    (_, _, hist, _) = r
                    min_mana = min(mana_sum(hist), min_mana)
            for r in res:
                (_, _, hist, _) = r
                if mana_sum(hist) <= min_mana:
                    n_turns.append(r)

            #for r in res:
            #    print(r)
        turns = n_turns
        #print(wins, min_mana)
    return min_mana, wins

'''
Hit Points: 51
Damage: 9
'''

hero = mob(50, mana=500)
boss = mob(51, atk=9)

mm, wins = iter_fight(hero, boss)
print(mm)
for w in wins:
    if mana_sum(w) == mm:
        print(w, mana_sum(w))




