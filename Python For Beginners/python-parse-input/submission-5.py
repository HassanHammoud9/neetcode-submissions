from typing import List

def read_integers() -> List[int]:
    mystring = input()
    mylist = mystring.split(",")
    for item in mystring:
        mylist.append(item)
    return mylist

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
