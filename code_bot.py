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

from os import write
import random
import csv


def make_dict():
    """Creates a dictionary using the HB Repo of Coding Challenges"""

    problems = {}

    with open('problems.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cc_name = row['cc_name']
            url_link = row['url_link']
            problems[cc_name] = url_link

    return problems



def choose_problems():
    """Function to choose three random coding challenges"""

    problems = make_dict()

    res = random.sample(list(problems.items()), k = 3)
    # res2 = random.choice(list(problems.items()))
    # res3 = random.choice(list(problems.items()))

    res0 = res[0]
    res1 = res[1]
    res2 = res[2]

    return res0, res1, res2



def display_problems():
    """Prints weekly Wed coding challenges"""

    res = choose_problems()

    cc_name1 = res[0][0]
    url_link1 = res[0][1]
    cc_name2 = res[1][0]
    url_link2 = res[1][1]
    cc_name3 = res[2][0]
    url_link3 = res[2][1]

    #TODO: implement datetime (i.e. "11.07.21")
    print('Weekly Wednesday Problems')
    print(f'Problem 1: {cc_name1} - {url_link1}')
    print(f'Problem 2: {cc_name2} - {url_link2}')
    print(f'Problem 3: {cc_name3} - {url_link3}')

    return cc_name1, url_link1, cc_name2, url_link2, cc_name3, url_link3



def remove_prob():
    """Remove problems from problems.csv - to avoid repeat"""

    #var for tuple
    weekly_probs = display_problems()

    cc_name1 = weekly_probs[0]
    url_link1 = weekly_probs[1]
    cc_name2 = weekly_probs[2]
    url_link2 = weekly_probs[3]
    cc_name3 = weekly_probs[4]
    url_link3 = weekly_probs[5]

    names_to_remove = [cc_name1, cc_name2, cc_name3]
    urls_to_remove = [url_link1, url_link2, url_link3]

    for name in names_to_remove:
        pass

    for url in urls_to_remove:
        pass

    return names_to_remove, urls_to_remove



def add_prob_to_used():
    """Add weekly problems to used_problems.csv - to avoid repeat"""

    problems_to_add = remove_prob()

    names = problems_to_add[0]
    urls = problems_to_add[1]

    #for testing
    # print('add_prob_to_used() - Problems to Add')
    # print(names)
    # print(urls)

    with open('used_problems.csv', 'a', newline='') as csvfile:
        fieldnames = ['cc_name', 'url_link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'cc_name': names[0], 'url_link': urls[0]})
        writer.writerow({'cc_name': names[1], 'url_link': urls[1]})
        writer.writerow({'cc_name': names[2], 'url_link': urls[2]})

add_prob_to_used()