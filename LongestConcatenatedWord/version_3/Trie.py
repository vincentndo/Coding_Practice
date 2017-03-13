class Node:
    """ The class Node for containing information of each node """

    def __init__(self, letter, word = "", branch_map = {}):
        self.letter = letter
        self.word = word
        self.branch_map = branch_map

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

    def get_branch_map(self):
        return self.branch_map

    def add_branch_map(self, tree):
        letter = tree.get_node().get_letter()
        self.branch_map[letter] = tree


class Tree:
    """ The general class Tree for supporting other specific
        tree data structures. Each branch is a tree. """

    def __init__(self, node, branches = []):
        self.node = node
        self.branches = branches
        for branch in branches:
            self.node.add_branch_map(branch)

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
        node = self.get_node()
        node.add_branch_map(tree)

    def __str__(self, indent = 0):
        node = self.get_node()

        if not node.get_letter():
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

        if not node.get_letter():
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

    def __init__(self, node = Node(None, "", {})):
        Tree.__init__(self, node, [])

    def add_word(self, wd):
        tree = self
        node = tree.get_node()

        for i in range(len(wd)):
            letter = wd[i]
            branch_map = node.get_branch_map()
            if letter in branch_map:
                tree = branch_map[letter]
                node = tree.get_node()
            else:
                # print(letter)
                # print(node.get_branch_map())
                node = Node(letter, "", {})
                new_tree = Trie(node)
                tree.add_branch(new_tree)
                tree = new_tree             
        node.set_word(wd)

    def contains(self, wd):
        tree = self
        node = self.get_node()

        for i in range(len(wd)):
            letter = wd[i]
            branch_map = node.get_branch_map()
            if letter in branch_map:
                node = branch_map[letter].get_node()
                if node.has_word() and wd == node.get_word():
                    return True
            else:
                return False
        return False

    def get_prefixes(self, wd):
        tree = self
        node = self.get_node()
        prefixes = []

        for i in range(len(wd)):
            letter = wd[i]
            branch_map = node.get_branch_map()
            if letter in branch_map:
                node = branch_map[letter].get_node()
                if node.has_word() and  wd != node.get_word():
                    prefixes.append(node.get_word())
            else:
                break
        return prefixes
