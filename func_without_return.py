# 1
def my_ascending(a: int, b: int) -> list[int]:  #a
    """Returns the numbers between a and b in ascending order."""
    return [num for num in range(a, b + 1)];

def my_details(s: str) -> tuple[str, str, str]:  #b
    """Returns the first, middle, and last character of a string."""
    length = len(s);
    middle = length // 2;
    return s[0], s[middle], s[-1];

def say_bool(b: bool) -> str:  #c
    """Returns 'yes' if the boolean is True, otherwise returns 'no'."""
    return "yes" if b else "no";

def print_zugi(numbers: list[int]) -> list[str]:  #d
    """Returns 'even' for even numbers and 'odd' for odd numbers in the list."""
    return ["even" if number % 2 == 0 else "odd" for number in numbers];

def my_statistics(scores: list[int]) -> dict[str, float | int]:  #e
    """Returns the highest score, lowest score, count, and average of the scores."""
    if not scores:
        return {"error": "No scores to analyze"};

    highest = max(scores);
    lowest = min(scores);
    count = len(scores);
    average = sum(scores) / count;

    return {
        "highest": highest,
        "lowest": lowest,
        "count": count,
        "average": average
    };

def my_statistics_extended(scores: list[int]) -> dict[str, float | int]:  #f
    """Returns additional statistics: number of scores above 90 and below 55, and the standard deviation."""
    import math;

    if not scores:
        return {"error": "No scores to analyze"};

    highest = max(scores);
    lowest = min(scores);
    count = len(scores);
    average = sum(scores) / count;

    above_90 = len([score for score in scores if score > 90]);
    below_55 = len([score for score in scores if score < 55])
    variance = sum((score - average) ** 2 for score in scores) / count
    std_deviation = math.sqrt(variance)

    return {
        "highest": highest,
        "lowest": lowest,
        "count": count,
        "average": average,
        "above_90": above_90,
        "below_55": below_55,
        "std_deviation": std_deviation
    }

def get_int(prompt: str) -> int:  #5
    """Gets an integer from the user input, ensuring it is a valid integer."""
    while True:
        try:
            return int(input(prompt));
        except ValueError:
            print("Invalid input. Please enter an integer.");

def int_get(prompt: str) -> int:  # bonus
    """Gets an integer from the user input, ensuring it is a valid integer, with a given prompt."""
    while True:
        try:
            return int(input(prompt));
        except ValueError:
            print("Invalid input. Please enter an integer.");

def no_return_func():  #6
    """Function with no return statement."""
    x = 10;

def return_none_func():  #6
    """Function that explicitly returns None."""
    return None

def explain_return_and_break():  #6
    """
    return: Exits the function and optionally returns a value.
    break: Exits the nearest enclosing loop.
    """
    result = ""
    for i in range(5):
        if i == 3:
            break
        result += str(i) + " ";
    return result;
