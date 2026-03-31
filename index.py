def build_index(filename):
    index = {}
    total_docs = 0

    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            doc_id = int(parts[0])
            words = parts[1:]
            total_docs += 1

            for word in words:
                word = word.lower()
                if word not in index:
                    index[word] = []
                index[word].append(doc_id)

    # ensure sorted postings
    for term in index:
        index[term] = sorted(list(set(index[term])))

    return index, total_docs