# Iterators to Sum to K

In this practice, you will use iterators to make a function more efficient.

## Starter Code

You are given two files:

* `lllist.py`: contains the `LLList` class as implemented in the lessons; a linked-list implementation of the list ADT
* `sum.py`: a program that contains a function `sum_k()`, which counts the number of pairs of items in an `LLList` that sum to a value k

## Approach

The goal of this exercise is to make the `sum_k()` method more efficient. Currently, because it uses nested loops and calls `get_item(i)` on an `LLList` object, `sum_k()` is an `O(n^3)` function.

The code at the bottom of `sum.py` populates an `LLList` object with 1,000 items and checks how many pairs of those items sum to 50. However, because of the poor efficiency of the function, it currently takes a long time to complete.

Your task is to use iterators to implement the `sum_k()` function. By the time you're finished, the running time of `sum_k()` should be improved to `O(n^2)`.

## Steps to Complete

The only task for you to complete is to change the `sum_k()` method so that it uses iterators. To do so, you should:

* Call the `iterator()` method on the `LLList` object to construct one or more iterators
* Rearrange the function to call the `has_next()` and `next()` functions of the iterator as needed
* Make sure that you are not summing an item of the list with itself. In other words, you should only be checking whether `item_i + item_j == k` where `i != j`.

## Testing

The only test for this function is at the bottom of `sum.py`. There, a random number generated is seeded to guarantee the same set of random numbers (and therefore same count of pairs that sum to k) whenever the program is run.

Before adding iterators, the `sum_k()` function should be correct but should take multiple minutes to complete. After adding iterators, it should only take a few seconds.
