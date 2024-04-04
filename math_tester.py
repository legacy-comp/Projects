import time
import random
import math

# variable constants (by user)
question_asked: int = 10
decimal_precision: int = 2
op_list: list = ['+', '-', '*', '/', '^', '√̅ ']
op_weights: tuple = (0.16, 0.16, 0.16, 0.16, 0.16, 0.16)

# constants
i: int = 0
asked_add: int = 0
asked_sub: int = 0
asked_mul: int = 0
asked_div: int = 0
asked_pow: int = 0
asked_sqrt: int = 0
correct_add: int = 0
correct_sub: int = 0
correct_mul: int = 0
correct_div: int = 0
correct_pow: int = 0
correct_sqrt: int = 0

ops = {
    '+': (lambda x, y: x + y),
    '-': (lambda x, y: x - y),
    '*': (lambda x, y: x * y),
    '/': (lambda x, y: round(x / y, decimal_precision)),
    '^': (lambda x: x**2),
    '√̅ ': (lambda x: math.sqrt(x))
}

def main():
    global i, asked_add, asked_div, asked_mul, asked_sub, asked_pow, asked_sqrt
    global correct_add, correct_sub, correct_mul, correct_div, correct_pow, correct_sqrt
    start_time = time.time()
    while i < question_asked:
        op: str = random.choices(population=op_list, weights=op_weights)[0]

        if op == '^' or op == '√̅ ':
            num1: int = random.randint(1, 100)
        else:
            num1: int = random.randint(1, 100)
            num2: int = random.randint(1, 100)

        if op == '^':
            correct_ans = ops[op](num1)
        elif op == '√̅ ':
            correct_ans = ops[op](num1**2)
        else:
            correct_ans = ops[op](num1, num2)

        while True:
            try:
                if op == '^':
                    ans = float(input(f"{num1}{op}2: "))
                elif op == '√̅ ':
                    ans = float(input(f"{op}{num1**2}: "))
                else:
                    ans = float(input(f"{num1}{op}{num2}: "))
                break
            except ValueError:
                continue

        if op == '+':
            asked_add += 1
            if ans == correct_ans:
                print("correct!")
                correct_add += 1
            else:
                print("incorrect")
                print(correct_ans)
        elif op == '-':
            asked_sub += 1
            if ans == correct_ans:
                print("correct!")
                correct_sub += 1
            else:
                print("incorrect")
                print(correct_ans)
        elif op == '*':
            asked_mul += 1
            if ans == correct_ans:
                print("correct!")
                correct_mul += 1
            else:
                print("incorrect")
                print(correct_ans)
        elif op == '/':
            asked_div += 1
            if ans == correct_ans:
                print("correct!")
                correct_div += 1
            else:
                print("incorrect")
                print(correct_ans)
        elif op == '^':
            asked_pow += 1
            if ans == correct_ans:
                print("correct!")
                correct_pow += 1
            else:
                print("incorrect")
                print(correct_ans)
        elif op == '√̅ ':
            asked_sqrt += 1
            if ans == correct_ans:
                print("correct!")
                correct_sqrt += 1
            else:
                print("incorrect")
                print(correct_ans)
        i += 1
    else:
        end_time = time.time()
        total_time = float("{:.2f}".format(end_time - start_time))
        total_correct = correct_add + correct_sub + correct_mul + correct_div + correct_pow + correct_sqrt
        total_asked = asked_add + asked_sub + asked_mul + asked_div + asked_pow + asked_sqrt
        print(f"\ntotal correct answers are {total_correct}/{total_asked}")
        print(f"in addition: {correct_add}/{asked_add} are correct")
        print(f"in subtraction: {correct_sub}/{asked_sub} are correct")
        print(f"in multiplication: {correct_mul}/{asked_mul} are correct")
        print(f"in division: {correct_div}/{asked_div} are correct")
        print(f"in square: {correct_pow}/{asked_pow} are correct")
        print(f"in square_root: {correct_sqrt}/{asked_sqrt} are correct")
        print(f"total time taken is {total_time}s")
        print(f"average time taken in each question is {total_time // 10}")

if __name__ == '__main__':
    main()
