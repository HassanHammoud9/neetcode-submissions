from typing import List

def read_integers() -> List[int]:
    num_string = str(input())
    num_string.split(",")
    return list(num_string)

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
