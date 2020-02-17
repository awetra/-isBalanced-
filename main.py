def is_balanced(line):
    line = ''.join(line.split())
    brackets = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = []

    for bracket in line:
        if bracket not in brackets:
            # Если bracket - открывающая скобка
            stack.append(bracket)
        elif stack and brackets[bracket] == stack[-1]:
            # Если последний элемент стека является открывающей скобкой для текущей закрывающей скобки
            stack.pop(-1)
        else:
            return False

    return False if stack else True


if __name__ == '__main__':
    print(is_balanced('{[]})'))
    print(is_balanced('{[}]'))
    print(is_balanced('{[]}'))
    print(is_balanced('{{[][]}[]}'))
    print(is_balanced('['))
    print(is_balanced('[]]'))
    print(is_balanced('[][]{}'))