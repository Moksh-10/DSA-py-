class node:
    def __init__(self):
        self.children = dict()
        self.is_endof_word = False

class Trie:
    def __init__(self) -> None:
        self.root = node()

    def insert(self, word):
        cn = self.root
        for c in word:
            if c not in cn.children:
                cn.children[c] = node()
            cn = c.children[c]
        cn.is_endof_word = True

