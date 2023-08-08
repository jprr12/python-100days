#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Step 1: store names in a list
invited = []
# open file containing names
with open('Input/Names/invited_names.txt', 'r') as names:
    for name in names.readlines():
        invited.append(name.strip('\n')) # clear whitespaces off the names and append the names to the list

# check name list if code worked; remove after testing
# print(invited)

# Step 2: open starting letter
with open('Input/Letters/starting_letter.txt', 'r') as letter:
    # store letter contents in a variable
    invitation = letter.read()
    
# print(invitation) # remove after testing

# Step 3: loop through name list
for name in invited:
    # replace [name] with the appropriate name in the list
    # Step 4: create outgoing letter each personalized with the names of invited
    with open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w') as outgoing_letter:
        outgoing_letter.write(invitation.replace('[name]', name))

