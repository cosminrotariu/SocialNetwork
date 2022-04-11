def shortest_chain_of_friends(network, start, end):
    """
    Find the shortest chain of friends between two people.
    :param network: a dictionary of friends
    :param start: the name of the person
    :param end: the name of the person
    :return: a list of names
    """

    path = [[start]]
    index = 0
    visited = {start}

    if start == end:
        return path[index], len(path[index]) - 1

    while index < len(path):
        current_path = path.__getitem__(index)
        last_person = current_path[-1]
        next_people = network[last_person]

        if end in next_people:
            current_path.append(end)
            return current_path, len(current_path) - 1

        for person in next_people:
            if person not in visited:
                new_path = current_path.copy()
                new_path.append(person)
                path.append(new_path)
                visited.add(person)

        index += 1

    return None


if __name__ == "__main__":
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B', 'E', 'F'],
             'E': ['B', 'F', 'H'],
             'F': ['C', 'E'],
             'G': ['C', 'H'],
             'H': ['G', 'E']
             }
    print(shortest_chain_of_friends(graph, 'A', 'G'))
