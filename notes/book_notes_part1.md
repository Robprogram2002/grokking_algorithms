## Chapter 1: Introduction to Algorithms
> *An algorithm is a set of instructions for accomplishing a task.*

### Binary search
Suppose you’re searching for a person in the phone book Their name starts with K. You could start at the
beginning and keep flipping pages until you get to the Ks. But you’re
more likely to start at a page in the middle, because you know the Ks
are going to be near the middle of the phone book.

Or suppose you’re searching for a word in a dictionary, and it
starts with O. Again, you’ll start near the middle.

This is a search problem. And all these cases use the same algorithm
to solve the problem: **binary search**.

Binary search is an algorithm; its input is a sorted list of elements. If an element you’re
looking for is in that list, binary search returns the position
where it’s located. Otherwise, binary search returns null.

**Example:** Here’s an example of how binary search works. I’m thinking of a
number between 1 and 100. You have to try to guess my number in the fewest tries possible. With
every guess, I’ll tell you if your guess is too low, too high, or correct.

Suppose you start guessing like this: 1, 2, 3, 4 …. . This is *simple search*. With
each guess, you’re eliminating only one number. If my number was 99,
it could take you 99 guesses to get there!

Here’s a better technique. Start with 50. Too low, but you just eliminated half the numbers! Now you know that
1–50 are all too low. Next guess: 75. Too high, but again you cut down half the remaining numbers!

> *With binary search, you guess the middle number and eliminate half the
remaining numbers every time*

This is binary search. Here’s how many numbers you can eliminate every time

100 items -> 50 items -> 25 items -> 13 items -> 7 items -> 4 items -> 2 items -> 1 item

Whatever number I’m thinking of, you can guess in a maximum of
seven guesses—because you eliminate so many numbers with every
guess!

> In general, for any  list of n, binary search will take log_2(n) steps to run in the worst case,
whereas simple search will take n steps.

**Questions:**
* Suppose you double the size of the list. What’s the maximum
number of steps now?
* Suppose you have a sorted list of 128 names, and you’re searching
through it using binary search. What’s the maximum number of
steps it would take?

#### Running Time
Generally you want to choose the most efficient algorithm—
whether you’re trying to optimize for time or space.Back to binary search. How much time do you save by using
it?

Well, the first approach was to check each number, one by
one. If this is a list of 100 numbers, it takes up to 100 guesses.
If it’s a list of 4 billion numbers, it takes up to 4 billion guesses. So the
maximum number of guesses is the same as the size of the list. This is
called **linear time**.

Binary search is different. If the list is 100 items long, it takes at most
7 guesses. If the list is 4 billion items, it takes at most 32 guesses.
Powerful, eh? Binary search runs in **logarithmic time**

#### Big O Notation
Big O notation is special notation that tells you how fast an algorithm is. Remember this:
> *Algorithm running times grow at different rates*

That is, as the number of items increases, binary search takes a little
more time to run. But simple search takes a lot more time to run. So
as the list of numbers gets bigger, binary search suddenly becomes a
lot faster than simple search. Bob thought binary search was 15 times
faster than simple search, but that’s not correct. If the list has 1 billion
items, it’s more like 33 million times faster. That’s why it’s not enough
to know how long an algorithm takes to run—you need to know how
the running time increases as the list size increases. That’s where Big O
notation comes in.

Big O notation tells you how fast an algorithm is. For example, suppose
you have a list of size n. Simple search needs to check each element, so
it will take n operations. The run time in Big O notation is O(n). Where
are the seconds? There are none—Big O doesn’t tell you the speed in
seconds. Big O notation lets you compare the number of operations. It
tells you how fast the algorithm grows

###### Big O establishes a worst-case run time
Suppose you’re using simple search to look for a person in the phone
book. You know that simple search takes O(n) time to run, which
means in the worst case, you’ll have to look through every single entry
in your phone book. In this case, you’re looking for Adit. This guy is
the first entry in your phone book. So you didn’t have to look at every
entry—you found it on the first try. Did this algorithm take O(n) time?
Or did it take O(1) time because you found the person on the first try?
Simple search still takes O(n) time. In this case, you found what you
were looking for instantly. That’s the best-case scenario. But Big O
notation is about the **worst-case scenario**.

So you can say that, in the
worst case, you’ll have to look at every entry in the phone book once.
That’s O(n) time. It’s a reassurance—*you know that simple search will
never be slower than O(n) time*

In summary:

• Algorithm speed isn’t measured in seconds, but in growth of the
number of operations.

• Instead, we talk about how quickly the run time of an algorithm
increases as the size of the input increases.

• Run time of algorithms is expressed in Big O notation.

• O(log n) is faster than O(n), but it gets a lot faster as the list of items
you’re searching grows.

## Chapter 2: Sort

### How memory works
Imagine you go to a show and need to check your things. A chest of
drawers is available.Each drawer can hold one element. You want to store two things, so you
ask for two drawers. You store your two things here. And you’re ready for the show! This is basically how your
computer’s  memory works

> *Your computer looks like a giant set of drawers, and each drawer has an address. Each time you want to store
an item in memory, you ask the computer  for some space, and it gives you an address where you can store your
item*

(fe0ffeeb is the address of a slot in memory)

 If you want to store multiple items, there are two basic ways to
do so: arrays and lists. There isn’t one right way to store items for every
use case, so it’s important to know the differences

### Arrays and linked lists

Suppose  you’re writing an app to manage your todos. You’ll want to store the
todos as a list in memory.Should you use an array, or a linked list? Let’s store the todos in an
array first, because it’s easier to grasp.

> Using an array means all your  tasks are stored **contiguously** (right next to each other) in memory.

Now suppose you want to add a fourth task. But the next drawer is taken up by someone else’s stuff!
It’s like going to a movie with your friends and finding a place to sit
but another friend joins you, and there’s no place for them. You have to
move to a new spot where you all fit. In this case, you need to ask your
computer for a different chunk of memory that can fit four tasks. Then
you need to move all your tasks there.

If another friend comes by, you’re out of room again—and you all have
to move a second time! What a pain. Similarly, adding new items to
an array can be a big pain. If you’re out of space and need to move to a
new spot in memory every time, adding a new item will be really slow.
One easy fix is to “hold seats”: even if you have only 3 items in your task
list, you can ask the computer for 10 slots, just in case. Then you can
add 10 items to your task list without having to move. This is a good
workaround, but you should be aware of a couple of downsides:

* You may not need the extra slots that you asked for, and then that
memory will be wasted. You aren’t using it, but no one else can use
it either

* You may add more than 10 items to your task list and have to
move anyway

So it’s a good workaround, but it’s not a perfect solution. Linked lists
solve this problem of adding items.

##### Linked Lists
With linked lists, your items can be anywhere in memory. Each item stores the address of the next item in the list.
A bunch of  random memory addresses are linked together.

It’s like a treasure hunt. You go to the first address, and it says, “The next
item can be found at address 123.” So you go to address 123, and it says,
“The next item can be found at address 847,” and so on. Adding an item
to a linked list is easy: you stick it anywhere in memory and store the
address with the previous item

With linked lists, you never have to move your items. You also avoid
another problem. Let’s say you go to a popular movie with five of your
friends. The six of you are trying to find a place to sit, but the theater
is packed. There aren’t six seats together. Well, sometimes this happens
with arrays. Let’s say you’re trying to find 10,000 slots for an array. Your
memory has 10,000 slots, but it doesn’t have 10,000 slots together. You
can’t get space for your array! A linked list is like saying, “Let’s split up
and watch the movie.” If there’s space in memory, you have space for
your linked list

If linked lists are so much better at inserts, what are arrays good for?

##### Arrays

Websites with top-10 lists use a scummy tactic to get more page views.
Instead of showing you the list on one page, they put one item on each
page and make you click Next to get to the next item in the list. This technique gives the websites
10 whole pages on which to show you ads, but it’s boring to click Next 9
times to get to #1. It would be much better if the whole list was on one
page and you could click each person’s name for more info.

Linked lists have a similar problem. Suppose you want to read the last
item in a linked list. You can’t just read it, because you don’t know what
address it’s at. Instead, you have to go to item #1 to get the address for
item #2. Then you have to go to item #2 to get the address for item #3.
And so on, until you get to the last item. Linked lists are great if you’re
going to read all the items one at a time: you can read one item, follow
the address to the next item, and so on. But if you’re going to keep
jumping around, linked lists are terrible.

> Arrays are different. You know the address for every item in your array.

*Arrays are great if you want to read random elements, because you can look up any element in your array
instantly*. With a linked list, the elements aren’t next to each other,
so you can’t instantly calculate the position of the fifth element in
memory

###### Inserting into the middle of a list
Suppose you want your todo list to work more like a calendar. Earlier,
you were adding things to the end of the list. Now you want to add them in the order in which they should
be done.

What’s better if you want to insert elements in the middle: arrays or
lists? With lists, it’s as easy as changing what the previous element
points to. But for arrays, you have to shift all the rest of the elements down
And if there’s no space, you might have to copy everything to a new
location! Lists are better if you want to insert elements into the middle

###### Deletions

What if you want to delete an element? Again, lists are better, because
you just need to change what the previous element points to. With
arrays, everything needs to be moved up when you delete an element.
Unlike insertions, deletions will always work. Insertions can fail
sometimes when there’s no space left in memory. But you can always
delete an element.

Run times for common operations on arrays and  linked lists:

                 Arrays  |   Lists

    Reading      O(1)    |   O(n)

    Insertion    O(n)    |   O(1)

    Deletion     O(n)    |   O(1)

t’s worth mentioning that insertions and deletions are O(1) time only
if you can instantly access the element to be deleted. It’s a common
practice to keep track of the first and last items in a linked list, so it
would take only O(1) time to delete those.

Which are used more: arrays or lists? Obviously, it depends on the use
case. But arrays see a lot of use because they allow **random access**.

There are two different types of access: **random access** and **sequential access**.
Sequential access means reading the elements one by one, starting
at the first element. Linked lists can only do sequential access. If you
want to read the 10th element of a linked list, you have to read the first
9 elements and follow the links to the 10th element. Random access
means you can jump directly to the 10th element. You’ll frequently
hear me say that arrays are faster at reads. This is because they provide
random access. A lot of use cases require random access, so arrays are
used a lot. Arrays and lists are used to implement other data structures,
too

### Selection sort

Suppose you have a bunch of music on your computer. For each artist, you have a play count.
You want to sort this list from most to least played, so that you can rank
your favorite artists. How can you do it?

One way is to go through the list and find the most-played artist. Add
that artist to a new list.Do it again to find the next-most-played artist. Keep doing this, and you’ll
end up with a sorted list

Let’s put on our computer science hats and see how long this will take to
run. To find the artist with the highest play count, you have to check each
item in the list. This takes O(n) time, as you just saw. So you have an
operation that takes O(n) time, and you have to do that n times

        This takes O(n × n) time or O(n^2) time.

Maybe you’re wondering: as you go through the operations, the number
of elements you have to check keeps decreasing. Eventually, you’re down
to having to check just one element. So how can the run time still be
O(n^2)? That’s a good question, and the answer has to do with constants
in Big O notation.

You’re right that you don’t have to check a list of n elements each time.
You check n elements, then n – 1, n - 2 … 2, 1. On average, you check a
list that has 1/2 × n elements. The runtime is O(n × 1/2 × n). But constants
like 1/2 are ignored in Big O notation so you just write O(n × n) or O(n^2)

In recap:

• Your computer’s memory is like a giant set of drawers.

• When you want to store multiple elements, use an array or a list.

• With an array, all your elements are stored right next to each other.

• With a list, elements are strewn all over, and one element stores
the address of the next one.

• Arrays allow fast reads.

• Linked lists allow fast inserts and deletes.

• All elements in the array should be the same type (all ints,
all doubles, and so on)

## Chapter 3: Recursion

Loop vs Recursion ? Both approaches accomplish the same thing, but the second approach
is clearer to me. Recursion is used when it makes the solution clearer.
There’s no performance benefit to using recursion; in fact, loops are
sometimes better for performance. I like this quote by Leigh Caldwell
on Stack Overflow:

> *“Loops may achieve a performance gain for
your program. Recursion may achieve a performance gain for your
programmer. Choose which is more important in your situation!”*

Many important algorithms use recursion, so it’s important to
understand the concept.

Because a recursive function calls itself, it’s easy to write a
function incorrectly that ends up in an infinite loop.

When you write a recursive function, you have to tell it when to stop
recursing. That’s why *every recursive function has two parts: the **base
case**, and the **recursive case**. The recursive case is when the function calls
itself. The base case is when the function doesn’t call itself again … so it
doesn’t go into an infinite loop.*

### The call stack

The **call stack** is an important concept in
general programming, and it’s also important to understand
when using recursion.

Suppose you’re throwing a barbecue. You keep a todo list for the
barbecue, in the form of a stack of sticky notes. You could add todo items
anywhere to the list or delete random items. The stack of
sticky notes is much simpler. When you insert an item,
it gets added to the top of the list. When you read an item,
you only read the topmost item, and it’s taken off the list. So your todo
list has only two actions: push (insert) and pop (remove and read).

This data structure is called a **stack**. The stack is a simple data structure.

> *Your computer uses a stack internally called the call stack*

Let’s see it in  action. Here’s a simple function:

        def greet(name):
            print("hello, " + name + "!")
            greet2(name)
            print("greeting ready to say bye ...")
            bye()

This function greets you and then calls two other functions. Here are
those two functions:

        def greet2(name):
            print("how are you " + name + "?")

        def bye():
            print("ok, bye")

Let’s walk through what happens when you call a function. Suppose you call greet(“maggie”). First, your computer
allocates a box  of memory for that function call. Now let’s use the memory. The variable name is set to “maggie”. That
needs to be saved in memory.

Every time you make a function call, your computer saves the values
for all the variables for that call in memory like this. Next, you print
hello, maggie! Then you call greet2(“maggie”). Again, your
computer allocates a box of memory for this function call.

Your computer is using a stack for these boxes. The second box is added
on top of the first one. You print how are you, maggie? Then you
return from the function call. When this happens, the box on top of the
stack gets popped off.

Now the topmost box on the stack is for the greet function, which
means you returned back to the greet function. When you called the
greet2 function, the greet function was **partially completed**. This is
the big idea behind this section:

> *when you call a function from another function, the calling function is paused in a partially completed state. All
the values of the variables for that function are still stored in memory.*

Now that you’re done with the greet2 function, you’re back to the
greet function, and you pick up where you left off. First you print
getting ready to say bye…. You call the bye function.
A box for that function is added to the top of the stack. Then you print
ok bye! and return from the function call.

And you’re back to the greet function. There’s nothing else to be done,
so you return from the greet function too. This stack, used to save the
variables for multiple functions, is called the **call stack**.

##### The call stack with recursion

Recursive functions use the call stack too! Let’s look at this in action
with the factorial function. Here’s a recursive function to calculate the factorial of a
number:

        def factorial(n):
            if x == 1:
                return 1
            else:
                return x * factorial(n-1)

Now you call fact(3). Let’s step through this call line by line and see
how the stack changes. Remember, the topmost box in the stack tells
you what call to fact you’re currently on.

(Make the process of recursion and stack call for yourself)

Notice that each call to fact has its own copy of x. You can’t access a
different function’s copy of x. The stack plays a big part in recursion.


Using the stack is convenient, but there’s a cost: saving all that info can
take up a lot of memory. Each of those function calls takes up some
memory, and when your stack is too tall, that means your computer is
saving information for many function calls. At that point, you have two
options:

• You can rewrite your code to use a loop instead.

• You can use something called **tail recursion**. That’s an advanced
recursion topic that is out of the scope of this book. It’s also only
supported by some languages, not all

## Chapter 4: Quick Sort

Sometimes
you’ll come across a problem that can’t be solved
by any algorithm you’ve learned. When a good
algorithmist comes across such a problem, they
don’t just give up. They have a toolbox full of
techniques they use on the problem, trying to
come up with a solution. **Divide-and-conquer**
is the first general technique you learn.

This chapter really gets into the meat of algorithms. After all,
an algorithm isn’t very useful if it can only solve one type of
problem. Instead, D&C gives you a new way to think about solving problems. D&C is another tool in your toolbox.
When you get a new  problem, you don’t have to be stumped. Instead, you can ask, “Can I
solve this if I use divide and conquer?”
At the end of the chapter, you’ll learn your first major D&C algorithm:
quicksort. Quicksort is a sorting algorithm, and a much faster one than
selection sort

### Divide & conquer

D&C algorithms are recursive algorithms. To solve a problem using D&C, there are two steps:

1. Figure out the base case. This should be the simplest possible case.

2. Divide or decrease your problem until it becomes the base case.

D&C isn’t a simple algorithm that you can apply to a problem. Instead,
it’s a way to think about a problem.

Suppose You’re given an array of numbers
You have to add up all the numbers and return the total. It’s pretty easy
to do this with a loop. But how would you do this with a recursive function?

Figure out the base case. What’s the simplest array you could
get? Think about the simplest case, and then read on. If you get an array
with 0 or 1 element, that’s pretty easy to sum up. So that will be the base case.
You need to move closer to an empty array with every recursive
call. How do you reduce your problem size? Slicing your array at each recursive call

**Sneak peak at functional programming:** “Why would I do this recursively if I can do it easily with a loop?” you
may be thinking. Well, this is a sneak peek into functional programming!
Functional programming languages like Haskell don’t have loops, so
you have to use recursion to write functions like this. If you have a good
understanding of recursion, functional languages will be easier to learn.

### Quicksort
It’s much faster than selection sort and is frequently used in real life.
Let’s use quicksort to sort an array. What’s the simplest array that a
sorting algorithm can handle. Well, some arrays don’t need to be sorted at all.

Empty arrays and arrays with just one element will be the base case. You
can just return those arrays as is—there’s nothing to sort.
Let’s look at bigger arrays. An array with two elements is pretty easy to
sort, too: "check if the first element is smaller than the second. If it is not, swap them"

What about an array of three elements? Remember, you’re using D&C. So you want to break down this array
until you’re at the base case. Here’s how quicksort works. First, pick an
element from the array. This element is called the **pivot**.

For now,  let’s say the first item in the array is the pivot. Now find the elements smaller than the pivot and
the elements larger  than the pivot

This is called **partitioning**. Now you have

* A sub-array of all the numbers less than the pivot

* The pivot

* A sub-array of all the numbers greater than the pivot
The two sub-arrays aren’t sorted. They’re just partitioned. But if they
were sorted, then sorting the whole array would be pretty easy.

If the sub-arrays are sorted, then you can combine the whole thing like
this—*left array + pivot + right array*—and you get a sorted
array.

How do you sort the sub-arrays? Well, the quicksort base case already
knows how to sort arrays of two elements (the left sub-array) and
empty arrays (the right sub-array). So if you call quicksort on the two
sub-arrays and then combine the results, you get a sorted array!

> This will work with any pivot

Here  are the steps:

1. Pick a pivot.

2. Partition the array into two sub-arrays: elements less than the pivot
and elements greater than the pivot.

3. Call quicksort recursively on the two sub-arrays.

This works with any element as the pivot.

##### Big O notation

Quicksort is unique because its speed depends on the pivot you choose.

There’s another sorting algorithm called **merge sort**, which is
O(n log n). Much faster! Quicksort is a tricky case. In the worst case,
quicksort takes O(n^2) time.
It’s as slow as selection sort! But that’s the worst case. In the average
case, quicksort takes O(n log n) time. So you might be wondering:

* What do worst case and average case mean here?

* If quicksort is O(n log n) on average, but merge sort is O(n log n)
always, why not use merge sort? Isn’t it faster?

**Merge sort vs. quicksort :**

Suppose you have this simple function to print every item in a list:

    def print_items(list):
     for item in list:
        print item

This function goes through every item in the list and prints it out.
Because it loops over the whole list once, this function runs in O(n)
time. Now, suppose you change this function so it sleeps for 1 second
before it prints out an item:

    from time import sleep
    def print_items2(list):
     for item in list:
        sleep(1)
        print item

Before it prints out an item, it will pause for 1 second. Suppose you
print a list of five items using both functions.Both functions loop through the list once,
so they’re both O(n) time.
Which one do you think will be faster in practice? I think print_items
will be much faster because it doesn’t pause for 1 second before printing
an item. So even though both functions are the same speed in Big O
notation, print_items is faster in practice. When you write Big O
notation like O(n), it really means this

        O(c*n)

*c is some fixed amount of time that your algorithm takes. It’s called the
constant*. For example, it might be 10 milliseconds * n for print_
items versus 1 second * n for print_items2.

You usually ignore that constant, because if two algorithms have
different Big O times, the constant doesn’t matter. Take binary search
and simple search, for example. Suppose both algorithms had these
constants.

    Simple search   Binary Search
      10ms * n        1sec * n

You might say, “Wow! Simple search has a constant of 10 milliseconds,
but binary search has a constant of 1 second. Simple search is way
faster!” Now suppose you’re searching a list of 4 billion elements. Here
are the times.

    Simple search                       Binary search
    10ms * 4 billion = 463 days         1sec * 32 = 32 seconds

As you can see, binary search is still way faster. That constant didn’t
make a difference at all.

*But sometimes the constant can make a difference. Quicksort versus
merge sort is one example. Quicksort has a smaller constant than
merge sort*. So if they’re both O(n log n) time, quicksort is faster. And
quicksort is faster in practice because it hits the average case way more
often than the worst case.
So now you’re wondering: what’s the average c ase versus the worst case?

##### Average case vs. worst case

The performance of quicksort heavily depends on the pivot you choose.
Suppose you always choose the first element as the pivot. And you
call quicksort with an array that is already sorted. Quicksort doesn’t
check to see whether the input array is already sorted. So it will still try
to sort it.

Notice how you’re not splitting the array into two halves. Instead, one
of the sub-arrays is always empty. So the call stack is really long. Now
instead, suppose you always picked the middle element as the pivot.

It’s so short! Because you divide the array in half every time, you don’t
need to make as many recursive calls. You hit the base case sooner, and
the call stack is much shorter

The first example you saw is the worst-case scenario, and the second
example is the best-case scenario. In the worst case, the stack size is
O(n). In the best case, the stack size is O(log n).

Note that, You pick one element as the
pivot, and the rest of the elements are divided into sub-arrays. You
touch all eight elements in the array. So this first operation takes O(n)
time. But  actually, you touch O(n) elements on every level of the call stack

Even if you partition the array differently, you’re still touching O(n)
elements every time. So each level takes O(n) time to complete

In this example, there are O(log n) levels (the technical way to say
that is, “The height of the call stack is O(log n)”). And each level takes
O(n) time. The entire algorithm will take O(n) * O(log n) = O(n log n)
time. This is the best-case scenario.

In the worst case, there are O(n) levels, so the algorithm will take
O(n) * O(n) = O(n^2) time

Well, guess what? I’m here to tell you that the *best case is also the
average case. If you always choose a random element in the array as the
pivot, quicksort will complete in O(n log n) time on average*.

Quicksort is one of the fastest sorting algorithms out there, and it’s a very good
example of D&C.

Recap of main ideas:

* D&C works by breaking a problem down into smaller and smaller
pieces. If you’re using D&C on a list, the base case is probably an
empty array or an array with one element.

* If you’re implementing quicksort, choose a random element as the
pivot. The average runtime of quicksort is O(n log n)!

* The constant in Big O notation can matter sometimes. That’s why
quicksort is faster than merge sort.

* The constant almost never matters for simple search versus binary
search, because O(log n) is so much faster than O(n) when your list
gets big.


## Chapter 5 : Hash Tables

Suppose you work at a grocery store. When a customer
buys produce, you have to look up the price in a book. If
the book is unalphabetized, it can take you a long time to
look through every single line for apple, O(n). If the book is alphabetized, you could run
binary search to find the price of an apple. That would
only take O(log n) time

You already know that binary search is darn fast. But as a cashier,
looking things up in a book is a pain, even if the book is sorted. You can
feel the customer steaming up as you search for items in the book. What
you really need is a buddy who has all the names and prices memorized.
Then you don’t need to look up anything: you ask her, and she tells you
the answer instantly

Your buddy Maggie can give you the price in O(1) time for any item, no
matter how big the book is. She’s even faster than binary search.

What a wonderful person! How do you get a “Maggie”?

Let’s put on our data structure hats. You know two data structures so
far: arrays and lists (I won’t talk about stacks because you can’t really
“search” for something in a stack)

You could implement this book as an array. Each item in the array is really two items:
one is the name of a kind of  produce, and the other is the price. If you sort this array by name, you
can run binary search on it to find the price of an item. So you can find
items in O(log n) time. But you want to find items in O(1) time. That is,
you want to make a “Maggie.” That’s where hash functions come in.

### Hash functions

A hash function is a function where you put in a string and you get  back a number
(String here means any kind of data—a sequence of bytes.)

> In technical terminology, we’d say that a hash function “maps strings
to numbers.”

You might think there’s no discernable pattern to what
number you get out when you put a string in. But there are some
requirements for a hash function:

* It needs to be consistent. For example, suppose you put in “apple” and
get back “4”. Every time you put in “apple”, you should get “4” back.
Without this, your hash table won’t work.

* It should map different words to different numbers. For example, a
hash function is no good if it always returns “1” for any word you put
in. In the best case, every different word should map to a different
number

So a hash function maps strings to numbers. What is that good for?
Well, you can use it to make your “Maggie”!

Start with an empty array. You’ll store all of your prices in this array. Let’s add the price of an apple.
Feed “apple” into the hash function

The hash function outputs “3”. So let’s store the price of an apple at
index 3 in the array.

        [ , , , 0.67 , ]
         0 1 2   3    4

Keep going, and eventually the whole array will be full of prices.

Now you ask, “Hey, what’s the price of an avocado?” You don’t need to
search for it in the array. Just feed “avocado” into the hash function.
It tells you that the price is stored at index 4. And sure enough,
there it is

> The hash function tells you exactly where the price is stored, so you
don’t have to search at all!

This works because:

* The hash function consistently maps a name to the same index. Every
time you put in “avocado”, you’ll get the same number back. So you
can use it the first time to find where to store the price of an avocado,
and then you can use it to find where you stored that price.

* The hash function maps different strings to different indexes

* The hash function knows how big your array is and only returns valid
indexes. So if your array is 5 items, the hash function doesn’t return
100

You just built a “Maggie”!

> *Put a hash function and an array together,
and you get a data structure called a **hash table***. A hash table is the first
data structure you’ll learn that has some extra logic behind it. Arrays
and lists map straight to memory, but hash tables are smarter. They use
a hash function to intelligently figure out where to store elements.

You can get an item from an  array instantly. And hash tables use an array to store the data, so they’re
equally fast.

You’ll probably never have to implement hash tables yourself. Any good
language will have an implementation for hash tables. Python has hash
tables; they’re called dictionaries.

#### Collisions

To understand the performance of hash tables, you first need to understand what
collisions are. First, I’ve been telling you a white lie. I told you that a hash function
always maps different keys to different slots in the array.
In reality, it’s almost impossible to write a hash function that does this.

This is called a **collision**: *two keys have been assigned the same slot*. This is a problem.
If you store the price of avocados at that slot, you’ll overwrite the price
of apples. Then the next time someone asks for the price of apples,
they will get the price of avocados instead! Collisions are bad, and you
need to work around them. There are many different ways to deal with
collisions. The simplest one is this: *if multiple keys map to the same
slot, start a linked list at that slot*

In this example, both “apple” and “avocado” map to the same slot.
So you start a linked list at that slot. If you need to know the price of
bananas, it’s still quick. If you need to know the price of apples, it’s a
little slower. You have to search through this linked list to find “apple”. If
the linked list is small, no big deal—you have to search through three or
four elements

There are two lessons here:

* *Your hash function is really important*. Ideally, your hash function would map
keys evenly all over the hash.

* If those linked lists get long, it slows down your hash table a lot. But
*they won’t get long if you use a good hash function!*

A good hash function will give you very
few collisions. So how do you pick a good hash function?

#### Performance
In the average case, hash tables take O(1) for everything. O(1) is called
*constant time*. It doesn’t mean instant. It means the time taken will stay the same, regardless of how
big the hash table is.

> In the worst case, a hash table takes O(n)—linear time—for everything,
which is really slow.

Look at the average case for hash tables. Hash tables are as fast as arrays
at searching (getting a value at an index). And they’re as fast as linked
lists at inserts and deletes. It’s the best of both worlds! But in the worst
case, hash tables are slow at all of those. So it’s important that you don’t
hit worst-case performance with hash tables. And to do that, you need
to avoid collisions. To avoid collisions, you need

* A low load factor

* A good hash function

#### Load Factor
The load factor of a hash table  is easy to calculate.

    number of items in hash table / total number of slots

Hash tables use an array for storage, so you count the number of  occupied slots in an array.

> Load factor measures how many empty slots remain in your hash table.

Suppose you need to store the price of 100 produce items in your hash
table, and your hash table has 100 slots. In the best case, each item will
get its own slot.

This hash table has a load factor of 1. What if your hash table has only
50 slots? Then it has a load factor of 2. There’s no way each item will
get its own slot, because there aren’t enough slots! Having a load factor
greater than 1 means you have more items than slots in your array.
Once the load factor starts to grow, you need to add more slots to your
hash table. This is called **resizing**.

 First you create a new array that’s bigger. The rule of thumb is to make an array that is twice the size.
Now you need to re-insert all of those items into this new hash table  using the hash function.

> *With a lower load factor, you’ll have fewer collisions, and your table will perform better. A
good rule of thumb is, resize when your load factor is greater than 0.7.*

You might be thinking, “This resizing business takes a lot of time!” And
you’re right. Resizing is expensive, and you don’t want to resize too
often. But averaged out, hash tables take O(1) even with resizing

#### A good hash function

A good hash function distributes values in the array evenly. A bad hash function groups values together
and produces a lot of  collisions

What is a good hash function? That’s something you’ll never have to
worry about—old men (and women) with big beards sit in dark rooms
and worry about that. If you’re really curious, look up the SHA function.
You could use that  as your hash function.

Hash tables are a powerful data structure because they’re so fast and
they let you model data in a different way. You might soon find that
you’re using them all the time.
