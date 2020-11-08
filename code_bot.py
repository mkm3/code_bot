"""
Pseudocode

hb_repo = { “cc_name” : “url_link”}
- column_a = “cc_name”
- column_b = “url_link”

*used_problems = { “cc_name” : “url_link” }

dict.values() - returns all values
dict.get(“key_name”) - returns value
dict.items() - return a list of (key, value) pairs in tuples


Functions - https://www.tutorialspoint.com/python3/python_dictionary.htm

"""

import random
import csv

def make_dict():

    problems = {}

    with open('problems.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cc_name = row['cc_name']
            url_link = row['url_link']
            problems[cc_name] = url_link

    return problems

def choose_problem():

    problems = make_dict()

    res = random.sample(list(problems.items()), k = 3)
    # res2 = random.choice(list(problems.items()))
    # res3 = random.choice(list(problems.items()))

    res0 = res[0]
    res1 = res[1]
    res2 = res[2]

    print(res0, res1, res2)
    return res0, res1, res2

def display_problems():

    res = choose_problem()

    #TODO: implement datetime (i.e. "11.07.21")
    print('Weekly Wednesday Problems')
    print(f'Problem 1: {res[0]}')
    print(f'Problem 2: {res[1]}')
    print(f'Problem 3: {res[2]}')

display_problems()

def remove_prob():
    pass

def add_prob_to_used():
    pass