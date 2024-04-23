import pickle


data = {"login": "gfkhd", "password": "1231534"}

# serialized_data = pickle.dumps(data)
#
# print(serialized_data)
#
# read_data = pickle.loads(serialized_data)
#
# print(type(read_data), read_data)

# with open('data.pickle', 'wb') as file:
#     pickle.dump(data, file)

with open('data.pickle', 'rb') as file:
    read_data = pickle.load(file)

print(type(read_data), read_data)

##################################################

import pickle
import gzip


data = {"login": "gfkhd", "password": "1231534"}


# with gzip.open("data.gz", 'wb') as file:
#     serialized_data = pickle.dumps(data)
#     file.write(serialized_data)


with gzip.open('data.gz', 'rb') as file:
    serialized_data = file.read()
    read_data = pickle.loads(serialized_data)

print(type(read_data), read_data)

########################################################

import pickle
import gzip
from pratcice3 import Person


with gzip.open("person.gz", 'rb') as file:
    serialized_data = file.read()
    read_person = pickle.loads(serialized_data)


print(type(read_person), read_person)
read_person.print_info()

#################################################################


import pickle
import gzip


data = {"logins": ["hjlk", "jkhj", "hjkj"],
        "passwords": ["2132", "4546843", 13451],
        "info": {"version": "1.0",
                 "date release": "2024"}}


with gzip.open("data.gz", 'wb') as file:
    serialized_data = pickle.dumps(data)
    file.write(serialized_data)


with gzip.open('data.gz', 'rb') as file:
    serialized_data = file.read()
    read_data = pickle.loads(serialized_data)

print(type(read_data), read_data)

#########################################################

import pickle
import gzip


# with open("large_file.txt", 'w') as file:
#     for i in range(100_000):
#         file.write(f"Line number {i+1} in large file.\n")

# with gzip.open('large_file.gz', 'wb') as gzip_file:
#     with open("large_file.txt", 'r') as txt_file:
#         data = txt_file.read()
#
#         serialized_data = pickle.dumps(data)
#         gzip_file.write(serialized_data)

# with open('large_file.pickle', 'wb') as pickle_file:
#     with open("large_file.txt", 'r') as txt_file:
#         data = txt_file.read()
#
#         pickle.dump(data, pickle_file)

with gzip.open("large_file.gz", 'rb') as file:
    serialized_data = file.read()
    data = pickle.loads(serialized_data)

    lines = data.split('\n')
    print(*lines[:10], sep='\n')

#################################################################

import pickle
import gzip


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Name {self.name} with age {self.age}')


person = Person("Anna", 31)

# with open('person.pickle', 'wb') as file:
#     pickle.dump(person, file)
#
# with open('person.pickle', 'rb') as file:
#     read_person = pickle.load(file)

with gzip.open("person.gz", 'wb') as file:
    serialized_data = pickle.dumps(person)
    file.write(serialized_data)

with gzip.open("person.gz", 'rb') as file:
    serialized_data = file.read()
    read_person = pickle.loads(serialized_data)


print(type(read_person), read_person)
read_person.print_info()