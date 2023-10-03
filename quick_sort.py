def quick_sort(array):
    if len(array) < 2:
        # Base case: arrays with 0 or 1 element are already “sorted.”
        return array
    else:
        # Recursive case
        pivot = array[0]
        # Sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # Sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([2, 10, 5, 135, -123, .24]))
