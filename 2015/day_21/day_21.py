from collections import namedtuple
from itertools import product
import sys

item = namedtuple('item', ['name', 'cost', 'damage', 'armor'])

shop = {
    'weapon': [
        item('NoneWeapon', 0, 0, 0),
        item('Dagger', 8, 4, 0),
        item('Shortsword', 10, 5, 0),
        item('Warhammer', 25, 6, 0),
        item('Longsword', 40, 7, 0),
        item('Greataxe', 74, 8, 0)
    ],
    'armor': [
        item('NoneArmor', 0, 0, 0),
        item('Leather', 13, 0, 1),
        item('Chainmail', 31, 0, 2),
        item('Splintmail', 53, 0, 3),
        item('Bandedmail', 75, 0, 4),
        item('Platemail', 102, 0, 5),
    ],
    'rings': [
        item('NoneRing', 0, 0, 0),
        item('Damage +1', 25, 1, 0),
        item('Damage +2', 50, 2, 0),
        item('Damage +3', 100, 3, 0),
        item('Defense +1', 20, 0, 1),
        item('Defense +2', 40, 0, 2),
        item('Defense +3', 80, 0, 3),
    ]
}

class mob:
    def __init__(self, hp, dmg, arm):
        self.hp = hp
        self.dmg = dmg
        self.arm = arm

    @property
    def alive(self):
        return self.hp > 0

    def take_dmg(self, dmg):
        dmg = max(1, dmg-self.arm)
        self.hp -= dmg

class hero(mob):
    def __init__(self, hp, items):
        dmg = sum(i.damage for i in items)
        arm = sum(i.armor for i in items)
        super().__init__(hp, dmg, arm)
        self.items = items

    @property
    def status(self):
        return self.hp, self.dmg, self.arm, self.items

def init_fight(items):
    boss = mob(109, 8, 2)
    you = hero(100, items)
    while True:
        boss.take_dmg(you.dmg)
        if not boss.alive:
            return True
        you.take_dmg(boss.dmg)
        if not you.alive:
            return False

min_cost = sys.maxsize
min_cost_setup = ()
max_cost = 0
max_cost_setup = ()
for items in list(product(*shop.values(), shop['rings'])):
    if items[2] == items[3] and items[2].name != 'NoneRing':
        continue
    if items[0].name == 'NoneWeapon':
        continue
    cost = sum(x.cost for x in items)
    if init_fight(items):
        min_cost = min(min_cost, cost)
        if min_cost == cost:
            min_cost_setup = items
    else:
        max_cost = max(max_cost, cost)
        if max_cost == cost:
            max_cost_setup = items


print(min_cost, min_cost_setup)
print(max_cost, max_cost_setup)