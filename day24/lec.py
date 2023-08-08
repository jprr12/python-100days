# day 24 - files, directories, and paths

# adding high score display feature in snake game
# local only

# ==================================================
# # opening, reading, writing files using with keyword
# # opening a file with open/close
# file = open('file.txt')
# contents = file.read()
# print(contents) # returns txt in file.txt
# file.close() # necessary everytime you open a file

# # opening a file with 'with' keyword
# with open('file.txt') as file:
#     contents = file.read()
#     print(contents)
# # immediately closes file after user is done

# # writing on external file with python
# with open('file.txt', mode='w') as file:
#     file.write('new text') # replaces all the text in the file
#     # replace mode to 'a' to append instead

# opening a non existent file will create that file instead
# with open('another_file.txt', mode='w') as file:
#     file.write('hello new world')
#     # creates a new file with some txt written on it

# ==================================================
# relative and absolute file paths
# absolute file paths
# relative file paths
with open('../../../file.txt') as file:
    content = file.read()
    print(content)

with open('snake/data.txt') as data:
    d = data.read()
    print(d)

