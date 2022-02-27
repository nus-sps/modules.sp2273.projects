import glob
import os

import pyperclip


def create_row(file_info, file_no):
    replace = {
        '_': ' '
    }

    difficulty = file_info.split(os.sep)[0]
    file_name = file_info.split(os.sep)[-1]

    for to_replace, replace_with in replace.items():
        file_name = file_name.replace(to_replace, replace_with)

    file_name = file_name[:-6]      # Drop extention

    row_info = f"|{file_no:02d}|{file_name.upper():<50s}|{difficulty}|\n"

    return row_info


file_list = glob.glob('**/*.ipynb', recursive=True)
file_list.sort()
file_list

header = f"|\#|{'Project Title':<50}|Difficulty|\n"
header += f"|:{'-'}:|:{'-'*49}|:{'-'*6}:|\n"

table_text = header

for i, file_info in enumerate(file_list, 1):
    table_text += create_row(file_info, i)

print(table_text)
pyperclip.copy(table_text)
