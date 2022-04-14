- the social network was represented by a graph of users and their friends
- in fact, I chose this representation to be a dictionary of users and their friends, i.e. every person is a key in the dictionary and their friends (neighbours) are the values because it's more easy to work with this representation (and it's also more efficient)

- to compute the shortest path between two users, I used the BFS algorithm (Breadth-First Search)
- I was considering using the Dijkstra's algorithm, but it's not efficient enough to compute the shortest path between two users (O(n+e) = BFS, O(e + n log n) = Dijkstra)
- Also, DFS wasn't an option because it's not a graph search algorithm, it's a tree search algorithm and does not accept cycles

- 