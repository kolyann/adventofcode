from collections import Counter

class tree:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value
        self.childs = []

    def add_child(self, child):
        if not self.has_child(child.name):
            self.childs.append(child)
        else:
            if child.name == self.name:
                raise ValueError("Duplicate name")
            self.has_child(child.name).add_child(child)

    def has_child(self, name):
        if self.name == name:
            return self
        for child in self.childs:
            rc = child.has_child(name)
            if rc:
                return rc
        return None

    def find_unbalanced(self):
        weights = [c.cweight() for c in self.childs]
        if len(set(weights)) == 1:
            return None
        else:
            wrong_weight, good_weight = [y[0] for y in sorted(Counter([x for x in weights]).items(), key=lambda x: x[1])]
            bad_child = [c for c in self.childs if c.cweight() == wrong_weight][0]
            if not bad_child.find_unbalanced():
                return bad_child.value - (wrong_weight - good_weight)
            else:
                return bad_child.find_unbalanced()

    def cweight(self):
        return self.value + sum([c.cweight() for c in self.childs])

    def __repr__(self):
        return ' <{}/{}/{}> '.format(self.name, self.value, self.childs)


data = list(list(map(lambda y: y.strip().replace('(', '').replace(')', ''), s.split('->'))) for s in map(lambda x: x.strip(), open('data.txt').readlines()))


parents = {}
trees = []

for r in data:
    root, *childs = r
    root, weight = root.split(' ')
    weight = int(weight)
    for c in childs:     # Бля, тут ровно 1 чайлд
        c = [x.strip() for x in c.split(',')]
        for child in c:
            parents[child] = root
    trees.append(tree(root, weight))

root = None
for t in trees:
    pname = parents.get(t.name)
    if not pname: #found root
        root = trees.pop(trees.index(t))
        break

while trees:
    move_trees = [t for t in trees if root.has_child(parents[t.name])]
    trees = [t for t in trees if t not in move_trees]
    for t in move_trees:
        parent = parents[t.name]
        root.has_child(parent).add_child(t)

print(root.find_unbalanced())