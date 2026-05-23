def concatenate(s1: str, s2: str) -> str:
    st = s1+s2
    if(len(st)>10):
        return "Too long!"
    return st




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
