def counting_sort(A):
    # Step 1: Find the maximum value in A to determine the range of input values
    k = max(A)

    # Step 2: Create a count array (C) of size k+1 and an output array (B) of the same length as A
    C = [0] * (k + 1)
    B = [0] * len(A)

    # Step 3: Count the occurrences of each value in A
    for j in range(len(A)):
        C[A[j]] += 1

    # Step 4: Update C to contain the number of elements less than or equal to each index
    for i in range(1, k + 1):
        C[i] += C[i - 1]

    # Step 5: Build the output array B
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    return B

# Example usage:
A = [87, 92, 55, 60, 75, 92, 40, 87, 95, 82, 70, 60, 55, 75, 85, 90, 92, 65, 70, 80]
sorted_A = counting_sort(A)
print("Before sorting: ", A)
print("After sorting: ", sorted_A)
