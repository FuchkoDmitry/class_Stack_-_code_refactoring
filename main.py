from stack import Stack


def balance(brackets_string):
    stack = Stack([])
    parentheses = {'(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{'}
    for bracket in brackets_string:
        if stack.is_empty() or parentheses[bracket] != stack.peek():
            stack.push(bracket)
        else:
            stack.pop()
    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    bracket_string = input()
    print(balance(bracket_string))








