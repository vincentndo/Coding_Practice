class Node:
    """ The class Node for containing information of each node """

    def __init__(self, letter, word = ""):
        self.letter = letter
        self.word = word

    def get_letter(self):
        return self.letter

    def has_word(self):
        if len(self.word) == 0:
            return False
        else:
            return True

    def get_word(self):
        return self.word

    def set_word(self, word):
        self.word = word


class Tree:
    """ The general class Tree for supporting other specific
        tree data structures. Each branch is a tree. """

    def __init__(self, node, branches = []):
        self.node = node
        self.branches = branches

    def get_node(self):
        return self.node

    def get_branches(self):
        return self.branches

    def is_leaf(self):
        if len(self.branches) == 0:
            return True
        else:
            return False

    def add_branch(self, tree):
        self.branches.append(tree)

    def __str__(self, indent = 0):
        node = self.get_node()

        if not node:
            string = "None"
        else:
            string = node.get_letter()

        if self.is_leaf():
            return string
        else:
            indent += 1
            for branch in self.branches:
                string += '\n' + "  " * indent + branch.__str__(indent)
            return string

    def __repr__(self, indent = 0):
        node = self.get_node()

        if not node:
            string = "None"
        else:
            if node.has_word():
                string = node.get_word()
            else:
                string = ""

        if self.is_leaf():
            return string
        else:
            indent += 1
            for branch in self.branches:
                if branch.get_node().has_word():
                    string += '\n' + "  " * indent + branch.__repr__(indent)
                else:
                    string += branch.__repr__(indent)
            return string


class Trie(Tree):
    """ The specific class Trie for storing words with prefixes. """

    def __init__(self, node = None):
        Tree.__init__(self, node, [])

    def add_word(self, wd):

        tree = self
        for i in range(len(wd)):
            letter = wd[i]
            match = False
            branches = tree.get_branches()
            for branch in branches:
                node = branch.get_node()

                if letter == node.get_letter():
                    match = True
                    tree = branch
                    break
            if match:
                pass
            else:
                node = Node(letter)
                new_tree = Trie(node)
                tree.add_branch(new_tree)
                tree = new_tree
        node.set_word(wd)

    def contains(self, wd):

        tree = self
        prefixes = []
        for i in range(len(wd)):
            letter = wd[i]
            match = False
            branches = tree.get_branches()
            for branch in branches:
                node = branch.get_node()
                if letter == node.get_letter():
                    match = True
                    tree = branch
                    if node.has_word() and  wd == node.get_word():
                        return True
                    break
            if not match:
                return False
        return False

    def get_prefixes(self, wd):

        tree = self
        prefixes = []
        for i in range(len(wd)):
            letter = wd[i]
            branches = tree.get_branches()
            for branch in branches:
                node = branch.get_node()
                match = False
                if letter == node.get_letter():
                    match = True
                    tree = branch
                    if node.has_word() and  wd != node.get_word():
                        prefixes.append(node.get_word())
                    break
            if not match:
                break
        return prefixes
