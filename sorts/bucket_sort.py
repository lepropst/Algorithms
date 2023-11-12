from sorts.insertion_sort import insertionSort


def bucketSort(x: list) -> list:
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    print(f"Number of buckets = 10\nmin = 0 max = {x}")
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets

    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)
        print(f"Inserted {j} at {index_b}")

    # Sort individual buckets
    for i in range(slot_num):
        print(f"Sorting {i} {arr[i]}")
        arr[i] = insertionSort(arr[i])

    # concatenates the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    print(x)
    return x
