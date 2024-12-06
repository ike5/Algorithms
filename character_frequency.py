def build_character_frequency_table(input_string: str):
    table = {}
    for i in range(len(input_string)):
        current_character = input_string[i]
        if current_character in table:
            table[current_character] = table[current_character] + 1
        else:
            table[current_character] = 1
    return table
