# Let’s write a function to find the smallest element  in an array:
def find_smallest(list_a):
    # Stores the smallest value
    smallest = list_a[0]
    # Stores the index of the smallest value
    index = 0
    for i in range(1, len(list_a)):
        if list_a[i] < smallest:
            smallest = list_a[i]
            index = i
    return index


# Now you can use this function to write selection sort:
def selection_sort(arr):
    sorted_array = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        # Finds the smallest element in the array,  adds it to the new array
        # and remove it from the original array
        sorted_array.append(arr.pop(smallest_index))
    return sorted_array


# Test
print(selection_sort([5, 3, 6, 2, 10]))
