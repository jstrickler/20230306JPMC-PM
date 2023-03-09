
# python type hints

def get_message():
    return "Hello, JPMC world"

m = get_message()
print(f"m: {m}")

print(f"get_message(): {get_message()}")

def show_message():
    message = get_message()
    print(message)

show_message()

def hello(whom="world"):
    print(f"Hello, {whom}")

hello("New York")
hello("world")
hello("")
hello()

#  def spam(p1, *p2):

def search_files(search_string, *file_paths):
    print(f"search_string: {search_string}")
    print(f"file_paths: {file_paths}")
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_string in raw_line:
                    print(raw_line.rstrip())

search_files('lizard', 'DATA/words.txt')
print('-' * 60)
search_files('rabbit', 'DATA/words.txt', 'DATA/alice.txt')
print('-' * 60)




