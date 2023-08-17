# list = [str(y) for y in input("Input Number: ").split()]
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
Stack = []
postfix_expr = input().split()
for token in postfix_expr:
    if is_number(token):
        Stack.append(float(token))
    else:
        if len(Stack) < 2:
            print("Invalid expression: Not enough operands.")
            exit()
        operand2 = Stack.pop()
        operand1 = Stack.pop()
        if token == '+':
            Stack.append(operand1 + operand2)
        elif token == '-':
            Stack.append(operand1 - operand2)
        elif token == '*':
            Stack.append(operand1 * operand2)
        elif token == '/':
            if operand2 == 0:
                print("Invalid expression: Division by zero.")
                exit()
            Stack.append(operand1 / operand2)
        elif token == '%':
            Stack.append(operand1 % operand2)
        elif token == '^':
            Stack.append(operand1 ** operand2)
        else:
            print("Invalid token:", token)
            exit()

if len(Stack) != 1:
    print("Invalid expression: Too many operands.")
    exit()

result = Stack[0]
print('%.1f' % result)






# def Postfix_Expression():
#     if len(list) > 50:
#         return "Input expression is too long."
#     list2 =[]
#     operater = set(['+','-','/','*','%','^'])
#     for char in list:
#         if char.isdigit():
#             list2.append(float(char))
#         elif char in operater:
#             B = list2.pop()
#             A = list2.pop()
#             if char=='+':
#                 list2.append(A + B)
#             elif char=='-':
#                 list2.append(A - B)
#             elif char=='*':
#                 list2.append(A * B)
#             elif char=='/':
#                 if list2 == 0:
#                     return "Invalid expression: Division by zero."
#                 list2.append(A / B)
#             elif char=='%':
#                 list2.append(A % B)
#             elif char=='^':
#                 list2.append(A**B)
