#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        print(ticket)
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    for i in range(length):
        if i == 0:
            route[i] = hash_table_retrieve(hashtable, "NONE")
        else:
            prevValue = route[i-1]
            route[i] = hash_table_retrieve(hashtable, prevValue)
    return route

if __name__ == '__main__':
    pass

#hash_table_insert(hashtable, ticket.source, ticket.destination)
    # We can hash each ticket such that the starting location is the key and the destination is the value. Then, when constructing the entire route, the `i`th location in the route can be found by checking the hash table for the `i-1`th location.
    # position 0 has NONE, destination
    # position 1 source has position 0's destinaion