class Node:
    def __init__(self, value):
        self.child_qntt = 0
        self.value = value
        self.childs = [None] * 26


class Trie:
    def __init__(self):
        self.root = Node("")
        self.size = 0

    def ch_is_in(self, root, ch):
        if root.childs[ord(ch) % 97]:
            return True
        return False

    def _insert(self, root, word, ind, l):
        if ind < l:
            node = Node(word[ind])

            if self.ch_is_in(root, word[ind]) == 0:
                root.childs[ord(word[ind]) % 97] = node
                root.child_qntt += 1
                self._insert(node, word, ind + 1, l)
            else:
                self._insert(root.childs[ord(word[ind]) % 97], word, ind + 1, l)
            return

    def insert(self, word):
        self._insert(self.root, word, 0, len(word))

    def get(self, word):
        l = len(word)
        node = self.root
        for i in range(l):
            if self.ch_is_in(node, word[i]) == 0:
                return False
            node = node.childs[ord(word[i]) % 97]
        return True

    def max_com_pref(self, arr, root):
        if root.child_qntt == 1:
            for i in range(26):
                if root.childs[i]:
                    arr.append(root.childs[i].value)
                    self.max_com_pref(arr, root.childs[i])
        return arr
