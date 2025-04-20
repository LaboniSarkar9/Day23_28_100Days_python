# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# read file
'''
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

'''

# write

with open("my_file.txt", mode="a") as file:
    file.write("\n New text.")

with open("new_file.txt", mode="w") as file:
    file.write("New text.")