# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class TreeNode:
    def __init__(self):
        self.children = {}


class PrefixTree:
    def __init__(self):
        self.head = TreeNode()

    def insert_words(self, words_arr):
        [self.insert_word(word) for word in words_arr]
    def insert_word(self, word_to_add):
        curr = self.head
        word_array = word_to_add.split('/')
        for word in word_array:
                if word not in curr.children:
                    curr.children[word] = TreeNode()
                curr = curr.children[word]

    def get_all_words(self):
        results = []
        stack = [(self.head, "")]
        while stack:
            node, prefix = stack.pop()
            if len(node.children) == 0:
                # this remove the extra '/' at the beginning of the word
                results.append(prefix[1:])
            for k, child_node in node.children.items():
                stack.append((child_node, f"{prefix}/{k}"))
        return results


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')
    prefix_tree = PrefixTree()

    prefix_tree.insert_word("abc")
    prefix_tree.insert_word("abc/def")
    prefix_tree.insert_word("abca")
    prefix_tree.insert_word("abc/def/ghi")
    prefix_tree.insert_word("abc/def/ghi")
    prefix_tree.insert_word("abc/def/ghi")
    prefix_tree.insert_word("abc/def/ghi/jkl")
    prefix_tree.insert_word("abc/def/ghijkl/jkl")
    prefix_tree.insert_word("def")
    print(prefix_tree.get_all_words())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

