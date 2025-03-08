''' Exercise 2. (Python) Write a Python program implementing a set data structure using only lists. 
You need to implement the following functions providing methods for set operations:
    ● add(set_data, elem) method that takes an element as input and adds it to the set represented by
    the list set_data. The method should not add the element if it already exists in the set.
    ● remove(set_data, elem) method that takes an element as input and removes it from the set
    represented by the list set_data. The method should not raise an error if the element does not exist
    in the set.
    ● contains(set_data, elem) method that takes an element as input and returns True if the element
    exists in the set, and False otherwise.
    ● size(set_data) method that returns the number of elements in the set.
    ● union(set_data1, set_data2) method that takes two sets as input and returns a new set that
    contains all the elements from both sets, without any duplicates.
    ● intersection(set_data1, set_data2) method that takes two sets as input and returns a new set
    that contains only the common elements between the two sets.
Test your set implementation, starting from an empty set (list) and then invoking several time the set
methods above defined.'''

from typing import list, bool

def add(set_data: list, elem) -> list:
    elem = input("Write element to add: ")
    if elem not in set_data:
        set_data.append(elem)
    else:
        pass
    return set_data

def remove(set_data: list, elem) -> list:
    elem = input("Write element to remove: ")
    if elem in set_data:
        set_data.remove(elem)
    else: 
        pass
    return set_data

def contains(set_data: list, elem) -> bool:
    elem = input("Write element to check: ")
    if elem in set_data:
        return True
    else:
        return False
    
def size(set_data: list) -> int:
    return len(set_data)

def union(set_data1: list, set_data2: list) -> list:
    return set.data1.union(set_data2)

def intersect(set_data1: list, set_data2: list) -> list:
    return set.data1.intersect(set_data2)

