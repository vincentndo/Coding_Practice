from Trie import *

def read_file_and_build_trie(filename, trie, prefix_map):

    file = open(filename)
    line = file.readline().strip()
    while line != "":
        
        trie.add_word(line)
        prefixes = trie.get_prefixes(line)

        if len(prefixes) != 0:
            prefix_map[line] = prefixes

        line = file.readline().strip()


if __name__ == "__main__":

    filename = "../wordsforproblem.txt"
    trie = Trie()
    prefix_map = {}
    read_file_and_build_trie(filename, trie, prefix_map)
    print(trie)
    print(prefix_map)
