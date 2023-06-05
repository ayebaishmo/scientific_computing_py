def arithmetic_arranger(problems , show_answers = False):
    # Declare the lines where the result will sit
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    arranged_problems = ""

    # The problems should not exceed 5
    if len(problems) > 5:
        return "Error: Too many problems"
    
    # Iterate through the problem to split it in to three parts
    for problem in problems:
        num1, operator, num2 = problem.split()

        # Checking if the operator are + or -
        if operator not in ["+", "-"]:
            return "Error: Operator must be + or  -."
        
        # Checking if the nums are digits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits"
        
        # Checks of the digits are more than 4
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits"
        
        # This line calculates the maximum length between num1 and num2 plus 2 account for additional space plus to
        #account for additional space needed fot the operator. It uses to align numbers
        width = max(len(num1), len(num2)) + 2

        # The eval method solves the problem by turning it in to solution 3 + 4 =7
        # However we have to turn the solution in to string. str
        result = str(eval(problem))

        # The rjust method is used to right align the numbers within specified width.
        line1 += num1.rjust(width)
        line2 += operator + num2.rjust(width - 1)
        line3 += "-" * width
        line4 += result.rjust(width)

        # These lines add four spaces to each line.
        if problem != problems[-1]:
            line1 = line1 + "    "
            line2 = line2 + "    "
            line3 = line3 + "    "
            line4 = line4 + "    "
    
    # The lines are then concatenated into the arranged_problems string, with newlines (\n) separating each line.
    arranged_problems += line1 + "\n" + line2 + "\n" + line3
    if show_answers:
        arranged_problems += "\n" + line4
    print(arranged_problems)

arithmetic_arranger(["2 + 3", "3 - 5", "9 + 5", "745 + 32"], True)