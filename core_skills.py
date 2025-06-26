import random
# rand_list =
random_list = []
for i in range(10):
    x = random.randint(1, 20) 
    random_list.append(x)


# list_comprehension_below_10 =
list1 = [x for x in random_list if x < 10]

# list_comprehension_below_10 =
list2 = list(filter(lambda x:x < 10,random_list))