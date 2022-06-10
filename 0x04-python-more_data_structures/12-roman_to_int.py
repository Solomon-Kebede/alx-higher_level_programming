#!/usr/bin/python3
def roman_to_int(roman_string):
    converter = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    if not isinstance(roman_string, str):
        return 0
    roman_nums_list = list(roman_string)
    result = [converter[roman_nums_list[0]]]
    for i in range(1, len(roman_nums_list)):
        val_1 = converter[roman_nums_list[i - 1]]
        val_2 = converter[roman_nums_list[i]]
        if val_1 >= val_2:
            result.append(val_2)
        else:
            result.append(-2 * val_1 + val_2)
    return sum(result)
