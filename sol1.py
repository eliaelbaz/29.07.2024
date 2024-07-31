from func_without_return import (
    my_ascending,
    my_details,
    say_bool,
    print_zugi,
    my_statistics,
    my_statistics_extended,
    get_int,
    int_get,
    no_return_func,
    return_none_func,
    explain_return_and_break
);

print("Ascending order from 7 to 12:");
print(my_ascending(7, 12));  #a

print("\nDetails of string 'AI is the best':");
print(my_details("AI is the best"));  #b

print("\nSay bool with True:");
print(say_bool(True)); #c
print("Say bool with False:");
print(say_bool(False));  #c


print("\nEven or odd for list [14, 14, 15, 10, 2, 3, 5]:");
print(print_zugi([14, 14, 15, 10, 2, 3, 5]));  #d

#  ( e . f)
scores = [];
while True:
    score = int_get("Enter a score (or type '-99' to finish): ");  # bonus
    if score == -99:
        break
    if 0 <= score <= 100:
        scores.append(score);

print("\nStatistics of scores:");
print(my_statistics(scores));  #e
print("\nExtended statistics of scores:");
print(my_statistics_extended(scores));  #f


print(no_return_func());  #6

print(return_none_func());  #6

print(explain_return_and_break());  #6
