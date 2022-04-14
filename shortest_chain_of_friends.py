def shortest_chain_of_friends(network, start, end):
    """
    Find the shortest chain of friends between two people.
    :param network: a dictionary of friends
    :param start: the name of the person
    :param end: the name of the person
    :return: a list of names, the length of the path
    """

    # check if all values from the list are in the network keys
    if not all(value2 in network.keys() for value in network.values() for value2 in value):
        raise ValueError("Not all values in the list are in the network keys")

    path = [[start]]  # list of paths
    index = 0  # index of the path
    visited = {start}  # set of visited nodes

    if start == end:  # if start and end are the same
        return len(path[index]) - 1  # return the path and the length of the path

    while index < len(path):
        current_path = path.__getitem__(index)  # current path
        last_person = current_path[-1]  # last person in the path
        next_people = network[last_person]  # next people in the path

        if end in next_people:  # if end is in the next people
            current_path.append(end)  # add end to the path
            return len(current_path) - 1  # return the path and the length of the path

        for person in next_people:  # for each person in the next people
            if person not in visited:  # if the person is not visited
                new_path = current_path.copy()  # copy the current path
                new_path.append(person)  # add the person to the path
                path.append(new_path)  # add the path to the list of paths
                visited.add(person)  # add the person to the set of visited nodes

        index += 1  # increment the index

    return -1  # return None and -1 if there is no path


if __name__ == "__main__":
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B', 'E', 'F'],
             'E': ['B', 'F', 'H'],
             'F': ['C', 'E'],
             'G': ['C', 'H'],
             'H': ['G', 'E'],
             'I': []
             }
    print(shortest_chain_of_friends(graph, 'A', 'D'))
