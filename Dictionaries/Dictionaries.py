#A dictionary in Python is a data structure that allows you to store and 
# retrieve values using keys. It is also known as a hashmap or associative
#  array in other programming languages. Dictionaries are implemented as hash 
# tables, providing fast access to values based on their keys.


my_dict= {'name':'satyam kumar mishra', 'company': 'cvent india pvt ltd', 
               'joining date': '2022', 'tenure':'2yrs 10 month'}
print(my_dict['name'])
print(my_dict['company'])
print(my_dict['joining date'])
print(my_dict['tenure'])


# for the list of dictionary we use []


my_dict_list= [{'name':'satyam kumar mishra', 'company': 'cvent india pvt ltd', 
               'joining date': '2022', 'tenure':'2yrs 10 month'},
{'name':'sahil', 'company': 'cvent india pvt ltd', 
               'joining date': '2022', 'tenure':'2yrs 10 month'}]
print(my_dict_list[0]['name'])
print(my_dict_list[1]['name'])



# modifying the disctionary
my_dict['age'] = 24 
my_dict['role'] = 'application support Enginer'




del my_dict['age'] # this is not working 

for key in my_dict:
    if key == 'name':
        print("Found")

if 'age' in my_dict:
    print('Age is present in the dictionary')
else:
    print("this has been deleted")
    






