# %% in random package we can use in random.choice() to choice elements in any indexable sequence
import random as r
my_list = [1, 2, 3, 4, 5, 'avi', 'helo', True, False]
r.choice(my_list)


# %% to unpack any iterable can use in *
my_list = [1, 2, 3, 4, 5, 'avi', 'helo', True, False]
print(*my_list)
print(my_list)

# or like this
string = "i live in jerusalem"
list_string = [*string]
print(list_string)
print(*string)

# %% print attributes of any element
string = "i live in jerusalem"
print(dir('string'))


# %% to complex some type
ConnectionOptions = dict[str, str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOptions]

# %% or new type
from typing import NewType
UserId = NewType('UserId', int)
some_id = UserId(524313)

# %% in dict can use in get to defolt value
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}


def greeting(userid):
    name = name_for_userid.get(userid, "there")
    return f"Hi {name}!"


# %% add = to Fstring print the value of vaeable with him name
my_list = [1, 2, 3, 4, 5, 'avi', 'hello', True, False]
print(f'{my_list=}')

# %% use pint to convernt between metric and unmetric unit
import pint
ureg = pint.UnitRegistry()
print(7*ureg.meter + 3*ureg.inch)


# %% * use to unpacked iterable
lst = [1, 2, 3, 4, 5, 6]
a, *b, c = lst
print(f'{a=}\n{b=}\n{c=}')


# %%
pow1 = [lambda x:x**n for n in range(4)]
pow2 = [lambda x, n=n: x**n for n in range(5)]
for i in pow2:
    print(i(3))

# %% use itertools.cycle to difinde some list as infintum
import itertools
names = itertools.cycle(['avi', 'moyshi', 'david', 'yosef'])
for i in range(100):
    print(names.__next__())

# %% import files form anthor folder, You can access one folder up like this
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

# import src.car  as car
#from  src.car import *


# %% using strint leaberi
import string
user_input = 'a'
while user_input != '':
    user_input = input('enter some leeter')
    assert len(user_input) == 1, 'your choice most be one leeter'
    categories = []
    if user_input not in string.printable:
        categories.append('your choice is not printable')
    if user_input in string.ascii_letters:
        categories.append('ascii_letters')
    if user_input in string.ascii_lowercase:
        categories.append('ascii_lowercase')
    if user_input in string.ascii_uppercase:
        categories.append('ascii_uppercase')
    if user_input in string.digits:
        categories.append('digits')
    if user_input in string.hexdigits:
        categories.append('hexdigits')
    if user_input in string.octdigits:
        categories.append('octdigits')
    if user_input in string.punctuation:
        categories.append('punctuation')
    if user_input in string.whitespace:
        categories.append('whitespace')
    print(user_input + " is \n\t" + '\n\t'.join(categories))


# %% use faker
# https://faker.readthedocs.io/en/master/providers.html
from faker import Faker
fake = Faker()
fake.sentence()
fake.name()
fake.address()
fake.text()

# %%

my_word_list = [
    'אני', 'אתה', 'הם',
    'אנשים', 'יפים', 'הולכים',
    'sesame', 'Jelly', 'beans',
    'pie', 'bar', 'Ice', 'oat']
fake.sentence(ext_word_list=my_word_list)
# %%


# %%
