
# APPENDIX 2: UNIVERSITY ENROLLMENT RECORDS

STUDENT_ID = "TUPM-26-1845"
LAST_NAME = "LANCION"
FAVORITE_ARTIST = "CUP OF JOE"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(ch) for ch in STUDENT_ID if ch.isdigit())
ARTIST_LENGTH = len(FAVORITE_ARTIST)
NAME_LENGTH = len(LAST_NAME)


def merge_sorted(a, b):
    i = j = comparisons = 0
    merged = []

    while i < len(a) and j < len(b):
        comparisons += 1

        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged, comparisons


def exercise2():
    dataset_a = [
        1000 + SEED_DIGIT * 10 + i * 3
        for i in range(8)
    ]

    dataset_b = [
        1000 + ARTIST_LENGTH * 10 + i * (NAME_LENGTH + 1)
        for i in range(7)
    ]

    merged, comparisons = merge_sorted(dataset_a, dataset_b)

    print("APPENDIX 2: UNIVERSITY ENROLLMENT RECORDS")
    print("Department A dataset:", dataset_a)
    print("Department B dataset:", dataset_b)
    print("Consolidated dataset:", merged)
    print("Records before consolidation:",
          len(dataset_a) + len(dataset_b))
    print("Records after consolidation:", len(merged))
    print("Merge comparisons:", comparisons)
    print("Ordering verification:",
          "PASS" if merged == sorted(dataset_a + dataset_b)
          else "FAIL")
    print("Time complexity: O(n + m)")
    print("Auxiliary space complexity: O(n + m)")


if __name__ == "__main__":
    exercise2()
