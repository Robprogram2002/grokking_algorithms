# The binary_search function takes a sorted array and an item. If the
# item is in the array, the function returns its position. You’ll keep track
# of what part of the array you have to search through.

def binary_search(a_list, item):
    # start and end  keep track of which part of the list you’ll search in.
    start = 0
    end = len(a_list) - 1
    while start <= end:  # While you haven’t narrowed it down  to one element
        middle_point = (start + end) // 2
        guess = a_list[middle_point]
        if guess == item:
            return middle_point
        elif item < guess:
            # The guess was too high
            end = middle_point - 1
        else:
            # The guess was too low
            start = middle_point + 1
    # The item doesn’t exist.
    return None


# Let's test it
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None

