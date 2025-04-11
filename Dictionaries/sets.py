#A set in Python is an unordered collection of unique elements. 
# It is useful for mathematical operations like union, intersection, and difference.


my_sets = {1,2,3,4,5}
my_sets.add(6);
my_sets.add(8);

print(my_sets)


set_1 = {1,2,3,4,5}
set_2 = {2,3,4,5,8}

union_list= set_1.union(set_2)

print(union_list)

intersection_list = set_1.intersection(set_2)
print(intersection_list)

diff_list = set_1.difference(set_2)
print(diff_list)

print(set_2.difference(set_1))


