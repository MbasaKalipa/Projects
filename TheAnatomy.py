#Add two numbers and then substract one
#def means a function is about to be defined

def sum_minus_one(number1,number2):   #function
    answer = number1 + number2
    final_answer = answer - 1
    return final_answer

a = 30
b = 23
answer = sum_minus_one(a,b)
print(answer)