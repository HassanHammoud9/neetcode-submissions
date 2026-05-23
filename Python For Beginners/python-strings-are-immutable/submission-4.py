def remove_fourth_character(word: str) -> str:
    rmc = word[:5]
    rmc2 = word[5:]
    return rmc + rmc2

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
