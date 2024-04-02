import random
import time

OPERATORS =["+","-","*"]
MIN_OPERAND = 2
MAX_OPERAND = 20
TOTAL_NUMBER_OF_PROBLEMS = 12

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator+ " " + str(right)
    answer = eval(expr)
    return expr, answer

TOTAL_NUMBER_OF_PROBLEMS=int(input("Enter the number problems you'd like to solve:  "))
print("There won't be any division cause it would be too hard, lol!")
start_Time = time.time();
for i in range(TOTAL_NUMBER_OF_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ":" + expr + "=")
        if guess == str(answer):
            break
end_time = time.time()
elapsed_time = end_time - start_Time
print("Congratulations on completing the test")
print("I'm sure you have a better understanding of how good your math actually is...")
print("It took you " + str(round(elapsed_time,2)) + " seconds to complete the test.")
print("See you next time Chow!")
