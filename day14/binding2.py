some_guy = 'Fred'

first_names = []
first_names.append(some_guy)

another_list_of_names = first_names
another_list_of_names.append('George')
some_guy = 'Bill'

print (some_guy, first_names, another_list_of_names)

# the binding of some_guy to the string object containing 'Fred' is added to the block's namespace. The name first_names is bound to an empty list object. On line 4, a method is called on the list object first_names is bound to, appending the object some_guy is bound to. At this point, there are still only two objects that exist: the string object and the list object. some_guy and first_names[0] both refer to the same object (Indeed, print(some_guy is first_names[0]) shows this).

# Let's continue to break things down. On line 6, a new name is bound: another_list_of_names. Assignment between names does not create a new object. Rather, both names are simply bound to the same object. As a result, the string object and list object are still the only objects that have been created by the interpreter. On line 7, a member function is called on the object another_list_of_names is bound to and it is mutated to contain a reference to a new object: 'George'. So to answer our original question, the output of the code is
