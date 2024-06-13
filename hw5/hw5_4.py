import re

def evaluate_expression(expression):
    try:
        # Check for unsupported characters
        if re.search(r'[^0-9+\-*/().\s]', expression):
            raise ValueError("Unsupported character error")

        # Check for balanced parentheses
        if expression.count('(') != expression.count(')'):
            raise ValueError("Unbalanced parentheses error")

        # Evaluate the expression
        result = eval(expression)
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Operand error"
    except ValueError as ve:
        return f"Error: {ve}"

def main():
    while True:
        user_input = input("Enter an expression to evaluate or 'q' to quit: ").strip()
        if user_input.lower() == 'q':
            break
        print(evaluate_expression(user_input))

if __name__ == "__main__":
    main()
