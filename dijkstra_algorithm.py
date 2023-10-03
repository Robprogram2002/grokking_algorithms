# To code this example, you’ll need three hash tables. You’ll update the costs and parents hash tables as the algorithm
# progresses. First, you need to implement the graph. You’ll use a hash table for that like earlier.
#
# But this time, you need to store the neighbors and the cost for getting to
# that neighbor. How do you represent the weights of those edges? Why not just use
# another hash table?
#
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# So graph["start"] is a hash table. You can get all the neighbors for Start like this:
print(graph["start"].keys())
# cost for node a
print(graph["start"]["a"])

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# Next you need a hash table to store the costs for each node.

# The cost of a node is how long it takes to get to that
# node from the start. You know it takes 2 minutes from
# Start to node B. You know it takes 6 minutes to get to
# node A (although you may find a path that takes less
# time). You don’t know how long it takes to get to the
# finish. If you don’t know the cost yet, you put down
# infinity

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")

# You also need another hash table for the parents:

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Finally, you need an array to keep track of all the nodes you’ve already
# processed, because you don’t need to process a node more than once:

processed = []


# That’s all the setup. Now let’s look at the algorithm


def dijkstra_algorithm(costs):
    node = find_lowest_cost_node(costs)  # Find the lowest-cost node that you haven't processed yet
    while node is not None:  # If you’ve processed all the nodes, this while loop is done.
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # Go through all the neighbors of this node.
            new_cost = cost + neighbors[n]  # calculate the new cost
            if costs[n] > new_cost:  # If it’s cheaper to get to this neighbor by going through this node
                costs[n] = new_cost  # update it costs
                parents[n] = node  # and its parent node. This node becomes the new parent for this neighbor
        processed.append(node)  # Mark the node as processed.
        node = find_lowest_cost_node(costs)  # Find the next node to process, and loop.


def find_lowest_cost_node(node_costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in node_costs:  # Go through each node.
        current_cost = node_costs[node]
        # If it’s the lowest cost so far and hasn’t been processed yet …
        if current_cost < lowest_cost and node not in processed:
            # set it as the new lowest-cost node.
            lowest_cost = current_cost
            lowest_cost_node = node
    return lowest_cost_node
