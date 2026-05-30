from typing import List

def read_integers() -> List[int]:
    num_string = str(input())
    mylist = num_string.split(",") 
    return mylist

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
