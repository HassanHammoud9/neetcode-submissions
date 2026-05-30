from typing import List

def read_integers() -> List[int]:
    mystring = str(input())
    mylist = mystring.split(",")
    result = []
    for item in mylist:
        result.append(int(item))
    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
