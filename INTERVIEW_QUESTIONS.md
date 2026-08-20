# Python Interview Questions

Commonly asked Python interview questions, each answered in its own
runnable file. Every file follows the same shape:

1. The **question** as an interviewer would ask it, at the top.
2. The **answer**, written out step by step in comments.
3. A `print(...)` demo at the bottom with the expected output.

Run any of them directly:

```bash
python arrays/max_subarray.py
```

---

## Arrays

| Question | File |
| --- | --- |
| Find two numbers that add up to a target | [two_sum.py](arrays/two_sum.py) |
| Find the duplicate numbers in a list | [find_duplicates.py](arrays/find_duplicates.py) |
| Find the missing number in a sequence | [missing_number.py](arrays/missing_number.py) |
| Find the second largest number | [second_largest.py](arrays/second_largest.py) |
| Largest sum of a contiguous subarray (Kadane's) | [max_subarray.py](arrays/max_subarray.py) |
| Move all zeroes to the end, in place | [move_zeroes.py](arrays/move_zeroes.py) |
| Merge overlapping intervals | [merge_intervals.py](arrays/merge_intervals.py) |
| Product of all other elements, without division | [product_except_self.py](arrays/product_except_self.py) |

## Strings

| Question | File |
| --- | --- |
| Check whether two strings are anagrams | [anagram.py](strings/anagram.py) |
| Find the first non-repeating character | [first_non_repeating.py](strings/first_non_repeating.py) |
| Count word frequency in a sentence | [word_frequency.py](strings/word_frequency.py) |
| Reverse the order of words in a sentence | [reverse_words.py](strings/reverse_words.py) |
| Check for a palindrome, ignoring punctuation | [palindrome_check.py](strings/palindrome_check.py) |
| Longest substring without repeating characters | [longest_unique_substring.py](strings/longest_unique_substring.py) |

## Hash maps

| Question | File |
| --- | --- |
| Find the k most frequent elements | [top_k_frequent.py](hash_maps/top_k_frequent.py) |
| Group words that are anagrams of each other | [group_anagrams.py](hash_maps/group_anagrams.py) |
| Count subarrays that sum to k (prefix sums) | [subarray_sum_k.py](hash_maps/subarray_sum_k.py) |

## Stacks

| Question | File |
| --- | --- |
| Check for balanced brackets | [valid_parentheses.py](stacks/valid_parentheses.py) |
| Design a stack with O(1) `get_min()` | [min_stack.py](stacks/min_stack.py) |
| Next greater element for every position | [next_greater_element.py](stacks/next_greater_element.py) |

## Recursion

| Question | File |
| --- | --- |
| nth Fibonacci number, then make it fast | [fibonacci_memo.py](recursion/fibonacci_memo.py) |
| Flatten an arbitrarily nested list | [flatten_nested_list.py](recursion/flatten_nested_list.py) |
| Generate all permutations of a list | [permutations.py](recursion/permutations.py) |

## Searching and sorting

| Question | File |
| --- | --- |
| Binary search a sorted list | [binary_search.py](searching_sorting/binary_search.py) |
| Sort a list of dicts by one or more fields | [sort_dicts_by_key.py](searching_sorting/sort_dicts_by_key.py) |
| Merge two sorted lists in O(n + m) | [merge_sorted_lists.py](searching_sorting/merge_sorted_lists.py) |

## Python language questions

These test knowledge of Python itself rather than algorithms, and come
up in almost every interview.

| Question | File |
| --- | --- |
| Why does a `[]` default argument leak between calls? | [mutable_default_argument.py](python_basics/mutable_default_argument.py) |
| Assignment vs shallow copy vs deep copy | [shallow_vs_deep_copy.py](python_basics/shallow_vs_deep_copy.py) |
| What is the difference between `is` and `==`? | [is_vs_equals.py](python_basics/is_vs_equals.py) |
| What do `*args` and `**kwargs` do? | [args_and_kwargs.py](python_basics/args_and_kwargs.py) |
| List comprehension vs generator expression | [list_vs_generator.py](python_basics/list_vs_generator.py) |
| What is a decorator? Write one. | [decorators_explained.py](python_basics/decorators_explained.py) |
| Why does this loop of lambdas print `[2, 2, 2]`? | [closures_and_late_binding.py](python_basics/closures_and_late_binding.py) |

## Data engineering

| Question | File |
| --- | --- |
| Retry an API call with backoff | [retry_decorator.py](data_engineer/retry_decorator.py) |
| Deduplicate records, keeping the latest | [deduplicate_latest.py](deduplicate_latest.py) |
| Validate rows against a schema | [schema_validation.py](schema_validation.py) |
| Top N per group | [top_n.py](top_n.py) |

---

## Complexity cheat sheet

| Pattern | Time | Used in |
| --- | --- | --- |
| Hash map lookup | O(1) average | two sum, group anagrams, subarray sum |
| Two pointers | O(n) | move zeroes, palindrome, merge sorted |
| Sliding window | O(n) | longest unique substring |
| Monotonic stack | O(n) | next greater element |
| Prefix sums | O(n) | subarray sum k, product except self |
| Binary search | O(log n) | binary search, insert position |
| Sort then sweep | O(n log n) | merge intervals |
| Backtracking | O(n * n!) | permutations |
