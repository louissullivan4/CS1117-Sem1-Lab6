# Y1-Sem1-Lab6
List manipulation and lists
1.Write your own version of the following Python functions, using while loops, and add comments to your code.  
Example of what is returned by the function call is shown: 

a. count(list, value) - function to return the number 
of times value occurs in list i. count("hello", "l") -> 2 (the integer 2 is returned) 
 
b. index(list, value) - function to return the first index that value occurs in list.  
Return -1 if the value does not occur in the list i. index("hello", "o") -> 4 ii. index("hello", "p") -> -1 
 
c. get_value(list, index) - function to return the value that occurs in the list at index i. get_value("hello", 1) -> "e" 
 
d. insert(list, index, value) - function to return list, after you have added value at index 
(remember to check the length of the list and if index is larger than len(list) add as a new index at the end of list) 
i. insert("hello", 1, "a") -> "hallo" ii. insert("hello", 5, "p") -> "hellop" 
 
e. value_in_list(list, value) - function to return True or False if value occurs in list 
i. we can then use "if value_in_list(list, value):" as a boolean check ii. value_in_list("hello", "o") - True 
iii. value_in_list("hello", "a") - False 
 
f. concat(list1, list2) - function to return a new list, which is a combination of list1 and list2 i. concat("hello", " world") -> "hello world" 
 
g. remove(value, list) - function to return list with the first occurrence of value removed from list i. remove("h", "hello") -> "ello"
