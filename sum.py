import random
from lllist import LLList

# Find the number of pairs in the LLList that sum to k
def sum_k(ll_list, k):
    count = 0

    for i in range(ll_list.length()):
        item1 = ll_list.get_item(i)

        for j in range (i, ll_list.length()):
            item2 = ll_list.get_item(j)

            if item1 + item2 == k:
                count += 1

    return count


ll_list = LLList()
random.seed(0)

# add a thousand random numbers to the list
for i in range(1000):
    ll_list.add_item(random.randint(1, 100), 0)

# count how many pairs sum to 50
count = sum_k(ll_list, 50)
if count != 4986:
    print("sum is incorrect; should be 4986 but is " + str(count))
else:
    print("count is correct")
