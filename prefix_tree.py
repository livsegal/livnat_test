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

    def reset_tree(self):
        self.head = TreeNode()

    def insert_word(self, word_to_add):
        curr = self.head
        word_array = word_to_add.split('/')
        for word in word_array:
            if word not in curr.children:
                curr.children[word] = TreeNode()
            curr = curr.children[word]

    def get_unique_words(self):
        results = []
        stack = [(self.head, "")]
        if not self.head.children:
            return results
        while stack:
            node, prefix = stack.pop()
            if not node.children:
                # this remove the extra '/' at the beginning of the word
                results.append(prefix[1:])
            for k, child_node in node.children.items():
                stack.append((child_node, f"{prefix}/{k}"))
        return results


def test_trie_work_as_expected(prefixes, expected_results):
    prefix_tree = PrefixTree()
    prefix_tree.insert_words(prefixes)
    assert set(prefix_tree.get_unique_words()) == set(expected_results)


def test_interview_example():
    prefixes = ["abc", "abc/def", "abca", "abc/def/ghi", "abc/def/ghi", "abc/def/ghi/jkl", "abc/def/ghijkl/jkl", "def"]
    expected_result = ['def', 'abca', 'abc/def/ghijkl/jkl', 'abc/def/ghi/jkl']
    test_trie_work_as_expected(prefixes, expected_result)


def test_duplicates_prefixes_return_only_one():
    prefixes = ["abc/def/ghi", "abc/def/ghi"]
    expected_result = ["abc/def/ghi"]
    test_trie_work_as_expected(prefixes, expected_result)


def test_no_overlapping_prefixes():
    prefixes = ["abc", "def", "ghp", "hca/def/abc/ghp"]
    expected_result = ['hca/def/abc/ghp', 'ghp', 'def', 'abc']
    test_trie_work_as_expected(prefixes, expected_result)


def test_diffrenciate_between_lower_upper_case():
    prefixes = ["abc", "ABC", ]
    expected_result = ["ABC", "abc"]
    test_trie_work_as_expected(prefixes, expected_result)


def test_empty():
    prefixes = []
    expected_result = []
    test_trie_work_as_expected(prefixes, expected_result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_interview_example()
    test_duplicates_prefixes_return_only_one()
    test_no_overlapping_prefixes()
    test_empty()
    test_diffrenciate_between_lower_upper_case()
