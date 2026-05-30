from typing import List

def read_integers() -> List[int]:
    num_string = str(input())
    num_string.split(",")
    mylist = num_string
    return mylist

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
