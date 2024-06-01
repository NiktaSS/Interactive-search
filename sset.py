#!/usr/bin/env python3

"""
Suffix tree to search in dictionary
"""


class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end_of_word = False


class SSet:
    def __init__(self, fname):
        """Saves filename of a dictionary file"""
        self.fname = fname
        self.words = None
        self.root = Node(None)

    def load(self) -> None:
        """
        Loads words from a dictionary file.
        Each line contains a word.
        File is not sorted.
        """
        with open(self.fname, 'r') as f:
            for line in f:
                self.insert(line.strip())

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, suffix):
        node = self.root
        for char in suffix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words(node, suffix)

    def _find_words(self, node, suffix):
        result = []
        if node.is_end_of_word:
            result.append(suffix)
        for char, child_node in node.children.items():
            result.extend(self._find_words(child_node, suffix + char))
        return result
