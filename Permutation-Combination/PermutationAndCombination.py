"""
"My fruit salad is a combination of apples, grapes and bananas" We don't care what order the fruits are in, they could also be "bananas, grapes and apples" or "grapes, apples and bananas", its the same fruit salad.
"The combination to the safe is 472". Now we do care about the order. "724" won't work, nor will "247". It has to be exactly 4-7-2.

So, in Mathematics we use more precise language:
    When the order doesn't matter, it is a Combination.
    When the order does matter it is a Permutation.
"""
from itertools import permutations, combinations

text = 'ravi'
perm_list = ["".join(p) for p in permutations(text)]
print(perm_list)


# distinct Combination of 2 letter words
comb_list = ["".join(c) for c in combinations(text, 2)]
print(comb_list)


# distinct Combination of 3 letter words
comb_list = ["".join(c) for c in combinations(text, 3)]
print(comb_list)
