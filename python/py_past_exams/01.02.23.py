'''Exercise 2. (Python) Create a program that analyzes the frequency of words in a text file and stores the
results in a dictionary. The program should also allow the user to perform several operations such as
displaying the frequency of a specific word, sorting the frequency of words in ascending or descending
order, and finding the top N most frequent words.
1. The path to the file should be taken from the command line argument
2. Read the text file and split the text into lowercase words (clean the text by removing punctuation
and converting it to lowercase)
2. Create a dictionary to store the frequency of each word. The key is the word and the value is its
frequency.
4. Implement the following functions:

    ● frequency_of_word(word): displays the frequency of a specific word

    ● sort_frequency(order='ascending'): sorts the frequency of words in ascending or descending order  

    ● top_N_frequent(N): displays the top N most frequent words  
5. Bonus:

    ● The program should also handle large text files efficiently.
    
    ● Remove Stop Words: Implement a function that removes common words such as "the", "a", "an", "and" from the frequency analysis. These words are known as stop words and do not add much value to the analysis.'''

import string 

input_f = input("Enter file to analyse: ")
open_f = open(input_f, "rt")
read_f = open_f.read()
string_f = str(read_f.strip())
lower_f = string_f.casefold()
clean_f = ''.join(char for char in lower_f if char not in string.punctuation)
split_f = clean_f.split()
frequency_dict = {}
for word in split_f:
    count = split_f.count(word)
    frequency_dict[word] = count
print(frequency_dict)


def frequence_of_word(word):
    if word in frequency_dict.keys():
        return f"the frequency of {word} is {frequency_dict.get(word)}"
    else:
        return "word not found"


def sort_frequency(order):
    if order not in ["ascending","descending"]:
        raise ValueError("invalid value for order. Only 'ascending' or 'descending' accepted.")
    elif order == "ascending":
        print(f"sorting in {order} order..")
        sorted_f_asc = dict(sorted(frequency_dict.items(), key=lambda item: item[1]))
        return sorted_f_asc
    elif order == "descending":
        print(f"sorting in {order} order..")
        sorted_f_desc = dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse= True))
        return sorted_f_desc
    

def top_N_frequent(n):
    if n > len(frequency_dict):
        raise ValueError("number too high")
    else:
        sorted_f_desc = sorted(frequency_dict.items(), key=lambda item: item[1], reverse= True)
        top_N = sorted_f_desc[:n]
        return top_N


print(frequence_of_word("24"))
print(sort_frequency("ascending"))
print(top_N_frequent(3))


''' Principles of clean code:
- started with a backbone: yes
- correct: yes
- readability: messed up in functions between print and return statements. I was not
    remembering how the 2 works. If the output of the function is relevant for further use, 
    use return! Print only to debug or for user interaction. Then to display the result, print
    the output of the function at call time.
- readability (small functions and meaningful names): tried my best but the first load and 
    tranform pipeline could be small separate functions.
- simplicity: the combinatorial space of all possible computer programs able to solve my 
    problems is huge, I don't know if mine is one of the simplest. I doubt.
- DRY: yes
- documentation: missing
- presence of scripts: the first part, functions are good
- reusable: no (but part of the fault is the problem description and arguments)
- testable: ni
- maintainable: hard to test independently everything but not bad either
- presence of unit test: no
'''

# Improved code by Chatgpt

import string
from collections import Counter
# definita funzione per lettura file

def process_file(filepath):
    stop_words = {"the", "a", "an", "and", "in", "on", "is", "to", "of", "it"}
    frequency_dict = Counter()
    with open (filepath, "r") as file:
        for line in file:
            # lowering, splitting and removing punctuation
            words = ''.join(char for char in line.lower() if char not in string.punctuation).split()
            # removing stopwords
            words_2 = [word for word in words if word not in stop_words]
            frequency_dict.update(words_2)

    return frequency_dict

def frequency_of_word(frequency_dict, word):
    return frequency_dict.get(word, 0)

def sort_frequency(frequency_dict, order):
    if order not in ["ascending", "descending"]:
        raise ValueError ("invalid value for order. Only 'ascending' or 'descending' accepted.") 
    else:
        return sorted(frequency_dict.items(), key=lambda item: item[1], reverse=(order == "descending"))
    
def top_N_frequent(frequency_dict, n):
    if n<=0:
        raise ValueError ("n must be a positive integer.")
    else:
        return sort_frequency(frequency_dict, order="descending")[:n]


filepath = input("provide file to analyse: ")
dict = process_file(filepath)
print(frequency_of_word(dict,"24"))
print(sort_frequency(dict, "ascending"))
print(top_N_frequent(dict, 3))

'''Migliorie:
    1. funzioni più semplici
    2. ottimizzata la lettura del file:
        il mio leggeva tutto il file e poi lo processavo
        ora leggo 1st linea e la processo, 2nd e così via.
    3. la frequenza delle parole viene contata con counter from collections di python. Se 
        gli si fornisce una stringa, conta i caratteri, se una lista, le parole.
    4. implementata rimozione delle stop words
    5. lettura e process del file sono ora una funzione.'''