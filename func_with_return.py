def my_avg(a: int, b: int) -> float:  #a
    """Returns the average of two integers."""
    return (a + b) / 2

def my_headline(s: str) -> str:  #b
    """Returns the string in uppercase with an exclamation mark at the end."""
    return s.upper() + "!"

def concat_list(list1: list[int], list2: list[int], list3: list[int]) -> list[int]:  #c
    """Concatenates three lists into one."""
    return list1 + list2 + list3
