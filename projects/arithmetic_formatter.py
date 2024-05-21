def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_operands = []
    operators = []
    second_operands = []
    solutions = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Incorrect problem format.'
        
        first_operand, operator, second_operand = parts
        
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)
        
        if display_answers:
            if operator == '+':
                solutions.append(str(int(first_operand) + int(second_operand)))
            elif operator == '-':
                solutions.append(str(int(first_operand) - int(second_operand)))

    line1 = []
    line2 = []
    line3 = []
    line4 = []
    
    for i in range(len(problems)):
        first_operand = first_operands[i]
        operator = operators[i]
        second_operand = second_operands[i]
        solution = solutions[i] if display_answers else ""
        
        width = max(len(first_operand), len(second_operand)) + 2
        line1.append(first_operand.rjust(width))
        line2.append(operator + " " + second_operand.rjust(width - 2))
        line3.append("-" * width)
        if display_answers:
            line4.append(solution.rjust(width))
    
    arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
    if display_answers:
        arranged_problems += "\n" + "    ".join(line4)
    
    return arranged_problems

# Examples
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
