class node:
    def __init__(self, name, children = [], val=0):
        self.name = name
        self.children = children
        self.val = val

    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)

    def jsone(self):
        jsone = dict(name=self.name, val=self.val)
        children = []
        for child in self.children:
            children.append(child.jsone()) 
        jsone['children'] = children
        return jsone