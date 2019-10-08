import itertools
import copy
from collections import Counter, defaultdict

# O(s * w!)
def calculate_anagrams_v1(word, text):
    if len(word) > len(text):
        raise "Word should be smaller than text"

    word_length = len(word)
    anagrams = [''.join(anagram) for anagram in itertools.permutations(word)]
    answers = []
    for i in range(len(text) - word_length + 1):
        for anagram in anagrams:
            if anagram == text[i : i+word_length]:
                answers.append(i)
    return answers

# O(s * w)
def calculate_anagrams_v2(word, text):
    if len(word) > len(text):
        raise "Word should be smaller than text"

    word_length = len(word)
    word_hash_table = Counter(word)
    answers = []
    for i in range(len(text) - word_length + 1):
        if word_hash_table == Counter(text[i : i+word_length]):
            answers.append(i)
    return answers


# O(s)
def calculate_anagrams(word, text):
    word_length = len(word)
    word_hashtable= Counter(word)

    # initial Counter
    answers = set()
    word_hashtable_tmp = defaultdict(int)
    word_hashtable_tmp.update(
        Counter(text[:word_length])
    )
    if word_hashtable == word_hashtable_tmp:
        answers.add(0)

    for i in range(word_length, len(text)):
        # Get and calculate previous element that is not on the substring anymore
        out_of_bound_element = text[i - word_length]
        out_of_bound_count = word_hashtable_tmp[out_of_bound_element] - 1

        # Get and calculate the element that showed in the substring
        inside_element = text[i]
        inside_element_count = word_hashtable_tmp[inside_element] + 1

        # If elements are equal, we do not need to update
        if inside_element != out_of_bound_element:
            word_hashtable_tmp.update({
                inside_element: inside_element_count,
                out_of_bound_element: out_of_bound_count
            })

            if out_of_bound_count == 0:
                del word_hashtable_tmp[out_of_bound_element]

        if word_hashtable == word_hashtable_tmp:
            # Get the beginning of the word
            answers.add(i - word_length + 1)

    # Could return a set, but I didn't want to change the assertions
    return list(answers)

assert calculate_anagrams('ab', 'abxaba') == [0, 3, 4]
assert calculate_anagrams('z', 'zzzzz') == [0, 1, 2, 3, 4]
assert calculate_anagrams('za', 'zazzz') == [0, 1]
assert calculate_anagrams('bcdefga', 'bcdefggha') == []
