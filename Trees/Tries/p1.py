# Add and search word
# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A
# . means it can represent any one letter.

class TrieNode:
    def __init__(self):
        self.__R = 26
        self.links = [None] * self.__R
        self.isEndOfString = False


class WordDictionary:
    def __init__(self):
        self.root = WordDictionary.get_node()

    @staticmethod
    def get_node():
        return TrieNode()

    @staticmethod
    def _char_to_alpha_index(ch):
        return ord(ch) - ord('a')

    def addWord(self, word):
        # Point to the root element (TrieNode)
        crawl_pointer = self.root
        # Get length of the word to insert
        length = len(word)
        for level in range(length):
            # Convert char in word to alpha_index
            alpha_index = WordDictionary._char_to_alpha_index(word[level])

            # If char not in crawl_pointer's links list, create a new TrieNode
            if not crawl_pointer.links[alpha_index]:
                crawl_pointer.links[alpha_index] = self.get_node()
            # Point to the new TrieNode
            crawl_pointer = crawl_pointer.links[alpha_index]

        # Mark end of string
        crawl_pointer.isEndOfString = True

    @staticmethod
    def search_prefix(word, root):
        crawl_pointer = root
        length = len(word)
        for level in range(length):
            if word[level] == '.':
                result = False
                for k in range(len(crawl_pointer.links)):
                    if crawl_pointer.links[k] is not None:
                        result = WordDictionary.search_prefix(word[level + 1:], crawl_pointer.links[k])
                        if result: return True
                return False
            else:
                alpha_index = WordDictionary._char_to_alpha_index(word[level])
                if crawl_pointer.links[alpha_index] is None:
                    return False
                crawl_pointer = crawl_pointer.links[alpha_index]
        return crawl_pointer.isEndOfString

    def search(self, word):
        return WordDictionary.search_prefix(word, self.root)
