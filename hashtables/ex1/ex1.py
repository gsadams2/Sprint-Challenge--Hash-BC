#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    for i in range(length):
        if hash_table_retrieve(ht, limit-weights[i]):
            index_one = i
            index_two = hash_table_retrieve(ht, limit-weights[i])
            if index_one > index_two:
                return (index_one, index_two)
            return (index_two, index_one)
    return None







    # dict = {}

    # for i in range(length):
        
    #     difference = limit - weights[i]

    #     if difference in dict:
    #         # print(i, dict[difference])
    #         return i, dict[difference]
    #     else:
    #         dict[weights[i]] = i
    #         print(dict[weights[i]])
    # return None

    


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

