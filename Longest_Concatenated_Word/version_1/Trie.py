class Tree:
    """ The general class Tree for supporting other specific
        tree data structures. Each branch is a tree. """

    def __init__(self, value, branches = []):
        self.value = value
        self.branches = branches

    def get_value(self):
        return self.value

    def get_branches(self):
        return self.branches

    def is_leaf(self):
        if len(self.branches) == 0:
            return True
        else:
            return False

    def add_branch(self, tree):
        self.branches.append(tree)

    def remove_branch(self, branch):
        return self.branches.remove(branch)

    def __str__(self, indent = 0):
        value = self.get_value()

        if not value:
            value = "None"
        
        string = value
        if self.is_leaf():
            return string
        else:
            indent += 1
            for branch in self.branches:
                string += '\n' + "  " * indent + branch.__str__(indent)
            return string


class Trie(Tree):
    """ The specific class Trie for storing words with prefixes. """

    def __init__(self, value = None):
        Tree.__init__(self, value, [])

    def add_word(self, wd):

        tree = Trie(wd)

        if self.is_leaf():
            self.add_branch(tree)
        else:

            branches = self.get_branches()

            for branch in branches[:]:
                value = branch.get_value()
                if is_prefix(value, wd):
                    branch.add_word(wd)
                    return
                elif is_prefix(wd, value):
                    tree.add_branch(branch)
                    self.remove_branch(branch)

            self.add_branch(tree)

    def get_prefixes(self, wd):

        prefixes = []
        value = self.get_value()
        branches = self.get_branches()

        if self.is_leaf() or not is_prefix(value, wd):
            return prefixes

        for branch in branches:
            value = branch.get_value()

            if is_prefix(value, wd):
                prefixes.append(value)
                return prefixes + branch.get_prefixes(wd)

        return prefixes

def is_prefix(wd_A, wd_B):
    """ The function is_prefix for checking if wd_A is prefix
        of wd_B """

    if not wd_A:
        return True

    a, b = len(wd_A), len(wd_B)
    if (a >= b):
        return False
    else:
        return wd_A == wd_B[0:a]
