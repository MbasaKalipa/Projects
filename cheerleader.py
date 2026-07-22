word = input("Enter your favourite word: ")# Getting the users iput name.
vowels = ["A", "E", "I", "O", "U"]  # vowels list to check if the letter is a vowel or not.
my_word = word.upper() # to change the final product to uppercase as instructed in the task. 

for letter in my_word:   # looping through the letters in the word and checking if they are vowels or not.
    if letter.upper() in vowels:    
        print(f"Give me an {letter}!")   # if the letter is a vowel, it will print "an" before the letter.
    else:
        print(f"Give me a {letter}!")     # if the letter is not a vowel, it will print "a" before the letter.
print(f"What does it say????? {my_word}!!!!!!") # Lastly here, it needs to print the final product as in shown in the task. 
