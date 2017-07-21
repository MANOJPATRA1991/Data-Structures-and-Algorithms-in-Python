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



