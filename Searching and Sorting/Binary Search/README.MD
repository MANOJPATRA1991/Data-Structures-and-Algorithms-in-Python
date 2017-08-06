# BINARY SEARCH

> Best for ordered list of items

# Description

## Analysis of Binary Search

To analyze the binary search algorithm, we need to recall that each comparison eliminates about half of the remaining items from 
consideration. 

### What is the maximum number of comparisons this algorithm will require to check the entire list? 

If we start with n items, about n/2 items will be left after the first comparison. 

After the second comparison, there will be about n/4. 

Then n/8, n/16, and so on. 

| Comparisons | Approximate Number of Items Left |
|-------------|----------------------------------|
| 1           | n/2                              |
| 2           | n/4                              |
| 3           | n/8                              |
| ...         |                                  |
| i           | n/2<sup>i</sup>                  |


The number of comparisons necessary to get to this point is i where n/2<sup>i</sup> = 1. 

Solving for i gives us *i=log ⁡n*. 

The maximum number of comparisons is logarithmic with respect to the number of items in the list. 

Therefore, the binary search is **O(log⁡n)**.


#### Things to Consider

Even though a binary search is generally better than a sequential search, it is important to note that for small values of n, the additional cost of sorting is probably not worth it. In fact, we should always consider whether it is cost effective to take on the extra work of sorting to gain searching benefits. If we can sort once and then search many times, the cost of the sort is not so significant. However, for large lists, sorting even once can be so expensive that simply performing a sequential search from the start may be the best choice.



