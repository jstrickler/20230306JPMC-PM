import sys

file_paths = sys.argv[1:]


for file_path in file_paths:
    print("reading:", file_path)
    with open(file_path) as file_in:
        for raw_line in file_in:
            pass  # etc etc


