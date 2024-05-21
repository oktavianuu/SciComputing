The problem for this project can be found here: [arithmetic formatter](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-an-arithmetic-formatter-project/build-an-arithmetic-formatter-project).

To tackle this problem, we will build a function called arithmetic_arranger which will take a list of arithmetic problems and arrange them vertically and side-by-side as per the specified rules. The function will also handle error checking and optionally display the results of the arithmetic operations.

Here's a step-by-step approach to implementing this function:

1. __Validate Input__: Check if the number of problems exceeds five, if the operators are valid, if the numbers contain only digits, and if the numbers do not exceed four digits.
2. __Format Problems__: For each valid problem, determine the width required for alignment based on the longer operand. Arrange the numbers and operators with the appropriate spacing.
3. __Construct the Output__: Combine all formatted problems into a single string with appropriate spacing and line breaks. If the display_answers flag is set to True, compute and include the answers.

Solution: the solution can be found in the ```arithmetic_formatter.py``` in this folder. 

#### Code explanation
1. __Validation__:
    * We check if the number of problems exceeds 5.
    * We split each problem and validate if it contains exactly three parts (two operands and one operator).
    * We check if the operator is either + or -.
    * We ensure both operands contain only digits and do not exceed four digits in length.
2. __Formatting__:
    * For each problem, calculate the required width for alignment, which is based on the length of the longer operand plus 2 spaces (one for the operator and one for padding).
    * Align the operands and operator properly with the calculated width.
    * Prepare lines for the top operand, the operator line, the dashes line, and optionally the result line.
3. __Constructing the Output__:
    * Join the formatted lines with four spaces between each problem.
    * Return the formatted string which can optionally include the computed results