import sys
lines: list[str] = []
while data := input():
    lines.append(data)

length = len(lines)

found_number = False
number_digits = ""
start_idx = 0
end_idx = 0

part_numbers: list[int] = []

for i in range(length):
    for j in range(len(lines[i])):
        current_char = lines[i][j]
        if current_char.isdigit():
            if not found_number:
                found_number = True
                start_idx = j
            number_digits += current_char
        elif found_number and not current_char.isdigit():
            found_number = False
            end_idx = j
        if not found_number and number_digits:
            is_part = False
            if i - 1 >= 0:
                is_part |= lines[i-1][start_idx] != "."
                is_part |= lines[i-1][end_idx] != "."
            if start_idx - 1 >= 0 and i - 1 >= 0:
                is_part |= lines[i-1][start_idx - 1] != '.'
            if start_idx - 1 >=0:
                is_part |= lines[i][start_idx - 1] != "."
            if i + 1 < length and start_idx - 1 >= 0:
                is_part |= lines[i + 1][start_idx - 1] != "."
            if i + 1 < length:
                is_part |= lines[i+1][start_idx] != "."
            