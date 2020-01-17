#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
#  output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

#What if we store each weight in the input list as keys? What would be a useful thing to store as the value for each key? 
#If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for `limit - weight`. If it does, then we've found the two items whose weights sum up to the `limit`!


    for ind,val in enumerate(weights):
        #determine remaining amount
        remaining = limit - val
        #check ht for by key that would fulfill the remaining amount
        positive_hit = hash_table_retrieve(ht, remaining)
        #if ht doesn't have an entry, create it.
        if positive_hit is None:
            hash_table_insert(ht, val, ind)
        else:
            if ind >= positive_hit: # val >= remaining
                return (ind, positive_hit)
            else: 
                return (positive_hit, ind)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


if __name__ == '__main__':
    pass
