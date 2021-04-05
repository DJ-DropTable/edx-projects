# %%
###########################
# template provided by: https://learning.edx.org/course/course-v1:MITx+6.00.2x+1T2021/
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Helper code -> edx.org

    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict

def make_data_stucture(hash_table):
    """
    Parameters:
    hash_table - dictionary with string key and integer value items
    
    Returns:
    dictionary with integer key and list value items
    """
    result = {}
    for h in hash_table.keys():
        value = hash_table[h]
        if value not in result:
            result[value] = []
        result[value].append(h)
    return result


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_new = make_data_stucture(cows)
    result = []
    while any(cows_new[k] for k in cows_new.keys()):
        i = 0
        remaining = limit
        current_result = []
        remaining_vals = [k for k in cows_new.keys() if cows_new[k]]
        remaining_vals.sort(reverse=True)
        while True:
            if i > len(remaining_vals) - 1:
                result.append(current_result)
                break
            val = remaining_vals[i]
            if val < remaining:
                if cows_new[val]:
                    current_result.append(cows_new[val][0])
                    cows_new[val].pop(0)
                    remaining -= val
                else:
                    i += 1
            else:
                i += 1
    return result
        

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_names = [v for v in cows.keys()]
    cows_set = get_partitions(cow_names)
    for attempt in cows_set:
        i = 0
        for a in attempt:
            weights = [cows[cow] for cow in a]
            if sum(weights) > limit:
                break
            i += 1
        if i == len(attempt):
            return attempt

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

if __name__ == '__main__':

    cows = load_cows("ps1_cow_data.txt")
    # limit=100
    # print(cows)
    # print(greedy_cow_transport(cows, limit))
    print(brute_force_cow_transport(cows))

# %%
