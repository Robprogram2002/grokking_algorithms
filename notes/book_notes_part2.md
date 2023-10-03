## Chapter 6: Breadth-first Search

Graph algorithms are some of the most useful algorithms .
Breadth-first search allows you to find the shortest distance
between two things. But shortest distance can mean a lot of things!

##### Introduction to graphs
Suppose you’re in San Francisco, and you want to go from Twin Peaks
to the Golden Gate Bridge. You want to get there by bus, with the
minimum number of transfers. What’s your algorithm to find the path with the fewest steps?

This type of problem is called a **shortest-path
problem**. You’re always trying to find the shortest something. It could
be the shortest route to your friend’s house. It could be the smallest
number of moves to checkmate in a game of chess. The algorithm to
solve a shortest-path problem is called **breadth-first search**.

To figure out how to get from Twin Peaks to the Golden Gate Bridge,
there are two steps:

1. Model the problem as a graph.

2. Solve the problem using breadth-first search.

### What is a graph?

A graph models a set of connections. Each graph is made up of **nodes** and **edges**.

        Alex  ----------->  John
        Node     Edge       Node

That’s all there is to it! Graphs are made up of nodes and edges. A node
can be directly connected to many other nodes. Those nodes are called
its **neighbors**.

Graphs are a way to model how different things are connected to one another.

### Breadth-first search

Breadth-first search  is a different kind of search algorithm: one that runs on
graphs. It can help answer two types of questions:

* Question type 1: Is there a path from node A to node B?

* Question type 2: What is the shortest path from node A to node B?

Now let’s look at the  algorithm in more detail. You’ll ask a question of type 1: “Is there a
path?”. Suppose you’re the proud owner of a mango farm. You’re looking for a
mango seller who can sell your mangoes. Are you connected to a mango
seller on Facebook? Well, you can search through your friends

This search is pretty straightforward. First, make a list of friends to search.
Now, go to each person in the list and check whether that person sells
mangoes. Suppose none of your friends are mango sellers. Now you have to
search through your friends’ friends.

Each time you search for someone from the list, add all of their friends
to the list

This way, you not only search your friends, but you search their friends,
too. Remember, the goal is to find one mango seller in your network.
So if Alice isn’t a mango seller, you add her friends to the list, too. That
means you’ll eventually search her friends—and then their friends, and
so on. *With this algorithm, you’ll search your entire network until you
come across a mango seller*. This algorithm is breadth-first search.

You saw how to answer question 1: Is there a mango seller in your network?
now let’s try to answer question 2: Who is the closest mango seller?

Can you find the closest mango seller? For example, your friends
are first-degree connections, and their friends are second-degree
connections.

You’d prefer a first-degree connection to a second-degree connection,
and a second-degree connection to a third-degree connection, and so
on. So you shouldn’t search any second-degree connections before you
make sure you don’t have a first-degree connection who is a mango
seller. Well, breadth-first search already does this! The way breadth-first
search works, the search radiates out from the starting point. So you’ll
check first-degree connections before second-degree connections

Another way to see this is, *first-degree connections
are added to the search list before second-degree
connections*.

You just go down the list and check people to see
whether each one is a mango seller. The first-degree
connections will be searched before the second degree connections, so you’ll find the mango seller
closest to you.

> *Breadth-first search not only finds a
path from A to B, it also finds the shortest path.*

Notice that this only works if you search people in the same order in
which they’re added. That is, if Claire was added to the list before Anuj,
Claire needs to be searched before Anuj. What happens if you search
Anuj before Claire, and they’re both mango sellers? Well, Anuj is a
second-degree contact, and Claire is a first-degree contact. You end up
with a mango seller who isn’t the closest to you in your network. So
you need to search people in the order that they’re added. There’s a data
structure for this: it’s called a **queue**.

#### Queues

A queue works exactly like it does in
real life. Suppose you and your friend
are queueing up at the bus stop. If you’re
before him in the queue, you get on the
bus first. A queue works the same way.
Queues are similar to stacks. You can’t
access random elements in the queue.
Instead, there are two only operations,
*enqueue and dequeue*

If you enqueue two items to the list, the first item you added will be
dequeued before the second item. You can use this for your search list!
People who are added to the list first will be dequeued and searched
first.

>The queue is called a FIFO data structure: First In, First Out.


>In contrast, a stack is a LIFO data structure: Last In, First Out.

### Implementing the graph

First, you need to implement the graph in code. How do you express a relationship like “you -> bob”?
Luckily, you know a data structure that lets you express
relationships: a hash table! Remember, a hash table allows you to map a key to a
value. In this case, *you want to map a node to all of its
neighbors*.

Here’s how you’d write it in Python:

    graph = {}
    graph = ["you"] = ["alice", "bob", "claire"]

Notice that “you” is mapped to an array. So graph[“you”] will give you
an array of all the neighbors of “you”.

A graph is just a bunch of nodes and edges, so this is all you need to
have a graph in Python. What about a bigger graph?

    graph = {}
    graph[“you”] = [“alice”, “bob”, “claire”]
    graph[“bob”] = [“anuj”, “peggy”]
    graph[“alice”] = [“peggy”]
    graph[“claire”] = [“thom”, “jonny”]
    graph[“anuj”] = []
    graph[“peggy”] = []
    graph[“thom”] = []
    graph[“jonny”] = []

Pop quiz: does it matter what order you add the key/value pairs in?

Answer: It doesn’t matter. Hash tables have no ordering, so it doesn’t matter what order you add
key/value pairs in.

Anuj, Peggy, Thom, and Jonny don’t have any neighbors. They have
arrows pointing to them, but no arrows from them to someone else.
This is called a **directed graph**—the relationship is only one way. So Anuj
is Bob’s neighbor, but Bob isn’t Anuj’s neighbor. An **undirected graph**
doesn’t have any arrows, and both nodes are each other’s neighbors.

Alice and Bob share a friend: Peggy. So Peggy will be added to the
queue twice: once when you add Alice’s friends, and again when you
add Bob’s friends. You’ll end up with two Peggys in the search queue

But you only need to check Peggy once to see whether she’s a mango
seller. If you check her twice, you’re doing unnecessary, extra work. So
once you search a person, you should mark that person as searched and
not search them again.

If you don’t do this, you could also end up in an infinite loop

> *Before checking a person, it’s important to make sure
they haven’t been checked already. To do that, you’ll
keep a list of people you’ve already checked.*

#### Running time

If you search your entire network for a mango seller, that means you’ll
follow each edge. So the running time is at least *O(number of edges)*. You also keep a queue of every person to search.
Adding one person to  the queue takes constant time: O(1). Doing this for every person will
take *O(number of people)* total. Breadth-first search takes *O(number of
people + number of edges)*, and it’s more commonly written as **O(V+E)**
(V for number of vertices, E for number of edges)


## Chapter 7: Dijkstra’s algorithm

In the last chapter, you figured out a way to get from point A to point B.
It’s not necessarily the fastest path. It’s the shortest path, because it has
the least number of segments. But suppose you add
travel times to those segments. Now you see that there’s a faster path

Breadth-first search will find you the path with the fewest segments. What if you want the fastest path instead?
You can do that fastest with a different algorithm called *Dijkstra’s algorithm*.

There are four steps to Dijkstra’s algorithm:

1. Find the “cheapest” node. This is the node you can get to in the least
amount of time (they would be the first movements).

2. Update the costs of the neighbors of this node

3. Repeat until you’ve done this for every node in the graph.

4. Calculate the final path.

**Step 1:** Find the cheapest node. You’re standing at the start, wondering
if you should go to node A or node B. How long does it take to get to
each node? It takes 6 minutes to get to node A and 2 minutes to get to node B.
The rest of the nodes, you don’t know yet.

Because you don’t know how long it takes to get  to the finish yet, you put down infinity
(you’ll see why soon). Node B is the closest node … it’s 2 minutes away.

        Node    Time To Node
         A           6
         B           2
       Finish       inf

**Step 2:** Calculate how long it takes to get to all of node B’s neighbors by
following an edge from B.

From node B takes 3 min to get to node A and 5 min to get to the Finish. So the total costs are (passing from node B)

        Node    Time
         A     2+3 = 5  (lower than previus cost 6)
         B       2
       Finish  2+5 = 7 (lower than previus cost inf)

Hey, you just found a shorter path to node A! It used to take 6 minutes
to get to node A. But if you go through node B, there’s a path that only takes 5 minutes!

When you find a shorter path for a neighbor of B, update its cost. In this
case, you found

* A shorter path to A (down from 6 minutes to 5 minutes)

* A shorter path to the finish (down from infinity to 7 minutes)

**Step 3:** Repeat!

**Step 1 again:** Find the node that takes the least amount of time
to get to. You’re done with node B, so node A has the next smallest
time estimate.

**Step 2 again:** Update the costs for node A’s neighbors. From node A takes 1 min to get to the finish
and 3 to get to node B. So the total cost passing from A are:

        Node     Timme
         A         5  (the current lower cost for these node)
         B      5+3 = 8 (greater than its current lower cost, so no need to update)
       Finsih   5+1 = 6 (lower than the previus cost, must be update it)

Woo, it takes 6 minutes to get to the finish now!

You’ve run Dijkstra’s algorithm for every node (you don’t need to run it
for the finish node). At this point, you know

* It takes 2 minutes to get to node B.

* It takes 5 minutes to get to node A.

* It takes 6 minutes to get to the finish

(Note that you only keep track of the lower cost for each node parting from the start, and you only update the
cost of a node when you find a path wit a lower cost to it)

I’ll save the last step, calculating the final path, for the next section. For now, just see the fianl path

        Start ---> Node B ---> Node A ---> Finish

Breadth-first search wouldn’t have found this as the shortest path,
because it has three segments. And there’s a way to get from the start to
the finish in two segments

In the last chapter, you used breadth-first search to find the shortest
path between two points. Back then, “shortest path” meant the path
with the fewest segments. But in Dijkstra’s algorithm, you assign a
number or **weight** to each segment. *Then Dijkstra’s algorithm finds the
path with the smallest total weight*.

###### Terminology

When you work with Dijkstra’s algorithm, each edge in the graph has a
number associated with it. These are called **weights**. A graph with weights is called a **weighted graph**.
A graph without weights is called an **unweighted graph**.

> To calculate the shortest path in an unweighted graph, use breadth-first
search. To calculate the shortest path in a weighted graph, use Dijkstra’s
algorithm.


Graphs can also have **cycles**. It means you can start at a node, travel around, and end up at the same
node. (...) So following the cycle will never give you the shortest path. An undirected graph means that both nodes
point to each other. That’s a cycle!

With an undirected graph, each edge adds another cycle. *Dijkstra’s algorithm only works with **directed acyclic graphs**,
called **DAGs** for short*

###### Trading a Piano
Enough terminology, let’s look at another example! Rama is trying to trade a music book for a piano.
In this graph, the nodes are all the items Rama can trade for. The
weights on the edges are the amount of money he would have to pay
to make the trade. So he can trade the poster for the guitar for $30, or
trade the LP for the guitar for $15. How is Rama going to figure out
the path from the book to the piano where he spends the least dough
Dijkstra’s algorithm to the rescue!

Before you start, you need some
setup. Make a table of the cost for
each node. The cost of a node is how
expensive it is to get to.

You’ll keep updating this table as the algorithm goes on. *To calculate the
final path, you also need a parent column on this table*.

**Step 1:** Find the cheapest node. In this case, the poster is the cheapest
trade, at $0. Is there a cheaper way to trade for the poster? This is a
really important point, so think about it. Can you see a series of trades
that will get Rama the poster for less than $0?

Answer: No. *Because the poster is the cheapest node Rama can get
to, there’s no way to make it any cheaper.* This is the key idea behind Dijkstra’s algorithm: *Look at the cheapest
node on your graph. There is no cheaper way to get to this node!*

**Step 2:** Figure out how long it takes to get to its neighbors (the cost).

You have prices for the bass guitar and the drum set in the table. Their
value was set when you went through the poster, so the poster gets set
as their parent. That means, to get to the bass guitar, you follow the edge
from the poster, and the same for the drums

        Parent          Node        Cost
      Book (Start)       LP          5
      Book (Start)     Poster        0
      Poster           Guitar       0+30 (its lower than the previus cost inf, update it)
      Poster           Drums        0+35 (its lower than the previus cost inf, update it)
      -----          Piano (End)    inf

(You have updated the cost for Guitar and Drums from inf to 30 and 35. And since to get to they you have to pass from
node Poster, this node is set as they parent node. )

**Step 1 again:** The LP is the next cheapest node at $5.

**Step 2 again:** Update the values of all of its neighbors

From LP takes 15 to get to the guitar and 20 to get to the drums so the total cost from these nodes are 15+5=20
and 20+5=25. You node that the cost for these nodes is lower than the previous lower cost passing from Poster node.
So you must update the new lower cost for the guitar and drums nodes, and also you must update the parent column
since  That means it’s cheaper to get to the drums and guitar by following the edge
from the LP. So you set the LP as the new parent for both instruments.

        Parent          Node        Cost
      Book (Start)       LP          5
      Book (Start)     Poster        0
      LP               Guitar       20
      LP               Drums        25
      -----          Piano (End)    inf

The bass guitar is the next cheapest item. Update its neighbors. Ok, you finally have a price for the piano, by trading
the guitar for the piano. So you set the guitar as the parent.

        Parent          Node        Cost
      Book (Start)       LP          5
      Book (Start)     Poster        0
      LP               Guitar       20
      LP               Drums        25
      Guitar          Piano (End)  20+20=40

Finally, the last node, the drum set.

        Parent          Node        Cost
      Book (Start)       LP          5
      Book (Start)     Poster        0
      LP               Guitar       20
      LP               Drums        25
      Drums          Piano (End)  25+10=35


Rama can get the piano even cheaper by trading the drum set for the
piano instead. *So the cheapest set of trades will cost Rama $35*.

**Calculating the path:** Now, as I promised, you need to figure out the path. So far, you know
that the shortest path costs $35, but how do you figure out the path? To
start with, look at the parent for piano.

Let’s see how you’d follow the edges. Piano has drums as its parent. And drums has the LP as its parent.
And Lp has the book (the start) as its parent.

So, By following the parents backward, you now have the complete path.

**Note :** So far, I’ve been using the term shortest path pretty literally: calculating
the shortest path between two locations or between two people. I
hope this example showed you that the shortest path doesn’t have to
be about physical distance. It can be about minimizing something. In
this case, Rama wanted to minimize the amount of money he spent.
Thanks, Dijkstra!

#### Negative-weight edges

Suppose Sarah offers to trade the LP for the poster, and
she’ll give Rama an additional $7. It doesn’t cost Rama
anything to make this trade; instead, he gets $7 back.
How would you show this on the graph?

The edge from the LP to the poster has a negative weight! Rama
gets $7 back if he makes that trade. So it makes sense to do the second trade—Rama gets $2 back that way!
The second path costs him $2 less, so he should take that path, right?
Well, guess what? If you run Dijkstra’s algorithm on this graph, Rama
will take the wrong path. He’ll take the longer path.

> *You can’t use Dijkstra’s algorithm if you have negative-weight edges. Negative-weight
edges break the algorithm.*

Why this happens?  Remember the answer to this question.

(....) You already processed the poster node, but you’re updating the cost for
it. This is a big red flag. Once you process a node, it means there’s no
cheaper way to get to that node. But you just found a cheaper way to
the poster!

Dijkstra’s algorithm assumed that because you were processing the poster node, there was
no faster way to get to that node. That assumption only works if you
have no negative-weight edges. So ***you can’t use negative-weight edges
with Dijkstra’s algorithm***. If you want to find the shortest path in a graph
that has negative-weight edges, there’s an algorithm for that! It’s called
the **Bellman-Ford algorithm**

### Implementation
(...)

## Chapter 8: greedy algorithms

**Example1 :** Suppose you have a classroom and want to hold as many classes
here as possible. You get a list of classes. You can’t hold all of these classes in there, because some of them
overlap.

You want to hold as many classes as possible in this classroom. How
do you pick what set of classes to hold, so that you get the biggest set of
classes possible? Sounds like a hard problem, right? Actually, the algorithm is so easy, it
might surprise you. Here’s how it works:

1. Pick the class that ends the soonest. This is the first class you’ll hold
in this classroom.

2. Now, you have to pick a class that starts after the first class.
Again, pick the class that ends the soonest. This is the second
class you’ll hold

Keep doing this, and you’ll end up with the answer!

Believe it or not, this simple algorithm finds the optimal solution to this
scheduling problem!

> *A greedy algorithm is simple: at each step, pick the optimal move. In technical terms: at each step you pick
the **locally optimal solution**, and in the end you’re left with the **globally optimal solution***

Obviously, greedy algorithms don’t always work. But they’re simple to write!

### The knapsack problem

Suppose you’re a greedy thief. You’re in a store with a
knapsack, and there are all these items you can steal.
But you can only take what you can fit in your knapsack.
The knapsack can hold 35 pounds. You’re trying to maximize the value of the items you put
in your knapsack. What algorithm do you use?

Again, the greedy strategy is pretty simple:

1. Pick the most expensive thing that will fit in your
knapsack.

2. Pick the next most expensive thing that will fit in
your knapsack. And so on

Except this time, it doesn’t work!

Your knapsack can hold 35 pounds of items. The stereo system is
the most expensive, so you steal that. Now you don’t have space for
anything else since the stereo wight 35 pounds.

You got $3,000 worth of goods. But wait! If you’d picked the laptop (20lbs) and
the guitar (15lbs) instead, you could have had $3,500 worth of loot!

Clearly, the greedy strategy doesn’t give you the optimal solution here.
But it gets you pretty close. In the next chapter, I’ll explain how to
calculate the correct solution. But if you’re a thief in a shopping center,
you don’t care about perfect. “Pretty good” is good enough.

> *sometimes, perfect is the
enemy of good. Sometimes all you need is an algorithm that solves the
problem pretty well. And that’s where greedy algorithms shine, because
they’re simple to write and usually get pretty close.*

Let’s look at one last example. This is an example where greedy
algorithms are absolutely necessary.

### The set-covering problem

Suppose you’re starting a radio show. You want to
reach listeners in all 50 states. You have to decide what
stations to play on to reach all those listeners. It costs
money to be on each station, so you’re trying to minimize the
number of stations you play on. You have a list of stations.

Each station covers a region, and
there’s overlap. How do you figure out the smallest set of
stations you can play on to cover all 50
states? Sounds easy, doesn’t it? Turns out
it’s extremely hard. Here’s how to do it:

1. List every possible subset of stations. This is called the **power set**. There are
2^n possible subsets.

2. From these, pick the set with the smallest number of stations that
covers all 50 states.

The problem is, it takes a long time to calculate every possible subset
of stations. It takes O(2^n) time, because there are 2^n stations. It’s
possible to do if you have a small set of 5 to 10 stations. But with all
the examples here, think about what will happen if you have a lot of
items. It takes much longer if you have more stations.

> There’s no algorithm that solves it fast enough! What can you do?

### Approximation algorithms

Greedy algorithms to the rescue! Here’s a greedy algorithm that comes
pretty close:

1. Pick the station that covers the most states that haven’t been covered
yet. It’s OK if the station covers some states that have been covered
already.

2. Repeat until all the states are covered

This is called an *approximation algorithm*. When calculating the exact
solution will take too much time, an approximation algorithm will
work. Approximation algorithms are judged by

* How fast they are

* How close they are to the optimal solution

Greedy algorithms are a good choice because not only are they simple
to come up with, but that simplicity means they usually run fast, too.
In this case, the greedy algorithm runs in O(n^2) time, where n is the
number of radio stations.

For this example, I’m going to use a subset of the states and the stations
to keep things simple.
First, make a list of the states you want to cover:

        states_needed = set([“mt”, “wa”, “or”, “id”, “nv”, “ut”, “ca”, “az”])

I used a set for this. A set is like a list, except that each item can show up
only once in a set. Sets can’t have duplicates.

You also need the list of stations that you’re choosing from. I chose to
use a hash for this:

    stations = {}
    stations[“kone”] = set([“id”, “nv”, “ut”])
    stations[“ktwo”] = set([“wa”, “id”, “mt”])
    stations[“kthree”] = set([“or”, “nv”, “ca”])
    stations[“kfour”] = set([“nv”, “ut”])
    stations[“kfive”] = set([“ca”, “az”])

The keys are station names, and the values are the states they cover. All the values are sets, too.
Making everything a set will make your life  easier, as you’ll see soon.
Finally, you need something to hold the final set of stations you’ll use:

        final_stations = set()

Now you need to calculate what stations you’ll use You need to go
through every station and pick the one that covers the most
uncovered states. I’ll call this best_station:

    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():

states_covered is a set of all the states this station covers that
haven’t been covered yet. The for loop allows you to loop over
every station to see which one is the best station. Let’s look at the body
of the for loop:

    # this is a new operation & -> set intersection

    covered = states_needed & states_for_station
    if len(covered) > len(states_covered):
         best_station = station
         states_covered = covered

So covered is the set of uncovered states
that this station covers! Next you check whether this station
covers more states than the current best_station. If so, this station is the new best_station. Finally, after the for
loop is over, you add best_station to the final list of stations:

        final_stations.add(best_station)

You also need to update states_needed. Because this station covers
some states, those states aren’t needed anymore:

    # set substraction
    states_needed -= states_covered

And you loop until states_needed is empty. Here’s the full code for
the loop:

    while states_needed:
     best_station = None
     states_covered = set()

     for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
         best_station = station
         states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

### NP-complete problems

The traveling-salesperson problem and the set-covering problem both
have something in common: you *calculate every possible solution and
pick the smallest/shortest one*. Both of these problems are **NP-complete**.

**Note :** What’s a good approximation algorithm for the traveling salesperson?
Something simple that finds a short path. See if you can come up with an
answer before reading on. Here’s how I would do it: arbitrarily pick a start city. Then, each time the
salesperson has to pick the next city to visit, they pick the closest unvisited
city

Here’s the short explanation of NP-completeness: some problems are
famously hard to solve. The traveling salesperson and the set-covering
problem are two examples. A lot of smart people think that it’s not
possible to write an algorithm that will solve these problems quickly.

NP-complete problems show up everywhere! It’s nice to know if the
problem you’re trying to solve is NP-complete. At that point, you can
stop trying to solve it perfectly, and solve it using an approximation
algorithm instead. But it’s hard to tell if a problem you’re working on is
NP-complete. Usually there’s a very small difference between a problem
that’s easy to solve and an NP-complete problem. For example, in the
previous chapters, I talked a lot about shortest paths.

You know how to calculate the shortest way to get from point A to point B. But if you want to find the shortest path
that connects several points,  that’s the traveling-salesperson problem, which is NP-complete.

The short answer: there’s no easy way to tell if the problem you’re working on is NP-complete. Here are some giveaways:

* Your algorithm runs quickly with a handful of items but really slows
down with more items.

* “All combinations of X” usually point to an NP-complete problem.

* Do you have to calculate “every possible version” of X because you
can’t break it down into smaller sub-problems? Might be
NP-complete.

* If your problem involves a sequence (such as a sequence of cities, like
traveling salesperson), and it’s hard to solve, it might be NP-complete.

* If your problem involves a set (like a set of radio stations) and it’s hard
to solve, it might be NP-complete.

* Can you restate your problem as the set-covering problem or the
traveling-salesperson problem? Then your problem is definitely
NP-complete


## Chapter 9: Dynamic Programming

You learn dynamic programming, a technique to solve a hard problem by breaking it up into subproblems and
solving those subproblems first.

Let’s revisit the knapsack problem from chapter 8. You’re a thief with a knapsack that can carry 4 lb
of goods.You have three items that you can put into the knapsack

        Stereo      Laptop      Guitar
        $3000       $2000       $1500
        4 lbs       3 lbs       1 lbs

What items should you steal so that you steal the maximum money’s
worth of goods? So how do you calculate the optimal solution?

Answer: With **dynamic programming**! Dynamic programming starts by
solving subproblems and builds up to solving the big problem.
For the knapsack problem, you’ll start by solving the problem for
smaller knapsacks (or “sub-knapsacks”) and then work up to solving
the original problem.

Every dynamic-programming algorithm starts with a grid. Here’s a grid
for the knapsack problem

              1       2       3       4
    Guitar
    Stereo
    Laptop

The rows of the grid are the items, and the columns are knapsack
weights from 1 lb to 4 lb. You need all of those columns because they
will help you calculate the values of the sub-knapsacks.
The grid starts out empty. You’re going to fill in each cell of the grid.
Once the grid is filled in, you’ll have your answer to this problem!

**1st row :** This is the guitar row, which means you’re trying to fit the guitar into
the knapsack. At each cell, there’s a simple decision: do you steal the
guitar or not? Remember, you’re trying to find the set of items to steal
that will give you the most value.
The first cell has a knapsack of capacity 1 lb. The guitar is also 1 lb,
which means it fits into the knapsack! So the value of this cell is $1,500,
and it contains a guitar.

Like this, each cell in the grid will contain a list of all the items that fit
into the knapsack at that point.

Let’s look at the next cell. Here you have a knapsack of capacity 2 lb.
Well, the guitar will definitely fit in there! The same for the rest of the cells in this row.
Remember, this is the first  row, so you have only the guitar to choose from. You’re pretending that
the other two items aren’t available to steal right now.

> This row represents the current best guess for this max

Is like we ask : what would be the best guess if the only item that you can steal is the guitar for a bag of different
capacities? Then, as tha table show, the answer is : for each bag stale the guitar (too obvious right?)

As we go through the algorithm, you’ll refine your estimate.

**2nd row :** This one is for the stereo. Now that you’re on the
second row, you can steal the stereo or the guitar. At every row, you can
steal the item at that row or the items in the rows above it. So you can’t
choose to steal the laptop right now, but you can steal the stereo and/or
the guitar. Let’s start with the first cell, a knapsack of capacity 1 lb. The
current max value you can fit into a knapsack of 1 lb is $1,500.

Should you steal the stereo or not?
You have a knapsack of capacity 1 lb. Will the stereo fit in there? Nope,
it’s too heavy! Because you can’t fit the stereo, $1,500 remains the max
guess for a 1 lb knapsack

Same thing for the next two cells. These knapsacks have a capacity of
2 lb and 3 lb. so your guesses remain unchanged

What if you have a knapsack of capacity 4 lb? Aha: the stereo finally fits!
The old max value was $1,500, but if you put the stereo in there instead,
the value is $3,000! Let’s take the stereo.

You just updated your estimate! If you have a 4 lb knapsack, you can
fit at least $3,000 worth of goods in it. You can see from the grid that
you’re incrementally updating your estimate

Now think the question as: What would be the best guess for each bag size if you could stale only the guitar and the
stereo? Then you update the mas value of each cell depending on the answer for this row

**3th row :** (....) At 4 lb, things get really interesting. This is an important part. The
current estimate is $3,000. You can put the laptop in the knapsack, but
it’s only worth $2,000. Hmm, that’s not as good as the old estimate. But wait! The laptop
weighs only 3 lb, so you have 1 lb free! You could put something in
this 1 lb.

What’s the maximum value you can fit into 1 lb of space? Well, you’ve
been calculating it all along. According to the last best estimate, you can fit the guitar into that 1 lb
space, and that’s worth $1,500.

You might have been wondering why you were calculating max values
for smaller knapsacks. I hope now it makes sense! When you have
space left over, you can use the answers to those subproblems to figure
out what will fit in that space. It’s better to take the laptop + the guitar
for $3,500. And this is the correct answer

Each cell’s value gets calculated with the same formula. Here it is.

        cell[i][j] = max of {
                1. the previous max(value at cell[i-1][j])
                2. value of the current item + value of the remaining space(= cell[-i][j-items'weight])
                }

You can use this formula with every cell in this grid, and you should
end up with the same grid I did. Remember how I talked about solving
subproblems? You combined the solutions to two subproblems to solve
the bigger problem

##### What happens if you add an item?
Suppose you realize there’s a fourth item you can steal that you didn’t
notice before! You can also steal an iPhone.

Do you have to recalculate everything to account for this new item?
Nope. Remember, dynamic programming keeps progressively
building on your estimate. But you may have a new max value

##### What happens if you change the order of the rows?
Does the answer change? Suppose you fill the rows in this order: stereo,
laptop, guitar. What does the grid look like?

> The answer doesn’t change. The order of the rows doesn’t matter

##### What happens if you add a smaller item?
Suppose you can steal a necklace. It weighs 0.5 lb, and it’s worth $1,000.
So far, your grid assumes that all weights are integers. Now you decide
to steal the necklace. You have 3.5 lb left over. What’s the max value
you can fit in 3.5 lb? You don’t know! You only calculated values for
1 lb, 2 lb, 3 lb, and 4 lb knapsacks. You need to know the value of a
3.5 lb knapsack.

> Because of the necklace, you have to account for finer granularity, so the
grid has to change.

##### Handling items that depend on each other

You can’t. Dynamic programming is powerful because it can solve
subproblems and use those answers to solve the big problem. *Dynamic
programming only works when each subproblem is discrete—when it
doesn’t depend on other subproblems*

### Longest common substring

You’ve seen one dynamic programming problem so far. What are
the takeaways?

* Dynamic programming is useful when ***you’re trying to optimize
something given a constraint.*** In the knapsack problem, you had to
maximize the value of the goods you stole, constrained by the size of
the knapsack.

* You can use dynamic programming when the problem can be broken
into discrete subproblems, and they don’t depend on each other.

It can be hard to come up with a dynamic-programming solution.  Some general tips follow:

* Every dynamic-programming solution involves a grid.

* ***The values in the cells are usually what you’re trying to optimize***.
For the knapsack problem, the values were the value of the goods.

* ***Each cell is a subproblem***, so think about how you can divide
your problem into subproblems. That will help you figure out what
the axes are

Suppose you run dictionary.com. Someone types in a word, and you give them the definition.
But if someone misspells a word, you want to be able to guess
what word they meant. Alex is searching for *fish*, but he
accidentally put in *hish*. That’s not a word in your dictionary,
but you have a list of words that are similar.

* Fish

* Vista

Alex typed hish. Which word did Alex mean to type: fish or vista?

**Making the grid :** What does the grid for this problem look like? You need to answer these
questions:

* What are the values of the cells?

* How do you divide this problem into subproblems?

* What are the axes of the grid?

In dynamic programming, you’re trying to maximize something. In this
case, you’re trying to find the longest substring that two words have in
common. What substring do hish and fish have in common? How about
hish and vista? That’s what you want to calculate.

Remember, the values for the cells are usually what you’re trying to
optimize. In this case, the values will probably be a number: the length
of the longest substring that the two strings have in common.
How do you divide this problem into subproblems? You could compare
substrings

Each cell will contain the length of the longest substring
that two substrings have in common. This also gives you a clue that the
axes will probably be the two words. So the grid probably looks like this.

        H       I       S       H

    F   0       0       0       0

    I   0       1       0       0

    S   0       0       2       0

    H   0       0       0       3

What’s the formula for filling in each cell of the grid?.
The truth is, there’s no easy way to calculate the formula here. You
have to experiment and try to find something that works. Sometimes
algorithms aren’t an exact recipe. They’re a framework that you build
your idea on top of.

Remember that each cell is the value of a
subproblem. Why does cell (3, 3) have a value of 2? Why does cell (3, 4)
have a value of 0?

Here is the formula:

* if the letter doesn't match the value is zero

* If they do match. The value is: value of top-left neighbor + 1

Here’s the grid for hish vs. vista

        V       I       S       T       A

    H   0       0       0       0       0

    I   0       1       0       0       0

    S   0       0       2       0       0

    H   0       0       0       0       0

One thing to note: for this problem, the final solution may not be in
the last cell! For the knapsack problem, this last cell always had the
final solution. But for the longest common substring, the solution is the
largest number in the grid—and it may not be the last cell.

Let’s go back to the original question: which string has more in
common with hish? hish and fish have a substring of three letters in
common. hish and vista have a substring of two letters in common.
Alex probably meant to type fish.

### Longest common subsequence

Suppose Alex accidentally searched for fosh. Which word did he mean:
fish or fort? Let’s compare them using the longest-common-substring formula.
They’re both the same: two letters! But fosh is closer to fish

You’re comparing the longest common substring, but you really need
to compare the *longest common subsequence: the number of letters in
a sequence that the two words have in common*. How do you calculate
the longest common subsequence?

Can you figure out the formula for this grid? The longest common
subsequence is very similar to the longest common substring, and
the formulas are pretty similar, too.

        F       O       S       H

    F   1       1       1       1

    O   1       2       2       2

    R   1       2       2       2

    T   1       2       2       2

    -----------------------------

        F       O       S       H

    F   1       1       1       1

    I   1       1       1       1

    S   1       1       2       2

    H   1       1       2       3

Here’s my formula for filling in each cell

* Of the top and left neighbors. If the letters don't match pick the larger

* If they do match, the value is: Value of top-left neighbor + 1   (just like longest common substring)

 So is dynamic programming ever really used? Yes:

* Biologists use the longest common subsequence to find similarities
in DNA strands. They can use this to tell how similar two animals or
two diseases are. The longest common subsequence is being used to
find a cure for multiple sclerosis.

* Have you ever used diff (like git diff)? Diff tells you the differences
between two files, and it uses dynamic programming to do so.

* We talked about string similarity. Levenshtein distance measures
how similar two strings are, and it uses dynamic programming.
Levenshtein distance is used for everything from spell-check to
figuring out whether a user is uploading copyrighted data.

##### Summary

* Dynamic programming is useful when you’re trying to optimize
something given a constraint.

* You can use dynamic programming when the problem can be
broken into discrete subproblems.

* Every dynamic-programming solution involves a grid.

* The values in the cells are usually what you’re trying to optimize.

* Each cell is a subproblem, so think about how you can divide your
problem into subproblems.

* There’s no single formula for calculating a dynamic-programming
solution.

