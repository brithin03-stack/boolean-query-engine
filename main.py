from index import build_index
from parser import to_postfix
from evaluator import evaluate


def is_valid_query(query):
    tokens = query.replace("(", " ( ").replace(")", " ) ").split()

    operators = {"AND", "OR", "NOT"}
    prev = None
    balance = 0  # for bracket checking

    for token in tokens:
        token_upper = token.upper()

        # Track brackets
        if token == "(":
            balance += 1
        elif token == ")":
            balance -= 1
            if balance < 0:
                return False

        # Two operands together → invalid
        if prev and prev not in operators and token_upper not in operators and token != "(" and prev != ")":
            return False

        # Two binary operators together → invalid
        if prev in {"AND", "OR"} and token_upper in {"AND", "OR"}:
            return False

        prev = token_upper

    if balance != 0:
        return False

    return True


def main():
    # Load inverted index
    index, total_docs = build_index("data.txt")

    print("Inverted Index:")
    print(index)
    print("\nEnter Boolean Query (type 'exit' to quit)\n")

    while True:
        query = input("Query: ")

        if query.lower() == "exit":
            print("Exiting...")
            break

        # 🔴 Validation step
        if not is_valid_query(query):
            print("Invalid query. Please check syntax.")
            print("-" * 40)
            continue

        try:
            postfix = to_postfix(query)
            result = evaluate(postfix, index, total_docs)

            print("Postfix:", postfix)
            print("Result Doc IDs:", result)
            print("-" * 40)

        except Exception:
            print("Invalid query. Please check syntax.")
            print("-" * 40)


if __name__ == "__main__":
    main()