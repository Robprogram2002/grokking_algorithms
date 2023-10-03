# To recap, here’s how the implementation will work
from collections import deque

# model the problem as a graph
graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"],
         "anuj": [], "peggy": [], "thom": [], "jonny": []}


def bread_first_search(name):
    # Make a queue to start. It will contain the people to check
    search_queue = deque()
    # Adds all of your neighbors to the search queue
    search_queue += graph[name]
    searched = []
    # Loop until the queue is empty
    while search_queue:
        # grabs the first person off the queue
        person = search_queue.popleft()
        # check if the person has been checked before
        if person not in searched:
            # check if the person is a mango seller
            if person_is_seller(person):
                # if it is, you are done
                print("person is a mango seller")
                return True
            else:
                # If not, then, add all their neighbors to the queue
                search_queue += graph[person]
                # and add the person to the people checked list
                searched.append(person)
    # if the queue is empty, there is not a mango seller in your network
    return False


# One final thing: you still need a person_is_seller function to tell you
# when someone is a mango seller. Here’s one:
def person_is_seller(name):
    return name[-1] == "m"


# This function checks whether the person’s name ends with the letter m.
# If it does, they’re a mango seller. Kind of a silly way to do it, but it’ll do
# for this example

bread_first_search("you")
