def orderAlt(input_list):
    list2 = sorted([element for element in input_list if element % 2 == 0])
    list3 = sorted([element for element in input_list if element % 2 != 0], reverse = True)
    return list2 +list3

list1 = []
i = 0

def get_user_input():
    user_list = []
    while True: 
        try:
            elemento = int(input("Inserire integer lista (digitare -1 per interrompere processo.): "))
            if elemento == -1:
                print("interruzione processo")
                break
            else:
                user_list.append(elemento)
                print(f"Lista corrente: {user_list}")
        except ValueError:
            print("Inserire numero intero valido.")
    return user_list

'''SOME TESTING

# If the input list is empty
assert orderAlt([]) == []
# If the input list contains only evens
assert orderAlt([2, 4, 6]) == [2, 4, 6]
# If the input list contains only odds
assert orderAlt([1, 3, 5]) == [5, 3, 1]'''

if __name__ == "__main__":
    # Collect user input
    list1= get_user_input()
    # print ordered list
    print("Lista riordinata: ", orderAlt(list1))


"""Principles of clean code:
    - started with a backbone: yes
    - correct: yes
    - readability (small functions and meaningful names): get_user_input was not a function at first,
        moreover I used list as parameter of the 1st funciton, not a good idea. list already exists 
        in py
    - simplicity: the combinatorial space of all possible computer programs able to solve my 
        problems is huge, I don't know if mine is one of the simplest. I doubt.
    - DRY: yes
    - documentation: missing, I should add docstrings and types of input/ output importing the typing 
        library
    - presence of scripts: at first yes
    - reusable: no (but part of the fault is the problem description and arguments)
    - testable: no at first, now yes
    - maintainable: hard to test independently everything but not bad either
    - presence of unit test: yes
    - modularity: yes thanks to the main variable
    """