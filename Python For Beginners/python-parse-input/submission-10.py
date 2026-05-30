from typing import List

def read_integers() -> List[int]:
    mystring = str(input())
    mystring = mystring.split(",")
    result = []
    for item in mystring:
        result.append(int(item))
    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
