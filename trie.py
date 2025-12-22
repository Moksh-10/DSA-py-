class node:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.root = node()

    def insert(self, word):
        cn = self.root
        for c in word:
            if c not in cn.children:
                cn.children[c] = node()
            cn = cn.children[c]
        cn.is_endof_word = True

    def search(self, word):
        cn = self.root
        for c in word:
            if c not in cn.children:
                return False
            cn = cn.children[c]
        return cn.is_end_of_word

    def has_prefix(self, word):
        cn = self.root
        for c in word:
            if c not in cn.children:
                return False
            cn = cn.children[c]
        return True

    def delete(self, word):
        self._delete(self.root, word, 0)
    
    def _delete(self, cn, word, index):
        if index == len(word):
            if not cn.is_end_of_word:
                return False




