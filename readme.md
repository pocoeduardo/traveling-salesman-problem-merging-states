# Traveling Salesman Problem by merging states

To set up a general breadth first search model algorithm, this python script solves the Traveling Salesman Problem generating each new state by adding a new unvisited node to every given path, but noticing a naive fact so that we reduce a little bit the complexity.

## State merging/joining

Suppose we have produced the two following partial paths:

1, 2, 3, 4

1, 3, 2, 4


The remaining nodes are the same for any continuation of these two paths. Why bother considering the longest so far if the other will yield always a shorter traveled distance when the following node order is equal? So, in general, when facing two paths with same node lengh, starting and ending nodes and the same intermediary nodes (with different ordering), the shortest one stays in the list to generate following paths. Any other is discarded so that the tree of possibilities do not increase so much.