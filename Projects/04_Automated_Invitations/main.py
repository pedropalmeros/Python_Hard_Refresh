#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def get_names():
    pass


def get_letter():
    pass

def personalize_letter():
    pass

name_file_dir = ".\\Input\\Names\\invited_names.txt"
letter_file_dir = ".\\Input\\Letters\\starting_letter.txt"
output_letter_dir = ".\\Output\\ReadyToSend\\"

with open(name_file_dir,'r') as name_file:
    names = name_file.readlines()
names = [name.rstrip() for name in names]
with open(letter_file_dir,'r') as letter_file:
    letter = letter_file.readlines()

for name in names:
    personalized_letter = letter[:]
    personalized_letter[0] = personalized_letter[0].replace("[name]", name)
    
    with open(f"{output_letter_dir}{name}.txt",'w') as personalized_letter_file:
        personalized_letter_file.writelines(personalized_letter)


    