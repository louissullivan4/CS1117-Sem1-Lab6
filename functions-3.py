# ScriptName: functions.py
# Author: Louis Sullivan 119363083

def count(list, value):
    '''
    function - count how many times <value> occurs in <list>
    :param list: - <list> input
    :param value: - <value> to search for
    :return:
    '''
    # set counter
    i = 0
    # accumulator to count how many times <value> occurs
    # set to zero to cover no <value> in <list>
    num_values = 0
    # loop over the length of the <list>
    while i < len(list):
        # if <value> and <list> index i are the same
        if list[i] == value:
            # increment the accumulator
            num_values += 1
        # increment the counter
        i += 1
    # return how many times <value> occurs in <list>
    return num_values

def index(list, value):
    '''
    function - find the <value> index in <list>
    :param list: - <list> input
    :param value: - <value> to search
    :return:
    '''
    # set counter
    i = 0
    # loop over the length of the <list>
    while i <= len(list):
        # if <value> and <list> index i are the same return i
        if list[i] == value:
            return i
        # if i is equal to the length of the list minus 1 return -1 (index starts at zero)
        if i == len(list)-1:
            return -1
        # increment the counter
        i += 1

def get_value(list, index):
    '''
    function - return the letter that occurs at the <index> at the point in the <list>
    :param list: - <list> input
    :param index: - <index> to search for
    :return:
    '''
    # set counter
    i = 0
    # loop over the length of the list
    while i <= len(list):
        # if the value of i equals the index number return the letter at i
        if i == index:
            return list[i]
        #increment i
        i += 1

def insert(list, index, value):
    '''
    function - insert a <value> into the list at a given <index> in the <list>
    :param list: - <list> input
    :param index: - <index> to search for
    :param value: - <value> to insert
    :return:
    '''
    # set counter
    i = 0
    # loop over the length of the list
    while i <= len(list):
        # checking to see if value is in the list
        if i == index:
            #check1 is equal index of i in the list
            check1 = list[:i]
            #increment check1 by the value
            check1 += value
            #check2 is equal to index of i from the start to zero
            check2 = list[i:]
            # list is equal to check1 plus check2
            list = check1 + check2
            #return the list
            return list
        # # if i is equal to the length of the list minus 1 return -1 (index starts at zero)
        if i == len(list)-1:
            #return the list and the value
            return list + value
        # increment the list by one
        i += 1

def value_in_list(list, value):
    '''
    function - find the <value> index in <list>
    :param list: - <list> input
    :param value: - <value> to search
    :return:
    '''
    # set counter
    i = 0
    # loop over the length of the <list>
    while i <= len(list):
        # if <value> and <list> index i are the same return True
        if list[i] == value:
            return True
        # if i is equal to the length of the list minus 1 return False (index starts at zero)
        if i == len(list)-1:
            return False
        # increment the counter
        i += 1

def concat(list1, list2):
    '''
    function - find the <value> index in <list>
    :param list1: - <list1> first list
    :param list2: - <list2> second list
    :return:
    '''
    output = list1 + " " + list2
    return output

def remove(list, value):
    '''
    function - insert a <value> into the list at a given <index> in the <list>
    :param list: - <list> input
    :param value: - <value> choose value
    :return:
    '''
    # set counter
    i = 0
    # loop over the length of the list
    while i <= len(list):
        # checking to see if value is in the list
        if list[i] == value:
            #check1 is equal to index of i on the list from
            check1 = list[:i]
            #check2 is equal to the value of of the index plus 1
            check2 = list[i+1:]
            # list is equal to check1 plus check2
            list = check1 + check2
            #return the list
            return list
        # # if i is equal to the length of the list minus 1 return -1 (index starts at zero)
        if i == len(list)-1:
            #return the list and the value
            return list + value
        # increment the list by one
        i += 1
