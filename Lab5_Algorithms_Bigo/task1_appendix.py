

import random

# Student-specific inputs
STUDENT_ID = "TUPM-26-1848"
SEED_NUM = 8

# Generate unique incident records
student_seed = SEED_NUM + sum(ord(char) for char in STUDENT_ID)
rng = random.Random(student_seed)

original_records = sorted(rng.sample(range(1000, 9999), 12))

# Rotate the records
rotation = SEED_NUM % (len(original_records) - 1) + 1
rotated_records = original_records[rotation:] + original_records[:rotation]

# Select target incident
target_index = (SEED_NUM * 3) % len(rotated_records)
target = rotated_records[target_index]


def binary_search_rotated(records, target):
    left = 0
    right = len(records) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if records[mid] == target:
            return mid, comparisons

        if records[left] <= records[mid]:
            if records[left] <= target < records[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if records[mid] < target <= records[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1, comparisons


def linear_search(records, target):
    comparisons = 0

    for index, record in enumerate(records):
        comparisons += 1

        if record == target:
            return index, comparisons

    return -1, comparisons


# Search using both algorithms
binary_position, binary_comparisons = binary_search_rotated(
    rotated_records, target
)

linear_position, linear_comparisons = linear_search(
    rotated_records, target
)

# Final output
print("=" * 45)
print("EMERGENCY DISPATCH RECORD SEARCH")
print("=" * 45)

print("Student ID:", STUDENT_ID)
print("Seed Number:", SEED_NUM)

print("\nOriginal Incident Records:")
print(original_records)

print("\nRotation Amount:", rotation)

print("\nRotated Incident Records:")
print(rotated_records)

print("\nTarget Incident:", target)

print("\nBINARY SEARCH ON ROTATED ARRAY")
if binary_position != -1:
    print("Position (1-based):", binary_position + 1)
else:
    print("Target incident not found.")

print("Equality Comparisons:", binary_comparisons)

print("\nLINEAR SEARCH")
if linear_position != -1:
    print("Position (1-based):", linear_position + 1)
else:
    print("Target incident not found.")

print("Equality Comparisons:", linear_comparisons)

print("\nCOMPLEXITY ANALYSIS")
print("Rotated Binary Search: O(log n) time")
print("Linear Search: O(n) time")
print("Auxiliary Space: O(1) for both algorithms")
print("=" * 45)
