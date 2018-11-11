class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)
    def encoder(self):
        json = dict(name=self.name, val=self.val)
        children = []
        for child in self.children:
            children.append(child.encoder()) 
        json['children'] = children
        return json