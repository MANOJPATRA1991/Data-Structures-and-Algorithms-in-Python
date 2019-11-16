class TrieNode:
    __R: int
    links: list
    isEndOfString: bool

    def __init__(self):
        self.__R = 26
        self.links = [None] * self.__R
        self.isEndOfString = False


class Trie:
    def __init__(self):
        self.root = Trie.get_node()

    @staticmethod
    def get_node():
        return TrieNode()

    @staticmethod
    def _char_to_alpha_index(ch):
        return ord(ch)-ord('a')

    def insert(self, key):
        # Point to the root element (TrieNode)
        crawl_pointer = self.root
        # Get length of the key to insert
        length = len(key)
        for level in range(length):
            # Convert char in key to alpha_index
            alpha_index = Trie._char_to_alpha_index(key[level])

            # If char not in crawl_pointer's links list, create a new TrieNode
            if not crawl_pointer.links[alpha_index]:
                crawl_pointer.links[alpha_index] = self.get_node()
            # Point to the new TrieNode
            crawl_pointer = crawl_pointer.links[alpha_index]

        # Mark end of string
        crawl_pointer.isEndOfString = True

    def search(self, key):
        crawl_pointer = self.root
        length = len(key)
        for level in range(length):
            alpha_index = Trie._char_to_alpha_index(key[level])
            if not crawl_pointer.links[alpha_index]:
                return False
            crawl_pointer = crawl_pointer.links[alpha_index]

        return crawl_pointer is not None and crawl_pointer.isEndOfString


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

        # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()