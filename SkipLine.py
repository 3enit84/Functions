def SkipLine(file_name, number_of_lines_to_skip):
    for i in range(number_of_lines_to_skip):
        line = file_name.readline()
    return line
