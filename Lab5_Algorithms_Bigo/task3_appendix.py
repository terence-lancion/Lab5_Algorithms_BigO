
from time import perf_counter

STUDENT_ID = "TUPM-26-1845"
LAST_NAME = "LANCION"
FAVORITE_ARTIST = "CUP OF JOE"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(c) for c in STUDENT_ID if c.isdigit())
ARTIST_SUM = sum(
    ord(c) - ord("A") + 1
    for c in FAVORITE_ARTIST.upper() if c.isalpha()
)

# Generate the same 12 unique order numbers for every test.
orders = [
    ((ID_SUM * 3) + i * (SEED_DIGIT + 3) + ARTIST_SUM) % 1000
    for i in range(12)
]
orders = sorted(set(orders))
while len(orders) < 12:
    orders.append(orders[-1] + 1)
orders = sorted(orders)

def bubble_sort(data):
    a = data.copy()
    comparisons = movements = 0
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                movements += 1
                swapped = True
        if not swapped:
            break
    return a, comparisons, movements

def selection_sort(data):
    a = data.copy()
    comparisons = movements = 0
    for i in range(len(a) - 1):
        minimum = i
        for j in range(i + 1, len(a)):
            comparisons += 1
            if a[j] < a[minimum]:
                minimum = j
        if minimum != i:
            a[i], a[minimum] = a[minimum], a[i]
            movements += 1
    return a, comparisons, movements

def insertion_sort(data):
    a = data.copy()
    comparisons = movements = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] <= key:
                break
            a[j + 1] = a[j]
            movements += 1
            j -= 1
        a[j + 1] = key
        movements += 1
    return a, comparisons, movements

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
}

conditions = {
    "Sorted": orders.copy(),
    "Reverse": orders[::-1],
    "Random": sorted(
        orders,
        key=lambda x: (x * SEED_DIGIT + ID_SUM) % 997
    ),
}

print("APPENDIX 3: E-COMMERCE ORDER PROCESSING")
print("Generated orders:", orders)

for condition, data in conditions.items():
    print(f"\n{condition} input: {data}")

    for name, algorithm in algorithms.items():
        start = perf_counter()
        result, comparisons, movements = algorithm(data)
        elapsed = (perf_counter() - start) * 1_000_000

        verified = result == sorted(orders)

        print(f"{name}:")
        print("  Sorted result:", result)
        print("  Comparisons:", comparisons)
        print("  Movements:", movements)
        print(f"  Execution time: {elapsed:.2f} microseconds")
        print("  Verification:", "PASS" if verified else "FAIL")

print("\nCOMPLEXITY ANALYSIS")
print("Bubble Sort: Best O(n), Average/Worst O(n^2)")
print("Selection Sort: Best/Average/Worst O(n^2)")
print("Insertion Sort: Best O(n), Average/Worst O(n^2)")
print("Auxiliary space: O(1) for all three algorithms")
