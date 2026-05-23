def remove_fourth_character(word: str) -> str:
    rm1 = word[:5]
    rm2 = word[5:]
    return rm1 + rm2


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
