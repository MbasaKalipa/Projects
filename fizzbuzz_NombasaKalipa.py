# matching the provided sample output
print ("Welcome to FizzBuzz!")

while True:
    maximum_num = int(input("Enter a maximum number: "))  #promting a user to enter a maximum number
    if maximum_num < 1:
        print("Please enter a number greater than or equal to 1.")
    else:
        break       # exit the loop if the input is indeed greater than or equal to 1

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0
    # initiating variables


for i in range(1, maximum_num + 1):
    # main loop: this loop iterates through numbers from 1 to the maximum number entered by the user.
    # the range function used in this for loop always stops one number short of the end value, hence "maximum_num + 1"
    if i % 3 == 0 and i % 5 == 0: # checking division by both 3 and 5
        print(f"{i} - FizzBuzz")
        fizzbuzz_count += 1
    elif i % 3 == 0:  # checking division by 3 only
        print(f"{i} - Fizz")
        fizz_count += 1
    elif i % 5 == 0:  # checking division by 5 only
        print(f"{i} - Buzz")
        buzz_count += 1
    else:          # if none of the above conditions are met, print the number only
        print(i)
print(f"Done! Checked {maximum_num} numbers.")
print(f"Summary: {fizz_count} Fizz, {buzz_count} Buzz, {fizzbuzz_count} FizzBuzz")
# once the for loop is done it checks all the numbers, program then provides summary of results.
