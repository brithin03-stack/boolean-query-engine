from operations import AND, OR, NOT

def evaluate(postfix, index, total_docs):
    stack = []

    for token in postfix:
        if token == "AND":
            b = stack.pop()
            a = stack.pop()
            stack.append(AND(a, b))

        elif token == "OR":
            b = stack.pop()
            a = stack.pop()
            stack.append(OR(a, b))

        elif token == "NOT":
            a = stack.pop()
            stack.append(NOT(a, total_docs))

        else:
            stack.append(index.get(token, []))

    return stack.pop()