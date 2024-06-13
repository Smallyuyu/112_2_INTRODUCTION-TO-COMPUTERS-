print('Welcome to the simple calculator program!')
while(1):
    s = float(input('Enter the first number: '))
    f = float(input('Enter the second number: '))
    op = str(input('Select an arithmetic operation (+, -, *, /): '))
    if(op == '+'):
        print('Result: ',s + f)
    elif(op == '-'):
        print('Result: ',s - f)
    elif(op == '*'):
        print('Result: ',s * f)
    elif(op == '/'):
        if(f == 0):
            print('Error: Division by zero!')
            continue
        print('Result: ',s / f)
    else:
        print('Error,Please again!')
    c = str(input('Do you want to perform another calculation? (yes or no): '))
    if(c == 'yes'):
        continue
    elif(c == 'no'):
        print('Goodbye!')
        break
