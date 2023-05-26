def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return ('', '', False)

    sorted_string1 = ''.join(sorted_chars(first_string.lower()))
    sorted_string2 = ''.join(sorted_chars(second_string.lower()))

    is_anagram = sorted_string1 == sorted_string2

    return sorted_string1, sorted_string2, is_anagram


def sorted_chars(string):
    chars = list(string)

    quicksort(chars, 0, len(chars) - 1)

    return ''.join(chars)


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1
