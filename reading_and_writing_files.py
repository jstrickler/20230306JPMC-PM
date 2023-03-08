import re
file_path = "DATA/mary.txt"

file_obj = open(file_path, "r")
# read file here....
file_obj.close()

with open(file_path) as mary_in:
    for raw_line in mary_in:  # mary_in.readline()
        line = raw_line.rstrip()  # remove \n from end of line
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()
    print(contents)
    print("=" * 20)
    print(repr(contents))
print('-' * 60)

with open(file_path) as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)

file_path = "DATA/alice.txt"
with open(file_path) as alice_in:
    for raw_line in alice_in:
        if re.search(r"\bpig\b", raw_line):
            if not '-pig' in raw_line:
                if not 'pig-' in raw_line:
                    line = raw_line.rstrip()
                    print(line)
print('-' * 60)

file_path = "DATA/breakfast.txt"
with open(file_path) as breakfast_in:
    foods = breakfast_in.read().splitlines()
    print(f"foods: {foods}")
    unique_foods = set(foods)
    print(f"unique_foods: {unique_foods}")

with open('DATA/words.txt') as words_in:
    with open('big_words.txt', "w") as words_out:
        for raw_word in words_in:
            word = raw_word.rstrip()
            if len(word) >= 20:
                words_out.write(raw_word)