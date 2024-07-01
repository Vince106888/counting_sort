# Counting Sort Implementation

This project contains a Python implementation of the counting sort algorithm. 

## Overview

Counting sort is an efficient sorting algorithm that works for a range of non-negative integer values. The algorithm processes the input array to determine the count of each unique value and then uses this information to sort the array.

## Example

Consider an example where `A = [0, 2, 1, 4, 6, 2, 1, 1, 0, 3, 7, 7, 9]` with `k = 9` and `n = 13`:

1. **Initialization**: Create `C` with size `k + 1 = 10` and `B` as the output array.
2. **Counting Frequencies**: Increment counts in `C` for each element in `A`. After this step, `C` might look like `[2, 3, 2, 1, 1, 0, 1, 2, 0, 1]`.
3. **Cumulative Counts**: Adjust `C` to have cumulative counts. After this step, `C` could be `[2, 5, 7, 8, 9, 9, 10, 12, 12, 13]`.
4. **Placement in Output Array**: Place elements from `A` into `B` based on their positions in `C`, decrementing counts in `C` after placing each element.
5. **Final Sorted Output**: `B = [0, 0, 1, 1, 1, 2, 2, 3, 4, 6, 7, 7, 9]`.
