# Boolean Query Engine

## Overview

This project is a simple Boolean Query Engine built as part of an Information Retrieval assignment.
It allows users to search documents using logical operators like AND, OR, and NOT.

The system takes a query as input and returns the document IDs that satisfy the condition.

---

## What I Implemented

* Built an inverted index from a set of documents
* Implemented Boolean operations: AND, OR, NOT
* Supported queries with brackets (nested queries)
* Converted queries from infix to postfix format
* Evaluated queries using a stack-based approach
* Optimized AND operation using skip pointers
* Added basic validation for incorrect queries

---

## How It Works

### Inverted Index

Each word is mapped to the list of document IDs where it appears.
For example:

```
data → [1, 3, 4]
```

---

### Query Processing

The input query is first converted into postfix form based on operator precedence:

```
NOT > AND > OR
```

---

### Execution

The postfix expression is evaluated using a stack:

* Terms push their posting lists
* Operators combine them step by step

---

### Boolean Logic

* AND → finds common documents
* OR → combines documents
* NOT → removes documents using the full document set

---

### Optimization

To improve performance, skip pointers are used in the AND operation.
Instead of checking every element, the algorithm jumps ahead using √n steps.

---

## How to Run

Open the project folder and run:

```
python main.py
```

Then enter queries like:

```
(data AND science) AND NOT physics
```

---

## Example

```
Query: data AND science
Postfix: ['data', 'science', 'AND']
Result Doc IDs: [1, 3, 4]
```

---

## Tech Used

* Python
* Basic data structures (lists, sets, stack)

---

## Final Note

This project helped me understand how search engines process queries internally, especially how Boolean retrieval and indexing work.

## 🎥 Demo Video

[Download Demo](./demo.mp4.mp4)