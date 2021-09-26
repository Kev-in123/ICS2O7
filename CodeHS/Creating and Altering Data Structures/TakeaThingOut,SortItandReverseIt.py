""" This is the Scratchpad!
This file is not graded, but you can use it to test your code.

You can write and test your function in the Scratchpad, but make
sure to copy and paste it into the Unit Test file before checking
your answer. Remember to only copy and paste the function you want
to submit, not all of your tests.
"""

# Add your own tests here
def remove_sort_reverse(my_list):
    # perform operations on `my_list` to 
    # 1. remove all "eggplant"s
    # 2. sort it
    # 3. reverse it!
    my_list=[c for c in my_list if c!="eggplant"]
    my_list.sort()
    my_list.reverse()
    return my_list



#['Niall Horan', 'Louis Tomlinson', 'Liam Payne', 'Harry Styles']
print(remove_sort_reverse(["Niall Horan", "Liam Payne", "Harry Styles", "eggplant", "Louis Tomlinson"]))
