

i = 0
while i < 3:
    print(i)
    i += 1
print("DONE\n")

while True:
    #  break -- exit loop
    #  continue -- go back to top
    user_name = input("Please enter your name: ")
    if user_name.strip() == '':
        print("please enter name")
        continue
    if user_name.lower() == 'q':
        break
    print(f"{user_name} registered")

print("goodbye")

