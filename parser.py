def precedence(op):
    if op == "NOT":
        return 3
    elif op == "AND":
        return 2
    elif op == "OR":
        return 1
    return 0


def to_postfix(query):
    tokens = query.replace("(", " ( ").replace(")", " ) ").split()
    output = []
    stack = []

    for token in tokens:
        token = token.upper()

        if token not in ["AND", "OR", "NOT", "(", ")"]:
            output.append(token.lower())

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()

        else:
            while (stack and precedence(stack[-1]) >= precedence(token)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output